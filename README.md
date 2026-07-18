# 🚀 AI Career Copilot

> A Multi-Agent AI Career Assistant that helps users identify internship opportunities, analyze skill gaps, generate personalized preparation strategies, build resumes, create daily study plans, and automate reminders.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![n8n](https://img.shields.io/badge/n8n-Workflow-EA4B71?logo=n8n)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-v1.0.0-blue)

---

## 📌 Overview

AI Career Copilot is a **multi-agent AI system** built using **Python** and **n8n** to automate internship planning and career preparation.

The system analyzes a user's skills, career goals, preparation timeline, and experience level to generate a personalized roadmap for landing internships. It also creates daily study schedules and sends reminder emails to help users stay consistent throughout their preparation.

This project was developed as part of the **Agentic AI Workshop Hackathon**.

---

## ✨ Features

### 🤖 Agent 1 – Internship Strategy Agent

- Matches users with relevant internship opportunities
- Analyzes required skills and identifies skill gaps
- Recommends companies and roles
- Generates personalized preparation strategies
- Builds resumes tailored to selected roles
- Provides internship application links and career guidance

### 📅 Agent 2 – Daily Planner Agent

- Converts preparation strategy into daily tasks
- Prioritizes tasks based on importance
- Estimates time required for each task
- Generates a structured daily study schedule
- Sends reminder emails through n8n automation

---

## ⚙️ Workflow

```text
                 User
                  │
                  ▼
           n8n Webhook
                  │
                  ▼
     Internship Strategy Agent
                  │
                  ▼
      Personalized Strategy
                  │
                  ▼
         Daily Planner Agent
                  │
                  ▼
       Personalized Study Plan
                  │
                  ▼
     Email Reminder via n8n
```

---

## 🏗️ System Architecture

```text
+---------------------------+
|          User             |
+---------------------------+
             |
             ▼
+---------------------------+
|       n8n Webhook         |
+---------------------------+
             |
             ▼
+---------------------------+
| Internship Strategy Agent |
+---------------------------+
             |
             ▼
+---------------------------+
|  Strategy Generation      |
+---------------------------+
             |
             ▼
+---------------------------+
|   Daily Planner Agent     |
+---------------------------+
             |
             ▼
+---------------------------+
|  Email Notification       |
+---------------------------+
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| FastAPI | REST API |
| n8n | Workflow Automation |
| OpenAI API | AI Reasoning |
| Pandas | Data Processing |
| CSV Dataset | Internship Dataset |

---

## 📂 Project Structure

```text
AI-Career-Copilot/
│
├── agents/
│   ├── internship_agent.py
│   └── planner_agent.py
│
├── data/
│   └── jobs.csv
│
├── utils/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── n8nRun.json
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/aditi-1731/AI-Career-Copilot.git
```

### Navigate to the project directory

```bash
cd AI-Career-Copilot
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```env
OPENAI_API_KEY=your_api_key
```

### Run the application

```bash
python main.py
```

---

## 📈 Future Improvements

- Replace n8n with a Python-based scheduler
- Add persistent memory for personalized recommendations
- Integrate a local LLM
- Implement ATS resume scoring
- Add RAG-based job recommendations
- Develop a frontend dashboard
- Support WhatsApp notifications
- Integrate calendar scheduling
- Add an interview preparation agent
- Track user progress over time

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Aditi Tripathi**
