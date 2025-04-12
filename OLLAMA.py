# Use AI to reconfirm

from ollama import chat
from ollama import ChatResponse

Text = []



# print(response['message']['content'])

def confirmation(text):
    response: ChatResponse = chat(model='gemma2:2b', messages=[
        {
            'role': 'system',
            'content': '這裏有一些人員名和待辦事宜的清單，請從以下文字内容中找到對應人員和相應事宜，格式爲‘名字，相應事宜’，如果找不到對應的文字内容或不確定，請以回復N/A'
        },
        {

            "role": "user",
            "content": text
        }
    ])
    return response['message']['content']

print(confirmation(''))
