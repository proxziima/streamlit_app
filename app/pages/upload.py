import streamlit as st
import pandas as pd

def show(go_to_map_columns):
    st.title('App de Análise de Similaridade')
    uploaded_file = st.file_uploader('Escolha um arquivo Excel', type='xlsx')

    if uploaded_file is not None:
        st.session_state.df = pd.read_excel(uploaded_file)
        st.sessioon_state.excel_columns = st.session_state.df.columns.tolist()
        go_to_map_columns()