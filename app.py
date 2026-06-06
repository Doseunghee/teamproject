import os
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

# Streamlit Community Cloud entrypoint
# 같은 GitHub 폴더에 index.html과 DB 파일 3개를 함께 올리면 됩니다.

BASE_DIR = Path(__file__).resolve().parent
INDEX_PATH = BASE_DIR / "index.html"

DB_FILES = [
    "graduate-analysis.db",
    "부모자녀데이터.db",
    "klips_project.db",
]

st.set_page_config(
    page_title="대한민국 계층 고착화 실태 분석 대시보드",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        .block-container {padding-top: 0rem; padding-bottom: 0rem; max-width: 100%;}
        header[data-testid="stHeader"] {display: none;}
        footer {display: none;}
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.title("파일 상태")

    if INDEX_PATH.exists():
        st.success("index.html 확인 완료")
    else:
        st.error("index.html 파일이 없습니다.")

    for db_name in DB_FILES:
        db_path = BASE_DIR / db_name
        if db_path.exists():
            st.success(f"{db_name} 확인 완료")
        else:
            st.error(f"{db_name} 파일이 없습니다.")

missing_files = [db for db in DB_FILES if not (BASE_DIR / db).exists()]

if not INDEX_PATH.exists():
    st.error("같은 폴더에 index.html을 올려주세요.")
    st.stop()

if missing_files:
    st.error("다음 DB 파일이 누락되었습니다: " + ", ".join(missing_files))
    st.stop()

html = INDEX_PATH.read_text(encoding="utf-8")
components.html(html, height=9000, scrolling=True)
