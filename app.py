from flask import Flask, render_template, request, redirect, url_for, session
import requests
import markdown
from markupsafe import Markup

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a random secret key

API_KEY = "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"

@app.route("/", methods=["GET", "POST"])
def index():
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
                html_content = markdown.markdown(
                    markdown_content,
                    extensions=['fenced_code', 'tables', 'nl2br']
                )
                # Store result in session
                session['result'] = str(html_content)
                session['prompt'] = user_input
            except Exception as e:
                session['result'] = f"Error: {e}"
                session['prompt'] = user_input
        
        # Redirect to prevent resubmission
        return redirect(url_for('index'))
    
    # GET request - display result if available
    result = Markup(session.pop('result', ''))  # pop removes it after displaying
    prompt = session.pop('prompt', '')
    
    return render_template("index.html", result=result, prompt=prompt)


if __name__ == "__main__":
    app.run(debug=True)