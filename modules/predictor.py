"""
Logic preprocessing input & menjalankan prediksi model.
"""

import numpy as np
import pandas as pd
from modules.config import get_algo_map, BINARY_COLS, ONEHOT_COLS, STRESS_MAP


def build_selection_map(art):
    """Mapping nama metode feature selection -> index kolom terpilih."""
    return {
        'No Selection': None,
        'Info Gain':    art['idx_ig'],
        'Chi-Square':   art['idx_chi2'],
        'CFS Subset':   art['idx_cfs'],
    }


def preprocess_input(raw_data: dict, art: dict) -> pd.DataFrame:
    """
    Ubah data mentah dari form wizard menjadi DataFrame yang siap
    di-scale, sesuai pipeline preprocessing saat training.
    """
    input_df = pd.DataFrame([raw_data])

    # Binary encoding (Yes/No -> 1/0)
    for col in BINARY_COLS:
        if col in input_df.columns:
            input_df[col] = input_df[col].map({'Yes': 1, 'No': 0}).astype(int)

    # Ordinal encoding untuk Stress
    if 'Stress' in input_df.columns:
        input_df['Stress'] = input_df['Stress'].map(STRESS_MAP)

    # One-hot encoding
    input_df = pd.get_dummies(input_df, columns=ONEHOT_COLS, drop_first=False, dtype=int)

    # Log transform kolom yang skewed
    for col in art['log_cols']:
        if col in input_df.columns:
            input_df[col] = np.log1p(input_df[col])

    # Samakan urutan & kelengkapan kolom dengan saat training
    input_aligned = input_df.reindex(columns=art['feat_names'], fill_value=0).astype(float)

    return input_aligned


def run_prediction(raw_data: dict, algo_name: str, sel_name: str, art: dict) -> dict:
    """
    Jalankan full pipeline: preprocessing -> scaling -> feature selection -> fit & predict.
    Return dict berisi prediksi (0/1) dan probabilitas.
    """
    input_aligned = preprocess_input(raw_data, art)
    input_scaled = art['scaler'].transform(input_aligned)

    sel_map = build_selection_map(art)
    idx_sel = sel_map[sel_name]
    X_pred = input_scaled[:, idx_sel] if idx_sel is not None else input_scaled

    ds = art['datasets'][sel_name]
    model = get_algo_map()[algo_name]
    model.fit(ds['Xtr'], art['y_train_bal'])

    pred = int(model.predict(X_pred)[0])
    proba = float(model.predict_proba(X_pred)[0][1]) if hasattr(model, 'predict_proba') else None

    return {'prediction': pred, 'probability': proba}