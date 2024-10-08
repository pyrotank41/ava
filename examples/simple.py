from pydantic import Field, BaseModel
import ava_mosaic_ai

import warnings
warnings.filterwarnings('error', category=UserWarning)

class CompletionModel(BaseModel):
    response: str = Field(description="Your response to the user.")
    reasoning: str = Field(description="Explain your reasoning for the response.")

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {
        "role": "user",
        "content": "If it takes 2 hours to dry 1 shirt out in the sun, how long will it take to dry 5 shirts?",
    },
]

llm = ava_mosaic_ai.get_llm(provider = "azure_openai")
llm.settings.default_model = "gpt-4o"
completion = llm.create_completion(
    response_model=CompletionModel,
    messages=messages,
)
assert isinstance(completion, CompletionModel)

print(f"Response: {completion.response}\n")
print(f"Reasoning: {completion.reasoning}")