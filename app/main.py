import streamlit as st
import pandas as pd
from app.config import UPLOAD_FOLDER
from app.pages import upload, map_columns, similarity_check


#Definir a variávcel de estado para a navegação
if 'page' not in st.session_state:
    st.session_state.page = 'upload'

def got_to_upload():
    st.session_state.page = 'upload'

def got_to_map_columns():
    st.session_state.page = 'map_columns'

def got_to_similarity_check():
    st.session_state.page = 'similarity_check'


# Gerenciar a navegação entre páginas
if st.session_state.page == 'upload':
    upload.show(got_to_map_columns)
elif st.session_state.page == 'map_columns':
    map_columns.show(got_to_map_columns, got_to_similarity_check)
elif st.session_state.page == 'similarity_check':
    similarity_check.show(got_to_upload)
