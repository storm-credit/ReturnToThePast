# Context Pack Registry

Status: CANON-OPERATIONS SUPPORT  
Owner: A21 Context Pack Compiler & Harness Runner

## 지위

Context Pack(CP)은 특정 작업을 위해 정본을 선별·요약한 읽기 전용 실행 묶음이다.

- CP는 정본이 아니다.
- CP가 원본과 충돌하면 원본이 우선한다.
- CP에만 존재하는 사실은 사용할 수 없다.
- CP는 생성 기준 main commit SHA를 기록한다.
- main 변경 뒤 영향 파일이 바뀌면 해당 CP는 STALE이다.

## 단계

- `series/`: 시리즈 공통 정본
- `grand-acts/`: Grand Act 단위
- `volumes/`: 권 단위
- `subacts/`: Subact 단위
- `episodes/`: 회차 단위
- `templates/`: CP 스키마

## 상태

- READY: 필수 의존성 존재, S0/S1 없음
- BLOCKED: 필수 설정 또는 정합성 문제 존재
- STALE: 기준 commit 이후 관련 정본 변경
- PROVISIONAL: 비차단 가정 포함, 원고 병합 전 해소 필요

## 생성 규칙

Episode CP는 상위 CP를 상속하되 필요한 내용을 원본 경로와 함께 다시 명시한다.

Episode CP 없이 A18 Prose Agent를 호출할 수 없다.

## CP와 MCP

- CP: 작품 내부의 읽기 묶음
- MCP: GitHub·파일·외부 도구 연결 계층

작품의 정본·캐릭터·아이템·종교 설정을 외부 MCP의 숨은 상태에만 저장하지 않는다.
