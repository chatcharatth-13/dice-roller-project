# 🎲 Dice Roller Project (Web + Docker)

A browser-based toolkit featuring:
- **Dice Roller** — roll any number of dice with any number of sides using `XdY` notation (e.g., `2d6`, `1d20`).
- **Shut the Box** — the classic dice-and-tiles game, now playable in your browser with save/load support.

Built with **Flask** for the backend and **HTML/CSS/JavaScript** for the frontend.  
Fully containerized for easy deployment with **Docker** or **Docker Compose**.

---

## 📦 Features

### Dice Roller
- Supports `roll` for a single 6‑sided die.
- Supports `roll XdY` for custom dice rolls.
- Displays individual results and total sum.

### Shut the Box
- 1–12 tile version.
- Rolls two dice each turn.
- Click tiles to select them; must match the roll sum.
- Saves progress automatically (`savegame.json`).
- Detects win/loss conditions.

---

## 📂 Project Structure

<pre>```project/ │ ├── 🐍 app.py               # Flask backend (routes for Dice Roller & Shut the Box) ├── 🧠 game_logic.py        # Core game logic (shared between CLI & web) │ ├── 📁 templates/           # HTML templates │   └── 🖥 index.html        # Main web UI with tabs for both games │ ├── 📁 static/              # Optional CSS/JS/image assets │ ├── 📜 requirements.txt     # Python dependencies ├── 🐳 Dockerfile           # Container build instructions ├── ⚙ docker-compose.yml    # Multi-container orchestration ├── 🚫 .dockerignore        # Files/folders excluded from Docker builds └── 📖 README.md            # Project documentation```</pre>

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/chatcharatth-13/dice-roller-project.git
cd dice-roller-project

2. Install dependencies (local run)
pip install -r requirements.txt


3. Run locally
python app.py


Visit: http://localhost:5000

🐳 Running with Docker
Build and run
docker-compose up --build


Then open: http://localhost:5000
Development mode (auto-reload)
If your docker-compose.yml mounts the project folder:
docker-compose up


Flask will reload when you edit files.

⚙ Configuration
- Port: Defaults to 5000 inside the container, mapped to 5000 on your host.
- Save file: savegame.json stores Shut the Box progress.
- In production, it’s excluded via .dockerignore for a fresh start each run.
- In development, comment it out in .dockerignore to persist progress.

🛠 Tech Stack
- Backend: Python 3 + Flask
- Frontend: HTML, CSS, JavaScript (vanilla)
- Containerization: Docker, Docker Compose

🎯 Usage
Dice Roller
- Select the Dice Roller tab.
- Enter a command:
- roll → roll 1d6
- roll 2d6 → roll two six-sided dice
- roll 1d20 → roll one twenty-sided die
- Click Roll to see results.
Shut the Box
- Select the Shut the Box tab.
- Click Start New Game.
- Click Roll Dice each turn.
- Click tiles to select them so their sum matches the roll.
- Click Submit Move to confirm.
- Win by shutting all tiles; lose if no moves are possible.

👤 Author
Chatcharat (Knight) 
Vejwasu (Earth)
