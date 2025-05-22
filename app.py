from flask import Flask, request, render_template
import joblib
import numpy as np
from feature_extractor import extract_features
from woa_feature_selector import optimize_features

app = Flask(__name__)
model = joblib.load("phishing_model.pkl")

# Example: assumed importance scores (replace with actual from your model)
feature_importances = [0.15, 0.10, 0.25, 0.05, 0.20, 0.10, 0.05, 0.10]

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            try:
                all_features = extract_features(url)
                selected_features = optimize_features(all_features, feature_importances)

                # If no features selected, fall back to all
                if not selected_features:
                    selected_features = all_features

                features = np.array(selected_features).reshape(1, -1)
                result = model.predict(features)[0]
                prediction = "Phishing 🛑" if result == 1 else "Legitimate ✅"
            except Exception as e:
                prediction = f"Error: {str(e)}"
    return render_template("index.html", prediction=prediction)
