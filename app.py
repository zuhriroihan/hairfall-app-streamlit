import streamlit as st
import joblib, numpy as np, pandas as pd
from sklearn.linear_model     import LogisticRegression
from sklearn.ensemble         import RandomForestClassifier
from sklearn.neighbors        import KNeighborsClassifier
from sklearn.svm              import SVC
from sklearn.naive_bayes      import GaussianNB
from sklearn.tree             import DecisionTreeClassifier

# ── Load Artifacts ───────────────────────────────────────────────
@st.cache_resource
def load_artifacts():
    return {
        'scaler':        joblib.load('model_artifacts/scaler.pkl'),
        'feat_names':    joblib.load('model_artifacts/all_feature_names.pkl'),
        'orig_cols':     joblib.load('model_artifacts/original_feature_cols.pkl'),
        'log_cols':      joblib.load('model_artifacts/log_transformed_cols.pkl'),
        'df_clean':      joblib.load('model_artifacts/df_clean.pkl'),
        'datasets':      joblib.load('model_artifacts/datasets.pkl'),
        'idx_ig':        joblib.load('model_artifacts/idx_ig.pkl'),
        'idx_chi2':      joblib.load('model_artifacts/idx_chi2.pkl'),
        'idx_cfs':       joblib.load('model_artifacts/idx_cfs.pkl'),
        'y_train_bal':   joblib.load('model_artifacts/y_train_bal.pkl'),
    }

art = load_artifacts()

ALGO_MAP = {
    'KNN':                 KNeighborsClassifier(n_neighbors=5),
    'SVM':                 SVC(kernel='rbf', probability=True, random_state=42),
    'Random Forest':       RandomForestClassifier(n_estimators=100, random_state=42),
    'Naive Bayes':         GaussianNB(),
    'J48':                 DecisionTreeClassifier(criterion='entropy', random_state=42),
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
}
SEL_MAP = {
    'No Selection': None,
    'Info Gain':    art['idx_ig'],
    'Chi-Square':   art['idx_chi2'],
    'CFS Subset':   art['idx_cfs'],
}

# ── UI ───────────────────────────────────────────────────────────
st.set_page_config(page_title="Hair Fall Prediction", page_icon="💇", layout="wide")
st.title("💇 Hair Fall / Baldness Risk Prediction")
st.markdown("Masukkan data pasien untuk memprediksi risiko kebotakan.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("⚙️ Konfigurasi Model")
    algo = st.selectbox("Algoritma", list(ALGO_MAP.keys()))
    sel  = st.selectbox("Feature Selection", list(SEL_MAP.keys()))

with col2:
    st.subheader("👤 Data Pasien")
    df_c    = art['df_clean']
    target  = 'Baldness'
    binary  = ['Genetics','Hormonal Changes','Poor Hair Care Habits',
                'Environmental Factors','Smoking','Weight Loss']
    onehot  = ['Medical Conditions','Medications & Treatments','Nutritional Deficiencies']
    inp     = {}

    for col in [c for c in df_c.columns if c != target]:
        if col == 'Age':
            inp[col] = st.slider("Age", 0, 100, 35)
        elif col == 'Stress':
            inp[col] = st.selectbox("Stress Level", ['Low', 'Medium', 'High'])
        elif col in binary:
            inp[col] = st.radio(col, ['Yes', 'No'], horizontal=True)
        elif col in onehot:
            opts = sorted(df_c[col].dropna().unique().tolist(), key=str)
            inp[col] = st.selectbox(col, opts)

# ── Prediksi ─────────────────────────────────────────────────────
if st.button("🔍 Prediksi", use_container_width=True):
    input_df = pd.DataFrame([inp])

    for c in binary:
        if c in input_df.columns:
            input_df[c] = input_df[c].map({'Yes':1,'No':0}).astype(int)
    if 'Stress' in input_df.columns:
        input_df['Stress'] = input_df['Stress'].map({'Low':0,'Medium':1,'High':2})
    input_df = pd.get_dummies(input_df, columns=onehot, drop_first=False, dtype=int)
    for c in art['log_cols']:
        if c in input_df.columns:
            input_df[c] = np.log1p(input_df[c])
    input_aligned = input_df.reindex(columns=art['feat_names'], fill_value=0).astype(float)
    input_scaled  = art['scaler'].transform(input_aligned)

    idx_sel = SEL_MAP[sel]
    Xp      = input_scaled[:, idx_sel] if idx_sel is not None else input_scaled

    ds      = art['datasets'][sel]
    model   = ALGO_MAP[algo]
    model.fit(ds['Xtr'], art['y_train_bal'])

    pred  = model.predict(Xp)[0]
    proba = model.predict_proba(Xp)[0][1] if hasattr(model, 'predict_proba') else None

    st.divider()
    if pred == 1:
        st.error(f"⚠️ **BERISIKO KEBOTAKAN** ({proba*100:.1f}% probabilitas)" if proba else "⚠️ BERISIKO KEBOTAKAN")
    else:
        st.success(f"✅ **TIDAK BERISIKO KEBOTAKAN** ({(1-proba)*100:.1f}% aman)" if proba else "✅ TIDAK BERISIKO KEBOTAKAN")

    if proba:
        st.progress(float(proba), text=f"Probabilitas botak: {proba*100:.1f}%")