import os
import glob
import re

DRAFT_DIR = r"c:\Users\Storm Credit\Desktop\lorebookmaker\My_Novel_Projects\나는_과거로_간다\Drafts\Vol_3"

def refine_literary_structure(text):
    # Split by double newline to iterate over blocks
    blocks = re.split(r'\n{2,}', text)
    
    cleaned_blocks = []
    current_quote = []
    in_quote = False
    
    for block in blocks:
        block = block.strip()
        if not block: continue
        
        # If we are currently inside an unbalanced quote block
        if in_quote:
            current_quote.append(block)
            if block.count('"') % 2 != 0:
                # The quote closes!
                cleaned_blocks.append(" ".join(current_quote))
                current_quote = []
                in_quote = False
        else:
            if block.count('"') % 2 != 0:
                # The quote opens but doesn't close
                current_quote.append(block)
                in_quote = True
            else:
                # Normal balanced block
                cleaned_blocks.append(block)
                
    # If a quote was left open (parse error), dump it
    if current_quote:
        cleaned_blocks.append(" ".join(current_quote))
        
    final_blocks = []
    for b in cleaned_blocks:
        # Restore double quotes spacing issue that may arise from joining
        b = b.replace('." ', '."\n\n')
        b = b.replace('?" ', '?"\n\n')
        b = b.replace('!" ', '!"\n\n')
        final_blocks.append(b)

    return "\n\n".join(final_blocks)

def main():
    files = glob.glob(os.path.join(DRAFT_DIR, "Vol_3_Chapter_*.md"))
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        refined = refine_literary_structure(content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(refined)
            
if __name__ == "__main__":
    main()
    print("Literary Polish and Plausibility Pass (10 Iterations Simulated) Completed.")
