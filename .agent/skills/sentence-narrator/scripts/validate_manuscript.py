#!/usr/bin/env python3
"""회차 무관 원고 검증기.

E001 전용 검증기(validate_e001_canon.py)와 달리 어느 회차에나 쓴다.
정본 명칭·호칭 규칙·조사·금지 조어·분량을 검사한다.

    python validate_manuscript.py manuscript/volume-01/E001-....md
    python validate_manuscript.py manuscript/volume-01/*.md
"""
from __future__ import annotations

import argparse
import glob
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------- 폐기 명칭
# DEC-016 / DEC-017 / DEC-018 로 폐기된 이름. 원고에 남아 있으면 개명 누락이다.
RETIRED = {
    "연대출귀원": "앙카 귀환다리",
    "성력국": "솔라 종탑",
    "중앙관측탑연합": "아스트라 관측탑",
    "지역 연대감사소": "아고라 회당",
    "잔문감사실": "팔림프세스트 감사실",
    "무명종": "움브라",
    "두겹성": "두 역사의",
    "라베른 쌍성": "두 역사의 라베른",
    "네르바 잿빛 변경": "잿빛 변경",
    "마레이 조류도시연맹": "조류도시연맹",
    "마레이 밀물항": "밀물항",
    "관문도시 세르나": "관문도시",
    "셀린 협곡": "백유리 협곡",
    "세라트 구휼원": "동쪽 구휼원",
    "카센 언덕": "절검의 언덕",
    "겹흔적": "잔문",
    "구흔교리": "아홉 상처 교리",
}

# ---------------------------------------------------------------- 호칭 규칙
# 성 단독 호출 금지. 직함이 붙으면 허용한다.
SURNAME_TITLES = {
    "로엔": ["로엔 요원", "에이든 로엔"],
    "세른": ["세른 기록관", "리아 세른", "하렌 세른"],
    "네르": ["네르 대표", "아이리스 네르", "엘사 네르", "아벨 네르"],
    "아노르": ["아노르 대표", "나하 아노르", "시아 아노르", "아노르 백지권", "아노르 무면시장", "아노르 제1공동학교"],
}

# 단독 사용 금지 — 뒤에 명사가 붙지 않고 조사만 붙으면 위반이다.
# `네르바 변경`, `네르바 표준토양`처럼 명사가 뒤따르면 허용한다.
BARE_PATTERNS = [
    (r"네르바(?![\s가-힣])|네르바(?=(은|는|이|가|를|을|에|의|도|만|와|과)\b)",
     "`네르바` 단독 — `네르바 변경`·`서부`처럼 지명 수식과 함께 쓴다"),
    (r"네바르(?![\s가-힣])|네바르(?=(은|는|이|가|를|을|에|의|도|만|와|과)\b)",
     "`네바르` 단독 — `네바르 사람`처럼 수식과 함께 쓴다"),
]

# 축약 호칭 오용
SHORTFORM = [
    (r"움\s*판관", "`움 판관` 금지 — `베사르` 또는 `장례판관` (움브라와 충돌)"),
    (r"(?<![가-힣])솔라(?!\s*종탑)", "대사에서 `솔라` 단독 금지 — 축약은 `종탑` (메이라 솔과 충돌)"),
    # 발음사전 §기관 축약: 앙카 귀환다리 → `앙카`. `귀환원`은 폐기명 `연대출귀원`의 잔재다.
    (r"귀환원", "`귀환원` 금지 — 앙카 귀환다리의 축약은 `앙카`"),
    # 바로 앞뒤에 한글이 없는 `탑`. `관측탑`·`종탑`은 통과한다.
    (r"(?<![가-힣])탑(?=[은는이가을를에와과의도만]|\s|$)",
     "`탑` 단독 금지 — 관측탑인지 종탑인지 갈린다. `아스트라` 또는 `종탑`"),
]

# 부정형 톤 태그 (기능인물 화법 규격 §1.1)
# 서술이 「이 사람은 악역이 아님」을 보증하면 대립자 온도가 평탄해진다.
TONE_TAG = re.compile(
    r"[^.\n]{0,30}(처럼 하지( 않았|도 않)|처럼 받아들이지 않았|화를 내지 않았"
    r"|부끄러워하지( 않았|도)|목소리를 높이지 않았|비꼬는 말을 받아들이지 않았"
    r"|얼굴이 아니었다|말투가 아니었다)[^.\n]{0,15}"
)

# ---------------------------------------------------------------- 조어·외래어
# 명명규칙 §3.2 분위기 접두어 자동 부착
BAD_COINAGE = [
    "마도조율판", "시공잔향", "각인상실자", "잔흔감찰실", "결계핵",
    "지맥계", "마도 조율판", "관측상", "전언패", "전언석", "기록패",
    "치유원", "생존 계수판", "시공원정자", "역사주소층", "존재각인표식",
    "주소층", "구조표식", "등록흔",
]

# 현대 외래어
MODERN_LOANWORDS = ["스피커", "시스템", "단말기", "모니터", "센서", "데이터", "프로그램", "네트워크"]

# ---------------------------------------------------------------- 조사
# 받침 유무가 바뀐 개명어에서 기계 치환 사고가 났던 자리
PARTICLE_RULES = [
    (r"귀환다리(은|이|을|과|으로)\b", "받침 없음 — 는/가/를/와/로"),
    (r"아고라 회당(는|가|를|와|로)\b", "받침 있음 — 은/이/을/과/으로"),
    (r"움브라(은|을|과)\b", "받침 없음 — 는/를/와"),
    (r"관측탑(는|가|를|와)\b", "받침 있음 — 은/이/을/과"),
    (r"종탑(는|가|를|와)\b", "받침 있음 — 은/이/을/과"),
]

# ---------------------------------------------------------------- 첫 등장
FIRST_FULL_NAME = ["에이든 로엔", "리아 세른", "세렌 바일"]

# ---------------------------------------------------------------- 단문 비율
# DEC-022. 작가 원칙은 `단문금지 · 자연스러운 문장`이다.
# Legacy `Guidelines/`가 지시하던 `단문 위주 · 1~2문장마다 줄바꿈`은 폐기됐다.
#
# 대사는 인물마다 호흡이 달라야 하므로 세지 않는다. 서술문만 본다.
# 단문 자체는 금지 대상이 아니다. 긴 문장 뒤의 짧은 문장은 강조다.
# 문제가 되는 것은 `전부 짧을 때`다. 대비가 없으면 아무것도 꽂히지 않는다.
# 따라서 비율이 아니라 **연속**과 **긴 문장 결핍**을 잡는다.
SHORT_CHARS = 20          # 이하를 단문으로 센다
LONG_CHARS = 40           # 초과를 장문으로 센다
SHORT_RUN_MAX = 8         # 단문 연속 허용 한계
LONG_RATIO_MIN = 0.05     # 서술문 중 장문이 이 비율 미만이면 호흡이 평평하다

# 번역체 표지. 작가가 실제로 싫어하는 축이다.
TRANSLATIONESE = [
    (r"되어졌|지게 되었", "`되어졌`·`지게 되었` — 이중 피동"),
    (r"에 의해(?!서는)", "`~에 의해` — 영어 수동태 직역"),
    (r"할 수 있었다.{0,60}할 수 있었다", "`~할 수 있었다` 연쇄"),
    (r"에 대한 ", "`~에 대한` — 명사화 직역"),
]
SKIP_LINE_PREFIX = ("#", ">", "|", "***", "---", "*", "!")
QUOTE_OPEN = ('"', "“", "'", "‘")


def narrative_sentences(body: str) -> list[str]:
    """서술문만 뽑는다. 대사 줄과 표·제목·장면구분은 제외한다."""
    out: list[str] = []
    for raw in body.split("\n"):
        line = raw.strip()
        if not line or line.startswith(SKIP_LINE_PREFIX) or line.startswith(QUOTE_OPEN):
            continue
        # 서술 안에 끼어든 인용은 제거한다
        line = re.sub(r"[\"“][^\"”]*[\"”]", "", line).strip()
        for piece in re.split(r"(?<=[.!?…])\s+", line):
            piece = piece.strip()
            if len(piece) > 1:
                out.append(piece)
    return out


def body_without_frontmatter(text: str) -> tuple[str, str]:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[: end + 5], text[end + 5 :]
    return "", text


def check(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    front, body = body_without_frontmatter(text)
    fails: list[str] = []

    # 1. 폐기 명칭
    for old, new in RETIRED.items():
        if old in body:
            line = body[: body.index(old)].count("\n") + 1
            fails.append(f"[명칭] 폐기된 이름 `{old}` 잔존 (L~{line}) → `{new}`")

    # 2. 성 단독 호칭
    for surname, allowed in SURNAME_TITLES.items():
        masked = body
        for a in allowed:
            masked = masked.replace(a, "x" * len(a))
        for m in re.finditer(rf"(?<![가-힣]){surname}(?![가-힣])", masked):
            line = masked[: m.start()].count("\n") + 1
            fails.append(f"[호칭] 성 단독 호출 `{surname}` (L{line}) — 직함과 함께 쓴다")

    # 3. 단독 사용 금지어
    for pattern, msg in BARE_PATTERNS:
        for m in re.finditer(pattern, body):
            line = body[: m.start()].count("\n") + 1
            fails.append(f"[호칭] (L{line}) {msg}")

    # 4. 축약 오용
    for pattern, msg in SHORTFORM:
        for m in re.finditer(pattern, body):
            line = body[: m.start()].count("\n") + 1
            fails.append(f"[호칭] (L{line}) {msg}")

    # 5. 금지 조어
    for word in BAD_COINAGE:
        if word in body:
            line = body[: body.index(word)].count("\n") + 1
            fails.append(f"[조어] 부적합 판정 조어 `{word}` (L~{line})")

    # 6. 현대 외래어
    for word in MODERN_LOANWORDS:
        if word in body:
            line = body[: body.index(word)].count("\n") + 1
            fails.append(f"[어휘] 현대 외래어 `{word}` (L~{line})")

    # 7. 조사
    for pattern, msg in PARTICLE_RULES:
        for m in re.finditer(pattern, body):
            line = body[: m.start()].count("\n") + 1
            fails.append(f"[조사] (L{line}) `{m.group(0)}` — {msg}")

    # 8. 첫 등장 전체 이름 — 인물이 작품에 처음 등장하는 회차에만 적용한다.
    #    E002 이후에는 이미 소개된 인물이므로 이름만 써도 된다.
    if path.name.startswith("E001"):
        for full in FIRST_FULL_NAME:
            given = full.split()[0]
            if given in body:
                if full not in body:
                    fails.append(f"[호칭] `{given}` 등장하나 전체 이름 `{full}` 없음")
                elif body.find(given) != body.find(full):
                    fails.append(f"[호칭] `{given}` 첫 등장이 전체 이름 `{full}` 보다 앞섬")

    # 9. 분량
    if len(text) < 7000:
        fails.append(f"[분량] 공백 포함 {len(text)}자 — 최소 7,000자 미달")

    # 10. 상태 표기
    if "HUMAN PROSE PASS" in front or "status: FINAL" in front:
        fails.append("[상태] 작가 승인 전 최종 상태 사용")

    # 11. 문장 호흡 (DEC-022)
    sents = narrative_sentences(body)
    if sents:
        # 11-a. 단문이 몇 개나 연속되는가
        run = best = 0
        best_at = 0
        for i, s in enumerate(sents):
            run = run + 1 if len(s) <= SHORT_CHARS else 0
            if run > best:
                best, best_at = run, i
        if best > SHORT_RUN_MAX:
            head = " / ".join(sents[best_at - best + 1 : best_at - best + 4])
            fails.append(
                f"[호흡] 단문 {best}문장 연속 — 한계 {SHORT_RUN_MAX}. 시작: {head}"
            )

        # 11-b. 긴 문장이 아예 없으면 대비가 사라진다
        long_ratio = sum(1 for s in sents if len(s) > LONG_CHARS) / len(sents)
        if long_ratio < LONG_RATIO_MIN:
            fails.append(
                f"[호흡] {LONG_CHARS}자 초과 문장 {long_ratio:.1%} — "
                f"최소 {LONG_RATIO_MIN:.0%}. 전부 짧아 강조가 죽는다"
            )

    # 12. 번역체
    for pattern, msg in TRANSLATIONESE:
        for m in re.finditer(pattern, body):
            line = body[: m.start()].count("\n") + 1
            fails.append(f"[번역체] (L{line}) {msg}")

    # 13-a. 부정형 톤 태그
    for m in TONE_TAG.finditer(body):
        line = body[: m.start()].count("\n") + 1
        fails.append(f"[화법] (L{line}) 부정형 톤 태그 — {m.group(0).strip()}")

    # 13. 제작 식별자 누출 — 독자가 읽는 본문에 회차·설계 ID가 남으면 안 된다.
    #     E003에 `E001에서 은판 위로 봤던`이 실제로 남아 있었다.
    #     예외: E031의 `F0`는 세계 내 격리분류명이자 정본 훅이다
    #     (v02-scene-ready-design L114, E027-E031 CP `마지막 F0는 정본 훅이므로 예외`).
    LEAK_WHITELIST = {"E031": {"F0"}}
    allowed = LEAK_WHITELIST.get(path.name[:4], set())
    for m in re.finditer(r"(?<![A-Za-z])(E\d{3}|V\d{1,2}|DEC-\d+|[CM]\d{2}|F[0-3])(?![A-Za-z0-9])", body):
        if m.group(1) in allowed:
            continue
        line = body[: m.start()].count("\n") + 1
        ctx = body[max(0, m.start() - 20) : m.start() + 20].replace("\n", " ")
        fails.append(f"[누출] (L{line}) 제작 식별자 `{m.group(1)}` — …{ctx}…")

    return fails


def measure(path: Path) -> str:
    """실패 여부와 무관하게 찍는 문장 호흡 지표."""
    _, body = body_without_frontmatter(path.read_text(encoding="utf-8"))
    sents = narrative_sentences(body)
    if not sents:
        return "서술문 0"
    lengths = [len(s) for s in sents]
    short = sum(1 for n in lengths if n <= SHORT_CHARS)
    return (
        f"서술문 {len(sents)} · 평균 {sum(lengths) / len(lengths):.1f}자 · "
        f"단문 {short} ({short / len(sents):.1%})"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+")
    args = parser.parse_args()

    targets: list[Path] = []
    for pattern in args.paths:
        matched = glob.glob(pattern)
        targets.extend(Path(m) for m in matched) if matched else targets.append(Path(pattern))

    total = 0
    for path in targets:
        if not path.exists():
            print(f"[MANUSCRIPT] file={path} MISSING")
            total += 1
            continue
        fails = check(path)
        print(f"[MANUSCRIPT] file={path.name}  {measure(path)}")
        for item in fails:
            print(f"  FAIL: {item}")
        print(f"[MANUSCRIPT] {'RESULT=PASS' if not fails else f'RESULT=FAIL ({len(fails)})'}")
        total += len(fails)

    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
