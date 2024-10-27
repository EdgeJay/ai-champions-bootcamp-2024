from openai import OpenAI
from langchain_community.embeddings import OpenAIEmbeddings
import tiktoken
import env

class OpenAIService:
    api_key: str
    client: OpenAI
    model: str
    temperature: float
    debug_mode: bool

    def __init__(self, api_key, model=env.llm_model(), temperature=0, debug_mode=False):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.debug_mode = debug_mode
    
    # initialise instance of OpenAI client
    def start(self):
        self.client = OpenAI(api_key=self.api_key)

    def get_embeddings(self):
        return OpenAIEmbeddings(openai_api_key=self.api_key)

    # get chat completion/reply from OpenAI model via OpenAI client
    def get_chat_completion(self, messages):
        # messages = [{"role": "user", "content": prompt}]
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature, # this is the degree of randomness of the model's output
        )
        return response.choices[0].message.content
    
    # estimate tokens consumed by prompt depending on LLM model used
    def estimate_token_counts(self, prompt):
        encoding = tiktoken.encoding_for_model(self.model)
        return len(encoding.encode(prompt))

    # estimate tokens consumed by multiple messages depending on LLM model used
    def estimate_token_counts_from_messages(self, messages):
        encoding = tiktoken.encoding_for_model(self.model)
        value = ' '.join([m.get('content') for m in messages])
        return len(encoding.encode(value))