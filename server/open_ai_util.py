from openai import OpenAI
from constants import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def summarize_abstract(abstract):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an engineer's helpful assistent. They need you to summarize research paper abstracts."},
            {"role": "user", "content": f"Write a one sentence summary of the following abstract: {abstract}"}
        ]
    )

    return completion