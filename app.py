from flask import Flask, render_template, request
import requests
import markdown
from markupsafe import Markup

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
                markdown_content = res.json()['choices'][0]['message']['content']
                # Convert markdown to HTML
                html_content = markdown.markdown(
                    markdown_content,
                    extensions=['fenced_code', 'tables', 'nl2br']
                )
                return render_template("index.html", result=output)
            except Exception as e:
                return render_template("index.html", result=output)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)