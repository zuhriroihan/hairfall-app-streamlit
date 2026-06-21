"""
Landing page — terinspirasi dari struktur myhair.ai (hero, how it works,
stats, testimonial, FAQ, CTA), menggunakan data dummy.
"""

import streamlit as st
from modules.state import go_to_wizard
from modules.config import LANDING_STATS, LANDING_STEPS, LANDING_TESTIMONIALS, LANDING_FAQS


def render_landing():
    _render_navbar()
    _render_hero()
    _render_trust_bar()
    _render_how_it_works()
    _render_stats()
    _render_testimonials()
    _render_faq()
    _render_cta()
    _render_footer()


def _render_navbar():
    st.markdown("""
    <div class="navbar">
        <div class="navbar-logo">Hair<span>Fall</span>AI</div>
    </div>
    """, unsafe_allow_html=True)


def _render_hero():
    st.markdown("""
    <div class="hero">
        <div class="hero-badge">🧠 Didukung Machine Learning</div>
        <h1>Cek Risiko <span>Kebotakan</span><br>Anda dalam Hitungan Detik</h1>
        <p>Analisis risiko kebotakan berbasis AI dari data klinis Anda. Dapatkan insight
        personal dan pahami faktor risiko yang memengaruhi kesehatan rambut Anda.</p>
    </div>
    """, unsafe_allow_html=True)

    col = st.columns([1, 1, 1])[1]
    with col:
        st.button("🔍 Mulai Prediksi Gratis", on_click=go_to_wizard,
                   use_container_width=True, key="hero_cta")

    stat_html = '<div style="text-align:center;"><div class="hero-stat-card">'
    for i, (num, label) in enumerate([
        ("94.2%", "Akurasi Model"),
        ("12,500+", "Analisis Selesai"),
        ("6", "Algoritma AI"),
    ]):
        if i > 0:
            stat_html += '<div style="width:1px;height:36px;background:#E2E8F0;"></div>'
        stat_html += f"""
        <div>
            <div class="hero-stat-number">{num}</div>
            <div class="hero-stat-label">{label}</div>
        </div>"""
    stat_html += '</div></div>'
    st.markdown(stat_html, unsafe_allow_html=True)


def _render_trust_bar():
    st.markdown("""
    <div class="trust-bar">
        Dipercaya oleh <strong>12.500+ pengguna</strong> untuk memahami risiko
        kesehatan rambut mereka
    </div>
    <br>
    """, unsafe_allow_html=True)


def _render_how_it_works():
    st.markdown('<div class="section-title">Cara Kerja</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Hanya 3 langkah sederhana untuk mengetahui '
        'risiko kebotakan Anda</div>',
        unsafe_allow_html=True,
    )

    cols = st.columns(3)
    for col, (icon, title, desc) in zip(cols, LANDING_STEPS):
        with col:
            st.markdown(f"""
            <div class="step-card">
                <div class="icon-circle">{icon}</div>
                <h3>{title}</h3>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)


def _render_stats():
    st.markdown('<div class="section-title">Platform Terpercaya</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Dibangun di atas data klinis nyata dan '
        'teknologi machine learning terkini</div>',
        unsafe_allow_html=True,
    )

    cols = st.columns(4)
    for col, (num, lbl) in zip(cols, LANDING_STATS):
        with col:
            st.markdown(f"""
            <div class="stat-box">
                <div class="num">{num}</div>
                <div class="lbl">{lbl}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)


def _render_testimonials():
    st.markdown('<div class="section-title">Apa Kata Mereka</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Dipercaya oleh ribuan pengguna di '
        'seluruh Indonesia</div>',
        unsafe_allow_html=True,
    )

    cols = st.columns(3)
    for col, (stars, text, name, date) in zip(cols, LANDING_TESTIMONIALS):
        with col:
            st.markdown(f"""
            <div class="testi-card">
                <div class="testi-stars">{stars}</div>
                <div class="testi-text">"{text}"</div>
                <div class="testi-author">{name}</div>
                <div class="testi-date">{date}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)


def _render_faq():
    st.markdown('<div class="section-title">Pertanyaan Umum</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    for q, a in LANDING_FAQS:
        with st.expander(q):
            st.write(a)

    st.markdown("<br>", unsafe_allow_html=True)


def _render_cta():
    st.markdown("""
    <div class="cta-section">
        <h2>Siap Mengetahui Risiko Kebotakan Anda?</h2>
        <p>Gratis, cepat, dan hanya butuh waktu 2 menit</p>
    </div>
    """, unsafe_allow_html=True)

    col = st.columns([1, 1, 1])[1]
    with col:
        st.button("Mulai Sekarang →", on_click=go_to_wizard,
                   use_container_width=True, key="cta_bottom")


def _render_footer():
    st.markdown("""
    <div class="footer">
        © 2026 HairFall AI · Dibuat untuk tujuan edukasi & riset machine learning<br>
        Bukan pengganti diagnosis medis profesional
    </div>
    """, unsafe_allow_html=True)