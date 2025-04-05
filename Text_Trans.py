
# Parameters
client = AzureOpenAI(
  azure_endpoint = "https://hkust.azure-api.net",
  api_version = "2024-06-01",
  api_key = "<your_azure_openai_api_key>" # See here to see how to get your HKUST Azure OpenAI API key: https://digitalhumanities.hkust.edu.hk/tutorials/how-to-use-hkust-azure-openai-api-key-with-python-with-sample-code-and-use-case-examples/
)

def Canto_to_Chi_OpenAI(message):
    try:
        response = client.chat.completions.create(
            model = 'gpt-4o',
            temperature = 1,
            messages = [
                {"role": "system", "content": """
                                            Translate the following text from spoken Cantonese text to written language of traditional Chinese text.
                                            """},
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content
    except:
        return None
    
Canto_to_Chi_OpenAI('香港三面環海，東面同南面係南中國海，西面係珠江口同零丁洋，東北面係大鵬灣，北面同中國大陸隔住條深圳河')