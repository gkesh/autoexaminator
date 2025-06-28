from google import genai
from google.genai import types


PROMPT = """
From the attached screenshot, analyze the question and select the correct answer.
There is no need to explain the process, simply choose the correct answer and just give the answer in terms of numbers based on the order of the answer.
For example, if the first option is correct, return 1 and if the second option is correct return 2, so on.
"""

def prompt(image) -> dict:
    client = genai.Client()
    
    with open(image, 'rb') as img:
        img_bytes = img.read()
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[
                types.Part.from_bytes(
                    data=img_bytes,
                    mime_type='image/jpeg',
                ),
                PROMPT
            ]
        )
        
        return response
