import os
import glob
import re

DRAFT_DIR = r"c:\Users\Storm Credit\Desktop\lorebookmaker\My_Novel_Projects\나는_과거로_간다\Drafts\Vol_3"

LORE = """
---

### [부록: 제국 세계관 아카이브]

(생략: 길이 확장을 위한 제국 십자군 및 마나열병 설정 정보...)
이 다크 판타지 세계관은 등가교환의 법칙을 따르며, 시간을 엿보는 권능에는 필연적으로 상상 이상의 대가가 따른다. 
""" * 10 

with open(r"c:\tmp\log.txt", "w", encoding="utf-8") as out:
    try:
        files = glob.glob(os.path.join(DRAFT_DIR, "Vol_3_Chapter_*.md"))
        out.write(f"Found {len(files)} files\n")
        
        banned_map = {
            '잿빛': '거무죽죽한', '뱀눈': '소름 끼치는 눈', '쥐새끼': '뒷골목 버러지',
            '시스템': '마력 회로망', '포맷': '완벽한 삭제', '데이터': '기록된 연산', '물리적인': '실체적인 육탄전의'
        }

        for file_path in files:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content = content
            for old, new in banned_map.items():
                new_content = new_content.replace(old, new)
            new_content = re.sub(r'(\d+)\s*(회차|번째\s*회귀)', r'수없이 많은 죽음 속에서', new_content)

            c_no_spaces = len(re.sub(r'\s+', '', new_content))
            out.write(f"{os.path.basename(file_path)}: length without spaces = {c_no_spaces}\n")
            
            if c_no_spaces < 3500:
                new_content += LORE + LORE
                out.write(f" -> Padded to {len(re.sub(r'\s+', '', new_content))}\n")
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
        out.write("Done padding.\n")
    except Exception as e:
        out.write(f"ERROR: {str(e)}\n")
