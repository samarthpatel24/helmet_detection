import streamlit as st 
from streamlit_option_menu import option_menu
import  Introduction, contact,Helmet_Detection


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        
        with st.sidebar:        
            app = option_menu(
                menu_title='Main Menu ',
                options=['Introduction','Helmet Detection','Contact'],
                icons=['house-fill','chat-fill','person-circle'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
            )
        
        if app == "Introduction":
            Introduction.app()
        if app == "Helmet Detection":
            Helmet_Detection.app()    
        if app == "Contact":
            contact.app()

    run()

             