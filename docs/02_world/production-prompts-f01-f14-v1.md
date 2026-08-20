# Faction Visual Production Prompts — F01–F14 v1

Status: **D16.3 MODEL-AGNOSTIC PROMPT PACK**  
Rule: 세력은 로고/색이 아니라 `shape grammar + material grammar + behavioral mark` 중 최소 2개로 식별한다.

공통 suffix:
`institutional visual language embedded in clothing, tools, architecture and behavior, no giant logo dependency, no faction color uniformity, practical fantasy materials, no direct franchise imitation`

---

## F01 왕실 중앙유지파

### Core Prompt
`central royal institution using closed circular forms with one controlled connection point, brass and red sealing wax integrated into approval tools and corridors, documents and movement visibly oriented toward a single center`

### Silent Read
닫힌 고리형 구조 / 중앙으로 정렬된 통로 / 승인슬롯.

### Corruption Variant
`circle closes further and physically covers other seal slots`

### DO NOT
`giant crown logo, everyone in royal blue, generic gold palace uniforms`

---

## F02 성당 정통력파

### Core Prompt
`civic religious institution where ritual and daily care occupy the same structures, triple wound-line geometry repeated in practical objects, lime plaster, clinic cloth and bell alloy, subgroup differences expressed through treatment marks, calendar scales or closing-line doctrine`

### DO NOT
`cross-shaped direct religious copy, all-white clergy, holy light aura, cathedral-only identity`

---

## F03 마탑 계산연합

### Core Prompt
`calculation institution using crossed axes and visible uncertainty ranges, observation glass, brass and thin record plates, workers marking ranges rather than single answers`

### Corruption Variant
`contract faction erases uncertainty bands and leaves one clean number`

### DO NOT
`wizard tower star symbols, glowing equations, purple robe uniform`

---

## F04 대기록소·주소관료단

### Core Prompt
`record bureaucracy using layered text blocks, correction marks, paper, thread, wax and wooden cases, original/revised/testimony copies physically stored in different forms`

### Corruption Variant
`unregistered person is represented by removal of the field itself, not merely an empty name`

### DO NOT
`giant book logo, magic archive, identical scribe robes`

---

## F05 국경 고정환 수비연합

### Core Prompt
`frontier defense institution using an open ring that contains fortress and village marks side by side, iron, timber, stabilization plates and warning cloth, every command token paired with a revocation-condition token`

### DO NOT
`military shield logo as sole identity, national-army uniform clone, heavy knight aesthetic`

---

## F06 서부 변경개혁연합

### Core Prompt
`reform coalition represented by overlapping local address boards, open circular structures and many small testimony points, repaired stone, regional textiles and copied ledgers, multiple village marks carried together instead of one flag`

### DO NOT
`rebel red flag faction, revolutionary uniform, heroic resistance logo`

---

## F07 복원파

### Core Prompt
`restoration movement using attempted complete circles stitched from family records, old uniform fragments and preserved photographs, repeated recording of vanished names, emotionally careful but capable of covering current-life markers`

### Extreme Variant
`repair seam expands until present-day markers are physically obscured`

### DO NOT
`cult masks, evil restorationists, ghost aesthetic, perfect nostalgia sepia`

---

## F08 F1 군정

### Core Prompt
`military administration based on rectangular zone grids and numbered cells, matte military boards, ration tokens and propaganda sheets, people categorized by sector before names`

### DO NOT
`fascist visual shorthand copied wholesale, black-red villain palette dependency, futuristic hologram command room`

---

## F09 자유해안 계약동맹

### Core Prompt
`coastal contract alliance using open wave lines and practical contract knots, waterproof cloth, salt plates and verdigris bronze, marks repeated along routes rather than borders`

### DO NOT
`pirate federation, anchor logo everywhere, navy-uniform monoculture`

---

## F10 북부 공방동맹

### Core Prompt
`workshop alliance proud of visible joints, replacement plates and repair history, iron, leather, impure crystal and workshop stamps, completed objects display maintenance access rather than polished perfection`

### DO NOT
`steampunk gear logo, dwarf guild stereotype, glowing forge symbols`

---

## F11 라하크 이동단 협의회

### Core Prompt
`mobile council whose identity is an unclosed route line and practical knots, layered travel cloth and natural fibers, route itself functioning as the mark rather than fixed flag`

### DO NOT
`tribal fantasy pattern, feather standard, animal totem, exotic nomad costume`

---

## F12 네바르 장례법정

### Core Prompt
`funerary legal institution using an empty center and thin verdict cords, matte cloth, incomplete crystals and restrained metal frames, separate visual marks for death, absence and erasure`

### DO NOT
`skull court, necromancer faction, gothic death cult, black aura`

---

## F13 백지권 권리연합

### Core Prompt
`rights coalition using lines that continue despite missing sections and multiple testimony points, repaired cloth, wooden boards and current-life household objects, present living evidence placed ahead of old documents`

### DO NOT
`white mystical faction, refugee uniform, blank-mask symbolism`

---

## F14 F3 연대개입산업연합

### Core Prompt
`time-intervention industry using modular seals arranged by function, dust-resistant cloth, standardized metal and replaceable contract plates, benefit and military contracts sharing the same physical connector as a troubling visual clue`

### Corruption Variant
`more contract modules occupy the same standardized sockets, functional efficiency increases while ownership concentration becomes visible`

### DO NOT
`cyberpunk corporation neon, sleek black techwear, hologram logo wall, sci-fi megacorp imitation`

---

# Faction Silent Language Board

제작 시 각 세력당 4컷:
1. 사람의 옷 일부
2. 사용도구
3. 실내/건축 일부
4. 행동 장면

**세력명·문장·대표색을 제거한 뒤** 14개 중 최소 10개는 2개 이상의 단서로 식별 가능해야 한다.

# Cross-Cluster Tests

- CENTRAL: F01/F02/F03/F04 — 왕실/생활의례/계산/기록 분리
- EDGE RIGHTS: F05/F06/F13 — 군사/개혁/현재권리 분리
- MOBILE: F09/F11 — 해상계약/육상이동 분리
- MATERIAL & DEATH: F10/F12 — 물질수리/장례법 분리
- FUTURE POWER: F08/F14 — 구역군정/모듈산업 분리

색을 grayscale로 제거했을 때 cluster 내부 세력이 다시 합쳐지면 FAIL.
