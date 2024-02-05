import streamlit as st
import pandas as pd
import datetime
import re

df = pd.read_csv("Csv//Students.csv")

def validate_email(email):
    pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"

    if re.match(pattern, email):
        return True
    return False
min=1
max=11
def app():
    st.header("Student Database:male-student:")
    st.subheader("Add View Delete")
    choice=st.selectbox('Choose Operation',['Add Student','View Student','Delete Student'],key="StudentsBox")
    if choice=="Add Student":
        with st.form(key="Studentform", clear_on_submit=True):
            studentName = st.text_input("Name")
            studentregistry=st.number_input("Registration Number",min_value=100000000)
            #p = re.compile(r'^\d{11}$')
            studentuniroll=st.number_input("Enter University roll number")
            # if not pattern.match(p):
            #     st.warning("Please enter a valid format.")
            pattern = re.compile(r'^[A-Za-z]{3}\d{6}$')
            studentroll=st.text_input("Enter College roll number")
            # if not pattern.match(studentroll):
            #     st.warning("Please enter a valid format.")
            #s = re.compile(r'^20\d{2}$')
            studentaddmission=st.text_input("Enter your admission year")
            # if not pattern.match(s):
            #     st.warning("Please enter a valid format.")
            studentGender = st.selectbox("Gender", ['Male', 'Female'])
            studentdob=st.date_input("Enter your date of birth",min_value=datetime.date(1980,1,1))
            studentaddress=st.text_area("Enter Address")
            studentEmail = st.text_input("Email")
            studentphn=st.text_input("Enter your phone number")
            studentbrnch=st.text_input("Enter your Branch name")
            studentsem=st.selectbox("Semester",[1,2,3,4,5,6,7,8])
            studentyear=st.selectbox("Year",[1,2,3,4])
            #m=re.compile(r'^\d{10}$')
            studentparph = st.text_input("Enter your Guardian's phone number")
            # if not pattern.match(m):
            #     st.warning("Please enter valid phone number.")
            studentID=studentroll[:-2]
            if st.form_submit_button("Submit"):
                if validate_email(studentEmail):
                    to_add = {"StudentID":[studentID],"Name": [studentName], "Registration": [studentregistry] ,"University Roll Number":[studentuniroll],
                              "College Roll Number":[studentroll],"Addmission of the student":[studentaddmission],"Gender": [studentGender],
                              "DOB":[studentdob],"Address":[studentaddress] , "phn":[studentphn],"Email": [studentEmail],
                              "Branch":[studentbrnch],"Semester":[studentsem],"Year":[studentyear],"Parent's phone number":[studentparph]}
                    to_add = pd.DataFrame(to_add)
                    to_add.to_csv("Csv//Students.csv", mode='a',
                                header=False, index=False)
                    #df = pd.read_csv("Csv//Teacher.csv")
                    st.success("Submitted")
                else:
                    st.warning("Invalid Email")
        #st.write("Submit")
    
    if choice=="View Student":
        st.table(df)
    if choice=="Delete Student":
        selectedName = st.selectbox("Search", df["Name"], key="DeleteBox")
        if st.button("Delete",key="DeleteButton"):
            cf = pd.read_csv("Csv//Students.csv")
            cf = cf[cf["Name"] != selectedName]
            cf.to_csv("Csv//Students.csv",index=False)
        #st.write("Delete")