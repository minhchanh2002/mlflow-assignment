from flask import Flask, request, render_template_string
import pandas as pd
import joblib

# Load model
model = joblib.load("best_model.pkl")

app = Flask(__name__)

# Giao diện HTML đơn giản
html_form = """
<!doctype html>
<title>Predict with Best Model</title>
<h2>Nhập dữ liệu để phân loại:</h2>
<form method=post>
  {% for i in range(10) %}
    <label>Feature {{i}}:</label>
    <input type="text" name="feature_{{i}}" required><br><br>
  {% endfor %}
  <input type="submit" value="Predict">
</form>

{% if prediction is not none %}
  <h3>Kết quả phân loại: {{ prediction }}</h3>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def predict():
    prediction = None
    if request.method == "POST":
        try:
            features = []
            for i in range(10):
                value = float(request.form.get(f"feature_{i}"))
                features.append(value)
            input_df = pd.DataFrame([features], columns=[f"feature_{i}" for i in range(10)])
            prediction = int(model.predict(input_df)[0])
        except Exception as e:
            prediction = f"Lỗi: {e}"
    
    return render_template_string(html_form, prediction=prediction)

if __name__ == "__main__":
    print("[INFO] Starting Flask web server at http://127.0.0.1:5000 ...")
    app.run(host="127.0.0.1", port=5000, debug=False)
