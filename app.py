from pathlib import Path
import streamlit as st
from PIL import Image
import pandas as pd


# --- PATH SETTINGS ---
current_directory = Path(__file__).parent if '__file__' in locals() else Path.cwd()
# css_file = current_directory / 'styles' / 'main.css'
resume_file = current_directory / 'details' / 'Resume-OM M PATEL.pdf'
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

PROJECTS = {
    'Meme App': {'url': 'https://github.com/PATELOM925/MemeApp', 'description': 'The "Meme App" is an innovative and fun Android application developed using Kotlin, Android development tools, and the powerful Glide library. This app is designed to bring a smile to your face by delivering a never-ending stream of hilarious and entertaining memes sourced from Reddits API through Retrofit.'},
    'Automated - Exam Paper Checker': {'url': 'https://github.com/PATELOM925/Automatic-Paper-Checker', 'description': "An automated grading system that's making assessment a breeze for teachers and professors, Integrated BERT-Uncased for NLP-based grading, employed Spacy & PyTesseract for image processing ensuring accuracy in assessing diverse exam formats."},
    'SQl AI': {'url': 'https://github.com/PATELOM925/SQL-AI', 'description': " SQL databases can be uploaded by the user and We have Implemented advanced natural language prompts, transforming input into precise SQL queries " },
}

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
# st.subheader('Skills')

# cols = st.columns(2, gap='small')
# cols[0].markdown('<p style="margin-bottom: -10px;"><strong>Programming Languages</strong></p>', unsafe_allow_html=True)
# cols[1].markdown('<p style="margin-bottom: -10px;">Python, Java, C, HTML+CSS</p>', unsafe_allow_html=True)

# cols = st.columns(2, gap='small')
# cols[0].markdown('<p style="margin-bottom: -10px;"><strong>Databases</strong></p>', unsafe_allow_html=True)
# cols[1].markdown('<p style="margin-bottom: -10px;">MySQL, MongoDB, SQLite, Firebase</p>', unsafe_allow_html=True)

# cols = st.columns(2, gap='small')
# cols[0].markdown('<p style="margin-bottom: -10px;"><strong>Libraries/Frameworks</strong></p>', unsafe_allow_html=True)
# cols[1].markdown('<p style="margin-bottom: -10px;">NumPy, Scipy, Pandas, Matplotlib, OpenCV, PIL, Tensorflow, Keras, NLTK, Streamlit, Flask, Pytesseract</p>', unsafe_allow_html=True)

# cols = st.columns(2, gap='small')
# cols[0].markdown('<p style="margin-bottom: -10px;"><strong>Developer Tools</strong></p>', unsafe_allow_html=True)
# cols[1].markdown('<p style="margin-bottom: -10px;">GIT, GITHUB, GOOGLE COLLAB, GCP, INTELLIJ, MICROSOFT OFFICE, ASANA, AI TOOLS, COMPASS, WORKBENCH</p>', unsafe_allow_html=True)

# cols = st.columns(2, gap='small')
# cols[0].markdown('<p style="margin-bottom: -10px;"><strong>Areas of Interest</strong></p>', unsafe_allow_html=True)
# cols[1].markdown('<p style="margin-bottom: -10px;">DATA SCIENCE, DATA ANALYST, ML-OPS, BIG DATA ANALYST, QUANTITATIVE ANALYST</p>', unsafe_allow_html=True)

# cols = st.columns(2, gap='small')
# cols[0].markdown('<p style="margin-bottom: -10px;"><strong>Soft Skills</strong></p>', unsafe_allow_html=True)
# cols[1].markdown('<p style="margin-bottom: -10px;">AVID LISTENER, PROBLEM SOLVING, FAST-LEARNER,TEAM LEADERSHIP, ADAPTIVE</p>', unsafe_allow_html=True)

# ols = st.columns(2, gap='small')
# cols[0].markdown('<p style="margin-bottom: -10px;"><strong>Hands in Emerging Tech</strong></p>', unsafe_allow_html=True)
# cols[1].markdown('<p style="margin-bottom: -10px;">LANGCHAIN, LLAMAINDEX, GENERATIVE AI</p>', unsafe_allow_html=True)

# Skills Table
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

# --- PROJECTS ---
st.write('#')
st.subheader('Projects')
for project, content in PROJECTS.items():
    st.write(f'* **[{project}]({content["url"]})**: {content["description"]}')

# # ---ACHIEVEMENTS---
# st.write('#')
# st.subheader('Achievements')
# st.write(
# '''
# - Filed 1 *Provisional Design Patent* and 1 *Provisional Product Patent* under Indian Patent Office
# - Amongst [top 4%](https://quine.sh/user/Kunal-Kumar-Sahoo) developers wordwide (Python, rank 115) on *Quine.sh*
# - Within top 10 best projects in University-level Smart India Hackathon, 2023
# - Received funding of **225K INR** for project idea under SSIP Policy
# - Won **150K INR** as prize money in *Robofest 3.0*
# - Second runner-up at *EnCode hackathon* at IIT Guwahati (sponsor: **Bosch**)
# - Grand finalist of *Azadi ka Amrit Mahotsav Hackathon 2022*, organized by Govt. of Gujarat
# '''
# )
 
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