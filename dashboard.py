import streamlit as st
import pandas as pd
import plotly.express as px
import time as t


def app():
    teacher_data = pd.read_csv("Csv//Teacher.csv")
    students_data = pd.read_csv("Csv//Students.csv")
    course_data = pd.read_csv("Csv//Courses.csv")
    session_data = pd.read_csv("Csv//Sessions.csv")
    st.header("Dashboard:chart_with_upwards_trend:")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(
            """
            <div style="padding: 10px; background-color: #0f089e; border-radius: 10px; text-align: center;">
                <h3>Students</h3>
                <p style="font-size: 30px; color: #1f77b4;">{}</p>
            </div>
            """.format(students_data[students_data.columns[0]].count()),
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            """
            <div style="padding: 10px; background-color: #0f089e; border-radius: 10px; text-align: center;">
                <h3>Teachers</h3>
                <p style="font-size: 30px; color: #ff7f0e;">{}</p>
            </div>
            """.format(teacher_data[teacher_data.columns[0]].count()),
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div style="padding: 10px; background-color: #0f089e; border-radius: 10px; text-align: center;">
                <h3>Courses</h3>
                <p style="font-size: 30px; color: #2ca02c;">{}</p>
            </div>
            """.format(course_data[course_data.columns[0]].count()),
            unsafe_allow_html=True
        )
    with col4:
        st.markdown(
            """
            <div style="padding: 10px; background-color: #0f089e; border-radius: 10px; text-align: center;">
                <h3>Sessions</h3>
                <p style="font-size: 30px; color: #d62728;">{}</p>
            </div>
            """.format(session_data[session_data.columns[0]].count()),
            unsafe_allow_html=True
        )
    selected_data = st.selectbox('Select Data', [
                                 'Select Data', 'Teacher Data', 'Students Data', 'course data', 'session data'])
    selected_chart_type = st.selectbox('Select Chart Type', [
                                       'Select Chart Type', 'Line Chart', 'Bar Chart', 'Pie Chart', 'Scatter Plot'])

    if selected_data == 'Teacher Data':
        with st.spinner("Processing..."):
            t.sleep(1)

        st.title("Teacher Data")
        st.dataframe(teacher_data, width=1500, height=100)

        if selected_chart_type != 'Select Chart Type':
            if selected_chart_type == 'Line Chart':
                chart_data = st.selectbox('Select a column for the line chart', teacher_data.columns)
                chart = px.line(teacher_data, x=teacher_data.index, y=chart_data)
            elif selected_chart_type == 'Bar Chart':
                position_counts = teacher_data['Position'].value_counts()
                fig_bar = px.bar(position_counts, x=position_counts.index,
                                 y=position_counts.values, labels={'x': 'Position', 'y': 'Count'})
                st.plotly_chart(fig_bar)
            elif selected_chart_type == 'Pie Chart':
                gender_counts = teacher_data['Gender'].value_counts()
                gender_distribution = pd.DataFrame({
                    'Gender': ['Male', 'Female'],
                    'Count': [gender_counts.get('Male', 0), gender_counts.get('Female', 0)]
                })
                fig_pie = px.pie(gender_distribution, names='Gender',
                                 values='Count', title='Gender Distribution')
                st.plotly_chart(fig_pie)
            elif selected_chart_type == 'Scatter Plot':
                x_axis = st.selectbox(
                    'Select x-axis column for scatter plot', teacher_data.columns)
                y_axis = st.selectbox(
                    'Select y-axis column for scatter plot', teacher_data.columns)
                chart = px.scatter(teacher_data, x=x_axis, y=y_axis)
            
                st.plotly_chart(chart)
        else:
            st.warning("Select a valid chart type")

    elif selected_data == 'Students Data':
        with st.spinner("Processing..."):
            t.sleep(1)
        st.title("Students Data")
        st.dataframe(students_data, width=1500, height=100)

        if selected_chart_type != 'Select Chart Type':
            if selected_chart_type == 'Line Chart':
                chart_data = st.selectbox(
                    'Select a column for the line chart', students_data.columns)
                chart = px.line(
                    students_data, x=students_data.index, y=chart_data)
            elif selected_chart_type == 'Bar Chart':
                chart_data = st.selectbox(
                    'Select a column for the bar chart', students_data.columns)
                chart = px.bar(
                    students_data, x=students_data.index, y=chart_data)
            elif selected_chart_type == 'Pie Chart':
                chart_column = st.selectbox(
                    'Select a column for the Pie Chart', students_data.columns)
                chart = px.pie(students_data, names=chart_column)
            elif selected_chart_type == 'Scatter Plot':
                x_axis = st.selectbox(
                    'Select x-axis column for scatter plot', students_data.columns)
                y_axis = st.selectbox(
                    'Select y-axis column for scatter plot', students_data.columns)
                chart = px.scatter(students_data, x=x_axis, y=y_axis)
            st.plotly_chart(chart)
        else:
            st.warning("Select a valid chart type")

    elif selected_data == 'session data':
        with st.spinner("Processing..."):
            t.sleep(1)
        st.title("Session Data")
        st.dataframe(session_data, width=1500, height=100)

        if selected_chart_type != 'Select Chart Type':
            if selected_chart_type == 'Line Chart':
                chart_data = st.selectbox(
                    'Select a column for the line chart', session_data.columns)
                chart = px.line(
                    session_data, x=session_data.index, y=chart_data)
            elif selected_chart_type == 'Bar Chart':
                chart_data = st.selectbox(
                    'Select a column for the bar chart', session_data.columns)
                chart = px.bar(
                    session_data, x=session_data.index, y=chart_data)
            elif selected_chart_type == 'Pie Chart':
                fig_pie = px.pie(session_data, names='Participants', title='Participants Distribution')
                st.plotly_chart(fig_pie)
            elif selected_chart_type == 'Scatter Plot':
                x_axis = st.selectbox(
                    'Select x-axis column for scatter plot', session_data.columns)
                y_axis = st.selectbox(
                    'Select y-axis column for scatter plot', session_data.columns)
                chart = px.scatter(session_data, x=x_axis, y=y_axis)
            st.plotly_chart(chart)
        else:
            st.warning("Select a valid chart type")

    elif selected_data == 'course data':
        with st.spinner("Processing..."):
            t.sleep(1)
        st.title("Course Data")
        st.dataframe(course_data, width=1500, height=100)

        if selected_chart_type != 'Select Chart Type':
            if selected_chart_type == 'Line Chart':
                chart_data = st.selectbox(
                    'Select a column for the line chart', course_data.columns)
                chart = px.line(course_data, x=course_data.index, y=chart_data)
            elif selected_chart_type == 'Bar Chart':
                chart_data = st.selectbox(
                    'Select a column for the bar chart', course_data.columns)
                chart = px.bar(course_data, x=course_data.index, y=chart_data)
            elif selected_chart_type == 'Pie Chart':
                chart_column = st.selectbox(
                    'Select a column for the Pie Chart', course_data.columns)
                chart = px.pie(course_data, names=chart_column)
            elif selected_chart_type == 'Scatter Plot':
                x_axis = st.selectbox(
                    'Select x-axis column for scatter plot', course_data.columns)
                y_axis = st.selectbox(
                    'Select y-axis column for scatter plot', course_data.columns)
                chart = px.scatter(course_data, x=x_axis, y=y_axis)
            st.plotly_chart(chart)
        else:
            st.warning("Select a valid chart type")

    else:
        st.warning("---NOTHING TO SHOW---")
