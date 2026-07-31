# 🚀 AI Career Copilot

> An AI-powered Career Assistant that helps students prepare for internships through personalized roadmaps, resume generation, study planning, and intelligent career guidance.

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-v0.2.0--dev-orange)
![Status](https://img.shields.io/badge/Status-Under_Development-orange)
---

# 📌 Overview

AI Career Copilot is a modular backend application built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy** following a clean layered architecture.

The project aims to become an AI-powered career assistant that helps students:

- Discover internship opportunities
- Analyze skill gaps
- Generate personalized preparation roadmaps
- Build ATS-friendly resumes
- Create daily study plans
- Automate reminders and notifications

Originally developed during an Agentic AI Workshop Hackathon, the project is now being expanded into a production-ready backend.

---

## 🏛 Architecture

```text
                Client
                   │
                   ▼
        FastAPI Authentication API
                   │
                   ▼
             Service Layer
                   │
                   ▼
               CRUD Layer
                   │
                   ▼
           SQLAlchemy ORM
                   │
                   ▼
             PostgreSQL Database
```

# ✨ Current Features

## ✅ Authentication

- User Registration API
- User Login API
- JWT Authentication
- Password Hashing (bcrypt)
- Token Verification
- Exception Handling
- Swagger Documentation

## ✅ Database

- PostgreSQL Integration
- SQLAlchemy ORM
- Alembic Database Migrations
- UUID Primary Keys
- User & User Profile Models

## ✅ Backend Architecture

- FastAPI
- Layered Architecture
- CRUD Layer
- Service Layer
- Pydantic v2 Validation
- Environment-based Configuration

## 🔐 Security

- JWT Authentication
- bcrypt Password Hashing
- Environment-based Secrets
- Input Validation using Pydantic
- Custom Exception Handling

---

# 🚧 Upcoming Features

- User Profile Management
- Internship Recommendation Agent
- Resume Builder
- Skill Gap Analysis
- Daily Study Planner
- Email Reminder Scheduler
- AI Interview Preparation
- RAG-based Career Guidance

---

# 🏗️ Current Architecture

```text
                Client
                   │
                   ▼
             FastAPI Routes
                   │
                   ▼
            Service Layer
                   │
                   ▼
              CRUD Layer
                   │
                   ▼
         SQLAlchemy ORM
                   │
                   ▼
             PostgreSQL
```

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| FastAPI | REST API |
| PostgreSQL | Database |
| SQLAlchemy | ORM |
| Alembic | Database Migrations |
| Pydantic v2 | Data Validation |
| Passlib | Password Hashing |
| JWT | Authentication |
| python-dotenv | Environment Variables |

---

# 📂 Project Structure

```text
career-copilot-ai/

├── alembic/
│   ├── versions/
│   └── env.py
│
├── app/
│   ├── agents/
│   ├── api/
│   ├── core/
│   ├── crud/
│   ├── database/
│   ├── models/
│   ├── schemas/
│   ├── security/
│   ├── services/
│   └── utils/
│
├── data/
│   └── jobs.csv
│
├── tests/
│
├── main.py
├── requirements.txt
├── alembic.ini
├── .env.example
├── README.md
└── LICENSE
```

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/aditi-1731/AI-Career-CoPilot.git
```

## Navigate

```bash
cd AI-Career-CoPilot
```

## Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment

Create a `.env` file:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/careercopilot

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60
```

## Run Database Migrations

```bash
alembic upgrade head
```

## Start FastAPI

```bash
uvicorn main:app --reload
```

---

## 📚 API Documentation

After running the server:

Interactive API documentation is automatically generated using FastAPI.

- Swagger UI → http://127.0.0.1:8000/docs
- ReDoc → http://127.0.0.1:8000/redoc


## 🔌 Current API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/api/v1/auth/register` | Register a new user |
| POST | `/api/v1/auth/login` | Login and receive JWT |


# 📊 Development Progress

- [x] Project Setup
- [x] PostgreSQL Integration
- [x] SQLAlchemy Models
- [x] Alembic Migrations
- [x] Password Hashing
- [x] JWT Authentication
- [x] CRUD Layer
- [x] Service Layer
- [x] Authentication API
- [ ] Protected Routes
- [ ] User Profile API
- [ ] Internship Recommendation Engine
- [ ] Resume Builder
- [ ] Daily Planner
- [ ] Email Scheduler
- [ ] Frontend Dashboard

---

# 🛣️ Roadmap

### v0.1.0
- ✔ Authentication
- ✔ Database
- ✔ JWT
- ✔ CRUD
- ✔ Service Layer

### v0.2.0
- □ Protected Routes
- □ User Profile API

### v0.3.0
- □ Internship Recommendation Engine

### v0.4.0
- □ Resume Builder
- □ ATS Scoring

### v0.5.0
- □ Daily Planner
- □ Scheduler

### v1.0.0
- □ Complete AI Career Copilot Platform

---
## 🤖 Planned AI Modules

- Internship Recommendation Agent
- Resume Analyzer
- ATS Resume Optimizer
- Skill Gap Analyzer
- Interview Preparation Agent
- Study Planner Agent

---

## 🎯 Long-Term Vision

The backend will evolve into a modular AI platform consisting of:

- Authentication Service
- User Profile Service
- Internship Recommendation Agent
- ATS Resume Builder
- Resume Optimizer
- Skill Gap Analyzer
- Study Planner Agent
- Interview Preparation Agent
- Notification Scheduler

# 📄 License

This project is licensed under the MIT License.

---

# 👩‍💻 Author

**Aditi Tripathi**
