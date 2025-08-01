from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
  <title>CVS Pill Calculator</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      background-color: #f4f4f4;
      padding: 30px;
      position: relative;
    }
    h1 {
      color: #cc0000;
    }
    input, button {
      padding: 12px;
      margin: 8px;
      font-size: 18px;
      border: 1px solid #ccc;
      border-radius: 8px;
    }
    input {
      width: 80%%;
    }
    button {
      background-color: #cc0000;
      color: white;
      border: none;
    }
    .result {
      margin-top: 20px;
      font-size: 20px;
      color: #333;
    }
    .cute-message {
      margin-top: 10px;
      font-style: italic;
      color: #990000;
    }
    .initials {
      position: absolute;
      top: 10px;
      right: 15px;
      font-weight: bold;
      font-size: 14px;
      color: #888;
      opacity: 0.6;
    }
  </style>
</head>
<body>
  <h1>💊 CVS Pill Calculator</h1>
  <div class="initials">CS</div>
  <form method="POST">
    <input name="pills" type="number" step="any" placeholder="Total number of pills" required><br>
    <input name="doses" type="number" step="any" placeholder="Doses per day" required><br>
    <button type="submit">Calculate</button>
  </form>

  {% if result %}
    <div class="result">{{ result }}</div>
    <div class="cute-message">{{ message }}</div>
  {% endif %}
</body>
</html>
"""

CUTE_MESSAGES = [
    "You're the best part of my day 💕", "One dose closer to leaving 😌",
    "I love you! ❤️", "Give the meds and smile 😁",
    "You’re doing amazing, sweetie 💪", "Sending virtual hugs from the web 🥰",
    "Medication math? You nailed it! 🧠", "Make that money! 💊💸",
    "One pill at a time, babe. 💘"
]


@app.route("/", methods=["GET", "POST"])
def home():
  result = ""
  message = ""
  if request.method == "POST":
    try:
      pills = float(request.form["pills"])
      doses = float(request.form["doses"])
      if doses == 0:
        result = "Cannot divide by zero."
      else:
        days = pills / doses
        result = f"{days:.2f} days of medication"
        message = random.choice(CUTE_MESSAGES)
    except:
      result = "Invalid input. Please enter numbers."
  return render_template_string(HTML, result=result, message=message)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
