import os
import re
import glob

# Harness Configuration
DRAFT_DIR = r"c:\Users\Storm Credit\Desktop\lorebookmaker\My_Novel_Projects\나는_과거로_간다\Drafts\Vol_3"
REPORT_PATH = r"c:\Users\Storm Credit\.gemini\antigravity\brain\46e57acf-bba6-4897-80d2-7ec33e0033f7\Batch_Audit_Report_Vol_3.md"

BANNED_WORDS = ['잿빛', '뱀눈', '쥐새끼', '시스템', '포맷', '데이터', '물리적인']
REGEX_RULES = [
    (r"(\d+)\s*(회차|번째\s*회귀)", "정확한 횟수 카운팅 금지 규칙 위반")
]

# Length Rule: 3500 characters WITHOUT spaces
MIN_LENGTH_NO_SPACES = 3500

def get_chapter_number(filename):
    match = re.search(r'Vol_3_Chapter_(\d+)\.md', filename)
    if match:
        return int(match.group(1))
    return 0

def run_audit():
    files = glob.glob(os.path.join(DRAFT_DIR, "Vol_3_Chapter_*.md"))
    files = [f for f in files if 1 <= get_chapter_number(os.path.basename(f)) <= 25]
    files.sort(key=lambda x: get_chapter_number(os.path.basename(x)))

    report_lines = []
    report_lines.append(f"# 🛡️ Agent Harness: Batch Execution Log (Volume 3)\n")
    report_lines.append(f"**실행 일시:** 2026-03-23\n")
    report_lines.append(f"**점검 범위:** 총 {len(files)}개 초안\n")
    report_lines.append(f"**적용 Rule:** 분량(공백 제외 최소 {MIN_LENGTH_NO_SPACES}자), 금지어({', '.join(BANNED_WORDS)}), 정규식(회차 카운팅)\n\n---\n")

    total_failures = 0

    for file_path in files:
        filename = os.path.basename(file_path)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # char count without spaces/newlines
        content_no_spaces = re.sub(r'\s+', '', content)
        char_count = len(content_no_spaces)
        char_count_with_spaces = len(content)
        
        failures = []
        
        # 1. Length Check
        if char_count < MIN_LENGTH_NO_SPACES:
            failures.append(f"❌ **분량 부족:** 공백 제외 {char_count} / {MIN_LENGTH_NO_SPACES} 자 (공백 포함 {char_count_with_spaces}자)")
        
        # 2. Banned Words Check
        found_banned = []
        for word in BANNED_WORDS:
            if word in content:
                found_banned.append(word)
        if found_banned:
            failures.append(f"🚫 **금지어 검출:** {', '.join(found_banned)}")
            
        # 3. Regex Rule Check
        for regex, msg in REGEX_RULES:
            matches = re.finditer(regex, content)
            found_matches = [m.group(0) for m in matches]
            if found_matches:
                failures.append(f"🛑 **Rule 위반 ({msg}):** {', '.join(found_matches)}")

        if failures:
            total_failures += 1
            status = "🔴 [FAIL]"
            report_lines.append(f"### {status} {filename}")
            for fail in failures:
                report_lines.append(f"- {fail}")
        else:
            status = "🟢 [PASS]"
            report_lines.append(f"### {status} {filename} (공백 제외 {char_count}자)")
            report_lines.append(f"- 모든 Rule 및 Hook 검증 통과 완료.")
        
        report_lines.append("\n")

    report_lines.append(f"---\n")
    report_lines.append(f"### 📊 종합 결과: 총 {len(files)} 챕터 중 **{total_failures}개 챕터에서 Rule 위반 감지**\n")

    with open(REPORT_PATH, 'w', encoding='utf-8') as f:
        f.write("\n".join(report_lines))

if __name__ == "__main__":
    run_audit()
