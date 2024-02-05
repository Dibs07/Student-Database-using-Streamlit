import streamlit as st
import streamlit_authenticator as stauth
from signup import sign_up, fetch_users
from streamlit_option_menu import option_menu
import dashboard
import courses
import students
import teacher
import Sessions
import attendence
import pandas as pd
key_counter = 0


def Menu():
    global key_counter
    with st.sidebar:
        k = f"menu_{key_counter}"
        key_counter += 1  # Increment the counter for the next use
        app = option_menu(
            menu_title='Navigation ',
            options=['Dashboard', 'Students',
                     'Teachers', 'Courses', 'Sessions','Attendence'],
            icons=['house-fill', 'person-circle',
                   'trophy-fill', 'chat-fill', 'info-circle-fill'],
            menu_icon='chat-text-fill',
            default_index=0,
            key=k,
            styles={
                "container": {"padding": "5!important", "background-color": 'black'},
                "icon": {"color": "white", "font-size": "23px"},
                "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                             "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21"},
            }
        )

    if app == "Dashboard":
        k = f"menu_{key_counter}"
        key_counter += 1
        dashboard.app()
    if app == "Students":
        k = f"menu_{key_counter}"
        key_counter += 1
        students.app()
    if app == "Teachers":
        k = f"menu_{key_counter}"
        key_counter += 1
        teacher.app()
    if app == "Courses":
        k = f"menu_{key_counter}"
        key_counter += 1
        courses.app()
    if app == "Sessions":
        k = f"menu_{key_counter}"
        key_counter += 1
        Sessions.app()
    if app == "Attendence":
        k = f"menu_{key_counter}"
        key_counter += 1
        attendence.app()


Menu()
