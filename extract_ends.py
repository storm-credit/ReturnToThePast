import glob

files = [
    r'Drafts\Vol_3\Vol_3_Chapter_9.md',
    r'Drafts\Vol_3\Vol_3_Chapter_10.md',
    r'Drafts\Vol_3\Vol_3_Chapter_12.md',
    r'Drafts\Vol_3\Vol_3_Chapter_14.md',
    r'Drafts\Vol_3\Vol_3_Chapter_21.md',
    r'Drafts\Vol_3\Vol_3_Chapter_22.md',
    r'Drafts\Vol_3\Vol_3_Chapter_25.md'
]

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    idx = content.find('### [부록: 제국 세계관 아카이브')
    if idx != -1:
        pure_content = content[:idx]
        lines = pure_content.strip().split('\n')
        print(f'--- {f} ---')
        print('\n'.join(lines[-10:]))
        print('=============================')
