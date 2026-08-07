#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REQUIRED = [
    "calendar: 건국력 664년 장야월 18일",
    "제7방벽",
    "12개 중 7개가 응답합니다.",
    "나머지 5개는?",
    "구조 가능 인원 3,812명.",
    "3,760명.",
    "3,541명.",
    "서부 구조대 31명.",
    "127",
    "119일",
    "156일",
    "제7방벽 추정 생존자 4,200명.",
    "즉시 구조 성공 예상 2,900명.",
    "2,417명.",
    "2,150명.",
    "지금 안정구역 생존자가 42만 명.",
    "19만 명.",
    "9일.",
    "12일.",
    "17일.",
    "5번째와 13번째",
    "브리핑 수령 확인.",
    "임무 동의 아님.",
    "추가 열람을 신청하겠습니다.",
    "에이든이 분명히 본 글자는 ‘세’뿐이었다.",
    "허가 없이 삭제 흔적에 접근한 사실이 감지되었습니다.",
]

ROUTE = [
    "관측실",
    "제3보고실",
    "제2브리핑실",
    "기록 접근실",
]

FORBIDDEN = [
    "마르칸 베르",
    "세렌은 무죄",
    "세렌 바일은 무죄",
    "임무 동의 완료",
    "시간 파견 출발 완료",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args()

    text = args.path.read_text(encoding="utf-8")
    failures: list[str] = []

    for phrase in REQUIRED:
        if phrase not in text:
            failures.append(f"정본 필수 요소 누락: {phrase}")

    last = -1
    for location in ROUTE:
        pos = text.find(location, last + 1)
        if pos == -1:
            failures.append(f"동선 위치 누락/순서 오류: {location}")
            break
        last = pos

    for phrase in FORBIDDEN:
        if phrase in text:
            failures.append(f"금지 확정/병합 표현 발견: {phrase}")

    if (
        "1명을 죽이면 19만 명이 늘어난다?" not in text
        or "선별실의 계산은 그래요." not in text
    ):
        failures.append("19만 예측값의 불확실성 문맥 손상")

    print(f"[CANON] file={args.path}")
    if failures:
        for item in failures:
            print(f"FAIL: {item}")
        print(f"[CANON] RESULT=FAIL ({len(failures)})")
        return 1

    print("[CANON] RESULT=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
