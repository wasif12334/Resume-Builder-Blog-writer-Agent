import streamlit as st
from crewai import Agent, Task, Crew
from litellm import completion
from dotenv import load_dotenv
import os

load_dotenv()

# Set the LLM model
MODEL = "gemini/gemini-1.5-flash"

# Define Resume Builder Agent
resume_writer = Agent(
    role="Resume Builder",
    goal="Generate a well-formatted Chronological Resume based on user input",
    backstory="An AI that specializes in professional resume writing",
    verbose=True
)

# Define Resume Building Task
def generate_resume(user_data):
    response = completion(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": f"Generate a resume for this user: {user_data}. Format it as a Chronological Resume."
            },
        ],
    )
    return response["choices"][0]["message"]["content"]

st.title("AI Resume Builder 🚀")

# Get User Input via Streamlit
full_name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
linkedin = st.text_input("LinkedIn (optional)")

degree = st.text_input("Degree")
university = st.text_input("University")
grad_year = st.text_input("Graduation Year")

skills = st.text_area("Skills (comma-separated)")
work_exp = st.text_area("Work Experience (if any)")
projects = st.text_area("Projects (comma-separated)")

if st.button("Generate Resume"):
    if not full_name or not email or not phone or not degree or not university or not grad_year:
        st.warning("Please fill in all required fields!")
    else:
        user_data = {
            "Full Name": full_name,
            "Email": email,
            "Phone": phone,
            "LinkedIn": linkedin,
            "Degree": degree,
            "University": university,
            "Graduation Year": grad_year,
            "Skills": skills.split(","),
            "Work Experience": work_exp,
            "Projects": projects.split(","),
        }
        
        st.write("Generating your resume... ⏳")
        
        # Generate Resume
        resume_text = generate_resume(user_data)
        
        st.subheader("Your AI-Generated Resume:")
        st.text_area("Generated Resume", resume_text, height=300)

