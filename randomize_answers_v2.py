import os
import re
import random
from pathlib import Path

def randomize_kawood_file(filepath):
    """Randomize answer positions in a kawood.md file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    i = 0
    result_lines = []
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this is a question header
        if line.startswith('## Question'):
            result_lines.append(line)
            i += 1
            
            # Collect the question content until we hit the answer
            question_content = []
            while i < len(lines) and not lines[i].startswith('**Answer:'):
                question_content.append(lines[i])
                i += 1
            
            # Now we're at the answer line
            if i < len(lines) and lines[i].startswith('**Answer:'):
                answer_line = lines[i]
                # Extract the current answer letter
                match = re.search(r'\*\*Answer: ([A-D])\*\*', answer_line)
                if match:
                    current_answer = match.group(1)
                    
                    # Extract options from question_content
                    options_data = []
                    for content_line in question_content:
                        opt_match = re.match(r'^- ([A-D])\. (.+)', content_line)
                        if opt_match:
                            letter = opt_match.group(1)
                            text = opt_match.group(2)
                            options_data.append((letter, text, content_line))
                    
                    if len(options_data) == 4:
                        # Shuffle option letters
                        shuffled = list(range(4))
                        random.shuffle(shuffled)
                        
                        # Create mapping from old position to new letter
                        mapping = {}
                        for old_pos, new_pos in enumerate(shuffled):
                            old_letter = options_data[old_pos][0]
                            new_letter = ['A', 'B', 'C', 'D'][new_pos]
                            mapping[old_letter] = new_letter
                        
                        # Update question content with new letters
                        new_question_content = []
                        for content_line in question_content:
                            opt_match = re.match(r'^- ([A-D])\. (.+)', content_line)
                            if opt_match:
                                old_letter = opt_match.group(1)
                                new_letter = mapping[old_letter]
                                text = opt_match.group(2)
                                new_question_content.append(f'- {new_letter}. {text}')
                            else:
                                new_question_content.append(content_line)
                        
                        # Update answer with new letter
                        new_answer_letter = mapping[current_answer]
                        new_answer_line = answer_line.replace(f'**Answer: {current_answer}**', f'**Answer: {new_answer_letter}**')
                        
                        result_lines.extend(new_question_content)
                        result_lines.append(new_answer_line)
                        i += 1
                    else:
                        result_lines.extend(question_content)
                        result_lines.append(lines[i])
                        i += 1
                else:
                    result_lines.extend(question_content)
                    result_lines.append(lines[i])
                    i += 1
            else:
                result_lines.extend(question_content)
        else:
            result_lines.append(line)
            i += 1
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(result_lines)
    
    return True

# Find all kawood.md files
base_path = Path(r"c:\Users\THE EYE INFORMATIQUE\OneDrive\Desktop\gen-ai-full-course")
kawood_files = list(base_path.rglob("kawood.md"))

print(f"Found {len(kawood_files)} kawood.md files")
success_count = 0
for kawood_file in sorted(kawood_files):
    try:
        if randomize_kawood_file(str(kawood_file)):
            print(f"✓ Randomized: {kawood_file.relative_to(base_path)}")
            success_count += 1
    except Exception as e:
        print(f"✗ Error in {kawood_file}: {e}")

print(f"\nCompleted randomization of {success_count}/{len(kawood_files)} files")
