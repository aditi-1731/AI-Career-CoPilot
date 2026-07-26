from openai import OpenAI
from utils.prompts import daily_planner_agent_prompt
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_daily_planner_agent(agent1_output):

    full_prompt = f"""
{daily_planner_agent_prompt}

--- INPUT FROM INTERNSHIP AGENT ---
{agent1_output}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": full_prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content