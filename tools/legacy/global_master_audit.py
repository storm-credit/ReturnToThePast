import glob, os, re

files = glob.glob(r'Drafts\Vol_*\Vol_*_Chapter_*.md')
banned_words = ['시스템', '포맷', '물리적인', '데이터', '잿빛', '쥐새끼', '크큭', '오열', '인과율', '뇌수', '퍼억', '우수수', '단말마']

failures = []
total = 0
for f in files:
    total += 1
    with open(f, 'r', encoding='utf-8') as file:
        text = file.read()
    
    kr_cnt = len(re.findall(r'[가-힣]', text))
    if kr_cnt < 3500:
        failures.append(f"Length FAIL: {f} ({kr_cnt} chars)")
        continue
        
    found_banned = []
    for word in banned_words:
        if word in text:
            found_banned.append(word)
    
    if found_banned:
        failures.append(f"Banned Word FAIL: {f} -> {', '.join(found_banned)}")

if len(failures) == 0:
    print(f"PASS GLOBAL MASTER AUDIT PASSED: All {total} chapters verified for Pure Korean Length (>3500) and Banned Words.")
else:
    print(f"FAIL GLOBAL MASTER AUDIT FAILED: {len(failures)} issues found.")
    for fail in failures:
        print(fail)
