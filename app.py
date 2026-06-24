import streamlit as st
import pickle

st.markdown("""
<style>
.main {
    padding-top: 2rem;
}
.stButton>button {
    border-radius: 10px;
    height: 3em;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# Page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# Load model
with open("student_model.pkl", "rb") as file:
    model = pickle.load(file)

# Header
st.title("🎓 Student Performance Predictor")
st.markdown("Predict a student's final score using Machine Learning")

st.divider()

# Input Section
st.subheader("📚 Student Details")

col1, col2 = st.columns(2)

with col1:
    study_hours = st.slider("Study Hours", 0, 12, 4)

with col2:
    attendance = st.slider("Attendance (%)", 0, 100, 80)

col3, col4 = st.columns(2)

with col3:
    assignments = st.slider("Assignments Completed", 0, 10, 5)

with col4:
    previous_score = st.slider("Previous Score", 0, 100, 70)

st.divider()

# Prediction Button
if st.button("🚀 Predict Performance", use_container_width=True):

    prediction = model.predict([[
        study_hours,
        attendance,
        assignments,
        previous_score
    ]])

    score = prediction[0]

    # Grade Logic
    if score >= 90:
        grade = "A+"
        emoji = "🏆"
    elif score >= 80:
        grade = "A"
        emoji = "🌟"
    elif score >= 70:
        grade = "B"
        emoji = "👍"
    elif score >= 60:
        grade = "C"
        emoji = "📘"
    else:
        grade = "D"
        emoji = "⚠️"

    st.success(f"Predicted Final Score: {score:.2f}")

    st.metric(
        label="Predicted Grade",
        value=f"{emoji} {grade}"
    )

    # Progress Bar
    st.subheader("Performance Meter")
    st.progress(min(int(score), 100))

    # Feedback
    if score >= 85:
        st.balloons()
        st.info("Excellent performance predicted!")
    elif score >= 70:
        st.info("Good performance predicted.")
    else:
        st.warning("Student may need additional support.")