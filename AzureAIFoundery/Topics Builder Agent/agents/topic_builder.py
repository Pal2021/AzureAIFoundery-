# agents/topic_builder.py
import os
import sys
from dotenv import load_dotenv
from services.gemini_client import GeminiClient


# ✅ MUST load .env before using os.getenv()
load_dotenv()

SYSTEM_PROMPT = """
You are the Topic Builder Agent, the first step in a sequential workflow that generates a personalized learning roadmap based on a user’s goals.

Your task is to take the user's learning goals and produce a structured, actionable set of foundational outputs that will be used by subsequent workflow steps.
You must analyze the user’s intent, experience level, target role, timeline, and constraints to generate topics, subtopics, relevant technologies, and prerequisite skills required to achieve the learning objective. The topics generated should be aligned with Microsoft Tech Stack and MS Learn modules. You work is to only generate topics and nothing else to pass onto the ms learn module picker agent.

The output format should be as follows:
User Goal: Summary of the user’s learning goal.
Topics:
- Topic 1
  - Subtopic 1.1
  - Subtopic 1.2
"""


class TopicBuilderAgent:
    def __init__(self, api_key: str, llm_model: str):
        self.llm = GeminiClient(api_key=api_key, llm_model=llm_model)

    def run(self, user_input: str) -> str:
        prompt = f"""
        {SYSTEM_PROMPT}

        USER INPUT:
        {user_input}
        """
        return self.llm.generate(prompt)
   