from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# LOAD MODEL DAN SCALER
model = joblib.load(os.path.join(BASE_DIR, 'model_salary_predictor.pkl'))

df = pd.read_csv(os.path.join(BASE_DIR, 'salaries.csv'))

# OPSI DROPDOWN
FORM_OPTIONS = {
    'work_year': sorted(df['work_year'].unique().tolist(), reverse=True),
    'experience_level': sorted(df['experience_level'].unique().tolist()),
    'employment_type': sorted(df['employment_type'].unique().tolist()),
    'job_title': sorted(df['job_title'].unique().tolist()),
    'employee_residence': sorted(df['employee_residence'].unique().tolist()),
    'remote_ratio': sorted(df['remote_ratio'].unique().tolist()),
    'company_location': sorted(df['company_location'].unique().tolist()),
    'company_size': sorted(df['company_size'].unique().tolist())
}

@app.route('/')
def home():
    return render_template('index.html', options=FORM_OPTIONS)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_df = pd.DataFrame([data])

        # PREDICT
        prediction = model.predict(input_df)[0]
        
        return jsonify({'result': round(prediction, 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)