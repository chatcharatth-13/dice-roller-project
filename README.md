# 🎲 Dice Roller Project (Web + Docker)

A browser-based toolkit featuring:
- **Dice Roller** — roll any number of dice with any number of sides using `XdY` notation (e.g., `2d6`, `1d20`).
- **Shut the Box** — the classic dice-and-tiles game, now playable in your browser with save/load support.

Built with **Flask** for the backend and **HTML** for the frontend.  
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

## 🚀 Getting Started

### 1. Clone the repository
`bash
git clone https://github.com/chatcharatth-13/dice-roller-project.git`

`cd dice-roller-project`

### 2. Install dependencies (local run)
pip install -r requirements.txt


### 3. Run locally
python app.py


Visit: http://localhost:5000

## 🐳 Running with Docker
Build and run
`docker-compose up --build`


Then open: http://localhost:5000
Development mode (auto-reload)
If your docker-compose.yml mounts the project folder:
docker-compose up


Flask will reload when you edit files.

## ⚙ Configuration
- Port: Defaults to 5000 inside the container, mapped to 5000 on your host.
- Save file: savegame.json stores Shut the Box progress.
- In production, it’s excluded via .dockerignore for a fresh start each run.
- In development, comment it out in .dockerignore to persist progress.

## 🛠 Tech Stack
- Backend: Python 3 + Flask
- Frontend: HTML
- Containerization: Docker, Docker Compose

## 🎯 Usage
* **Dice Roller**
   *Select the Dice Roller tab.
   * Enter a command:
   * roll → roll 1d6
   * roll 2d6 → roll two six-sided dice
   * roll 1d20 → roll one twenty-sided die
   * Click Roll to see results.
* **Shut the Box**
   * Select the Shut the Box tab.
   * Click Start New Game.
   * Click Roll Dice each turn.
   * Click tiles to select them so their sum matches the roll.
   * Click Submit Move to confirm.
   *  Win by shutting all tiles; lose if no moves are possible.

## 👤 Authors
**Chatcharat Thongsuepsai (Knight)**
* **Self Grade**
    * Contribution: 10
    * Communication: 7
    * Collaboration: 9
* **Peer Grade**
    * Contribution: 10
    * Communication: 8
    * Collaboration: 9
* **Weighted Average by Source: Self Grade: 30% (0.3), Peer Grade: 70% (0.7)**
    * Avg Self Grade: 8.67
    * Avg Peer Grade: 9.00
    * Final Weighted Score: 8.90

**Vejwasu Boonyor (Earth)**
* **Self Grade**
    * Contribution: 8
    * Communication: 8
    * Collaboration: 8
* **Peer Grade**
    * Contribution: 7
    * Communication: 8
    * Collaboration: 9
* **Weighted Average by Source: Self Grade: 30% (0.3), Peer Grade: 70% (0.7)**
    * Avg Self Grade: 8.00
    * Avg Peer Grade: 8.00
    * Final Weighted Score: 8.00

## 🎲 Colab Notebooks & Presentation
* **Sprint 1:** [Week1/Sprint1 Colab](https://colab.research.google.com/drive/1FnTkxwaipIMXnhL8Zisg0tnQbo4AgA-A?usp=sharing)
* **Sprint 2:** [Week2/Sprint2 Colab](https://colab.research.google.com/drive/1BmnGrpV152t0dT1SCXXN_6GWZbAIr8k2?usp=sharing)
* **Sprint 3:** [Week3/Sprint3 Colab](https://colab.research.google.com/drive/1RV4uUEZhyXVIww9SW9dtGm42ey54vNgm?usp=sharing)
* **Final Project:** [Sprint Final Colab](https://colab.research.google.com/drive/1okmOfQbHJQev_9RU1s4cc0qT1gG7Sg4a?usp=sharing)

* **Presentation:** [Canva](https://www.canva.com/design/DAGzu-J97zw/A0-jPUkiQnLRqUEMIrgX6A/view?utm_content=DAGzu-J97zw&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=he61e4618f9)

