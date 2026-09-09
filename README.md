# StudyWise CLI 🚀

StudyWise is an offline-first terminal productivity system combining:
- 📚 Study Planner
- 💰 Expense Tracker
- 🧠 Flashcards with spaced repetition
- 📊 Dashboard and productivity score
- 🔥 XP, levels and streaks

## Requirements
Python 3.10+ recommended.

## Install
```bash
python -m venv venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# If PowerShell blocks scripts:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt
python main.py
```

## Quick demo
Create a subject, add a task, add an expense, create a flashcard deck, add cards, then use the dashboard.

Database: `data/studywise.db` (SQLite, created automatically).
