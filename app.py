import streamlit as st
#For Modal Box After Computation
@st.dialog("Your Results:", width="large")
def results():
        if absences >= 4:
            st.title("You just failed your subject grade due to your excessive absences!😠")
        else:
            st.metric(label="Your Computed Prelim Grade", value=f"{prelim_grade:,.2f}")
            st.subheader("To Pass the Subject with 75 Overall Grade")
            col1, col2 = st.columns(2)
            col1.metric(label="Your Needed Midterm Grade", value=f"{required_passing:,.2f}")
            col2.metric(label="Your Needed Final Grade", value=f"{required_passing:,.2f}")
            st.subheader("To be Eligible for Dean's Lister with 90 Overall Grade")
            col3, col4 = st.columns(2)
            col3.metric(label="Your Needed Midterm Grade", value=f"{required_dean:,.2f}")
            col4.metric(label="Your Needed Final Grade", value=f"{required_dean:,.2f}")
        if st.button("Okay!"):
            st.rerun()
if results not in st.session_state:
#Title
    st.title("I am Grader! Your Subject Grade Calculator🧮")
    st.subheader("I will Calculate your Needed Grade to Pass the Subject and TO BE PART OF THE DEAN'S LIST Based on your Preliminary Performance")
    st.caption("Needed Inputs for Computation:")
#Input Field
    col1, col2, col3, col4, col5 = st.columns(5)
    absences = col1.number_input("Absences", min_value=0, max_value=18)
    prelim_exam = col2.number_input("Prelim Exam Grade", min_value=0.00, max_value=100.00)
    quizzes = col3.number_input("Quizzes Grade", min_value=0.00, max_value=100.00)
    requirements = col4.number_input("Requirements Grade", min_value=0.00, max_value=100.00)
    recitation = col5.number_input("Recitation Grade", min_value=0.00, max_value=100.00)
#Calculation Field
    def compute_absences(absences):
        if absences == 3:
            absences = int(70)
        elif absences == 2:
            absences = int(80)
        elif absences == 1:
            absences = int(90)
        elif absences == 0:
            absences = int(100)
        else:
            absences = int(0)
        return absences
    attendance = compute_absences(absences)
    class_standing = quizzes * .4 + requirements * .3 + recitation * .3
    prelim_grade = attendance * .1 + prelim_exam * .6 + class_standing * .3
#Calculate Passing Grade
    midterm_weight = .3
    final_weight = .5
    remains_passing = 75 - (prelim_grade * .2)
    required_passing = remains_passing / (midterm_weight + final_weight)
#Calculate Dean Grade
    remains_dean = 90 - (prelim_grade * .2)
    required_dean = remains_dean / (midterm_weight + final_weight)
#Text Prompting
    execute = st.button("Compute", type="primary", use_container_width=(True))
if execute:
    results()