#!/usr/bin/env python3
"""Randomize answer keys in kawood.md files line by line."""

import re
import random
from pathlib import Path

def randomize_kawood_answers():
    root_dir = Path(r"c:\Users\THE EYE INFORMATIQUE\OneDrive\Desktop\gen-ai-full-course")
    kawood_files = sorted(list(root_dir.glob("**/kawood.md")))
    print(f"Found {len(kawood_files)} kawood.md files")
    
    for kawood_file in kawood_files:
        try:
            randomize_file(kawood_file)
            print(f"✓ {kawood_file.relative_to(root_dir)}")
        except Exception as e:
            print(f"✗ {kawood_file.name}: {e}")

def randomize_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by "## Question" to process each question
    parts = content.split("## Question")
    if len(parts) <= 1:
        return
    
    # Keep the header
    new_content = parts[0]
    
    for i in range(1, len(parts)):
        part = "## Question" + parts[i]
        new_part = randomize_question_block(part)
        new_content += new_part
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

def randomize_question_block(block):
    lines = block.split('\n')
    new_lines = []
    i = 0
    
    # Add question header and description
    while i < len(lines) and not lines[i].startswith('- A.') and not lines[i].startswith('- B.') and not lines[i].startswith('- C.') and not lines[i].startswith('- D.'):
        new_lines.append(lines[i])
        i += 1
    
    # Collect 4 options
    options = []
    while i < len(lines) and (lines[i].startswith('- A.') or lines[i].startswith('- B.') or lines[i].startswith('- C.') or lines[i].startswith('- D.')):
        opt = lines[i]
        options.append(opt)
        i += 1
    
    # Find answer
    answer_letter = None
    while i < len(lines):
        if lines[i].startswith('**Answer:'):
            match = re.search(r'\*\*Answer: ([A-D])\*\*', lines[i])
            if match:
                answer_letter = match.group(1)
            break
        i += 1
    
    if len(options) == 4 and answer_letter:
        # Get text of correct option
        correct_text = None
        for opt in options:
            if opt[2] == answer_letter:
                correct_text = opt[4:]  # Skip "- X. "
                break
        
        # Shuffle options
        random.shuffle(options)
        
        # Find new position of correct answer
        new_letter = None
        for idx, opt in enumerate(options):
            if opt[4:] == correct_text:
                new_letter = chr(ord('A') + idx)
                break
        
        # Rewrite options with new letters
        new_options = []
        for idx, opt in enumerate(options):
            new_letter_char = chr(ord('A') + idx)
            new_opt = f"- {new_letter_char}. {opt[4:]}"
            new_options.append(new_opt)
        
        new_lines.extend(new_options)
        new_lines.append('')  # Blank line
        
        # Add updated answer
        while i < len(lines):
            if lines[i].startswith('**Answer:'):
                new_lines.append(f"**Answer: {new_letter}**")
                i += 1
                break
            new_lines.append(lines[i])
            i += 1
    else:
        new_lines.extend(options)
    
    # Add remaining lines
    while i < len(lines):
        new_lines.append(lines[i])
        i += 1
    
    return '\n'.join(new_lines)

if __name__ == "__main__":
    random.seed(None)
    randomize_kawood_answers()
    print("\n✅ All kawood.md files randomized!")
