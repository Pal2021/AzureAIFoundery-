import os
from services.gemini_client import GeminiClient

SYSTEM_PROMPT = """
You are the MS Learn Module Picker Agent, the second step in a sequential workflow.

You receive structured topics from the Topic Builder Agent.
Your job is to map each topic and subtopic to the most relevant Microsoft Learn modules.
IMPORTANT: Return your response as plain text with clear formatting.
Do NOT use JSON. Use markdown bullet points instead. and bellow i hava mentained json just ignoe it 
Rules:
- Use ONLY real Microsoft Learn URLs
- Do NOT hallucinate URLs or make up module names
- Use the Web Search tool to verify current MS Learn catalog
- Return structured list with: module name, URL, description, mapped topic

Output Format:
{
  "modules": [
    {
      "topic": "Topic Name",
      "subtopic": "Subtopic Name",
      "module_name": "Real MS Learn Module Name",
      "url": "https://learn.microsoft.com/...",
      "description": "Brief description"
    }
  ]
}
"""

class MSLearnModulePickerAgent:
    def __init__(self, api_key: str, llm_model: str):
        self.llm = GeminiClient(api_key=api_key, llm_model=llm_model)

    def run(self, topics_json: str) -> str:
        prompt = f"""
        {SYSTEM_PROMPT}

        TOPICS FROM PREVIOUS AGENT:
        {topics_json}

        Search Microsoft Learn catalog and return matching modules as JSON.
        """
        return self.llm.generate(prompt)