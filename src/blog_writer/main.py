# from crewai.flow.flow import Flow, start, listen
# from litellm import completion
# from dotenv import load_dotenv
# class Blog(Flow):
#     model = "gemini/gemini-1.5-flash"

#     @start()
#     def generate_topic(self):
#         response = completion(
#             model=self.model,
#             messages=[
#                 {
#                     "role": "user",
#                     "content": "Return a random blog on city of pakistan  ."
#                 },
#             ],
#         )

#         topic = response["choices"][0]["message"]["content"]
#         print(f"Topic: {topic}")
#         return topic

#     @listen(generate_topic)
#     def generate_blog(self, topic):
#         response = completion(
#             model=self.model,
#             messages=[
#                 {
#                     "role": "user",
#                     "content": f"Generate a blog of maximum 200 words on {topic}"
#                 },
#             ],
#         )
#         blog = response["choices"][0]["message"]["content"]
#         return blog


