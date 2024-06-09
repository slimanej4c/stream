import openai
import requests
import time
import os
import openai

from openai import OpenAI
# Document URL: https://info.undp.org/erecruit/documents/FAQ.pdf
dataset="""Document content:
Question: salut? Answer: salut comment je peux cous iaderrerer.
Question: est ce il y a des produit  Answer: oui quelle produit que vous chercher
Question: il y a quoi  Answer: toutes les aryicle tawa et makla
Question: chkon m3aya ou chkon nta ou mnho kachiou  mnho ou c est qui  ? Answer: m3ak farid.
Question: What browsers are compatible with UNDP’s eRecruit system?Answer: UNDP’s eRecruit system was optimised for Google Chrome, Internet Explorer 6 and above. The usage of Internet Explorer 9 is required in compatibility view mode. We suggest that you use one of these browsers to make sure your application is submitted successfully.
Question: I am having problems logging into my profile. The browser is not responding. What should I do? Answer: If you are having problems logging in to your UNDP eRecruit profile in order to apply for a job opening this could stem from a number of reasons, some of which - such as internet connectivity - are outside of UNDP’s control. However, we suggest that you follow these instructions in order to address these types of issues: • Check that you are using the recommended browsers (and versions). • Clear your cache/browser history. You can find information about how to clear your browser history at http://www.refreshyourcache.com/en/home. Please make sure that you are aware of the consequences when clearing the cache in your browser before taking this action.
Question: What if I need help using UNDP’s eRecruit system? Answer: For general inquiries or assistance in using UNDP’s eRecruit system, please contact the HelpDesk at https://info.undp.org/sas/erecruit/Assets/HelpDesk.aspx.
Question: Why do I need to register? Answer: It is required that all applicants must first register in UNDP’s eRecruit system. After your registration is complete, a personal account is created so that you may complete your personal information and apply to advertised job postings.
Question: When registering, what should I use as my username? Answer: It is suggested that you should use a valid e-mail address as your username when registering in the UNDP’s eRecruit system.
Question: What password format is accepted? Answer: UNDP encourages the use of strong passwords. Passwords should be a minimum of 8 characters in length and contain a combination of letters and numbers.
Question: How can I change my password? Answer: Select the ‘Change Password’ option from the ‘Personal Information’ link after you have logged in to the system. Click on the ‘Forgot User Name or Password?’ link and follow the instructions to retrieve your forgotten password.
Question: I have forgotten my password. What should I do? Answer: If you have forgotten your password, click on the link Forgot User ID or Password and complete one of the two options.
Question: Will my data be secure? Answer: UNDP’s eRecruit data is stored on a private secure database and UNDP is the owner of the data. The system meets the UNDP's stringent security requirements.
Question: Do I have to complete all of the information in each of the sections? Answer: All fields marked with an asterisk (*) are required information and must be completed for each section.
Question: Do I need to complete all of the information in one session? Answer: You can save your application at any time during the application process and continue at a later time. When completing a section, we encourage that you use the save button regularly in order to ensure that your information is not lost.
Question: How do I select dates using the calendar feature? Answer: Dates can be selected in two ways. You can either A) type the date directly in the field using the dd/mm/yyyy format or B) select the date by clicking on the calendar icon and choose the year month and day.
Question: What should I do if my relevant information is not included in one of the drop-down options? Answer: You will be required to choose from the available drop-down options. Please choose the option that is the closest to your personal information, skills and experience.
Question: How do I use the Look-up feature? Answer: To use the Look-up feature, click on the magnifying glass icon. After, type in either the full or partial value in the given field and click the button Look Up. Lastly, select the appropriate value from the search result.
Question: Is there a spell check feature available? Answer: For various text description fields in each section, a spell click feature is available. To use the spell check feature, click on the dictionary icon to the left of the text field where available.
Question"  Can I apply to a job posting even if I do not meet the minimum requirements? Answer: You will not be able to apply to a job posting if your relevant education, work experience, language skills and possible other qualifications do not meet the minimum requirements specified in the job posting.
Question:  Can I review my application before submission? Answer: Once you have clicked on the button submit my application, you will be able to review your full application details before the final submission. If you wish to modify any of the details displayed on the Application Preview page, you may do so by returning to the previous page.
Question: How do submit my application? Answer: You will first need to complete all of the required information in the personal profile sections and answer the relevant job-related questions. After, you will be able to submit your application by clicking the button submit my application.
Question: The deadline for submitting an application has expired. Can I still apply? Answer: It is essential to submit your application in the eRecruit system before midnight CET time of the job posting’s closing date. Regrettably, we are unable to accept late applications.
Question: After I submit my application, will I receive a confirmation? Answer: After you have submitted your application online, you will receive an automated email confirming receipt of your application.
Question: Can I revise or amend my application once it has been submitted? Answer: You are able to revise or amend any sections of your personal profile before the job posting’s closing date. Please note that the closing date of all UNDP job postings are effective midnight, CET time.
Question: What if I want to submit additional documents to my application? Answer: UNDP does not require that you attach additional documents to your application. However, at any time during the recruitment process, you may be requested by a UNDP Recruitment Specialist to submit additional validating documents to your personal profile in support of your application. If you receive a request to upload specific documents, first navigate to the Careers Home page  My Career Tools page. Click on Applicant Attachments and add the relevant documents in the attachments section.
Question: Can I apply for more than one job posting at the same time? Answer: You may apply to multiple UNDP job postings given that you meet the minimum requirements for each.
Question: Is there a fee for submitting my application? Answer: UNDP does not charge any fee at any stage of the recruitment process whether at the application, interview, processing or training stage. UNDP does not require or need to know any information relating to the bank account details of applicants. Any such request should be rejected as these schemes are fraudulent.
Question: How can I check on the status of my application? Answer: At all times, you may view the status of the vacancies you have applied. To do so, navigate to the Careers Home page  My Career Tools  Applications page. On the My Applications page, you will be able to view the Recruiting Status for each of your applications.
"""

# Remplacez 'YOUR_OPENAI_API_KEY' par votre clé API
api_key = 'sk-proj-BCtNALBJdUhNjwA2XKPoT3BlbkFJ14y9f2uLvjfWYGvLCL2r'
os.environ["OPENAI_API_KEY"] = api_key
client = OpenAI()

messages = [{"role": "system", "content": """I want you to act as a support agent. Your name is "My Super Assistant". You will provide me with answers from the given info. If the answer is not included, say exactly "Ooops! I don't know that." and stop after that. Refuse to answer any question not about the info. Never break character."""}]
messages.append({"role": "assistant", "content": dataset})
while True:
    user_input = input("You: ")
    if user_input == "quit":
        break

    messages.append({"role": "user", "content": user_input})
    chat_response = client.chat.completions.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        temperature=0.0,
        max_tokens=300,
    )
    messages.append({"role": "assistant", "content": chat_response.choices[0].message.content})
    print("Assistant:", chat_response.choices[0].message.content)