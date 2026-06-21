"""
HairFall AI — Entry point aplikasi Streamlit.
Hanya bertugas: setup halaman, load resource, dan routing antar page.
Logic detail ada di folder modules/.
"""

import streamlit as st
from modules.config import PAGE_TITLE, PAGE_ICON
from modules.data_loader import load_artifacts, load_css
from modules.state import init_state
from modules.landing import render_landing
from modules.wizard_steps import render_wizard

# ── Page Config (harus paling atas) ──────────────────────────────
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Load CSS & Artifacts ─────────────────────────────────────────
load_css()
artifacts = load_artifacts()

# ── Init Session State ───────────────────────────────────────────
init_state()

# ── Routing ───────────────────────────────────────────────────────
if st.session_state.page == "landing":
    render_landing()
else:
    render_wizard(artifacts)