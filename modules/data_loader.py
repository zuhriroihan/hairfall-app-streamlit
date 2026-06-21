"""
Loader untuk model artifacts (.pkl) dan CSS custom.
"""

import streamlit as st
import joblib
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
ARTIFACTS_DIR = ROOT_DIR / "model_artifacts"
ASSETS_DIR = ROOT_DIR / "assets"


@st.cache_resource
def load_artifacts():
    """Load semua model artifacts hasil export dari Colab."""
    return {
        'scaler':       joblib.load(ARTIFACTS_DIR / 'scaler.pkl'),
        'feat_names':   joblib.load(ARTIFACTS_DIR / 'all_feature_names.pkl'),
        'log_cols':     joblib.load(ARTIFACTS_DIR / 'log_transformed_cols.pkl'),
        'df_clean':     joblib.load(ARTIFACTS_DIR / 'df_clean.pkl'),
        'datasets':     joblib.load(ARTIFACTS_DIR / 'datasets.pkl'),
        'idx_ig':       joblib.load(ARTIFACTS_DIR / 'idx_ig.pkl'),
        'idx_chi2':     joblib.load(ARTIFACTS_DIR / 'idx_chi2.pkl'),
        'idx_cfs':      joblib.load(ARTIFACTS_DIR / 'idx_cfs.pkl'),
        'y_train_bal':  joblib.load(ARTIFACTS_DIR / 'y_train_bal.pkl'),
    }


def load_css():
    """Inject CSS custom dari assets/style.css."""
    css_path = ASSETS_DIR / "style.css"
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)