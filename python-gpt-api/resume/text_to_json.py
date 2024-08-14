from openai import OpenAI
import os
# from dotenv import load_dotenv

# load_dotenv()

client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))

def convert_to_json(text):
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role":"system",
                "content":"You are a helpful research assistant."
            },
            {
                "role":"user",
                "content":f"Convert this numbered list: {text} to a json list. Just return the json nothing else. No need to add indexes or any other text. Do not add 'json' or anything in the front"
            }
        ]
    )
    return response.choices[0].message.content

# text = """1. Emphasize experience in building and developing backend applications, showcasing proficiency in designing and implementing RESTful micro-services for scalability and performance.
# 2. Highlight expertise in modern object-oriented programming languages such as Java, Python, or Scala, demonstrating strong coding skills and ability to craft efficient backend solutions.
# 3. Showcase proficiency in database technologies including relational databases like PostgreSQL and non-relational databases like DynamoDB, showcasing a deep understanding of data storage and management for backend systems."""

# print(convert_to_json(text))