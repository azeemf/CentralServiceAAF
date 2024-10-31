import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import os

def main():
    yaml_path = os.path.expanduser('~/ServiceConfigs/c.yaml') 
    with open(yaml_path) as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
    )

    try:
        authenticator.login()
    except:
        st.error("Auth Failed")

    if st.session_state['authentication_status']:
        st.rerun()

    elif st.session_state['authentication_status'] is False:
        st.error('Username/password is incorrect')

    elif st.session_state['authentication_status'] is None:
        st.warning('Please enter your username and password')

    st.link_button("Experiance", url="https://exp.aaf-services.uk", use_container_width=True)

    icol1, icol2, icol3 = st.columns(3)

    with icol1:
        st.write(" ")
    
    with icol2:
        st.image("MBA Creations Logo.png", width=250)

    with icol3:
        st.write(" ")

main()