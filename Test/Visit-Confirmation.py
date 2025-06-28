import requests
import json


def send_confirmation(text_message):
    """Send text to the confirmation API endpoint"""
    url = "https://instantly-beloved-griffon.ngrok-free.app/confirmation"

    try:
        # Prepare the request data
        data = {"text": text_message}
        headers = {"Content-Type": "application/json"}

        # Send POST request
        response = requests.post(
            url,
            data=json.dumps(data),
            headers=headers,
            timeout=10  # 10 second timeout
        )

        # Check response
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "error": f"API request failed with status {response.status_code}",
                "response": response.text
            }

    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


# Example usage
if __name__ == "__main__":
    # Test with different messages
    test_messages = [
        "Hello world",
        "API test",
        "粤语测试"  # Cantonese test
    ]

    for message in test_messages:
        print(f"Sending: '{message}'")
        result = send_confirmation(message)
        print("Response:", json.dumps(result, indent=2))
        print("-" * 50)
