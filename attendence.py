import streamlit as st
import pandas as pd
from datetime import datetime

students_df = pd.read_csv('Csv//Students.csv')

def calculate_percentage_attendance(student_id, attendance_df):
    total_sessions = len(attendance_df)
    attended_sessions = attendance_df[str(student_id)].sum()
    percentage_attendance = (attended_sessions / total_sessions) * 100 if total_sessions > 0 else 0
    return f"{percentage_attendance:.2f}%"

def app():
    try:
        attendance_df = pd.read_csv('Csv//attendance.csv')
    except FileNotFoundError:
        attendance_df = pd.DataFrame(columns=['Date'] + students_df['StudentID'].astype(str).tolist())

    st.title("Attendance System")
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Student List")
        selected_student = st.selectbox("Select a student", students_df['Name'])
        st.header("Student Data")
        st.write(students_df[['StudentID', 'Name']])

    with col2:
        if st.button("Mark Attendance"):
            current_date = datetime.now().strftime("%Y-%m-%d")

            if 'Date' not in attendance_df.columns:
                attendance_df.insert(0, 'Date', '')

            if current_date not in attendance_df['Date'].values:
                attendance_df.loc[len(attendance_df.index)] = [current_date] + [False] * len(students_df)

            student_id = students_df.loc[students_df['Name'] == selected_student, 'StudentID'].values[0]
            attendance_df.loc[attendance_df['Date'] == current_date, str(student_id)] = True
            st.success(f"Attendance marked for {selected_student}")
            attendance_df.to_csv('Csv//attendance.csv', index=False)

        st.subheader("Attendance Status")
        st.write(attendance_df)

        if st.button("Export Attendance"):
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            attendance_df.to_csv(f'attendance_{timestamp}.csv', index=False)
            st.success("Attendance exported successfully")

        if st.button("Clear Attendance"):
            attendance_df = pd.DataFrame(columns=['Date'] + students_df['StudentID'].astype(str).tolist())
            st.success("Attendance cleared")

        st.subheader("Student Data")
        student_id = students_df.loc[students_df['Name'] == selected_student, 'StudentID'].values[0]
        percentage_attendance = calculate_percentage_attendance(student_id, attendance_df)
        st.write(f"Percentage Attendance: {percentage_attendance}")


