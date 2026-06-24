from services.azure_client import AzureClient

SYSTEM_PROMPT = """
You are the Study Plan Generator Agent, the third step in a sequential workflow.

You receive curated Microsoft Learn modules (with URLs, descriptions, and subtopic mapping) and the user's timeline information.
Your job is to convert these modules into a structured, realistic, and achievable week-by-week study plan, factoring in the user's available time, pace, module complexity, and learning depth.

Your output MUST be clean, human friendly.
"""

class StudyPlanGeneratorAgent:
    def __init__(self, api_key: str = None, base_url: str = None, model: str = None):
        self.llm = AzureClient(api_key=api_key, base_url=base_url, model=model)

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