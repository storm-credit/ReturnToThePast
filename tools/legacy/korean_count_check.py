import glob, re

files = glob.glob(r'Drafts\Vol_3\Vol_3_Chapter_*.md')
failures = []
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        text = file.read()
    kr_cnt = len(re.findall(r'[가-힣]', text))
    if kr_cnt < 3500:
        failures.append((f, kr_cnt))

failures.sort(key=lambda x: int(re.search(r'\d+', x[0].split('_')[-1]).group()))

print(f"Total files checked: {len(files)}")
print(f"Files under 3500 pure Korean characters: {len(failures)}")
for f, cnt in failures:
    print(f"{f}: {cnt}")
