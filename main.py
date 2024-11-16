import streamlit as st


hide_github_icon = """
<style>
.block-container div:nth-child(2) > div:nth-child(3) {
  display: none;
}
</style>
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)
# Sidebar Menu
st.sidebar.title("Menu")
menu = st.sidebar.selectbox("Select Category", ["Reports", "Tools"])

# Initialize placeholders for display
selected_option_text = "Welcome to the Lung Cancer Prediction Platform"

# Reports Section
if menu == "Reports":
    st.sidebar.subheader("Reports Menu")
    report_section = st.sidebar.selectbox(
        "Select Subcategory",
        ["Details", "Statistical Analysis"]
    )
    
    if report_section == "Details":
        report_page = st.sidebar.radio(
            "Select Page",
            ["Dashboard", "Diagnosis Anomalies", "Risk Prediction"]
        )
        if report_page == "Dashboard":
            selected_option_text = "Reports > Details > Dashboard"
            # exec(open("reports/details/dashboard.py").read())
        elif report_page == "Diagnosis Anomalies":
            selected_option_text = "Reports > Details > Diagnosis Anomalies"
            # exec(open("reports/details/diagnosis_anomalies.py").read())
        elif report_page == "Risk Prediction":
            selected_option_text = "Reports > Details > Risk Prediction"
            # exec(open("reports/details/risk_prediction.py").read())

    elif report_section == "Statistical Analysis":
        stat_page = st.sidebar.radio(
            "Select Page",
            ["Comparison", "Risk Level"]
        )
        if stat_page == "Comparison":
            selected_option_text = "Reports > Statistical Analysis > Comparison"
            # exec(open("reports/stat_analysis/comparasion.py").read())
        elif stat_page == "Risk Level":
            selected_option_text = "Reports > Statistical Analysis > Risk Level"
            # exec(open("reports/stat_analysis/risk_level.py").read())

# Tools Section
elif menu == "Tools":
    st.sidebar.subheader("Tools Menu")
    tools_page = st.sidebar.radio(
        "Select Tool",
        ["Chatbot", "Factors Risk Analysis", "Generate Case Studies"]
    )
    if tools_page == "Chatbot":
        selected_option_text = "Tools > Chatbot"
        # exec(open("tools/chatbot.py").read())
    elif tools_page == "Factors Risk Analysis":
        selected_option_text = "Tools > Factors Risk Analysis"
        # exec(open("tools/factors_risk_analysis.py").read())
    elif tools_page == "Generate Case Studies":
        selected_option_text = "Tools > Generate Case Studies"
        # exec(open("tools/generate_casestudies.py").read())

# Main Content Area
st.title("Lung Cancer Prediction Platform")
st.subheader(selected_option_text)
st.write("The content of the selected page will be displayed here.")
