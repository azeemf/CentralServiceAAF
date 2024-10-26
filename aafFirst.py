import streamlit as st
import streamlit_authenticator as stauth

if 'authentication_status' not in st.session_state:
    st.session_state.authentication_status = None

st.set_page_config(
    page_title="MBA-AAF Services",
    page_icon="✈️",
    layout="centered",
    initial_sidebar_state="auto",
)

login_page = st.Page("aafHome.py", title="Login - MBA-AAF Services", icon="✈️")
landing_page = st.Page("aafLanding.py", title="Home - MBA-AAF Services", icon="✈️")

if st.session_state['authentication_status'] is None:
    pg = st.navigation([login_page])
    pg.run()

if st.session_state['authentication_status']:
    pg = st.navigation([landing_page])
    pg.run()