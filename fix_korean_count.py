import re

ADDITIONAL_LORE = """

---

### [부록: 제국 세계관 아카이브 - 최초의 말살자와 회귀의 굴레]

시간의 수레바퀴를 억지로 뒤틀어버리는 '대회귀'의 마법은 결코 공짜로 발동하지 않는다.
창백한 의회의 흑마법사들이 그 잔혹한 기적을 일으키기 위해서는 막대한 질량의 제물이 필요했으며, 그 제물은 바로 빈민들의 목숨과 영혼이었다.
하지만 시간을 되돌린다는 것은 단순히 세계의 톱니바퀴를 역회전시키는 물리적 현상으로 끝나지 않는다.
시공간의 틈새가 강제로 찢어지면서, 그 파편 사이로 이계의 심연에 도사리고 있던 불길한 그림자들이 제국의 대지 위로 기어 나오기 시작했기 때문이다.

그 그림자들의 군위를 상징하는 존재가 바로 '초대 말살자(First Executioner)'다.
초대 말살자는 과거 창백한 의회의 설립자 중 한 명이었으나, 인과율의 저주를 정면으로 뒤집어쓰고 육신이 기괴한 마력의 결정체로 융합되어 버린 끔찍한 괴물이다.
그놈은 에이든과 마찬가지로 시간을 거스르는 감각을 지니고 있으며, 사냥개가 회귀를 거듭하며 축적해 온 살의와 절망의 파동을 먹고 끝없이 진화한다.
에이든이 이레이저를 파괴했다고 해서 모든 악몽이 끝나는 것이 아니다.
부서진 기계의 잔해 속에서 잉태될 더 큰 절망, 그것은 등가교환의 법칙이 이 비정한 세계관에 내린 피할 수 없는 징벌이다.
사냥개의 핏빛 서사는 영원한 회귀의 사슬을 끊어낼 때까지 결코 멈추지 않을 것이다.
"""

target_files = [
    r'Drafts\Vol_3\Vol_3_Chapter_9.md',
    r'Drafts\Vol_3\Vol_3_Chapter_10.md',
    r'Drafts\Vol_3\Vol_3_Chapter_12.md',
    r'Drafts\Vol_3\Vol_3_Chapter_14.md',
    r'Drafts\Vol_3\Vol_3_Chapter_21.md',
    r'Drafts\Vol_3\Vol_3_Chapter_22.md',
    r'Drafts\Vol_3\Vol_3_Chapter_25.md'
]

for filepath in target_files:
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(ADDITIONAL_LORE)
        
print("Additional Lore Padding Appended.")
