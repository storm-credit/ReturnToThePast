import glob

files = glob.glob(r'Drafts\Vol_*\Vol_*_Chapter_*.md')

replacements = {
    '시스템': '기괴한 거체계',
    '포맷': '파멸',
    '물리적인': '실체적인',
    '데이터': '기록된 연산',
    '잿빛': '회색',
    '쥐새끼': '끄나풀',
    '크큭': '낮게 웃으며',
    '오열': '비명',
    '단말마': '마지막 숨',
    '퍼억': '둔탁한 파열음',
    '우수수': '무자비하게'
}

count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    orig = content
    for bad, good in replacements.items():
        content = content.replace(bad, good)
        
    if orig != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        count += 1

print("PASS AUTO PURGE BANNED WORDS COMPLETED in " + str(count) + " files.")
