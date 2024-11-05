import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import os
from datetime import date
import time

var = 0

@st.fragment(run_every="1s")
def usageStats(var):
    var = var + 1
    st.write(var)
    time.sleep(1)

def sidebar(authenticator):
    with st.sidebar:
        authenticator.logout()
    with st.popover("Show Usage"):
        usageStats()

def topBar(authenticator):
    tbcol1, tbcol2 = st.columns(2)

    with tbcol1:
        st.subheader("Welcome " + st.session_state["name"])

    with tbcol2:
        today = date.today()
        text_today = today.strftime("%B %d, %Y")
        st.subheader(f"{text_today}")

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
    topBar(authenticator)

main()