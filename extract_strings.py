import os
import re

def extract_strings():
    pattern1 = re.compile(r'_\(["\'](.*?)["\']\)')
    pattern2 = re.compile(r'\{%\s*trans\s+["\'](.*?)["\']\s*%\}')
    
    strings = set()
    
    for root, _, files in os.walk('.'):
        if 'env' in root or 'venv' in root or '.git' in root or '__pycache__' in root:
            continue
        for file in files:
            if file.endswith('.py') or file.endswith('.html'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    strings.update(pattern1.findall(content))
                    strings.update(pattern2.findall(content))
                    
    with open('strings.txt', 'w', encoding='utf-8') as out:
        for s in sorted(strings):
            out.write(s + '\n')

if __name__ == '__main__':
    extract_strings()
