"""
Konfigurasi & konstanta global untuk HairFall AI App.
"""

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

# ── Page Config ──────────────────────────────────────────────────
PAGE_TITLE = "Hair Fall Prediction"
PAGE_ICON = "🩺"

# ── Algoritma & Feature Selection ───────────────────────────────
def get_algo_map():
    """Return dict algoritma (instance baru tiap dipanggil, hindari shared state)."""
    return {
        'KNN':                 KNeighborsClassifier(n_neighbors=5),
        'SVM':                 SVC(kernel='rbf', probability=True, random_state=42),
        'Random Forest':       RandomForestClassifier(n_estimators=100, random_state=42),
        'Naive Bayes':         GaussianNB(),
        'J48':                 DecisionTreeClassifier(criterion='entropy', random_state=42),
        'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    }

ALGO_NAMES = ['KNN', 'SVM', 'Random Forest', 'Naive Bayes', 'J48', 'Logistic Regression']
SEL_NAMES = ['No Selection', 'Info Gain', 'Chi-Square', 'CFS Subset']

# ── Kolom Fitur ──────────────────────────────────────────────────
BINARY_COLS = [
    'Genetics', 'Hormonal Changes', 'Poor Hair Care Habits',
    'Environmental Factors', 'Smoking', 'Weight Loss',
]
ONEHOT_COLS = [
    'Medical Conditions', 'Medications & Treatments', 'Nutritional Deficiencies',
]
STRESS_MAP = {'Low': 0, 'Medium': 1, 'High': 2}

# ── Wizard Steps ─────────────────────────────────────────────────
WIZARD_STEPS = ["Data Diri", "Riwayat & Kondisi", "Gaya Hidup", "Model & Hasil"]

# ── Data Dummy untuk Landing Page ───────────────────────────────
LANDING_STATS = [
    ("94.2%", "Akurasi Tertinggi"),
    ("12,500+", "Analisis Dilakukan"),
    ("24", "Kombinasi Model"),
    ("11", "Faktor Risiko Dianalisis"),
]

LANDING_STEPS = [
    ("📋", "Isi Data Klinis", "Jawab beberapa pertanyaan singkat seputar riwayat kesehatan dan gaya hidup Anda."),
    ("🤖", "AI Menganalisis", "Model machine learning kami memproses data menggunakan 6 algoritma berbeda."),
    ("📊", "Lihat Hasil", "Dapatkan prediksi risiko kebotakan beserta tingkat probabilitasnya secara instan."),
]

LANDING_TESTIMONIALS = [
    ("⭐⭐⭐⭐⭐", "Hasil analisisnya cepat banget dan penjelasannya mudah dipahami. Jadi lebih aware sama faktor risiko yang aku punya.", "Dimas Pratama", "12 Juni 2026"),
    ("⭐⭐⭐⭐⭐", "Suka sama tampilannya yang simpel tapi tetap informatif. Wizard step-nya juga membantu biar nggak bingung isi data.", "Rina Wulandari", "3 Juni 2026"),
    ("⭐⭐⭐⭐", "Awalnya ragu karena gratis, ternyata akurasinya cukup masuk akal dibanding kondisi aku sehari-hari. Recommended buat awareness.", "Bagas Nugroho", "28 Mei 2026"),
]

LANDING_FAQS = [
    ("Apa itu HairFall AI?", "HairFall AI adalah aplikasi yang memprediksi risiko kebotakan berdasarkan data klinis dan gaya hidup menggunakan machine learning, dengan 6 algoritma berbeda yang bisa dibandingkan."),
    ("Bagaimana cara kerja prediksinya?", "Anda mengisi data seperti usia, riwayat genetik, kondisi medis, dan gaya hidup. Sistem kami memproses data tersebut melalui model yang sudah dilatih dengan dataset klinis untuk menghasilkan prediksi risiko."),
    ("Apakah data saya disimpan?", "Tidak. Data yang Anda masukkan hanya digunakan untuk proses prediksi saat itu juga dan tidak disimpan di server."),
    ("Apakah hasil ini menggantikan diagnosis dokter?", "Tidak. Hasil prediksi ini bersifat edukatif dan tidak menggantikan konsultasi dengan dokter atau ahli trikologi profesional."),
]