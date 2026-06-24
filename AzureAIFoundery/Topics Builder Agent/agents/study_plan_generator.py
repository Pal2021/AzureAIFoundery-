from services.gemini_client import GeminiClient

SYSTEM_PROMPT = """
You are the Study Plan Generator Agent, the third step in a sequential workflow.

You receive:
1. Curated Microsoft Learn modules (with URLs, descriptions, subtopic mapping)
2. User's timeline and availability

Your job:
- Convert modules into a week-by-week study plan
- Factor in: available hours per week, module complexity, prerequisites
- Make it realistic and achievable

Output Format:
{
  "plan_title": "Personalized Learning Path",
  "total_weeks": N,
  "weekly_commitment": "X hours/week",
  "weeks": [
    {
      "week": 1,
      "topics": ["Topic 1", "Topic 2"],
      "modules": [
        {"name": "Module Name", "url": "...", "hours": 3}
      ],
      "milestones": "What to achieve this week"
    }
  ]
}
"""

class StudyPlanGeneratorAgent:
    def __init__(self, api_key: str, llm_model: str):
        self.llm = GeminiClient(api_key=api_key, llm_model=llm_model)

    def run(self, modules_json: str, user_timeline: str) -> str:
        prompt = f"""
        {SYSTEM_PROMPT}

        MODULES FROM PREVIOUS AGENT:
        {modules_json}

        USER TIMELINE & CONSTRAINTS:
        {user_timeline}

        Generate the complete study plan.
        """
        return self.llm.generate(prompt)