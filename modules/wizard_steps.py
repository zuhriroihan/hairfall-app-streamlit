"""
4 Step Wizard untuk form input data pasien + halaman hasil prediksi.
"""

import streamlit as st
from modules.config import ALGO_NAMES, SEL_NAMES, WIZARD_STEPS
from modules.state import next_step, prev_step, go_to_landing, reset_wizard
from modules.predictor import run_prediction


def render_wizard(art):
    st.button("← Kembali ke Beranda", on_click=go_to_landing, key="back_home")

    st.markdown("""
    <div class="main-header">
        <h1>🩺 Hair Fall Risk Prediction</h1>
        <p>Prediksi risiko kebotakan berdasarkan data klinis Anda</p>
    </div>
    """, unsafe_allow_html=True)

    _render_progress_bar()

    step = st.session_state.step
    if step == 1:
        _step_1_data_diri()
    elif step == 2:
        _step_2_riwayat_kondisi(art)
    elif step == 3:
        _step_3_gaya_hidup(art)
    elif step == 4:
        _step_4_model_hasil(art)


def _render_progress_bar():
    html = '<div class="wizard-progress">'
    for i, label in enumerate(WIZARD_STEPS, 1):
        if i == st.session_state.step:
            cls = "active"
        elif i < st.session_state.step:
            cls = "done"
        else:
            cls = ""
        html += f'<div class="wizard-step {cls}">{i}. {label}</div>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)


# ── STEP 1: Data Diri ────────────────────────────────────────────
def _step_1_data_diri():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="step-label">Step 1 dari 4</div>', unsafe_allow_html=True)
    st.markdown('<div class="step-title">👤 Data Diri</div>', unsafe_allow_html=True)

    data = st.session_state.data
    data['Age'] = st.slider("Usia", 0, 100, data.get('Age', 30))
    data['Stress'] = st.selectbox(
        "Tingkat Stress", ['Low', 'Medium', 'High'],
        index=['Low', 'Medium', 'High'].index(data.get('Stress', 'Medium')),
    )

    st.markdown('</div>', unsafe_allow_html=True)
    st.button("Lanjut →", on_click=next_step, use_container_width=True, key="next_1")


# ── STEP 2: Riwayat & Kondisi ────────────────────────────────────
def _step_2_riwayat_kondisi(art):
    df_c = art['df_clean']
    data = st.session_state.data

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="step-label">Step 2 dari 4</div>', unsafe_allow_html=True)
    st.markdown('<div class="step-title">🏥 Riwayat & Kondisi Medis</div>', unsafe_allow_html=True)

    data['Genetics'] = st.radio(
        "Riwayat Genetik Kebotakan", ['Yes', 'No'], horizontal=True,
        index=['Yes', 'No'].index(data.get('Genetics', 'No')),
    )
    data['Hormonal Changes'] = st.radio(
        "Perubahan Hormonal", ['Yes', 'No'], horizontal=True,
        index=['Yes', 'No'].index(data.get('Hormonal Changes', 'No')),
    )

    opts_mc = sorted(df_c['Medical Conditions'].dropna().unique().tolist(), key=str)
    data['Medical Conditions'] = st.selectbox(
        "Kondisi Medis", opts_mc,
        index=opts_mc.index(data.get('Medical Conditions', opts_mc[0])),
    )

    opts_med = sorted(df_c['Medications & Treatments'].dropna().unique().tolist(), key=str)
    data['Medications & Treatments'] = st.selectbox(
        "Obat / Treatment yang Dikonsumsi", opts_med,
        index=opts_med.index(data.get('Medications & Treatments', opts_med[0])),
    )

    st.markdown('</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    c1.button("← Kembali", on_click=prev_step, use_container_width=True, key="prev_2")
    c2.button("Lanjut →", on_click=next_step, use_container_width=True, key="next_2")


# ── STEP 3: Gaya Hidup ───────────────────────────────────────────
def _step_3_gaya_hidup(art):
    df_c = art['df_clean']
    data = st.session_state.data

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="step-label">Step 3 dari 4</div>', unsafe_allow_html=True)
    st.markdown('<div class="step-title">🏃 Gaya Hidup & Lingkungan</div>', unsafe_allow_html=True)

    binary_fields = [
        ("Kebiasaan Perawatan Rambut Buruk", "Poor Hair Care Habits"),
        ("Paparan Faktor Lingkungan", "Environmental Factors"),
        ("Merokok", "Smoking"),
        ("Penurunan Berat Badan Signifikan", "Weight Loss"),
    ]
    for label, key in binary_fields:
        data[key] = st.radio(
            label, ['Yes', 'No'], horizontal=True, key=f"radio_{key}",
            index=['Yes', 'No'].index(data.get(key, 'No')),
        )

    opts_nd = sorted(df_c['Nutritional Deficiencies'].dropna().unique().tolist(), key=str)
    data['Nutritional Deficiencies'] = st.selectbox(
        "Defisiensi Nutrisi", opts_nd,
        index=opts_nd.index(data.get('Nutritional Deficiencies', opts_nd[0])),
    )

    st.markdown('</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    c1.button("← Kembali", on_click=prev_step, use_container_width=True, key="prev_3")
    c2.button("Lanjut →", on_click=next_step, use_container_width=True, key="next_3")


# ── STEP 4: Model & Hasil ────────────────────────────────────────
def _step_4_model_hasil(art):
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="step-label">Step 4 dari 4</div>', unsafe_allow_html=True)
    st.markdown('<div class="step-title">⚙️ Pilih Model & Lihat Hasil</div>', unsafe_allow_html=True)

    algo = st.selectbox("Algoritma", ALGO_NAMES, key="algo_select")
    sel = st.selectbox("Metode Feature Selection", SEL_NAMES, key="sel_select")

    st.markdown('</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    c1.button("← Kembali", on_click=prev_step, use_container_width=True, key="prev_4")
    predict_clicked = c2.button("🔍 Prediksi Sekarang", use_container_width=True, key="predict_btn")

    if predict_clicked:
        with st.spinner("Menganalisis data..."):
            result = run_prediction(st.session_state.data, algo, sel, art)
            st.session_state.result = result

    if st.session_state.result is not None:
        _render_result(st.session_state.result)
        st.button("🔄 Mulai Ulang", on_click=reset_wizard,
                   use_container_width=True, key="restart_btn")


def _render_result(result: dict):
    pred = result['prediction']
    proba = result['probability']

    st.markdown("<br>", unsafe_allow_html=True)

    if pred == 1:
        pct = f"{proba * 100:.1f}%" if proba is not None else "-"
        st.markdown(f"""
        <div class="result-risk">
            <div class="result-title">⚠️ Berisiko Kebotakan</div>
            <p>Probabilitas: <strong>{pct}</strong></p>
        </div>""", unsafe_allow_html=True)
    else:
        pct = f"{(1 - proba) * 100:.1f}%" if proba is not None else "-"
        st.markdown(f"""
        <div class="result-safe">
            <div class="result-title">✅ Tidak Berisiko Kebotakan</div>
            <p>Tingkat aman: <strong>{pct}</strong></p>
        </div>""", unsafe_allow_html=True)

    if proba is not None:
        st.progress(float(proba), text=f"Probabilitas risiko: {proba * 100:.1f}%")