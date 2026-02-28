# 🚀 AI Career Simulator

AI Career Simulator is a gamified web application that simulates career progression using XP, levels, and mission-based growth.

Built using Flask, SQLite, Tailwind CSS, and GitHub Copilot assistance.

---

## 🎯 Features

- XP-based progression system
- Dynamic level scaling algorithm
- Track-based mission generation
- Persistent SQLite database
- Game-style UI (XP bar, levels)
- AI Career Mission Generator
- Multi-track system:
  - Frontend
  - Backend
  - AI
  - DevOps

---

## 🧠 XP & Level System

- Starts at Level 1
- 100 XP required for first level
- XP requirement increases by 1.5x each level
- Progress bar dynamically updates
- XP stored persistently in SQLite database

The level calculation uses a scaling progression model to simulate real-world career growth complexity.

---

## 🤖 AI Career Mission Generator

Missions are dynamically generated based on:

- Selected career track
- Current user level

Each mission completion rewards XP and updates the level accordingly.

This creates a gamified simulation of career progression.

---

## 🛠 Tech Stack

- Python 3
- Flask
- SQLite
- Tailwind CSS
- GitHub Copilot

---

## 🤖 GitHub Copilot Usage

GitHub Copilot was used throughout development to:

- Generate Flask route scaffolding
- Assist in SQLite schema creation
- Suggest level progression logic
- Help structure mission generation engine
- Assist in debugging XP update issues
- Provide Tailwind UI structure suggestions

All Copilot suggestions were reviewed, tested, and modified where necessary to ensure correctness and performance.

---

## 🔒 Security Practices

- No secrets stored in repository
- No API keys exposed
- Local SQLite database used for persistence
- Clean project structure
- No hardcoded credentials

---

## ▶️ How to Run

1. Clone repository:

```bash
git clone <your-repo-link>
```

2. Navigate into project:

```bash
cd AI-Career-Simulator
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run application:

```bash
python app.py
```

5. Open browser:

```
http://127.0.0.1:5000
```

---

## 📌 Project Purpose

This project was built as part of the Microsoft Agents League Creative Apps track, demonstrating:

- Creative AI-assisted application development
- Gamified UI/UX design
- Backend engineering with Flask
- Persistent data handling with SQLite
- Responsible and documented use of GitHub Copilot

---

## 👨‍💻 Developer

Madhu Sudhan