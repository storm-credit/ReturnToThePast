#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

BLOCKED = [
    "주소층",
    "주소 연결 상실",
    "구조표식",
    "압력계",
    "서부 구조대 로엔",
    "잔여 기록 접근",
    "원본이 보관된 기록층",
    "사망대장",
    "빛점",
    "등록흔",
    "검은 유리구",
    "사본끼리 우선순위",
    "사람의 등록 기록과 현재 위치가 서로 맞지 않습니다.",
]

REQUIRED_CLARITY = [
    "등록 정보와 위치 신호가 계속 어긋납니다.",
    "등록 인원 위치 확인 불가.",
    "구조 신호 확인해.",
    "도시를 붙드는 고정망",
    "회색열 치료를 기다리는 병사였다.",
    "도시의 달력과 난방·병원 설비를 새 계절에 맞춰 조정하는 날",
    "소거는 죽음과 달랐다.",
    "원본 기록이 보관된 구역",
    "허가 없이 삭제 흔적에 접근",
]


def body_without_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5 :]
    return text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args()

    text = args.path.read_text(encoding="utf-8")
    body = body_without_frontmatter(text)
    failures: list[str] = []

    if len(text) < 7000:
        failures.append(f"공백 포함 분량 부족: {len(text)}자")

    for phrase in BLOCKED:
        if phrase in body:
            failures.append(f"첫 청취 차단 표현 잔존: {phrase}")

    for phrase in REQUIRED_CLARITY:
        if phrase not in body:
            failures.append(f"필수 설명 누락: {phrase}")

    if "status: AUTHOR REVIEW" not in text:
        failures.append("AUTHOR REVIEW 상태 누락")
    if "HUMAN PROSE PASS" in text or "status: FINAL" in text:
        failures.append("작가 승인 전 최종 상태 사용")

    first_aiden = body.find("에이든")
    first_full = body.find("에이든 로엔")
    if first_aiden == -1 or first_aiden != first_full:
        failures.append("에이든 첫 등장 전체 이름 규칙 위반")
    if "서부 구조대 에이든." not in body:
        failures.append("현장 호출명 에이든 누락")
    if "에이든 로엔 요원" not in body or "현장요원 에이든 로엔" not in body:
        failures.append("공식 전체 이름 호명 누락")
    if re.search(r"서부 구조대\s+로엔", body):
        failures.append("성 단독 현장 호출 잔존")
    if "리아 세른" not in body or "세렌 바일" not in body:
        failures.append("주요 인물 첫 등장 전체 이름 누락")

    print(f"[READ-ALOUD] file={args.path}")
    print(f"[READ-ALOUD] chars={len(text)}")
    if failures:
        for item in failures:
            print(f"FAIL: {item}")
        print(f"[READ-ALOUD] RESULT=FAIL ({len(failures)})")
        return 1

    print("[READ-ALOUD] RESULT=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
