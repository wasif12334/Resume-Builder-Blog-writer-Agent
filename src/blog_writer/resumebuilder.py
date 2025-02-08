from crewai.flow.flow import Flow, start, listen
from litellm import completion
from dotenv import load_dotenv

load_dotenv()
class resumeBuilder(Flow):
    model = "gemini/gemini-1.5-flash"

    @start()
    def UserInput(self):

        resume_data = {}

        resume_data["Full Name"] = input("Enter your full name: ")
        resume_data["Email"] = input("Enter your email: ")
        resume_data["Phone"] = input("Enter your phone number: ")
        resume_data["LinkedIn"] = input("Enter your LinkedIn profile (or type 'N/A'): ")

        resume_data["Degree"] = input("Enter your degree: ")
        resume_data["University"] = input("Enter your university name: ")
        resume_data["Graduation Year"] = input("Enter your graduation year: ")

        skills = input("Enter your skills (comma-separated): ")
        resume_data["Skills"] = skills.split(",")

        resume_data["Work Experience"] = input("Enter your work experience (or type 'N/A' if none): ")

        projects = input("Enter your project names (comma-separated): ")
        resume_data["Projects"] = projects.split(",")

    
       
        return resume_data

    @listen(UserInput)
    def buildResume(self, userData):
        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"Generate a resume about {userData} and format in a Chronological Resume"
                },
            ],
        )
        resume = response["choices"][0]["message"]["content"]
        return resume


resume = resumeBuilder()
result = resume.kickoff()

print(f"Generated Blog: {result}")