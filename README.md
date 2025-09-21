Dice Roller App
A web-based application featuring a versatile dice roller and the classic "Shut the Box" game. The project is built with a Python/Flask backend and a dynamic JavaScript frontend. The entire application is containerized using Docker for simple and reliable setup.

Live Preview
(Optional: You can take a screenshot of your running application, upload it to a site like Imgur, and paste the link here to make it look even more professional!)

Key Technologies
Backend: Python, Flask

Frontend: HTML, Tailwind CSS, JavaScript

Containerization: Docker, Docker Compose

Features
Dice Roller: Roll any number of dice with any number of sides (e.g., 2d6, 1d20).

Shut the Box: A fully interactive single-player game.

Web GUI: A clean, modern, and responsive user interface.

Containerized: Runs anywhere Docker is installed, with no need to install Python or other dependencies manually.

How to Run This Project
To get this project running locally, please follow these steps.

1. Prerequisites

You must have Docker installed on your system.

You must have Git installed to clone the repository.

2. Clone the Repository

Open your terminal and clone this repository to your local machine:

git clone [https://github.com/chatcharatth-13/dice-roller-project.git](https://github.com/chatcharatth-13/dice-roller-project.git)

3. Navigate to the Directory

cd dice-roller-project

4. Build and Run with Docker Compose

Use this single command to build the Docker image and start the application:

docker-compose up --build

5. Open in Your Browser

Once the container is running, open your favorite web browser and navigate to:

http://localhost:5000
