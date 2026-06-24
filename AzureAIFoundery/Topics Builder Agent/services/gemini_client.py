# services/gemini_client.py
import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
llm_model = os.getenv("GEMINI_MODEL")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")


class GeminiClient:
    def __init__(self, api_key: str, llm_model: str):
        self.client = genai.Client(api_key=api_key)
        self.llm_model = llm_model

    def generate(self, prompt: str, max_retries: int = 3) -> str:
        for attempt in range(max_retries):
            try:
                # Use models.generate_content — stable API, no config issues
                response = self.client.models.generate_content(
                    model=self.llm_model,
                    contents=prompt
                )
                return response.text
            
            except Exception as e:
                error_msg = str(e).lower()
                
                if "429" in error_msg or "quota" in error_msg or "too_many_requests" in error_msg:
                    wait_time = (attempt + 1) * 5
                    print(f"⚠️ Rate limit. Waiting {wait_time}s... (attempt {attempt + 1}/{max_retries})")
                    time.sleep(wait_time)
                    
                    if attempt == max_retries - 1:
                        raise Exception("Rate limit exceeded. Try again later.")
                else:
                    raise e