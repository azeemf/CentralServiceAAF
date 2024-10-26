import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import os


def sidebar(authenticator):
    with st.sidebar:
        authenticator.logout()

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

    sidebar(authenticator)

    st.write("Logged in")

main()