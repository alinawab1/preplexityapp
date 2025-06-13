from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "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"  # Replace with your actual key

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        user_input = request.form.get("prompt", "")
        if user_input:
            url = "https://api.perplexity.ai/chat/completions"
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "sonar",
                "messages": [
                    {"role": "system", "content": "Be precise and concise."},
                    {"role": "user", "content": user_input}
                ]
            }

            try:
                res = requests.post(url, headers=headers, json=payload)
                res.raise_for_status()
                output = res.json()['choices'][0]['message']['content']
            except Exception as e:
                output = f"Error: {str(e)}"
    return render_template("index.html", result=output)

if __name__ == "__main__":
    app.run(debug=True)

