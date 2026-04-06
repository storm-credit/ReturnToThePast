import glob
import re

files = glob.glob(r'Drafts\Vol_*\Vol_*_Chapter_*.md')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    # Apply the same literary structure polishing from V3
    blocks = content.split('\n\n')
    new_blocks = []
    temp_quotes = []
    in_quote = False
    
    for block in blocks:
        block = block.strip()
        if not block:
            continue
            
        if block.startswith('#') or block.startswith('***') or block.startswith('---'):
             new_blocks.append(block)
             continue
             
        # Merge separated single \n blocks if they are non-dialogue wall-of-texts
        # Wait, the literary_polish_vol3.py logic was:
        lines = block.split('\n')
        merged_lines = []
        for line in lines:
            line = line.strip()
            if not line: continue
            merged_lines.append(line)
        
        for line in merged_lines:
            if line.startswith('"'):
                in_quote = True
                temp_quotes.append(line)
                if line.endswith('"'):
                    in_quote = False
                    new_blocks.append(' '.join(temp_quotes))
                    temp_quotes = []
            elif in_quote:
                temp_quotes.append(line)
                if line.endswith('"'):
                    in_quote = False
                    new_blocks.append(' '.join(temp_quotes))
                    temp_quotes = []
            else:
                new_blocks.append(line)
                
    final_text = '\n\n'.join(new_blocks) + '\n'
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(final_text)

print(f"PASS GLOBAL FORMATTING SYNC COMPLETED: {len(files)} chapters synchronized to V3 hardboiled rhythm.")
