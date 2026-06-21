"""
Session state initialization & fungsi navigasi antar halaman/step.
"""

import streamlit as st


def init_state():
    """Inisialisasi semua session state yang dibutuhkan app."""
    if 'page' not in st.session_state:
        st.session_state.page = 'landing'   # 'landing' atau 'wizard'
    if 'step' not in st.session_state:
        st.session_state.step = 1            # step wizard 1-4
    if 'data' not in st.session_state:
        st.session_state.data = {}           # data form yang diisi user
    if 'result' not in st.session_state:
        st.session_state.result = None       # hasil prediksi terakhir


def go_to_wizard():
    st.session_state.page = 'wizard'


def go_to_landing():
    st.session_state.page = 'landing'
    st.session_state.step = 1
    st.session_state.data = {}
    st.session_state.result = None


def next_step():
    st.session_state.step += 1


def prev_step():
    st.session_state.step -= 1


def reset_wizard():
    st.session_state.step = 1
    st.session_state.data = {}
    st.session_state.result = None