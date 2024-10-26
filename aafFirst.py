import streamlit as st
import streamlit_authenticator as stauth

login_page = st.Page("aafHome.py", title="Login - MBA-AAF Services", icon="✈️")

pg = st.navigation([login_page])
pg.run()