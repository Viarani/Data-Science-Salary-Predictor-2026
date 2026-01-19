from flask import Flask, render_template, request, jsonify
import pandas as pd
import pycountry
import joblib
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# 1. LOAD MODEL DAN DATA
model = joblib.load(os.path.join(BASE_DIR, 'model_salary_predictor.pkl'))
df = pd.read_csv(os.path.join(BASE_DIR, 'salaries.csv'))

# 2. FUNGSI OTOMATIS KONVERSI KODE NEGARA KE NAMA
def get_country_name(code):
    country = pycountry.countries.get(alpha_2=code)
    return country.name if country else code

# 3. BUAT MAPPING LOKASI DARI DATASET (OTOMATIS)
# Mengambil semua kode unik dari kolom residence dan company_location
all_country_codes = set(df['employee_residence'].unique().tolist() + df['company_location'].unique().tolist())
location_mapping = {code: get_country_name(code) for code in all_country_codes}

# 4. OPSI DROPDOWN
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

# 5. MAPPING LABEL UI
UI_LABELS = {
    'experience_level': {'EN': 'Entry-level / Junior', 'MI': 'Mid-level / Intermediate', 'SE': 'Senior-level', 'EX': 'Executive / Director'},
    'employment_type': {'FT': 'Full-time', 'PT': 'Part-time', 'CT': 'Contract', 'FL': 'Freelance'},
    'remote_ratio': {0: 'No remote work (On-site)', 50: 'Hybrid (partially remote)', 100: 'Fully remote'},
    'location': location_mapping, # Menggunakan hasil mapping otomatis pycountry
    'company_size': {'S': 'Small (1–50 employees)', 'M': 'Medium (51–500 employees)', 'L': 'Large (501+ employees)'}
}

@app.route('/')
def home():
    return render_template('index.html', options=FORM_OPTIONS, labels=UI_LABELS)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # 1. List Fitur Sesuai Urutan Model
        features = ['work_year', 'experience_level', 'employment_type', 'job_title', 
                    'employee_residence', 'remote_ratio', 'company_location', 'company_size']
        
        # 2. Buat DataFrame
        input_df = pd.DataFrame([data])[features]

        # 3. MAPPING STRING KE ANGKA (Label Encoding Manual)
        # Kita harus mengubah semua kolom kategori menjadi angka agar model tidak error float
        category_cols = ['experience_level', 'employment_type', 'job_title', 
                         'employee_residence', 'company_location', 'company_size']
        
        for col in category_cols:
            # Menggunakan .hash() adalah cara cepat jika kamu tidak punya file LabelEncoder
            # Tapi cara terbaik adalah menyesuaikan dengan angka di Notebook kamu
            input_df[col] = input_df[col].apply(lambda x: abs(hash(x)) % 1000) 

        # 4. PREDIKSI
        prediction = model.predict(input_df)[0]
        return jsonify({'result': round(prediction, 2)})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)