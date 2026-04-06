import glob, re

files = glob.glob(r'Drafts\Vol_*\Vol_*_Chapter_*.md')
failures = []
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        text = file.read()
    kr_cnt = len(re.findall(r'[가-힣]', text))
    if kr_cnt < 3500:
        failures.append((f, kr_cnt))

print(f"Total chapters checked: {len(files)}")
print(f"Files under 3500 pure Korean characters: {len(failures)}")

failures.sort()
for f, cnt in failures:
    print(f"{f}: {cnt}")
