# Visual Negative Prompt & Collision Rules v1

Status: **D16.3 HARD PRODUCTION GUARD**  
Purpose: 프롬프트가 개별적으로 좋아 보여도 전체 IP에서 얼굴/실루엣/기능이 수렴하는 것을 막는다.

---

# 1. Global Negative Layer

모든 이미지 생성/제작 브리프에 의미상 다음 금지층을 적용한다.

## Character
- identical beauty-standard faces
- symmetrical model-like faces for all characters
- same V-shaped jaw across cast
- same narrow nose / same eye spacing
- all men tall, broad-shouldered, heroic
- all women slim, long-haired, delicate
- youthifying older characters
- glamour makeup not justified by role
- spotless fantasy costume
- generic black long coat protagonist
- cape/hood used as default differentiation
- weapon as sole identity
- glowing eyes as time-power shorthand
- unexplained scars
- unexplained tattoos
- evil-looking antagonist coding

## Relic
- RPG rarity glow
- gem color = power tier
- oversized legendary weapon inflation
- pristine museum restoration
- floating runes without canon basis
- gold filigree added only for value
- stronger final form
- owner-exclusive aura unless canon

## Beast
- pet behavior
- saddle/harness unless canon explicitly demands it
- cute mascot face normalization
- giant scale by default
- elemental aura by species
- collectible monster pose on white background as final
- evolution stages
- rarity color variants

## Landmark / Faction
- one-color biome
- every citizen wearing faction color
- giant logo pasted on all buildings
- postcard beauty without life/function
- architecture copied from one real-world culture wholesale
- P1 as sterile utopia
- Era F as generic cyberpunk

---

# 2. Face Collision Metrics

8축:
1. face length/width
2. brow structure
3. eye spacing/depth
4. nose bridge/tip
5. jaw/chin
6. age/skin texture
7. facial asymmetry/life trace
8. default facial tension

일반 인물쌍: 4/8 이상 차이.  
동일기능/유사연령 위험군: 5/8 이상.  
비예외 목표: 6/8 이상.

C01↔C08은 동일인 다른 시기 예외. 골격 유사 허용, age/body/gear에서 분리.

C01↔C30은 얼굴로 연결 암시 금지. 8/8 분리 목표.

---

# 3. Body Collision Metrics

7축:
1. height impression
2. shoulder/hip ratio
3. torso/leg proportion
4. center of gravity
5. habitual posture
6. hand usage
7. walking/standing rhythm

같은 성별/연령대 캐릭터 3명 이상이 동일 체형이면 FAIL.

헤어/의상/소품을 제거한 회색 마네킹 비교를 요구한다.

---

# 4. Dangerous Character Clusters

## Time / traveler cluster
C01 에이든 / C08 젊은 에이든 / C29 렌 바르 / C30 이름 없는 여행자

- C01: 돌아가려는 현장요원, 낮은 중심, 비대칭 수선장비
- C08: 같은 골격의 더 가볍고 열린 구조
- C29: 귀환 빈자리를 현지생활 도구가 채움
- C30: 영웅장비 없는 평범한 여행자

## Record cluster
C02 리아 / C12 엘사 / C22 하렌

- C02: 겹침/유동/반투명
- C12: 분산/생활/야외
- C22: 원본/블록/보존

## Local-life cluster
C03 아이리스 / C17 유나 / C27 시아

- C03: 사람흐름/주민표식
- C17: 숨긴 가족조각/평범한 민간인
- C27: 아이 높이/학교명부

## Military cluster
C04 마르칸 / C24 브란

- C04: 국가 군정/구역/배급
- C24: 요새/마을/철회조건

## Workshop cluster
C13 도르칸 / C25 케론

- C13: 제작/접합/소유
- C25: 수리/진동/가동시간

## Coast cluster
C16 마리엔 / C19 에스라 / C28 토마르

- C16: 공증/방수문서
- C19: 외교/항구매듭
- C28: 노동/하역

## Central authority cluster
C05 오르바드 / C20 오렐 / C21 레오르

- C05: 건국현장 조정
- C20: 절차/수선행정
- C21: 승인/왕권속도

---

# 5. Hair-Off Test

캐릭터 승인 전 동일 조명에서:
- 머리카락을 단색 cap으로 단순화
- 색 제거
- 장신구 제거

그 상태에서도 얼굴 70% 이상 구분 가능해야 한다.

머리색이 핵심 식별자면 FAIL.

---

# 6. Prop-Off Test

대표소품을 가린 전신을 비교한다.

PASS 조건:
- 자세/비율/복식구조만으로 위험군 구별
- 캐릭터 직업이 정확히 맞지 않아도 ‘다른 사람’임은 확실

FAIL 시 소품을 더 추가하지 않는다. 몸/실루엣을 수정한다.

---

# 7. Group Shot Gate

8명 이상 그룹 장면에서 검사:
- 같은 포즈 3명 초과 금지
- 같은 시선방향 일렬배치 금지
- 전원이 정면으로 서는 홍보사진 금지
- 키 차이를 머리 한 개 단위로 기계적으로 배치 금지
- 역할에 따라 손/발/무게중심이 달라야 함

Group Shot이 개별 캐릭터성을 지우면 개인 시트 PASS라도 전체 FAIL.

---

# 8. Relic Collision Gate

12개 유산을 silhouette-only로 놓고 검사.

필수 분포:
- small handheld
- document/media
- wearable/work gear
- map/layer object
- public installation
- funerary object
- authority frame
- shield/protective object
- distributed procedure/object system

R01–R12를 전부 ‘손에 든 판타지 아이템’으로 만들면 FAIL.

Final 감정도 분산:
- 반환
- 공개
- 파괴
- 봉인
- 분해
- 분산
- 매장
- 용해
- 공공보관
- 절차화

---

# 9. Beast Collision Gate

몸통을 지우고 `trace only`로 5종을 비교한다.

- B01: 긴 경로/발자국
- B02: 군집 공명/빈 공간
- B03: 진동/암석 정지
- B04: 역방향 수면/항로
- B05: 동일 발자국/관찰불일치

흔적만 보고 구분이 안 되면 외형을 더 화려하게 하지 말고 생태 연출을 강화한다.

---

# 10. Landmark Collision Gate

8개 지역 one-shot에서 색을 grayscale로 제거한다.

PASS 조건:
- L01 수직/수평/탑군 3층
- L02 끊긴 벽/학교/시장
- L03 산 단면/층형 작업도시
- L04 수문/제방/곡창 수평선
- L05 조수에 열리는 다리/시장
- L06 이동칸막이/공동명부/생활
- L07 지하통로/패치벽/재사용
- L08 낮은 생활축/게시/병원/학교

모두 ‘겹쳐진 옛벽’로 보이면 FAIL.

---

# 11. Faction Silent Test

로고/문장/색을 제거하고도 다음 3축 중 2개로 세력 추정 가능해야 한다.
- shape grammar
- material grammar
- behavioral mark

로고를 떼면 세력 구분이 사라지면 FAIL.

---

# 12. Reference Leak Test

결과를 보고 다음 질문에 하나라도 YES면 검토:
- 특정 유명 캐릭터 이름이 즉시 떠오르는가?
- 특정 게임의 무기/갑옷이 1:1로 연상되는가?
- 특정 영화 도시 실루엣을 그대로 옮긴 것 같은가?
- 특정 작가 화풍 모사가 결과의 핵심인가?

유사성은 ‘원리’가 아니라 ‘표면 결과’에서 발생하면 수정한다.

---

# 13. Variant Drift Gate

같은 캐릭터 Variant는 다음 5 Face Anchors를 유지한다.
- skull ratio
- eye placement
- nose structure
- jaw/chin
- asymmetry anchor

바뀌는 것은 age/wear/hair/gear/state.

Variant마다 다른 사람처럼 보이면 FAIL.

---

# 14. Final Hard Stops

- C30을 에이든 노년형으로 확정
- 마르칸 생존 Variant
- R03 재주조 완전체 Final
- R06 최종 영웅갑옷
- R10 최종 왕관
- 신수 포획/탑승/장착
- P1 중앙 영웅 기념도시
- 얼굴/몸이 전부 젊고 이상적으로 보이는 cast sheet
