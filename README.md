# 💇 Hair Fall Risk Prediction App

Aplikasi web prediksi risiko kebotakan berbasis Machine Learning yang dibangun menggunakan **Streamlit**. Pengguna dapat memasukkan data pasien dan memilih kombinasi algoritma serta metode seleksi fitur untuk mendapatkan prediksi risiko kebotakan secara interaktif.

---

## 🚀 Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://hairfall-app-streamlit.streamlit.app)

---

## 📌 Fitur

- Prediksi risiko kebotakan berdasarkan data klinis pasien
- Pilihan **6 algoritma klasifikasi**:
  - K-Nearest Neighbors (KNN)
  - Support Vector Machine (SVM)
  - Random Forest
  - Naive Bayes
  - J48 (Decision Tree)
  - Logistic Regression
- Pilihan **4 metode feature selection**:
  - No Selection
  - Info Gain
  - Chi-Square
  - CFS Subset
- Menampilkan hasil prediksi beserta nilai probabilitas
- UI bersih dan responsif

---

## 🧠 Dataset

Dataset yang digunakan: [Baldness Risk Factor Dataset](https://www.kaggle.com/datasets/dari4510/baldness-risk-factor-dataset) dari Kaggle.

**Fitur input pasien:**

| Fitur | Tipe | Keterangan |
|---|---|---|
| Age | Numerik | Usia pasien (0–100) |
| Genetics | Biner | Riwayat genetik kebotakan |
| Hormonal Changes | Biner | Perubahan hormonal |
| Stress | Ordinal | Tingkat stres (Low / Medium / High) |
| Poor Hair Care Habits | Biner | Kebiasaan perawatan rambut buruk |
| Environmental Factors | Biner | Paparan faktor lingkungan |
| Smoking | Biner | Kebiasaan merokok |
| Weight Loss | Biner | Penurunan berat badan signifikan |
| Medical Conditions | Kategorikal | Kondisi medis yang diderita |
| Medications & Treatments | Kategorikal | Obat / perawatan yang dikonsumsi |
| Nutritional Deficiencies | Kategorikal | Defisiensi nutrisi |

---

## 🔧 Tech Stack

- **Frontend & App:** [Streamlit](https://streamlit.io)
- **Machine Learning:** scikit-learn, imbalanced-learn (SMOTE)
- **Data Processing:** pandas, numpy
- **Model Persistence:** joblib

---

## 📁 Struktur Folder

```
hairfall-app-streamlit/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .gitignore
└── model_artifacts/        # Pre-trained model files (.pkl)
    ├── scaler.pkl
    ├── datasets.pkl
    ├── all_feature_names.pkl
    ├── original_feature_cols.pkl
    ├── log_transformed_cols.pkl
    ├── df_clean.pkl
    ├── idx_ig.pkl
    ├── idx_chi2.pkl
    ├── idx_cfs.pkl
    ├── y_train_bal.pkl
    └── y_test.pkl
```

---

## ⚙️ Cara Menjalankan Lokal

**1. Clone repo**
```bash
git clone https://github.com/USERNAME/hairfall-app-streamlit.git
cd hairfall-app-streamlit
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Jalankan aplikasi**
```bash
streamlit run app.py
```

**4. Buka browser**
```
http://localhost:8501
```

---

## 📊 Alur Machine Learning

```
Dataset (Kaggle)
    ↓
Data Cleaning & EDA
    ↓
Encoding (Binary / Ordinal / One-Hot)
    ↓
Pre-processing (Log Transform + RobustScaler)
    ↓
Data Balancing (SMOTE)
    ↓
Feature Selection (Info Gain / Chi-Square / CFS)
    ↓
Training 6 Algoritma × 4 Feature Selection = 24 Kombinasi
    ↓
Evaluasi (Accuracy, Precision, Recall, F1, AUC-ROC)
    ↓
Prediksi Interaktif
```

---

## 👤 Author

Dibuat sebagai bagian dari project magang / penelitian machine learning.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
