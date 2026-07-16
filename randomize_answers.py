import os
import re
import random
from pathlib import Path

def randomize_kawood_file(filepath):
    """Randomize answer positions in a kawood.md file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all questions with their options and answers
    # Pattern: ## Question X: ... options ... Answer: X
    question_pattern = r'(## Question \d+:.*?)(\n\n**Answer: [A-D]\*\*)'
    
    def randomize_question(match):
        question_block = match.group(1)
        answer_line = match.group(2)
        
        # Extract current answer
        current_answer_match = re.search(r'\*\*Answer: ([A-D])\*\*', answer_line)
        if not current_answer_match:
            return match.group(0)
        
        current_answer = current_answer_match.group(1)
        
        # Find all options (A, B, C, D)
        option_pattern = r'- ([A-D])\. (.+?)(?=\n- [A-D]\.|$)'
        options = re.findall(option_pattern, question_block, re.DOTALL)
        
        if len(options) != 4:
            return match.group(0)
        
        # Create mapping: old letter -> new letter
        old_letters = ['A', 'B', 'C', 'D']
        new_letters = ['A', 'B', 'C', 'D']
        random.shuffle(new_letters)
        
        mapping = dict(zip(old_letters, new_letters))
        
        # Replace options with new letters
        modified_block = question_block
        for old_letter in old_letters:
            pattern = rf'- {old_letter}\. '
            new_letter = mapping[old_letter]
            modified_block = modified_block.replace(f'- {old_letter}. ', f'- {new_letter}. ', 1)
        
        # Update answer
        new_answer = mapping[current_answer]
        new_answer_line = f'\n\n**Answer: {new_answer}**'
        
        # Replace explanation if present
        if ' — ' in answer_line:
            explanation = answer_line.split(' — ', 1)[1]
            new_answer_line = f'\n\n**Answer: {new_answer}** — {explanation}'
        
        return modified_block + new_answer_line
    
    # Apply randomization
    modified_content = re.sub(question_pattern, randomize_question, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(modified_content)
    
    return True

# Find all kawood.md files
base_path = Path(r"c:\Users\THE EYE INFORMATIQUE\OneDrive\Desktop\gen-ai-full-course")
kawood_files = list(base_path.rglob("kawood.md"))

print(f"Found {len(kawood_files)} kawood.md files")
for kawood_file in sorted(kawood_files):
    try:
        if randomize_kawood_file(str(kawood_file)):
            print(f"✓ Randomized: {kawood_file.relative_to(base_path)}")
    except Exception as e:
        print(f"✗ Error in {kawood_file}: {e}")

print(f"\nCompleted randomization of {len(kawood_files)} files")
