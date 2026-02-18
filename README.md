# 🚀 AI Career Simulator  
### Microsoft Agents League – Creative Apps Submission  

AI Career Simulator is a gamified full-stack web application that transforms career development into a level-based progression system inspired by RPG mechanics.

Instead of tracking learning passively, users earn XP, level up, and visually see their growth across different technical domains such as Frontend, Backend, AI, and DevOps.

This project demonstrates creative application design powered by GitHub Copilot and built using Flask, SQLite, and Tailwind CSS.

---

# 🎯 Problem It Solves

Most career learning platforms feel static and unmotivating.  
Progress is often linear and lacks emotional engagement.

AI Career Simulator introduces:

- 🎮 Game-style progression  
- 📈 Visual XP tracking  
- 🏆 Level-based growth  
- 🧠 Skill-category tracking  
- 💾 Persistent progress storage  

It turns career growth into a rewarding interactive experience.

---

# 🧠 Core Features

- Advanced scalable XP engine
- Lifetime cumulative XP tracking
- Level progression with 1.5x XP scaling
- Multi-track XP categories:
  - Frontend
  - Backend
  - AI
  - DevOps
- Persistent SQLite database
- Clean Flask architecture
- Gamified UI with animated progress bars
- Secure SQL parameterized queries

---

# 🎮 XP Engine Architecture

## 🔹 Lifetime XP Model

XP is stored as cumulative lifetime XP.

Level is calculated dynamically based on total XP.

---

## 🔹 Level Scaling Formula

- Level 1 → 100 XP
- Each next level requires 1.5× the previous level

Example:

Level 1 → 100 XP  
Level 2 → 150 XP  
Level 3 → 225 XP  
Level 4 → 337 XP  
Level 5 → 506 XP  

This creates exponential growth difficulty similar to RPG systems.

---

## 🔹 Progress Calculation

The engine calculates:

- Current Level
- XP in current level
- XP required for next level
- Progress percentage

All computed dynamically using the XP engine module.

---

# 🗄 Database Schema

SQLite database (`career.db`)

Table: `users`

Fields:

- id (Primary Key)
- username
- total_xp
- level
- frontend_xp
- backend_xp
- ai_xp
- devops_xp
- created_at

XP is updated safely using parameterized queries.

---

# 🏗 Tech Stack

Backend:
- Python
- Flask
- SQLite

Frontend:
- Tailwind CSS
- Jinja Templates

Development Assistant:
- GitHub Copilot

---

# 🔒 Security & Best Practices

- .env excluded via .gitignore
- No API keys committed
- SQL injection protected with parameterized queries
- Modular architecture (database, xp_engine, app separated)
- Clean commit history

---

# 🤖 GitHub Copilot Usage (Required Documentation)

GitHub Copilot was meaningfully used throughout development in the following areas:

## 1️⃣ XP Algorithm Development

Copilot assisted in:
- Generating level-scaling logic
- Structuring XP progression loops
- Designing progress percentage calculation

## 2️⃣ Database Initialization

Copilot helped scaffold:
- SQLite schema creation
- Demo user insertion logic
- Safe conditional creation checks

## 3️⃣ Flask Routing

Copilot accelerated:
- Route structure design
- Dynamic XP update routes
- Redirect logic
- Template rendering patterns

## 4️⃣ UI Design

Copilot provided:
- Tailwind layout suggestions
- Progress bar structure
- Responsive container setup
- Button styling variations

## 5️⃣ Debugging Support

Copilot Chat assisted in:
- Resolving Flask import issues
- Fixing database schema resets
- Debug mode configuration
- XP miscalculation troubleshooting

---

# 💡 How Copilot Enhanced Creativity

Copilot did not replace architectural decisions.  
Instead, it:

- Accelerated boilerplate generation
- Reduced debugging friction
- Enabled rapid experimentation
- Helped iterate on XP logic faster
- Suggested structural improvements

The creative direction, system design, and game mechanics were human-designed, while Copilot acted as a development accelerator.

# 👤 Author

Madhu Sudhan  
AI Career Simulator  
Microsoft Agents League – Creative Apps Track  
2026