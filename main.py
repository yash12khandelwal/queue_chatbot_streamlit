import streamlit as st
from multiapp import MultiApp
from apps import home, manual_user # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Add User", manual_user.app)

# The main app
app.run()
