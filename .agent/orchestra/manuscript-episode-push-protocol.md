# Manuscript Episode Push Protocol v1

Status: OPERATIONS  
Applies After: Pre-Writing Gate OPEN  
Unit: one episode per branch, PR and squash merge

## 1. 기본 원칙

- E001부터 E375까지 순서대로 집필한다.
- 한 번에 여러 화를 한 파일이나 한 PR에 묶지 않는다.
- 각 화는 정본 장면카드·연대·인물상태·미스터리·장면밀도 보정표를 읽고 작성한다.
- 한 화 원고는 공백 포함 최소 7,000자이며 상한은 없다.
- 최소치를 맞추기 위한 설명·대사·이동 반복은 금지한다.
- 사건·설정·인물 의도는 D7/D8/D9 정본을 조용히 바꾸지 않는다.

## 2. 파일과 브랜치

### 브랜치

`agent/manuscript-eNNN`

예:

`agent/manuscript-e001`

### 원고 파일

`manuscript/volume-NN/ENNN-episode-title.md`

### 품질기록

`manuscript/quality/ENNN-quality-report.md`

## 3. 편당 작업순서

1. 최신 `main` 확인
2. 이전 화 원고와 품질보고서 확인
3. 해당 화 D6 카드 확인
4. D9 보정·연대·인물·미스터리·유산·손실 장부 확인
5. 실제 장면 수 Q/S/E/X 결정
6. 원고 작성
7. `sentence-narrator`로 문장별 낭독 적합성 검사
8. 자연스러운 한국어·번역체·생동감·이름·호칭 검사
9. 시간·부상·거리·보급·정보상한 검사
10. 글자수 검사
11. 품질보고서 작성
12. 브랜치 비교: `behind_by=0`
13. PR 생성
14. squash merge
15. PR `closed/merged=true`와 실제 merge SHA 확인
16. `main`에서 원고와 보고서 재확인
17. 다음 화로 이동

## 4. 원고 머리말

각 원고 파일은 다음 메타데이터를 가진다.

```yaml
---
title: 제N화 제목
episode: ENNN
volume: NN
status: MANUSCRIPT REVIEW
pov: 인물
calendar: 건국력 연월일
subjective_day: 에이든 누적일
scene_density: Q|S|E|X
canon_card: 관련 설계파일
previous_episode: ENNN
next_episode_cause: 다음 원인
---
```

메타데이터는 낭독 기본 모드에서 읽지 않는다.

## 5. 편당 품질보고서

필수 항목:

- 공백 포함 글자수
- 장면 수와 Q/S/E/X 유형
- POV와 정보상한
- 현재 연대와 누적일
- 인물·부상·소지품 상태
- 공개·재점화된 미스터리
- 사용한 설정·기관·유산
- 발생한 영구·임시 비용
- 훅 유형
- 번역체·호칭·고유명사 검사
- 반복 위험
- 다음 화 진입상태
- 판정: PASS / REVISION / BLOCKED

`BLOCKED`인 화는 PR을 만들지 않는다.

## 6. 원고 문체

- 자연스러운 현대 한국어 문장
- 절제된 다크 판타지
- 시간 음모 스릴러의 불완전한 정보
- 관료제 공포의 무심한 절차
- 정치 판타지의 합리적 대립
- 감각과 행동에 연결된 생동감
- 번역체·과잉 수동태·명사화 최소화
- 인물별 대사와 호칭 차별화
- 소리 내 읽었을 때 의미가 한 번에 들어오는 호흡

특정 작품의 문장·대사·장면·연기·고유 반전을 모사하지 않는다.

## 7. 자동 진행과 중단조건

다음 화로 자동 이동한다.

중단하는 경우:

- S0/S1 정본 충돌
- 이전 화와 현재 화의 사망·부상·위치·소유권 불일치
- 장면카드만으로 해결할 수 없는 작가 전용 선택
- GitHub 브랜치가 최신 main보다 뒤처짐
- 품질검사 BLOCKED

이 경우 원고를 억지로 완성하지 않고 문제·원인·대안·영향을 기록한다.

## 8. 완료조건

E001–E375가 각각 다음 조건을 만족해야 시리즈 원고 완료다.

- 원고 파일 존재
- 품질보고서 존재
- 편당 최소 글자수 통과
- 개별 PR squash merge
- main 재확인
- 권별 퇴고 감사
- 최종 미스터리·손실·연대·인물·설정 회수 감사
