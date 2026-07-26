import pandas as pd
from openai import OpenAI
from utils.prompts import internship_sprint_agent_prompt
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_internship_sprint_agent(goal, skills):
    skills = [s.strip().lower() for s in skills]

    df = pd.read_csv("data/jobs.csv")
    df = df.head(20)  

    jobs_text = df.to_string(index=False)

    prompt = internship_sprint_agent_prompt.format(
        goal=goal,
        skills=", ".join(skills),
        jobs=jobs_text
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",   
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content