# from flask import Flask, request, jsonify
# import joblib
# import pandas as pd
# import numpy as np
# from sklearn.preprocessing import LabelEncoder

from flask import Flask, request, jsonify
from flask_cors import CORS   
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


app = Flask(__name__)
CORS(app)  
# ------------------------------------------------------------
# 1️⃣ Load Trained Model
# ------------------------------------------------------------
model_path = "./models/optimized_random_forest.joblib"

try:
    model = joblib.load(model_path)
    print("✅ Optimized model loaded successfully!")
except FileNotFoundError:
    raise Exception("❌ Model file not found! Please check the path.")

# ------------------------------------------------------------
# 2️⃣ Load Reference Dataset & Prepare Encoders
# ------------------------------------------------------------
df_ref = pd.read_csv("./data/processed/soil_reduced_features.csv")

categorical_cols = ['State', 'District', 'Farmer_ID', 'Soil_Type']
encoders = {col: LabelEncoder() for col in categorical_cols}

for col in categorical_cols:
    encoders[col].fit(df_ref[col])

# Get model’s expected feature order
expected_features = list(model.feature_names_in_)
print("🧩 Model expects features:", expected_features)

# ------------------------------------------------------------
# 3️⃣ Prediction Route
# ------------------------------------------------------------
@app.route('/predict', methods=['POST'])
def predict():
    """
    Example JSON Input:
    {
      "State": "Maharashtra",
      "District": "Pune",
      "Farmer_ID": "F101",
      "Soil_Type": "Loamy",
      "pH": 6.8,
      "EC": 0.45,
      "OC": 1.2,
      "N": 40,
      "P": 25,
      "K": 30,
      "Moisture": 12.5
    }
    """
    try:
        data = request.get_json()
        input_df = pd.DataFrame([data])

        # Handle and encode categorical columns
        for col in categorical_cols:
            if col in input_df.columns:
                val = input_df[col].iloc[0]
                # Handle unseen labels dynamically
                if val not in encoders[col].classes_:
                    encoders[col].classes_ = np.append(encoders[col].classes_, val) 
                input_df[col] = encoders[col].transform(input_df[col])

        # Ensure all expected columns exist
        for col in expected_features:
            if col not in input_df.columns:
                input_df[col] = 0  # fill missing numerical features

        # Reorder columns to match training
        input_df = input_df[expected_features]

        # Predict
        prediction = model.predict(input_df)[0]

        return jsonify({
            "status": "success",
            "predicted_crop_suitability": int(prediction)
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400


# ------------------------------------------------------------
# 4️⃣ Run Flask App
# ------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True, port=5000)
