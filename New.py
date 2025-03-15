from ollama import chat
from ollama import ChatResponse

Text = []


# response: ChatResponse = chat(model='gemma2:2b', messages=[
# {
#     'role': 'system',
#     'content': ''
#   },
#     {
#
#       "role": "user",
#       "content": ""
#     }
#   ])

# print(response['message']['content'])

def confirmation(Text):
    response: ChatResponse = chat(model='gemma2:2b', messages=[
        {
            'role': 'system',
            'content': '這裏有一些人員名和待辦事宜的清單，請從以下文字内容中找到對應人員和相應事宜，如果找不到對應的文字内容，請以回復N/A'
        },
        {

            "role": "user",
            "content": Text
        }
    ])
    return response['message']['content']

print(confirmation(''))


