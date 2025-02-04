from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

DEEPSEEK_API_URL = "https://openrouter.ai/api/v1/chat/completions"
DEEPSEEK_API_KEY = "<api key>"  # Replace with your actual API key

# Endpoint for code suggestions
@app.route('/suggest', methods=['POST'])
def suggest():
    data = request.json
    code = data.get('code', '')

    if not code:
        return jsonify({"error": "No code provided"}), 400

    try:
        response = requests.post(
            DEEPSEEK_API_URL,
            headers={
                "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
                "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional
                "X-Title": "<YOUR_SITE_NAME>",      # Optional
            },
            json={
                "model": "deepseek/deepseek-r1-distill-qwen-1.5b",
                "messages": [
                    {"role": "user", "content": f"Suggest improvements for the following code :\n{code}"}
                ]
            }
        )

        response.raise_for_status()
        suggestion = response.json()['choices'][0]['message']['content']

        return jsonify({"suggestion": suggestion})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/detect-errors', methods=['POST'])
def detect_errors():
    data = request.json
    code = data.get('code', '')

    if not code:
        return jsonify({"error": "No code provided"}), 400

    try:
        response = requests.post(
            DEEPSEEK_API_URL,
            headers={
                "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
                "HTTP-Referer": "<YOUR_SITE_URL>",
                "X-Title": "<YOUR_SITE_NAME>",
            },
            json={
                "model": "deepseek/deepseek-r1-distill-qwen-1.5b",
                "messages": [
                    {"role": "user", "content": f"Detect errors in the following code and suggest fixes:\n{code}"}
                ]
            }
        )

        response.raise_for_status()
        errors = response.json()['choices'][0]['message']['content']

        return jsonify({"errors": errors})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/refactor', methods=['POST'])
def refactor():
    data = request.json
    code = data.get('code', '')

    if not code:
        return jsonify({"error": "No code provided"}), 400

    try:
        response = requests.post(
            DEEPSEEK_API_URL,
            headers={
                "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
                "HTTP-Referer": "<YOUR_SITE_URL>",
                "X-Title": "<YOUR_SITE_NAME>",
            },
            json={
                "model": "deepseek/deepseek-r1-distill-qwen-1.5b",
                "messages": [
                    {"role": "user", "content": f"Refactor the following code to improve efficiency and readability and just return the code:\n{code}"}
                ]
            }
        )

        response.raise_for_status()
        refactoredCode = response.json()['choices'][0]['message']['content']

        return jsonify({"refactoredCode": refactoredCode})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    code = data.get('code', '')

    if not code:
        return jsonify({"error": "No code provided"}), 400

    try:
        response = requests.post(
            DEEPSEEK_API_URL,
            headers={
                "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
                "HTTP-Referer": "<YOUR_SITE_URL>",
                "X-Title": "<YOUR_SITE_NAME>",
            },
            json={
                "model": "deepseek/deepseek-r1-distill-qwen-1.5b",
                "messages": [
                    {"role": "user", "content": f"Summarize the following code in natural language:\n{code}"}
                ]
            }
        )

        response.raise_for_status()
        summary = response.json()['choices'][0]['message']['content']

        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)