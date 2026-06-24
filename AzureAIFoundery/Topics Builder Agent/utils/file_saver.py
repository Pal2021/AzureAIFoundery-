# utils/file_saver.py
import os
from datetime import datetime

def save_study_plan(content: str, filename: str = None) -> str:
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"study_plan_{timestamp}.md"
    
    os.makedirs("outputs", exist_ok=True)
    filepath = f"outputs/{filename}"
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"✅ Saved to: {filepath}")
    return filepath