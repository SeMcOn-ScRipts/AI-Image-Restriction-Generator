from google import genai
from google.genai import types

# NOTE: Replace "YOUR_GEMINI_API_KEY" with your actual Google Gemini API key
client = genai.Client(api_key="YOUR_GEMINI_API_KEY")

system_instruction = (
    "You are a visual deconstruction AI. When the user gives you a prompt, "
    "do not use the exact names of modern objects if you can describe their "
    "shape, color, and texture instead. Break the image down into exact visual "
    "details. For example, instead of 'smoking a cigarette', describe it as "
    "'holding a small white cylinder with a glowing orange tip, producing wisps "
    "of grey, translucent vapor that curl upward'."
)

user_prompt = input("What image do you want to describe?: ")

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=user_prompt,
    config=types.GenerateContentConfig(
        system_instruction=system_instruction
    )
)

print("\n--- AI Detailed Description ---")
print(response.text)