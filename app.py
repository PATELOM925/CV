from pathlib import Path
import streamlit as st
from PIL import Image
import pandas as pd


# --- PATH SETTINGS ---
current_directory = Path(__file__).parent if '__file__' in locals() else Path.cwd()
# css_file = current_directory / 'styles' / 'main.css'
resume_file = current_directory / 'details' / 'Resume - OM M PATEL Updated.pdf'
profile_pic = current_directory / 'details' / 'Profile Photo - Om Patel.png'

# --- GENERAL SETTINGS ---
PAGE_TITLE = 'CV | OM M PATEL'
PAGE_ICON = ':rocket:'
NAME = 'OM M PATEL'
DESCRIPTION = '''Diving Deep in Data'''
EMAIL = 'iampatelom@gmail.com'

SOCIAL_MEDIA = {
    'https://www.svgrepo.com/show/503359/github.svg': 'https://github.com/PATELOM925',
    'https://www.svgrepo.com/show/110195/linkedin.svg': 'https://www.linkedin.com/in/om-m-patel-b539b8213/',
    'https://www.svgrepo.com/show/489456/email.svg': 'mailto:iampatelom@gmail.com',
    'https://www.svgrepo.com/show/303115/twitter-3-logo.svg': 'https://twitter.com/om_m_patel',
}

# PROJECTS = {
#         'ChatPDF AI': {'url': 'https://chatpdf-ai-om-m-patel.streamlit.app/', 'description': "ChatPDF AI leverages advanced NLP techniques and integration with Streamlit Cloud to streamline PDF analysis tasks, achieving an impressive 89% accuracy rate. With features like efficient document retrieval, it empowers users in making informed decisions faster."n " },
#         'SQl AI': {'url': 'https://github.com/PATELOM925/SQL-AI', 'description': " SQL databases can be uploaded by the user and We have Implemented advanced natural language prompts, transforming input into precise SQL queries " },
#         'Automated - Exam Paper Checker': {'url': 'https://github.com/PATELOM925/Automatic-Paper-Checker', 'description': "An automated grading system that's making assessment a breeze for teachers and professors, Integrated BERT-Uncased for NLP-based grading, employed Spacy & PyTesseract for image processing ensuring accuracy in assessing diverse exam formats."},
#         'Meme App': {'url': 'https://github.com/PATELOM925/MemeApp', 'description': 'The "Meme App" is an innovative and fun Android application developed using Kotlin, Android development tools, and the powerful Glide library. This app is designed to bring a smile to your face by delivering a never-ending stream of hilarious and entertaining memes sourced from Reddits API through Retrofit.'},
    

# }

#learnt from 
Learnt_From = {
    'Krish Naik': 'https://www.youtube.com/@krishnaik06',
    'StatQuest with Josh Starmer': 'https://www.youtube.com/@statquest',
    'Towards Data Science' : 'https://towardsdatascience.com/',
    'DeepLearning,AI' : 'https://www.deeplearning.ai/',
    'iNeuron' : 'https://ineuron.ai/'
 }

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD PDF & PROFILE PIC ---
with open(resume_file, 'rb') as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap='small')

with col1:
    st.image(profile_pic, width=321 , channels='RGB', use_column_width=True)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label='📄 Download My Resume',
        data=PDFbyte,
        file_name=resume_file.name,
        mime='application/octet-stream',
    )


# --- SOCIAL LINKS ---
st.write('#')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f'<a href="{link}"><img src="{platform}" alt="HTML tutorial" style="width:42px;height:42px;"></a>', unsafe_allow_html=True)


st.write('#')
st.subheader('Skills')

# Data for the skills table
skills_data = [
    ('Programming Languages', 'Python, Java, C, HTML+CSS'),
    ('Databases', 'MySQL, MongoDB, SQLite, Firebase'),
    ('Libraries/Frameworks', 'NumPy, Scipy, Pandas, Matplotlib, OpenCV, PIL, Tensorflow, Keras, NLTK, Streamlit, Flask, Pytesseract'),
    ('Developer Tools', 'GIT, GITHUB, GOOGLE COLLAB, GCP, INTELLIJ, MICROSOFT OFFICE, ASANA, AI TOOLS, COMPASS, WORKBENCH'),
    ('Areas of Interest', 'DATA SCIENCE, DATA ANALYST, ML-OPS, BIG DATA ANALYST, QUANTITATIVE ANALYST'),
    ('Soft Skills', 'AVID LISTENER, PROBLEM SOLVING, FAST-LEARNER, TEAM LEADERSHIP, ADAPTIVE'),
    ('Hands in Emerging Tech', 'LANGCHAIN, LLAMAINDEX, GENERATIVE AI'),
]
index = ['A','B','C','D','E','F','G']
# Create a DataFrame without index and header
skills_df = pd.DataFrame(skills_data, columns=['Category', 'Skills'],index=index)

# Display the table
st.table(skills_df)

# --- EXPERIENCE & QUALIFICATIONS ----
st.write('#')
st.subheader('Education')

cols = st.columns(4)
cols[0].write('🎓 **B.Tech in CSE**')
cols[1].write('*Pandit Deendayal Energy University(PDEU)*')
cols[2].write('2021--Present')
cols[3].write('CGPA: 8.69/10')

cols = st.columns(4)
cols[0].write('🎓 **Class XII**')
cols[1].write('*GEB, Vadodara*')
cols[2].write('2021')
cols[3].write('Percentage: 83%')

cols = st.columns(4)
cols[0].write('🎓 **JEE MAINS**')
cols[1].write('*NTA*')
cols[2].write('2021')
cols[3].write('Percentile: 96%')


# st.write('#')
# st.subheader('Experience')
# st.write(
#     '''
# - 📌 Android Developer (Intern) @ *Patchmax pvt ltd.* (May 2023 -- July 2023)
#     - Succesfully Learnt Android Development in Kotlin and Built Apps/features.
#     - Grateful to my team who taught me "Transforming Visions into Seamless Apps".
#     - Major Skills Used: REST APIs, Firebase, Kotlin, Azure Blob, MySQL.
# - 📌 Creator @ *ASK OM PATEL* (Nov 2021 -- July 2022)
#     - Spreaded Financial and Startup knowledge and gained more than 55,000 eyeballs on *[Instagram](https://www.instagram.com/askompatel/).*
#     - Used *[Youtube](https://www.youtube.com/@iampatelom)* to spread the startup knowledge in native language(Gujarati).
#     - Major Skills Used: Adobe Premiere Pro, Canva, Social Media Marketing
# - 📌 Graphic Designer  @ Aasan Study (Mar 2020 -- Feb 2022)
#     - Created engaging Educational Content for the website(https://aasanstudy.com/)
#     - Designed Graphics for educational posts for Instagram, youtube and website.
#     - Major Skills USed: Adobe Photoshop, Adobe Illustrator, Web Content Writing'''
# )


# --- PROJECTS ---
st.write('#')
st.subheader('Projects')
st.write(
    '''
    :pushpin: [**SQl AI**](https://github.com/PATELOM925/SQL-AI) - Access Database In Your Language
    - Allows Users to upload SQL databases and Access them in Natural Language prompts.
    - Transforms input into precise SQL queries with  an accuracy over *90%*.

    :pushpin: [**ChatPDF AI**](https://chatpdf-ai-om-m-patel.streamlit.app/) - Talk With Your PDFs
    - let's user retrieve necessary information from PDF (Q/A chatbot).
    - Accuracy rate over 80% and Empowers them to make informed discussion.

    :lightbulb: [**Autograder**](https://github.com/PATELOM925/AutoGrader) - Precision In Every Grade
    - Automated grading system for teachers and professors.
    - Integration of BERT-Uncased for NLP-based grading, along with Spacy & PyTessearch for Image processing.
    - Ensures accuracy in assessing diverse exam formats.

    :lightbulb: [**Meme App**](https://github.com/PATELOM925/MemeApp) - Laughter Just A Click Away
    - Innovative and fun Android application developed using Kotlin and Sourced from Reddit's API through Retrofit.
    - Utilizes Android development tools and Glide library to Deliver a never-ending stream of hilarious memes. 
    '''
)

# PROJECTS = {
#      'ChatPDF AI - Talk With Your PDFs \n': {
#         'url': 'https://chatpdf-ai-om-m-patel.streamlit.app/',
#         'description': " - Leverages advanced NLP techniques \n"
#                        " - Integration with Streamlit Cloud for streamlined PDF analysis \n"
#                        " - Achieves an impressive 89% accuracy rate \n"
#                        " - Empowers users in making informed decisions faster"
#     },
#     'Autograder - Precision In Every Grade \n': {
#         'url': 'https://github.com/PATELOM925/Automatic-Paper-Checker',
#         'description': " - Automated grading system for teachers and professors \n"
#                        " - Integration of BERT-Uncased for NLP-based grading \n"
#                        " - Utilizes Spacy & PyTesseract for image processing \n"
#                        " - Ensures accuracy in assessing diverse exam formats"
#     },
#     'Meme App': {
#         'url': 'https://github.com/PATELOM925/MemeApp \n',
#         'description': " - Innovative and fun Android application developed using Kotlin \n"
#                        " - Utilizes Android development tools and Glide library \n"
#                        " - Delivers a never-ending stream of hilarious memes \n"
#                        " - Sourced from Reddit's API through Retrofit"
#     }
# }

st.write('#')
st.subheader('**Experience**')
st.write(
    '''
:pushpin: **Android Developer (Intern) @ Patchmax pvt ltd. (May 2023 -- July 2023)**
 - Successfully Learned Android Development in Kotlin and Built Apps/features.
 - Grateful to my team who taught me "Transforming Visions into Seamless Apps".
 - Major Skills Used: REST APIs, Firebase, Kotlin, Azure Blob, MySQL.

:pushpin: **Creator @ ASK OM PATEL (Nov 2021 -- July 2022)**
 - Spread Financial and Startup knowledge and gained more than 55,000 eyeballs on *[Instagram](https://www.instagram.com/askompatel/).*
 - Used *[Youtube](https://www.youtube.com/@iampatelom)* to spread the startup knowledge in native language (Gujarati).
 - Major Skills Used: Adobe Premiere Pro, Canva, Social Media Marketing

:pushpin: **Graphic Designer @ Aasan Study (Mar 2020 -- Feb 2022)**
 - Created engaging Educational Content for the *[website](https://aasanstudy.com/)*.
 - Designed Graphics for educational posts for Instagram, YouTube, and website.
 - Major Skills Used: Adobe Photoshop, Adobe Illustrator, Web Content Writing
'''
)



# ---ACHIEVEMENTS---
st.write('#')
st.subheader('Certifications')
st.write(
'''
- [Generative AI with Large Language Models](https://www.coursera.org/account/accomplishments/certificate/XGBDJAYXTEF7)
- [Langchain Chat With Your Data](https://coursera.org/share/4b21792f6551d0c5096f1d761417278f)
- [Excel](https://olympus.mygreatlearning.com/courses/12583/certificate)
'''
)
 
# Learnt From
st.write('#')
st.subheader('Learnt From')
for name, link in Learnt_From.items():
    st.markdown(f'<a href="{link}" style="line-height: 1.0;">{name}</a>', unsafe_allow_html=True)


# ---CO-CURRICULARS---
st.write('#')
st.subheader('Co-Curricular Activities')
st.write(
    '''
- **President** @ *[Tattvam](https://www.instagram.com/tattvam.pdeu/)- The Sanskrit Club of PDEU*(May 2023 - Present)
- **Graphic Head** @ *[Tattvam](https://www.instagram.com/tattvam.pdeu/) - The Sanskrit Club of PDEU*(May 2022 - May 2023)

'''
)
