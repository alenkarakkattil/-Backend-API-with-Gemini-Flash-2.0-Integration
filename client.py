import requests
import time

while True:
    prompt = input("Enter your prompt (or 'exit' to quit): ")
    if prompt.lower() == 'exit':
        break

    try:
        start = time.time()
        response = requests.post(
            "http://127.0.0.1:8000/generate/",
            json={"prompt": prompt}
        )
        end = time.time()

        if response.status_code == 200:
            print("\nGemini Response:\n", response.json()["response"])
            print(f"Response Time: {end - start:.2f} seconds\n")
        else:
            print("Server error:", response.status_code, response.text)

    except requests.exceptions.Timeout:
        print("⚠️ Request timed out. Gemini API is taking too long.")
    except Exception as e:
        print("Unexpected error:", e)
