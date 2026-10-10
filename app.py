import streamlit as st
from utils import check_password, load_custom_css

def main():
    # --- PAGE CONFIGURATION ---
    st.set_page_config(
        page_title="Baseline App Shell",
        page_icon="⚡",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # --- LOAD STYLES ---
    load_custom_css()

    # --- INITIALIZE SESSION STATE ---
    if "user_authenticated" not in st.session_state:
        st.session_state["user_authenticated"] = False
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "Dashboard"

    # --- AUTHENTICATION CHECK ---
    if not st.session_state["user_authenticated"]:
        if not check_password():
            st.stop()

    # --- SIDEBAR NAVIGATION ---
    st.sidebar.title("Navigation")
    page_options = ["Dashboard", "Data Analysis", "Settings"]
    st.sidebar.radio(
        "Select View:",
        options=page_options,
        key="current_page"
    )

    st.sidebar.markdown("---")
    st.sidebar.caption("System Status: Active")

    # --- ROUTER LOGIC ---
    current_page = st.session_state["current_page"]

    if current_page == "Dashboard":
        render_dashboard()
    elif current_page == "Data Analysis":
        render_data_analysis()
    elif current_page == "Settings":
        render_settings()

def render_dashboard():
    st.title("📊 Dashboard Baseline")
    st.write("Welcome to the core application workspace.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Active Sessions", "12", "+2")
    col2.metric("Processing Time", "1.2s", "-0.3s")
    col3.metric("System Load", "34%", "0%")

def render_data_analysis():
    st.title("📈 Data Analysis")
    st.write("Upload or query records here.")
    
    uploaded_file = st.file_uploader("Upload CSV Data", type=["csv"])
    if uploaded_file:
        st.success("File uploaded successfully!")

def render_settings():
    st.title("⚙️ Application Settings")
    st.text_input("API Base URL", value="https://api.example.com/v1")
    st.toggle("Enable Verbose Logging", value=True)

if __name__ == "__main__":
    main()
