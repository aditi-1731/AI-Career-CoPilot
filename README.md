# 🚀 AI Career Copilot

> An AI-powered career assistant designed to help students and job seekers discover opportunities, identify skill gaps, build personalized preparation plans, improve resumes, and manage their career journey.

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql)](https://www.postgresql.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)](https://www.sqlalchemy.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Under_Development-orange)](https://github.com/aditi-1731/AI-Career-CoPilot)

---

## 📌 Overview

**AI Career Copilot** is an AI-powered career assistance platform for students, freshers, and job seekers.

The project started as a **Python + n8n multi-agent prototype** during an Agentic AI Workshop Hackathon. It is now being developed into a structured full-stack application with a FastAPI backend, PostgreSQL database, authentication system, and a modern web frontend.

The long-term goal is to bring multiple career preparation activities into one platform:

- 🎯 Career and internship opportunity discovery
- 📊 Skill gap analysis
- 📄 Resume building and optimization
- 📅 Personalized daily preparation plans
- 🎤 Interview preparation
- 🤖 AI-powered career guidance
- 🔔 Automated reminders and notifications
- 📈 Career progress tracking

---

# 📈 Project Evolution

The project is being developed incrementally.

```text
v1.0.0
Initial AI Prototype
Python + n8n
        │
        ▼
v1.1.0
Backend Foundation
FastAPI + PostgreSQL + JWT
        │
        ▼
v2.0.0
Full-Stack AI Career Copilot
Backend + Frontend + AI Services

```
---
## 📈 Project Evolution

The project is being developed incrementally, with each major version representing a stage in its architecture and functionality.

### 🏷️ v1.0.0 — Initial AI Prototype

The first version was a **multi-agent AI system built using Python and n8n**.

#### Features

- Internship recommendation agent
- Skill gap analysis
- Personalized preparation strategy
- Resume generation
- Daily planner agent
- Email reminder integration
- n8n workflow automation

#### Tech Stack

- Python
- FastAPI
- n8n
- OpenAI API
- Pandas

📌 **Status:** Released as `v1.0.0`

---

### 🏷️ v1.1.0 — Backend Foundation

The project was expanded from the initial prototype into a structured backend application.

#### Added

- FastAPI backend architecture
- PostgreSQL database
- SQLAlchemy ORM
- Alembic migrations
- UUID-based database models
- User and User Profile models
- JWT authentication
- Password hashing
- Pydantic validation
- CRUD layer
- Service layer
- Protected routes
- Authentication APIs
- Swagger and ReDoc API documentation
- Environment-based configuration

📌 **Status:** Released as `v1.1.0`

---

### 🚧 v2.0.0 — Full-Stack Development

`v2.0.0` is currently under development.

The project is being reorganized into a full-stack monorepo containing a dedicated backend and frontend.

#### V2 Goals

- Full-stack application
- Modern frontend dashboard
- FastAPI backend
- PostgreSQL database
- JWT authentication
- User profile management
- Internship recommendation system
- Skill gap analysis
- Resume builder
- ATS resume optimization
- Daily career and study planner
- AI interview preparation
- Career guidance
- Notification and reminder system
- Modular AI services

📌 **Status:** In Development
---

## 🏗️ System Architecture

```text
                         ┌─────────────────────┐
                         │      Frontend       │
                         │   Web Dashboard     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    FastAPI API      │
                         │      Backend        │
                         └──────────┬──────────┘
                                    │
                ┌───────────────────┼───────────────────┐
                │                   │                   │
                ▼                   ▼                   ▼
        Authentication        Career Services      User Services
                │                   │                   │
                └───────────────────┼───────────────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     PostgreSQL      │
                         │      Database       │
                         └─────────────────────┘
```

---

## ✨ Current Features

### 🔐 Authentication

The backend currently provides a JWT-based authentication system.

- User registration
- User login
- JWT access tokens
- JWT token verification
- Password hashing
- Protected routes
- Authentication exception handling
- Request validation
- Environment-based secrets

### 🗄️ Database

The application uses PostgreSQL as its primary relational database.

Current database capabilities:

- PostgreSQL integration
- SQLAlchemy ORM
- Alembic migrations
- UUID-based primary keys
- User model
- User Profile model
- Created and updated timestamps
- Database session management

### 🏗️ Backend Architecture

The backend follows a modular layered architecture.

```text
API / Routes
     ↓
Services
     ↓
CRUD
     ↓
SQLAlchemy Models
     ↓
PostgreSQL
```
---
## 📚 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

http://127.0.0.1:8000/docs

### ReDoc

http://127.0.0.1:8000/redoc

---

## 🔌 Current API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/v1/auth/register` | Register a new user |
| POST | `/api/v1/auth/login` | Login and receive a JWT |

More endpoints will be introduced during V2 development.
---

## 🧠 Planned AI Modules

The AI layer will be expanded during V2 development.

### 🎯 Internship Recommendation Agent

The agent will analyze the user's:

- Career goal
- Target role
- Skills
- Experience level
- Preferred location
- Timeframe

It will identify suitable internship or job opportunities and provide:

- Required skills
- Skill gaps
- Application information
- Preparation recommendations
- Personalized strategy

### 📊 Skill Gap Analyzer

The Skill Gap Analyzer will compare the user's current skills with the requirements of a target role.

Expected output:

- Existing skills
- Missing skills
- Skill priority
- Recommended learning areas
- Preparation roadmap

### 📄 Resume Builder

The Resume Builder will create structured resumes using the user's:

- Education
- Skills
- Projects
- Experience
- Achievements
- Target role

The generated resume will be designed to remain structured and ATS-friendly.

### 🔎 ATS Resume Optimizer

The ATS Resume Optimizer will analyze a resume against a target job description.

It will help identify:

- Missing keywords
- Skill mismatches
- Weak sections
- Job-specific improvements
- Formatting issues
- Content optimization opportunities

### 📅 Daily Planner Agent

The Daily Planner Agent will convert a career strategy into actionable daily tasks.

The planner will consider:

- Career goal
- Skill gaps
- Task priority
- Estimated preparation time
- User progress
- Target timeframe

Example workflow:

```text
Career Goal
     ↓
Skill Gap Analysis
     ↓
Preparation Strategy
     ↓
Daily Tasks
     ↓
Progress Tracking
```

---

## 🛠️ Tech Stack

### Backend

| Technology | Purpose |
|---|---|
| Python 3.13 | Backend development |
| FastAPI | REST API |
| PostgreSQL | Relational database |
| SQLAlchemy | ORM |
| Alembic | Database migrations |
| Pydantic | Data validation |
| JWT | Authentication |
| Passlib / bcrypt | Password hashing |

### Frontend

| Technology | Purpose |
|---|---|
| Next.js | Web application |
| React | UI development |
| TypeScript | Type-safe frontend |
| Tailwind CSS | Styling |

### Development Tools

| Tool | Purpose |
|---|---|
| Git | Version control |
| GitHub | Repository and releases |
| VS Code | Development |
| Swagger / OpenAPI | API documentation and testing |
| PostgreSQL | Local development database |
---

## 📂 Project Structure

```text
AI-Career-CoPilot/
│
├── backend/
│   │
│   ├── app/
│   │   ├── agents/
│   │   ├── api/
│   │   ├── core/
│   │   ├── crud/
│   │   ├── database/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── security/
│   │   ├── services/
│   │   └── utils/
│   │
│   ├── alembic/
│   │   ├── versions/
│   │   └── env.py
│   │
│   ├── data/
│   ├── tests/
│   │
│   ├── main.py
│   ├── requirements.txt
│   ├── alembic.ini
│   └── .env.example
│
├── frontend/
│   │
│   ├── public/
│   ├── src/
│   ├── package.json
│   ├── package-lock.json
│   ├── next.config.ts
│   └── ...
│
├── .gitignore
├── README.md
└── LICENSE
```
## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/aditi-1731/AI-Career-CoPilot.git
cd AI-Career-CoPilot
```
### 🐍 Backend Setup
```
Navigate to the backend:

cd backend
Create Virtual Environment
python -m venv venv
Windows PowerShell
.\venv\Scripts\Activate.ps1
Windows CMD
venv\Scripts\activate
Install Backend Dependencies
pip install -r requirements.txt
```

### 🔐 Configure Environment Variables

Create a .env file inside the backend/ directory.
```
Example:

DATABASE_URL=postgresql://username:password@localhost:5432/careercopilot

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60

⚠️ Never commit your .env file to GitHub.

The repository should contain an example environment file such as:

.env.example
```

### 🗄️ Database Setup

Make sure PostgreSQL is running and the required database exists.

From the backend/ directory, run:

alembic upgrade head
▶️ Start the Backend

From the backend/ directory:
```
uvicorn main:app --reload
```
The backend will run at:
```
http://127.0.0.1:8000
```
## 📚 Test the Backend API

Open the following URLs in your browser.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```
### 💻 Frontend Setup

Open a new terminal.

From the project root:
```
cd frontend
```
Install frontend dependencies:
```
npm install
```
Start the development server:
```
npm run dev
```
The frontend will normally be available at:
```
http://localhost:3000
```

### 🔗 Backend + Frontend

During V2 development, the frontend will communicate with the FastAPI backend through REST APIs.
```
┌──────────────────────┐
│      Next.js         │
│      Frontend        │
└──────────┬───────────┘
           │
           │ HTTP / REST
           ▼
┌──────────────────────┐
│      FastAPI         │
│       Backend        │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│     PostgreSQL       │
│      Database        │
└──────────────────────┘
```
## 🧪 Testing

Backend tests are maintained inside:

```text
backend/tests/
```
Tests can be executed using:
```
pytest
```

## 📊 Development Progress
### ✅ Completed
- Initial AI prototype
- n8n automation workflows
- Internship planning workflow
- Daily planner workflow
- Resume generation workflow
- Email automation
- FastAPI backend foundation
- PostgreSQL integration
- SQLAlchemy ORM
- Alembic migrations
- UUID-based database models
- User model
- User Profile model
- Password hashing
- JWT authentication
- CRUD layer
- Service layer
- Authentication APIs
- Protected routes
- Frontend project initialization

### 🚧 In Progress
- Frontend-backend integration
- User profile management
- Frontend authentication
- Internship recommendation engine
- Skill gap analyzer
- Resume builder
- ATS resume optimization
- Daily planner
- Notification scheduler

## 🔜 Planned
- AI interview preparation
- Career guidance agent
- RAG-based career recommendations
- Progress tracking
- Personalized dashboard
- Advanced AI agent orchestration
- Production deployment
- Monitoring and logging

---

## 🛣️ Version History

| Version | Status | Description |
|---|---|---|
| `v1.0.0` | ✅ Released | Initial Python + n8n multi-agent AI prototype |
| `v1.1.0` | ✅ Released | Backend foundation with FastAPI, PostgreSQL, SQLAlchemy, Alembic and JWT authentication |
| `v2.0.0` | 🚧 In Development | Full-stack AI Career Copilot with backend and frontend |

---

## 🗺️ Project Roadmap

```text
                         AI CAREER COPILOT
                                │
                                ▼
                    ┌──────────────────────┐
                    │       v1.0.0         │
                    │  Initial AI Prototype│
                    └──────────┬───────────┘
                               │
                    Python + n8n Multi-Agent
                               │
             ┌─────────────────┼─────────────────┐
             ▼                 ▼                 ▼
       Internship Agent   Daily Planner    Resume Generation
             │                 │                 │
             └─────────────────┼─────────────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       v1.1.0         │
                    │ Backend Foundation   │
                    └──────────┬───────────┘
                               │
                  ┌────────────┼────────────┐
                  ▼            ▼            ▼
              FastAPI      PostgreSQL     JWT Auth
                  │            │            │
                  └────────────┼────────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       v2.0.0         │
                    │  Full-Stack Platform │
                    └──────────┬───────────┘
                               │
          ┌────────────────────┼────────────────────┐
          ▼                    ▼                    ▼
      Frontend             AI Services        User Dashboard
          │                    │                    │
          ├────────────┬───────┼────────────┬───────┤
          ▼            ▼       ▼            ▼       ▼
       Resume       Skill    Internship   Planner  Interview
       Builder       Gap     Matching     Agent     Agent
          │            │       │            │       │
          └────────────┴───────┼────────────┴───────┘
                               │
                               ▼
                     Career Guidance Platform
```

---

## 🎯 Long-Term Vision

AI Career Copilot aims to become a centralized career preparation platform where users can manage their complete career journey from a single application.

The intended user flow is:

```text
                    Career Goal
                         │
                         ▼
                Current Skill Profile
                         │
                         ▼
                  Skill Gap Analysis
                         │
                         ▼
               Opportunity Discovery
                         │
                         ▼
                  Resume Building
                         │
                         ▼
             Personalized Roadmap
                         │
                         ▼
                    Daily Tasks
                         │
                         ▼
                Interview Preparation
                         │
                         ▼
                  Progress Tracking
                         │
                         ▼
                   Career Growth
```
## 🔄 Development Philosophy

The project follows an incremental development approach.
```
Prototype
   ↓
Backend Foundation
   ↓
Full-Stack Architecture
   ↓
AI Services
   ↓
Integration
   ↓
Testing
   ↓
Deployment
```

## 🏷️ Releases

| Release | Description |
|---|---|
| `v1.0.0` | Initial Python + n8n multi-agent prototype |
| `v1.1.0` | Backend foundation and JWT authentication |
| `v2.0.0` | 🚧 Full-stack development in progress |

For complete release history, visit the project's GitHub Releases page:

👉 [View GitHub Releases](https://github.com/aditi-1731/AI-Career-CoPilot/releases)

---

## 🌱 Current Development Branch

The current major development work is being carried out on:

```text
v2-development
v2.0.0
```
## 🤝 Future Development

Future development will focus on connecting the existing backend foundation with the frontend and gradually integrating the AI career services.

The system will eventually bring together:

```text
Authentication
      +
User Profile
      +
Opportunity Discovery
      +
Skill Analysis
      +
Resume Services
      +
Career Planning
      +
Interview Preparation
      +
Progress Tracking
      =
AI Career Copilot
```
## 📄 License

This project is licensed under the MIT License.

See the LICENSE file for more information.

## 👩‍💻 Author

** Aditi Tripathi **
