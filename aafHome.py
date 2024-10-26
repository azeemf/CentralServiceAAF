import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

def main():
    with open('~/ServiceConfigs/c.yaml') as file:
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
        authenticator.logout()
        st.write("Shit")


    elif st.session_state['authentication_status'] is False:
        st.error('Username/password is incorrect')

    elif st.session_state['authentication_status'] is None:
        st.warning('Please enter your username and password')


st.set_page_config(
    page_title="MBA-AAF Services",
    page_icon="✈️",
    layout="centered",
    initial_sidebar_state="auto",
)


main()