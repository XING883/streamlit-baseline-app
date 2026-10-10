import streamlit as st

def load_custom_css():
    """Injects lightweight custom styling into the Streamlit app."""
    custom_css = """
        <style>
            .block-container { padding-top: 2rem; }
            footer { visibility: hidden; }
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def check_password():
    """Simple passcode check pattern using secrets.toml."""
    if st.session_state.get("password_correct", False):
        return True

    password_input = st.text_input("Enter Passcode", type="password", key="password_input")

    if password_input:
        expected_password = st.secrets.get("APP_PASSWORD", "admin123")
        if password_input == expected_password:
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("Incorrect Password")

    return False
