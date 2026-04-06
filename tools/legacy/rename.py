import os
import re

directories = [
    r'c:\Users\Storm Credit\Desktop\lorebookmaker\My_Novel_Projects\나는_과거로_간다\Drafts\Vol_1',
    r'c:\Users\Storm Credit\Desktop\lorebookmaker\My_Novel_Projects\나는_과거로_간다\outline'
]

target_name = '칼슨'

for directory in directories:
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = re.sub(r'레이먼(?!드)', target_name, content)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f'Updated: {filepath}')
