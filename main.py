from fastapi import FastAPI
from pydantic import BaseModel
import requests
from agents.internship_sprint_agent import run_internship_sprint_agent
from agents.daily_planner_agent import run_daily_planner_agent

app = FastAPI()

# ✅ Input schema
class UserInput(BaseModel):
    goal: str
    skills: list[str]
    email: str

@app.get("/")
def home():
    return {"message": "InternPilot AI (OpenAI Powered) is running 🚀"}

@app.post("/run")
def run_agents(data: UserInput):
    try:
        # 🔍 Log user input
        print("\n=== USER INPUT ===")
        print("Goal:", data.goal)
        print("Skills:", data.skills)
        print("Email:", data.email)

        # ✅ Validation
        if not data.goal.strip():
            return {"status": "error", "message": "Goal cannot be empty"}

        if not data.skills:
            return {"status": "error", "message": "Skills cannot be empty"}

        # 🚀 Step 1: Run Agent 1
        print("\n⏳ Running Internship Agent (OpenAI)...")
        agent1_output = run_internship_sprint_agent(
            goal=data.goal,
            skills=data.skills
        )

        print("\n=== Agent 1 Output ===\n", agent1_output)

        # ❌ If Agent 1 failed
        if not agent1_output or "Error" in agent1_output:
            return {
                "status": "error",
                "message": "Agent 1 failed",
                "details": agent1_output
            }

        # 🚀 Step 2: Run Agent 2
        print("\n⏳ Running Daily Planner Agent (OpenAI)...")
        agent2_output = run_daily_planner_agent(agent1_output)

        print("\n=== Agent 2 Output ===\n", agent2_output)

        # 🚀 Send data to n8n webhook
        webhook_url = "https://aditit818.app.n8n.cloud/webhook-test/internpilot"

        payload = {
            "email": data.email,
            "agent1_output": agent1_output,
            "agent2_output": agent2_output
        }

        try:
            response = requests.post(webhook_url, json=payload)
            print("✅ Sent to n8n:", response.status_code)
        except Exception as e:
            print("❌ Failed to send to n8n:", e)

        # ❌ If Agent 2 failed
        if not agent2_output or "Error" in agent2_output:
            return {
                "status": "error",
                "message": "Agent 2 failed",
                "details": agent2_output
            }

        # ✅ Final Response
        return {
            "status": "success",
            "goal": data.goal,
            "skills": data.skills,
            "email": data.email,
            "agent1_output": agent1_output,
            "agent2_output": agent2_output
        }

    except Exception as e:
        print("\n❌ ERROR OCCURRED:", str(e))

        return {
            "status": "error",
            "message": str(e)
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)