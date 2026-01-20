# 📊 Data Science Salary Predictor 2026

Aplikasi berbasis web untuk memprediksi **estimasi gaji tahunan profesional di bidang Data Science** menggunakan pendekatan **Machine Learning**.

---

## 🏙️ Background
Dalam industri data yang berkembang pesat, transparansi gaji menjadi satu diantara pertimbangan krusial bagi calon para praktisi. Proyek ini bertujuan untuk menganalisis faktor-faktor yang memengaruhi kompensasi global, seperti tingkat pengalaman, lokasi perusahaan, rasio kerja jarak jauh (remote), dan faktor-faktor lainnya. Dengan model ini, calon praktisi data dapat mengestimasi nilai pasar mereka di tahun 2026 berdasarkan tren historis.

---

## 📁 Dataset Overview

Data yang digunakan berasal dari file **`salaries.csv`** yang mencakup catatan gaji profesional data di seluruh dunia.

### 🔹 Fitur Lokasi
- `employee_residence`
- `company_location`  
  (menggunakan standar **ISO 3166-1 alpha-2**)

### 🔹 Fitur Lainnya
- `work_year`
- `experience_level`
- `employment_type`
- `job_title`
- `remote_ratio`
- `company_size`

### 🎯 Target
- `salary_in_usd` → Gaji tahunan dalam mata uang USD

---

## 🧹 Data Preprocessing & Feature Engineering

Tahapan preprocessing yang dilakukan meliputi:

- **Handling Categorical Data**  
  Mengonversi fitur kategori (seperti *Job Title* dan *Location*) menjadi representasi numerik agar dapat diproses oleh model.

- **Standardisasi Lokasi**  
  Menggunakan library `pycountry` untuk memetakan kode negara ISO menjadi nama lengkap pada antarmuka pengguna (UI).

- **Feature Selection**  
  Memilih fitur dengan korelasi kuat terhadap besaran gaji untuk meningkatkan akurasi prediksi.

---

## 🤖 Modeling Approach

- **Algorithm**  
  Model dikembangkan menggunakan algoritma regresi dan dilatih melalui Jupyter Notebook (`code.ipynb`).

- **Deployment**  
  Model disimpan dalam format `.pkl` menggunakan `joblib` untuk integrasi cepat dengan backend Flask.

- **Evaluation**  
  Model dievaluasi untuk meminimalkan error prediksi agar estimasi mendekati kondisi pasar.

---

## ⚙️ Arsitektur Aplikasi

Aplikasi ini menggunakan integrasi antara **Flask (Backend)** dan **Modern HTML/CSS (Frontend)**.

### 🔧 Backend (Flask – Port 5000)
- Bertindak sebagai API yang memuat model Machine Learning  
- Melakukan encoding data input pengguna secara *on-the-fly*  
- Menyediakan data dropdown secara dinamis dari file CSV  

### 🎨 Frontend (Modern UI)
- Antarmuka kartu modern (*Modern Card UI*) yang responsif  
- Format mata uang internasional untuk hasil prediksi  
- Validasi input untuk memastikan data yang dikirim ke model akurat  

---

## 📂 Struktur Folder

```plaintext
Salary-Predictor-2026/
├── app.py                       # Inti backend Flask & logika prediksi
├── salaries.csv                 # Dataset utama
├── model_salary_predictor.pkl   # Model ML yang sudah dilatih
├── prototype.ipynb              # Notebook eksperimen ML
└── templates/
    └── index.html               # Antarmuka pengguna (UI)
```

---

## 🚀 Cara Menjalankan Proyek
1. Buka terminal.
2. Arahkan ke direktori backend.
3. Jalankan perintah berikut:

```bash
python app.py
```

4. Tunggu hingga muncul pesan:

```text
Running on http://127.0.0.1:5000
```

---

### 🌐 Akses Aplikasi
Buka browser dan kunjungi:

```text
http://127.0.0.1:8000
```
