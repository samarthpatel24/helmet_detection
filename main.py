import streamlit as st 
from streamlit_option_menu import option_menu
import  About, contact,Helmet_Detection


st.set_page_config(
    page_title="Helmet Detection",
    page_icon="🪖",
    initial_sidebar_state="expanded"
)

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
                options=['About','Helmet Detection','Contact'],
                icons=['info-circle-fill','chat-fill','person-circle'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'#0E1117'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#FFCCCB"},
        "nav-link-selected": {"background-color": "#ff4b4b"},}
                
            )
        
        if app == "About":
            About.app()
        if app == "Helmet Detection":
            Helmet_Detection.app()    
        if app == "Contact":
            contact.app()

    run()
             
