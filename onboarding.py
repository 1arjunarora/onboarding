import base64
import os
from typing import Dict
import requests
import pandas as pd
from io import BytesIO
from PIL import Image
from typing import List, Dict
import sys
import json
import streamlit as st

# ============================================================================================================
# streamlit app and buttons setup
# ============================================================================================================

# Let’s create a header for our web application
image_path = os.path.join(os.path.dirname(__file__), "employee-onboarding.jpg")
st.image(image_path, width=175)
st.title("AI Assisted Onboarding Portal")

# Let’s create the inputs
col1, col2, col3 = st.columns(3)
Dept = col1.selectbox("Which Department Are You In?",["Marketing", "Operations", "Engineering", "Product"])
Role = col2.selectbox("What is Your Role",["Analyst", "Lead/Manager", "Director", "VP+"])
Region = col3.selectbox("Region",["North America", "Europe", "APAC"])
Goals = st.text_area("What are some of your personal goals over the next 3 months?",'For example: I want to successfully onboard to the culture and AI/ML team within the San Francisco office, and contribute to 1 client project by month 2')

# ============================================================================================================
# Making Predictions Finally
# ============================================================================================================

# predict button formatting
st.title("Generate A Personalized 3 Month Onboarding Roadmap Based On My Interests and Team Objectives")

# predictions
if st.button('Click Here To Generate Your Personalized Onboarding Plan '):  
    st.write('1. Orientation: On 7/12, please report to the SF office for your formal orientation. You will receive your employee ID, complete any required paperwork, and meet the HR director 2. Since you mentioned AI/ML, please setup a call with Kathy Lee, who is our in house AI expert and will provide more details on the organization. Here is a document on the AI organization to review as well. Enjoy!')
             #2. Team Introduction - Once you have settled in, we will arrange a team meeting where you can meet your colleagues and get acquainted with everyone. It will be a great opportunity to learn about ongoing projects, team dynamics, and individual responsibilities. 3. Equipment and Access: Our IT team will provide you with the necessary equipment, such as a laptop, software tools, and access credentials. If you have any specific requirements or preferences, please let us know in advance. 4. Onboarding Buddy: To help you navigate your first few weeks, we have assigned Joe Martinez as your onboarding buddy. Joe will be your go-to person for any questions, guidance, or assistance you may need. They will introduce you to our processes, tools, and answer any queries you may have. 5. Training and Development: We are committed to your professional growth. As part of your onboarding, we have planned training sessions and mentorship opportunities tailored to your role. You will have the chance to enhance your skills and contribute to challenging projects. 6. Communication Channels: We utilize various communication tools such as Slack, email, and project management software. We encourage open communication, collaboration, and knowledge sharing across the team. Please familiarize yourself with our communication channels and join relevant groups. 7. Company Culture: At [Company Name], we take pride in our inclusive and supportive work culture. We value diversity, respect different perspectives, and foster a collaborative environment. Feel free to explore our company values, policies, and any upcoming team events.')

# ============================================================================================================
# Enable users to make recommendations based on sample roles
# ============================================================================================================

st.header('View What Excellent Onboarding Looked Like For Others In Similar Roles')
col1, col2, col3 = st.columns(3)

with col1:
    img1_path = os.path.join(os.path.dirname(__file__), "images/male.png")
    st.image(img1_path)
    img1_button = st.button("Learn how John Led Critical AI Projects Within 3 months of onboarding in 2022", key='1')
with col2:
    img2_path = os.path.join(os.path.dirname(__file__), "images/female.png")
    st.image(img2_path)
    img2_button = st.button("Learn how Nathalie Moved From Analyst to VP Within 5 years at the company", key='2')
with col3:
    img3_path = os.path.join(os.path.dirname(__file__), "images/gay-pride.png")
    st.image(img3_path)
    img3_button = st.button("Learn how Arjun started a company wide initiative for diversity and inclusiveness as a director of AI/ML", key='3')


if img1_button:
    st.write('Finding onboarding plan for John..')

elif img2_button:
    st.write('Finding examples of leadership goal planning..')

elif img3_button:
    st.write('Finding examples of diversity and inclusiveness initiatives, culture and resource onboarding..')

