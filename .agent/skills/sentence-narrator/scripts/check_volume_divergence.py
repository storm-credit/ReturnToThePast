#!/usr/bin/env python3
"""권 단위 분화 검사기.

`validate_manuscript.py`는 회차를 하나씩 본다. 그래서 **스무 편이 똑같아지는 것**을
잡지 못한다. 실제로 E001~E020 수술 후 검증기는 20/20 PASS를 냈지만,
20편 전부가 같은 연결어미로 문장을 붙이고 같은 신체 부위로 감정을 대신했다.

이 검사기는 회차 안이 아니라 **회차 사이**를 본다.

    python check_volume_divergence.py manuscript/volume-01/E0*.md
"""
from __future__ import annotations

import argparse
import glob
import re
import sys
from collections import Counter
from pathlib import Path

# ---------------------------------------------------------------- 기준
CONNECTIVE_MAX = 0.45   # 한 연결어미가 권 전체 절 연결에서 차지할 수 있는 상한
BODY_MAX = 0.50         # 한 신체 채널이 한 회차 신체 비트에서 차지할 수 있는 상한
CLONE_MIN = 14          # 이 길이 이상이 두 회차에 똑같이 나오면 복제
TENURE_MAX = 1          # 같은 근속연수 표현이 권 안에서 나올 수 있는 횟수

CONNECTIVES = {
    "-고,": r"[가-힣]고, ",
    "-는데": r"[가-힣]는데[ ,]",
    "-지만": r"[가-힣]지만[ ,]",
    "-면서": r"[가-힣]면서[ ,]",
    "-자,": r"[가-힣]자, ",
    "-며,": r"[가-힣]며, ",
    "-어서,": r"[가-힣][아어]서, ",
    "-도록": r"[가-힣]도록 ",
}

BODY = {
    "손": r"손(?![님])", "눈·시선": r"눈(?![물])|시선", "고개": r"고개",
    "어깨": r"어깨", "발": r"발(?![음])|걸음", "입·목": r"입술|목소리|숨",
}

# 근속연수. `640년`(연호) · `피해`·`위해`·`향해`(동사)를 잡지 않도록 좁힌다.
# 수사 + `년째/해째` 형태만 센다.
NUM = r"(?:[0-9]{1,2}|[일이삼사오육칠팔구십]+|한|두|세|네|다섯|여섯|일곱|여덟|아홉|열|스물|서른|마흔|쉰|예순)"
TENURE = rf"(?<![가-힣0-9])({NUM})\s*(년째|해째|년 만에|해 만에)"


def sentences(text: str) -> list[str]:
    body = text.split("\n---\n", 2)[-1]
    out = []
    for line in body.split("\n"):
        line = line.strip()
        if not line or line[0] in "#>|*-!" or line[0] in '"“\'‘':
            continue
        out += [s.strip() for s in re.split(r"(?<=[.!?…])\s+", line) if len(s.strip()) > 1]
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    args = ap.parse_args()

    files: list[Path] = []
    for p in args.paths:
        files += [Path(m) for m in sorted(glob.glob(p))] or [Path(p)]
    files = [f for f in files if f.exists()]
    if not files:
        print("파일 없음")
        return 1

    texts = {f.name[:4]: f.read_text(encoding="utf-8") for f in files}
    fails: list[str] = []

    # 1. 연결어미 쏠림 — 권 전체
    conn = Counter()
    for t in texts.values():
        for name, pat in CONNECTIVES.items():
            conn[name] += len(re.findall(pat, t))
    total = sum(conn.values())
    print(f"[권] 회차 {len(texts)}편 · 절 연결 {total}개")
    print("  연결어미 분포")
    for name, n in conn.most_common():
        share = n / total if total else 0
        mark = "  ← 쏠림" if share > CONNECTIVE_MAX else ""
        print(f"    {name:8} {n:5}  {share:6.1%}{mark}")
        if share > CONNECTIVE_MAX:
            fails.append(f"[분화] 연결어미 `{name}`가 권 전체의 {share:.1%} — 상한 {CONNECTIVE_MAX:.0%}")

    # 2. 신체 채널 독식 — 회차별
    print("  신체 비트 채널")
    for eid, t in texts.items():
        c = Counter({k: len(re.findall(v, t)) for k, v in BODY.items()})
        tot = sum(c.values())
        if not tot:
            continue
        top, n = c.most_common(1)[0]
        if n / tot > BODY_MAX:
            fails.append(f"[분화] {eid} 신체 비트의 {n/tot:.1%}가 `{top}` — 상한 {BODY_MAX:.0%}")
            print(f"    {eid}  {top} {n}/{tot} ({n/tot:.0%})  ← 독식")

    # 3. 문장 복제 — 회차를 건너 같은 문장
    seen: dict[str, str] = {}
    for eid, t in texts.items():
        for s in sentences(t):
            key = re.sub(r"\s+", "", s)
            if len(key) < CLONE_MIN:
                continue
            if key in seen and seen[key] != eid:
                fails.append(f"[복제] {seen[key]}·{eid} 동일 문장 — {s[:44]}")
            seen.setdefault(key, eid)

    # 4. 근속연수 중복 — 단역들이 같은 햇수를 말한다
    ten = Counter()
    where: dict[str, list[str]] = {}
    for eid, t in texts.items():
        for m in re.finditer(TENURE, t):
            k = m.group(1) + m.group(2).strip()
            ten[k] += 1
            where.setdefault(k, []).append(eid)
    for k, n in ten.items():
        if n > TENURE_MAX:
            fails.append(f"[복제] 근속 `{k}` {n}회 — {' '.join(sorted(set(where[k])))}")

    # 5. 따옴표 통일
    for eid, t in texts.items():
        if '"' in t:
            fails.append(f"[표기] {eid} 곧은따옴표 사용 — 나머지 회차는 둥근따옴표")

    print()
    for f in fails:
        print(f"  FAIL: {f}")
    print(f"[권] {'RESULT=PASS' if not fails else f'RESULT=FAIL ({len(fails)})'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
