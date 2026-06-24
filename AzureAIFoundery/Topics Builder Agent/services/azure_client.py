import os
from dotenv import load_dotenv
from anthropic import AnthropicFoundry

load_dotenv()


class AzureClient:
    def __init__(self, api_key: str = None, base_url: str = None, model: str = None):
        self.api_key = api_key or os.getenv("AZURE_API_KEY")
        self.base_url = base_url or os.getenv("AZURE_FOUNDRY_URL")
        self.model = model or os.getenv("AZURE_MODEL", "claude-sonnet-4-6")

        self.client = AnthropicFoundry(
            api_key=self.api_key,
            base_url=self.base_url
        )

    def generate(self, prompt: str, max_tokens: int = 4096) -> str:
        """Non-streaming (original)"""
        message = self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text

    def generate_stream(self, prompt: str, max_tokens: int = 4096):
        """Streaming - yields chunks like ChatGPT"""
        with self.client.messages.stream(
            model=self.model,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}]
        ) as stream:
            for text in stream.text_stream:
                yield text