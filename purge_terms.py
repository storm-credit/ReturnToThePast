import glob
import os

files = glob.glob(r'Drafts\Vol_*\Vol_*_Chapter_*.md')
count_ingwa = 0
count_noesu = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    orig_content = content
    content = content.replace('인과율', '섭리')
    content = content.replace('뇌수', '영혼')
    
    if orig_content != content:
        count_ingwa += orig_content.count('인과율')
        count_noesu += orig_content.count('뇌수')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
            
print(f'Replaced 인과율 -> 섭리: {count_ingwa} times.')
print(f'Replaced 뇌수 -> 영혼: {count_noesu} times.')
