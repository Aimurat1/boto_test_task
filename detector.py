import openai
from credentials import openai_token

openai.api_key = openai_token

def is_meaningful(text= None):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[{'role': 'user', 'content': f"""
Based on the provided examples and your knowledge, identify is this feedback meaningful? Answer "Yes" or "No"
Examples: "ыдвшоаыолвтас" - No, "ля ля ля ля ля " - No, "good" - No, "123" - No, "👍" - Yes, "Все ок" - Yes, "было челенджево, но суперски. респект" - Yes, "1. Интересно 2. Креативно 3. всё понятно." - Yes
Feedback: {text}
    """}]
    )
    return response['choices'][0]['message']['content'] == "Yes"

def main() -> None:
    while(True):
      text = input("Введите фидбэк: ")
      print(is_meaningful(text))

if __name__ == '__main__':
    main()

