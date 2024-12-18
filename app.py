from pathlib import Path
import streamlit as st
from PIL import Image
import pandas as pd

# --- PATH SETTINGS --- 
current_directory = Path(__file__).parent if '__file__' in locals() else Path.cwd()
resume_file = current_directory / 'details' / 'OM_CV.pdf'
profile_pic = current_directory / 'details' / 'Profile Photo - Om Patel.png'

# --- GENERAL SETTINGS ---
PAGE_TITLE = 'CV | OMKUMAR MITESHBHAI PATEL'
PAGE_ICON = ':rocket:'
NAME = 'OMKUMAR MITESHBHAI PATEL'
DESCRIPTION = '''Diving Deep in Data'''
EMAIL = 'iampatelom@gmail.com'

SOCIAL_MEDIA = {
    'https://upload.wikimedia.org/wikipedia/commons/a/ae/Github-desktop-logo-symbol.svg': 'https://github.com/PATELOM925',
    'https://www.svgrepo.com/show/110195/linkedin.svg': 'https://www.linkedin.com/in/om-m-patel-b539b8213/',
    'https://upload.wikimedia.org/wikipedia/commons/7/7e/Gmail_icon_%282020%29.svg': 'mailto:iampatelom@gmail.com',
    'https://www.svgrepo.com/show/303115/twitter-3-logo.svg': 'https://twitter.com/om_m_patel',
    'https://www.svgrepo.com/show/349422/kaggle.svg': 'https://www.kaggle.com/iamommpatel',
}

Learnt_From = {
    'Krish Naik': 'https://www.youtube.com/@krishnaik06',
    'StatQuest with Josh Starmer': 'https://www.youtube.com/@statquest',
    'Towards Data Science': 'https://towardsdatascience.com/',
    'DeepLearning.AI': 'https://www.deeplearning.ai/',
    'iNeuron': 'https://ineuron.ai/'
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD PDF & PROFILE PIC ---
with open(resume_file, 'rb') as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- CUSTOM CSS ---
# --- CUSTOM CSS ---
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        color: white;
        background: linear-gradient(135deg, #0b3d91, #1f65cc);
    }
    .stApp {
        background: linear-gradient(135deg, #0b3d91, #1f65cc);
        color: white;
    }
    .stButton > button {
        color: white;
        background-color: #ffd700; /* Golden yellow */
        border: none;
        border-radius: 8px;
        padding: 8px 16px;
        font-size: 16px;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #ffc300;
        color: navy;
    }
    .stTitle, .stHeader, .stSubheader {
        color: #ffd700; /* Golden yellow */
    }
    .stMarkdown a {
        color: #ffd700;
        text-decoration: none;
    }
    .stMarkdown a:hover {
        color: #ffc300;
        text-decoration: underline;
    }
    .stImage > img {
        border-radius: 50%;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.6);
    }
    .stTable {
        background-color: #0b3d91;
        color: white;
        border-collapse: collapse;
    }
    .stTable th {
        color: #ffd700;
    }
    .stTable td {
        color: white;
        border-top: 1px solid #1f65cc;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# st.markdown(
#     """
#     <style>
#     body {
#         color: white;
#         background-color: #121212;
#     }
#     .stApp {
#         background-color: #121212;
#     }
#     .stButton > button {
#         color: white;
#         background-color: #1DB954;
#         border: none;
#         border-radius: 4px;
#     }
#     .stButton > button:hover {
#         background-color: #1ED760;
#     }
#     .stTitle, .stHeader, .stSubheader {
#         color: #1DB954;
#     }
#     .stMarkdown {
#         color: white;
#     }
#     .stImage > img {
#         border-radius: 50%;
#     }
#     .stTable {
#         color: white;
#         background-color: ##FFFFFF;
#         border-color: #1DB954;
#     }
#     a {
#         color: #1DB954;
#     }
#     a:hover {
#         color: #1ED760;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap='small')

with col1:
    st.image(profile_pic, width=300, use_container_width=True)

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

# --- SKILLS ---
st.write('#')
st.subheader('Skills')

skills_data = [
    ('Programming Languages', 'Python, Java, C, HTML+CSS'),
    ('Databases', 'MySQL, MongoDB, SQLite, Firebase'),
    ('Libraries/Frameworks', 'NumPy, Scipy, Pandas, Matplotlib, OpenCV, PIL, Tensorflow, Keras, NLTK, Streamlit, Flask, Pytesseract'),
    ('Developer Tools', 'GIT, GITHUB, DOCKER, STREAMLIT CLOUD, AWS, MICROSOFT OFFICE, ASANA, CONFLUENCE, JIRA, AI TOOLS, COMPASS, WORKBENCH'),
    ('Areas of Interest', 'DATA SCIENCE, DATA ANALYST, ML-OPS, BIG DATA ANALYST, QUANTITATIVE ANALYST'),
    ('Soft Skills', 'AVID LISTENER, PROBLEM SOLVING, FAST-LEARNER, TEAM LEADERSHIP, ADAPTIVE'),
    ('Hands in Emerging Tech', 'LANGCHAIN, LLAMAINDEX, GENERATIVE AI, NLP'),
]
index = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
skills_df = pd.DataFrame(skills_data, columns=['Category', 'Skills'], index=index)

st.table(skills_df)

# --- EXPERIENCE ---
st.write('#')
st.subheader('**Experience**')
st.write(
    '''
:pushpin: **Data Science Intern @ Sharperly (March 2024 -- July 2024)**
 - Developed a geocoding solution using Python (Flask, Geopandas, etc.), reducing dependency on Google Cloud API and cutting costs up to 55%.
 - Scraped and processed address data using Overpass Turbo, Beautiful Soup, and Selenium.
 - Performed exploratory data analysis (EDA) on geospatial datasets, contributed to training machine learning models for geospatial analysis by leveraging KNN and other algorithms.
 - Optimized MongoDB databases to store data, and further contributed to authentication and credit management systems for APIs.
 - Collaborated code workflows with GitHub, coordinated tasks and documentation using Jira and Confluence.
 
:pushpin: **Android Developer (Intern) @ Patchmax pvt ltd. (May 2023 -- July 2023)**
 - Successfully learned Android Development in Kotlin and built apps/features.
 - Grateful to my team who taught me "Transforming Visions into Seamless Apps".
 - Major Skills Used: REST APIs, Firebase, Kotlin, Azure Blob, MySQL.

:pushpin: **Creator @ ASK OM PATEL (Nov 2021 -- July 2022)**
 - Spread financial and startup knowledge and gained more than 55,000 eyeballs on [Instagram](https://www.instagram.com/askompatel/).
 - Used [YouTube](https://www.youtube.com/@iampatelom) to spread startup knowledge in the native language (Gujarati).
 - Major Skills Used: Adobe Premiere Pro, Canva, Social Media Marketing.

:pushpin: **Graphic Designer @ Aasan Study (Mar 2020 -- Feb 2022)**
 - Created engaging educational content for the [website](https://aasanstudy.com/).
 - Designed graphics for educational posts for Instagram, YouTube, and website.
 - Major Skills Used: Adobe Photoshop, Adobe Illustrator, Web Content Writing.
'''
)

# --- PROJECTS ---
st.write('#')
st.subheader('Projects')
st.write(
    '''
    :computer: [**Driver Pay Forecasting**](https://github.com/PATELOM925/Uber_NYC_Driver_Pay_Prediction) - Uber NYC Driver Pay Prediction
    - Implemented machine learning and deep learning models (ANN, Random Forest, LSTM, BiLSTM, LSTM+GRU) and performed comparative analysis for pay prediction.
    - Analyzed and visualized factors impacting Uber driver pay through features like date, time, location, and other trip details using PowerBI.
    
    :computer: [**Indian Weather Prediction**](https://www.kaggle.com/code/iamommpatel/indian-weather-predictor) - Ranked in Top-5 for Kaggle's ML Olympiad (Forecasting India's Weather)
    - Achieved high accuracy (R²: 0.9844) by comparing & selecting the best regression model (XGBoost, Gradient Boosting, Linear Regression, Decision Tree, etc.).
    - Performed EDA showcasing diverse graphs and model evaluation metrics.
    
    :computer: [**SQL AI**](https://github.com/PATELOM925/SQL-AI) - Access Database In Your Language
    - Allows users to upload SQL databases and access them in natural language prompts.
    - Transforms input into precise SQL queries with an accuracy over 80%.

    :computer: [**ChatPDF AI**](https://chatpdf-ai-om-m-patel.streamlit.app/) - Talk With Your PDFs
    - Lets users retrieve necessary information from PDF (Q/A chatbot).
    - Accuracy rate over 80% and empowers them to make informed decisions.

    :computer: [**Autograder**](https://github.com/PATELOM925/AutoGrader) - Precision In Every Grade
    - Automated grading system for teachers and professors.
    - Integration of BERT-Uncased for NLP-based grading, along with Spacy & PyTessearch for image processing.
    - Ensures accuracy in assessing diverse exam formats.

    :computer: [**Meme App**](https://github.com/PATELOM925/MemeApp) - Laughter Just A Click Away
    - Innovative and fun Android application developed using Kotlin and sourced from Reddit's API through Retrofit.
    - Utilizes Android development tools and Glide library to deliver a never-ending stream of hilarious memes. 
    '''
)

# --- CO-CURRICULAR ACTIVITIES ---
st.write('#')
st.subheader('Co-Curricular Activities')
st.write(
    '''
- **President** @ *[Tattvam](https://www.instagram.com/tattvam.pdeu/)- The Sanskrit Club of PDEU* (June 2023 - June 2024)
- **Graphic Head** @ *[Tattvam](https://www.instagram.com/tattvam.pdeu/) - The Sanskrit Club of PDEU* (May 2022 - May 2023)
- **Research Presenter** @ *ADCIS 2024, BITS Pilani* - Presented paper titled "Automated Sleep Stage Classification using Machine Intelligence Techniques" (September 2024, accepted/presented/under press in Springer Journal)
- **Top-5 Rank** @ *Kaggle's ML Olympiad* - Forecasting India’s Weather (April 2024 - May 2024)
- **Volunteer** @ *Vardaan Foundation, Vadodara* - Civic and Social Internship: Taught digital literacy to underprivileged students (June 2022 - July 2022)
    '''
)
# st.write(
#     '''
# - **President** @ *[Tattvam](https://www.instagram.com/tattvam.pdeu/)- The Sanskrit Club of PDEU*(June 2023 - June 2024)
# - **Graphic Head** @ *[Tattvam](https://www.instagram.com/tattvam.pdeu/) - The Sanskrit Club of PDEU*(May 2022 - May 2023)

# '''
# )

# --- CERTIFICATIONS ---
st.write('#')
st.subheader('Certifications')
st.write(
    '''
- [Generative AI Project](https://learn.ineuron.ai/certificate/fa40c5f4-fe71-42a6-8557-9a8a1abdb7d4)
- [NPTEL](https://internalapp.nptel.ac.in/NOC/NOC24/SEM1/Ecertificates/107/noc24-de06/Course/NPTEL24DE06S55570004730616807.pdf)
- [Generative AI with Large Language Models](https://www.coursera.org/account/accomplishments/certificate/XGBDJAYXTEF7)
- [Langchain Chat With Your Data](https://coursera.org/share/4b21792f6551d0c5096f1d761417278f)
- [Excel](https://www.sololearn.com/certificates/CT-S9OKVGDH)

'''
)

# --- LEARNT FROM ---
st.write('#')
st.subheader('Learnt From')
for mentor, link in Learnt_From.items():
    st.write(f'[{mentor}]({link})')








#try 1

# from pathlib import Path
# import streamlit as st
# from PIL import Image
# import pandas as pd


# # --- PATH SETTINGS --- 
# current_directory = Path(__file__).parent if '__file__' in locals() else Path.cwd()
# # css_file = current_directory / 'styles' / 'main.css'
# resume_file = current_directory / 'details' / 'Resume_CV_OM_M_Patel.pdf'
# profile_pic = current_directory / 'details' / 'Profile Photo - Om Patel.png'

# # --- GENERAL SETTINGS ---
# PAGE_TITLE = 'CV | OM M PATEL'
# PAGE_ICON = ':rocket:'
# NAME = 'OM M PATEL'
# DESCRIPTION = '''Diving Deep in Data'''
# EMAIL = 'iampatelom@gmail.com'

# SOCIAL_MEDIA = {
#     'https://www.svgrepo.com/show/503359/github.svg': 'https://github.com/PATELOM925',
#     'https://www.svgrepo.com/show/110195/linkedin.svg': 'https://www.linkedin.com/in/om-m-patel-b539b8213/',
#     'https://www.svgrepo.com/show/489456/email.svg': 'mailto:iampatelom@gmail.com',
#     'https://www.svgrepo.com/show/303115/twitter-3-logo.svg': 'https://twitter.com/om_m_patel',
#     'https://www.svgrepo.com/show/349422/kaggle.svg': 'https://www.kaggle.com/iamommpatel',
# }

# # PROJECTS = {
# #         'ChatPDF AI': {'url': 'https://chatpdf-ai-om-m-patel.streamlit.app/', 'description': "ChatPDF AI leverages advanced NLP techniques and integration with Streamlit Cloud to streamline PDF analysis tasks, achieving an impressive 89% accuracy rate. With features like efficient document retrieval, it empowers users in making informed decisions faster."n " },
# #         'SQl AI': {'url': 'https://github.com/PATELOM925/SQL-AI', 'description': " SQL databases can be uploaded by the user and We have Implemented advanced natural language prompts, transforming input into precise SQL queries " },
# #         'Automated - Exam Paper Checker': {'url': 'https://github.com/PATELOM925/Automatic-Paper-Checker', 'description': "An automated grading system that's making assessment a breeze for teachers and professors, Integrated BERT-Uncased for NLP-based grading, employed Spacy & PyTesseract for image processing ensuring accuracy in assessing diverse exam formats."},
# #         'Meme App': {'url': 'https://github.com/PATELOM925/MemeApp', 'description': 'The "Meme App" is an innovative and fun Android application developed using Kotlin, Android development tools, and the powerful Glide library. This app is designed to bring a smile to your face by delivering a never-ending stream of hilarious and entertaining memes sourced from Reddits API through Retrofit.'},
    

# # }

# #learnt from 
# Learnt_From = {
#     'Krish Naik': 'https://www.youtube.com/@krishnaik06',
#     'StatQuest with Josh Starmer': 'https://www.youtube.com/@statquest',
#     'Towards Data Science' : 'https://towardsdatascience.com/',
#     'DeepLearning,AI' : 'https://www.deeplearning.ai/',
#     'iNeuron' : 'https://ineuron.ai/'
#  }

# st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# # --- LOAD PDF & PROFILE PIC ---
# with open(resume_file, 'rb') as pdf_file:
#     PDFbyte = pdf_file.read()
# profile_pic = Image.open(profile_pic)
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-color: #e3e5fa;
#         padding: 2px;
#     }
#     body, h1, h2, h3, h4, h5, h6, p, div, span {
#         color: black !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # --- HERO SECTION ---
# col1, col2 = st.columns(2, gap='small')

# with col1:
#     st.image(profile_pic,width = 321,channels='RGB', use_column_width=True)

# with col2:
#     st.title(NAME)
#     st.write(DESCRIPTION)
#     st.download_button(
#         label='📄 Download My Resume',
#         data=PDFbyte,
#         file_name=resume_file.name,
#         mime='application/octet-stream',
#     )


# # --- SOCIAL LINKS ---
# st.write('#')
# cols = st.columns(len(SOCIAL_MEDIA))
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].write(f'<a href="{link}"><img src="{platform}" alt="HTML tutorial" style="width:42px;height:42px;"></a>', unsafe_allow_html=True)


# st.write('#')
# st.subheader('Skills')

# # Data for the skills table
# skills_data = [
#     ('Programming Languages', 'Python, Java, C, HTML+CSS'),
#     ('Databases', 'MySQL, MongoDB, SQLite, Firebase'),
#     ('Libraries/Frameworks', 'NumPy, Scipy, Pandas, Matplotlib, OpenCV, PIL, Tensorflow, Keras, NLTK, Streamlit, Flask, Pytesseract'),
#     ('Developer Tools', 'GIT, GITHUB, GOOGLE COLLAB, STREAMLIT CLOUD, AWS, MICROSOFT OFFICE, ASANA, CONFLUENCE, JIRA, AI TOOLS, COMPASS, WORKBENCH'),
#     ('Areas of Interest', 'DATA SCIENCE, DATA ANALYST, ML-OPS, BIG DATA ANALYST, QUANTITATIVE ANALYST'),
#     ('Soft Skills', 'AVID LISTENER, PROBLEM SOLVING, FAST-LEARNER, TEAM LEADERSHIP, ADAPTIVE'),
#     ('Hands in Emerging Tech', 'LANGCHAIN, LLAMAINDEX, GENERATIVE AI, NLP'),
# ]
# index = ['A','B','C','D','E','F','G']
# # Create a DataFrame without index and header
# skills_df = pd.DataFrame(skills_data, columns=['Category', 'Skills'],index=index)

# # Display the table
# st.table(skills_df)

# # --- EXPERIENCE & QUALIFICATIONS ----
# st.write('#')
# st.subheader('Education')

# cols = st.columns(4)
# cols[0].write('🎓 **B.Tech in CSE**')
# cols[1].write('*Pandit Deendayal Energy University(PDEU)*')
# cols[2].write('2021--Present')
# cols[3].write('CGPA: 8.69/10')

# cols = st.columns(4)
# cols[0].write('🎓 **Class XII**')
# cols[1].write('*GEB, Vadodara*')
# cols[2].write('2021')
# cols[3].write('Percentage: 83%')

# cols = st.columns(4)
# cols[0].write('🎓 **JEE MAINS**')
# cols[1].write('*NTA*')
# cols[2].write('2021')
# cols[3].write('Percentile: 96%')


# # st.write('#')
# # st.subheader('Experience')
# # st.write(
# #     '''
# # - 📌 Android Developer (Intern) @ *Patchmax pvt ltd.* (May 2023 -- July 2023)
# #     - Succesfully Learnt Android Development in Kotlin and Built Apps/features.
# #     - Grateful to my team who taught me "Transforming Visions into Seamless Apps".
# #     - Major Skills Used: REST APIs, Firebase, Kotlin, Azure Blob, MySQL.
# # - 📌 Creator @ *ASK OM PATEL* (Nov 2021 -- July 2022)
# #     - Spreaded Financial and Startup knowledge and gained more than 55,000 eyeballs on *[Instagram](https://www.instagram.com/askompatel/).*
# #     - Used *[Youtube](https://www.youtube.com/@iampatelom)* to spread the startup knowledge in native language(Gujarati).
# #     - Major Skills Used: Adobe Premiere Pro, Canva, Social Media Marketing
# # - 📌 Graphic Designer  @ Aasan Study (Mar 2020 -- Feb 2022)
# #     - Created engaging Educational Content for the website(https://aasanstudy.com/)
# #     - Designed Graphics for educational posts for Instagram, YouTube and website.
# #     - Major Skills USed: Adobe Photoshop, Adobe Illustrator, Web Content Writing'''
# # )


# # --- PROJECTS ---
# st.write('#')
# st.subheader('Projects')
# st.write(
#     '''
#     :computer:[**Indian Weather Prediction**](https://www.kaggle.com/code/iamommpatel/indian-weather-predictor) - Ranked in Top-5 for Kaggle's ML Olympiad (Forecasting India's Weather)
#     - Achieved high accuracy (R²: 0.9844) by comparing & selecting the best regression model (XGBoost, Gradient Boosting, Linear Regression, Decision Tree, etc)
#     - Performed EDA showcasing diverse graphs and model evaluation metrics
    
#     :computer: [**SQl AI**](https://github.com/PATELOM925/SQL-AI) - Access Database In Your Language
#     - Allows Users to upload SQL databases and Access them in Natural Language prompts.
#     - Transforms input into precise SQL queries with  an accuracy over *90%*.

#     :computer: [**ChatPDF AI**](https://chatpdf-ai-om-m-patel.streamlit.app/) - Talk With Your PDFs
#     - let's user retrieve necessary information from PDF (Q/A chatbot).
#     - Accuracy rate over 80% and Empowers them to make informed discussion.

#     :computer: [**Autograder**](https://github.com/PATELOM925/AutoGrader) - Precision In Every Grade
#     - Automated grading system for teachers and professors.
#     - Integration of BERT-Uncased for NLP-based grading, along with Spacy & PyTessearch for Image processing.
#     - Ensures accuracy in assessing diverse exam formats.

#     :computer: [**Meme App**](https://github.com/PATELOM925/MemeApp) - Laughter Just A Click Away
#     - Innovative and fun Android application developed using Kotlin and Sourced from Reddit's API through Retrofit.
#     - Utilizes Android development tools and Glide library to Deliver a never-ending stream of hilarious memes. 
#     '''
# )

# # PROJECTS = {
# #      'ChatPDF AI - Talk With Your PDFs \n': {
# #         'url': 'https://chatpdf-ai-om-m-patel.streamlit.app/',
# #         'description': " - Leverages advanced NLP techniques \n"
# #                        " - Integration with Streamlit Cloud for streamlined PDF analysis \n"
# #                        " - Achieves an impressive 89% accuracy rate \n"
# #                        " - Empowers users in making informed decisions faster"
# #     },
# #     'Autograder - Precision In Every Grade \n': {
# #         'url': 'https://github.com/PATELOM925/Automatic-Paper-Checker',
# #         'description': " - Automated grading system for teachers and professors \n"
# #                        " - Integration of BERT-Uncased for NLP-based grading \n"
# #                        " - Utilizes Spacy & PyTesseract for image processing \n"
# #                        " - Ensures accuracy in assessing diverse exam formats"
# #     },
# #     'Meme App': {
# #         'url': 'https://github.com/PATELOM925/MemeApp \n',
# #         'description': " - Innovative and fun Android application developed using Kotlin \n"
# #                        " - Utilizes Android development tools and Glide library \n"
# #                        " - Delivers a never-ending stream of hilarious memes \n"
# #                        " - Sourced from Reddit's API through Retrofit"
# #     }
# # }

# st.write('#')
# st.subheader('**Experience**')
# st.write(
#     '''

# :pushpin: **Data Science Intern @ Sharperly (Feb 2024 -- July 2024)**
#  - Developed a geocoding solution using Python (Flask, Geopandas, etc.), reducing dependency on Google Cloud API and cutting costs by 65%.
#  - Created a MongoDB database to store geo-coordinates, reducing server load by 134%.
#  - Enhanced location accuracy with a proximity search algorithm, ensuring recognition within a 10-meter range.
#  - Conducted data scraping for addresses using OpenStreetMap and Overpass Turbo.
#  - Managed code workflows with GitHub, and coordinated tasks and documentation using Jira and Confluence.
 
# :pushpin: **Android Developer (Intern) @ Patchmax pvt ltd. (May 2023 -- July 2023)**
#  - Successfully Learned Android Development in Kotlin and Built Apps/features.
#  - Grateful to my team who taught me "Transforming Visions into Seamless Apps".
#  - Major Skills Used: REST APIs, Firebase, Kotlin, Azure Blob, MySQL.

# :pushpin: **Creator @ ASK OM PATEL (Nov 2021 -- July 2022)**
#  - Spread Financial and Startup knowledge and gained more than 55,000 eyeballs on *[Instagram](https://www.instagram.com/askompatel/).*
#  - Used *[Youtube](https://www.youtube.com/@iampatelom)* to spread the startup knowledge in native language (Gujarati).
#  - Major Skills Used: Adobe Premiere Pro, Canva, Social Media Marketing

# :pushpin: **Graphic Designer @ Aasan Study (Mar 2020 -- Feb 2022)**
#  - Created engaging Educational Content for the *[website](https://aasanstudy.com/)*.
#  - Designed Graphics for educational posts for Instagram, YouTube, and website.
#  - Major Skills Used: Adobe Photoshop, Adobe Illustrator, Web Content Writing
# '''
# )



# # ---ACHIEVEMENTS---
# st.write('#')
# st.subheader('Certifications')
# st.write(
# '''
# - [Generative AI with Large Language Models](https://www.coursera.org/account/accomplishments/certificate/XGBDJAYXTEF7)
# - [Langchain Chat With Your Data](https://coursera.org/share/4b21792f6551d0c5096f1d761417278f)
# - [Excel](https://olympus.mygreatlearning.com/courses/12583/certificate)
# '''
# )
 
# # Learnt From
# st.write('#')
# st.subheader('Learnt From')
# for name, link in Learnt_From.items():
#     st.markdown(f'<a href="{link}" style="line-height: 1.0;">{name}</a>', unsafe_allow_html=True)


# # ---CO-CURRICULARS---
# st.write('#')
# st.subheader('Co-Curricular Activities')
# st.write(
#     '''
# - **President** @ *[Tattvam](https://www.instagram.com/tattvam.pdeu/)- The Sanskrit Club of PDEU*(May 2023 - Present)
# - **Graphic Head** @ *[Tattvam](https://www.instagram.com/tattvam.pdeu/) - The Sanskrit Club of PDEU*(May 2022 - May 2023)

# '''
# )














# #NEW TRY 2

# from pathlib import Path
# import streamlit as st
# from PIL import Image
# import pandas as pd

# # --- PATH SETTINGS --- 
# current_directory = Path(__file__).parent if '__file__' in locals() else Path.cwd()
# resume_file = current_directory / 'details' / 'Om_M_Patel_Resume_July24.pdf'
# profile_pic = current_directory / 'details' / 'Profile Photo - Om Patel.png'

# # --- GENERAL SETTINGS ---
# PAGE_TITLE = 'CV | OM M PATEL'
# PAGE_ICON = ':rocket:'
# NAME = 'OM M PATEL'
# DESCRIPTION = '''Diving Deep in Data'''
# EMAIL = 'iampatelom@gmail.com'

# SOCIAL_MEDIA = {
#     'https://www.svgrepo.com/show/503359/github.svg': 'https://github.com/PATELOM925',
#     'https://www.svgrepo.com/show/110195/linkedin.svg': 'https://www.linkedin.com/in/om-m-patel-b539b8213/',
#     'https://www.svgrepo.com/show/489456/email.svg': 'mailto:iampatelom@gmail.com',
#     'https://www.svgrepo.com/show/303115/twitter-3-logo.svg': 'https://twitter.com/om_m_patel',
#     'https://www.svgrepo.com/show/349422/kaggle.svg': 'https://www.kaggle.com/iamommpatel',
# }

# Learnt_From = {
#     'Krish Naik': 'https://www.youtube.com/@krishnaik06',
#     'StatQuest with Josh Starmer': 'https://www.youtube.com/@statquest',
#     'Towards Data Science': 'https://towardsdatascience.com/',
#     'DeepLearning,AI': 'https://www.deeplearning.ai/',
#     'iNeuron': 'https://ineuron.ai/'
# }

# st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# # --- LOAD PDF & PROFILE PIC ---
# with open(resume_file, 'rb') as pdf_file:
#     PDFbyte = pdf_file.read()
# profile_pic = Image.open(profile_pic)
# st.markdown(
#     """
#     <style>
#     body, h1, h2, h3, h4, h5, h6, p, div, span, table, .stMarkdown {
#         color: black !important;
#     }
#     .stButton > button {
#         color: white !important;
#         background-color: white;
#     }
#     thead th, tbody th {
#         color: black !important;
#     }
#     .stDataFrame thead tr, .stDataFrame tbody tr {
#         color: black !important;
#     }
#     .stApp {
#         background-color: #e3e5fa;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )


# # --- HERO SECTION ---
# col1, col2 = st.columns(2, gap='small')

# with col1:
#     st.image(profile_pic, width=321, channels='RGB', use_column_width=True)

# with col2:
#     st.title(NAME)
#     st.write(DESCRIPTION)
#     st.download_button(
#         label='📄 Download My Resume',
#         data=PDFbyte,
#         file_name=resume_file.name,
#         mime='application/octet-stream',
#     )

# # --- SOCIAL LINKS ---
# st.write('#')
# cols = st.columns(len(SOCIAL_MEDIA))
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].write(f'<a href="{link}"><img src="{platform}" alt="HTML tutorial" style="width:42px;height:42px;"></a>', unsafe_allow_html=True)

# # --- SKILLS ---
# st.write('#')
# st.subheader('Skills')

# # Data for the skills table
# skills_data = [
#     ('Programming Languages', 'Python, Java, C, HTML+CSS'),
#     ('Databases', 'MySQL, MongoDB, SQLite, Firebase'),
#     ('Libraries/Frameworks', 'NumPy, Scipy, Pandas, Matplotlib, OpenCV, PIL, Tensorflow, Keras, NLTK, Streamlit, Flask, Pytesseract'),
#     ('Developer Tools', 'GIT, GITHUB, DOCKER, STREAMLIT CLOUD, AWS, MICROSOFT OFFICE, ASANA, CONFLUENCE, JIRA, AI TOOLS, COMPASS, WORKBENCH'),
#     ('Areas of Interest', 'DATA SCIENCE, DATA ANALYST, ML-OPS, BIG DATA ANALYST, QUANTITATIVE ANALYST'),
#     ('Soft Skills', 'AVID LISTENER, PROBLEM SOLVING, FAST-LEARNER, TEAM LEADERSHIP, ADAPTIVE'),
#     ('Hands in Emerging Tech', 'LANGCHAIN, LLAMAINDEX, GENERATIVE AI, NLP'),
# ]
# index = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# # Create a DataFrame without index and header
# skills_df = pd.DataFrame(skills_data, columns=['Category', 'Skills'], index=index)

# # Display the table
# st.table(skills_df)

# # --- EXPERIENCE ---
# st.write('#')
# st.subheader('**Experience**')
# st.write(
#     '''
# :pushpin: **Data Science Intern @ Sharperly (March 2024 -- July 2024)**
#  - Developed a geocoding solution using Python (Flask, Geopandas, etc.), reducing dependency on Google Cloud API and cutting costs upto 55%.
#  - Scraped and processed address data using Overpass Turbo, Beautiful Soup, and Selenium.
#  - Performed exploratory data analysis (EDA) on geospatial datasets, Contributed to training machine learning models for geospatial analysis by leveraging KNN and other algorithms.
#  - Optimized MongoDB databases to store data, and further contributed to authentication and credit management systems for APIs.
#  - Collaborated code workflows with GitHub, coordinated tasks and documentation using Jira and Confluence
 
# :pushpin: **Android Developer (Intern) @ Patchmax pvt ltd. (May 2023 -- July 2023)**
#  - Successfully Learned Android Development in Kotlin and Built Apps/features.
#  - Grateful to my team who taught me "Transforming Visions into Seamless Apps".
#  - Major Skills Used: REST APIs, Firebase, Kotlin, Azure Blob, MySQL.

# :pushpin: **Creator @ ASK OM PATEL (Nov 2021 -- July 2022)**
#  - Spread Financial and Startup knowledge and gained more than 55,000 eyeballs on *[Instagram](https://www.instagram.com/askompatel/).*
#  - Used *[Youtube](https://www.youtube.com/@iampatelom)* to spread the startup knowledge in native language (Gujarati).
#  - Major Skills Used: Adobe Premiere Pro, Canva, Social Media Marketing

# :pushpin: **Graphic Designer @ Aasan Study (Mar 2020 -- Feb 2022)**
#  - Created engaging Educational Content for the *[website](https://aasanstudy.com/)*.
#  - Designed Graphics for educational posts for Instagram, YouTube, and website.
#  - Major Skills Used: Adobe Photoshop, Adobe Illustrator, Web Content Writing
# '''
# )

# # --- PROJECTS ---
# st.write('#')
# st.subheader('Projects')
# st.write(
#     '''
#     :computer:[**Driver Pay Forecasting**](https://github.com/PATELOM925/Uber_NYC_Driver_Pay_Prediction) - Uber NYC Driver Pay Prediction
#     - Implemented machine learning and deep learning models (ANN, Random Forest, LSTM, BiLSTM,LSTM+GRU) and performed comparative analysis for pay prediction
#     - Analyzed and Visualized factors impacting Uber driver pay through features like date, time, location, and other trip details using PowerBI.
    
#     :computer:[**Indian Weather Prediction**](https://www.kaggle.com/code/iamommpatel/indian-weather-predictor) - Ranked in Top-5 for Kaggle's ML Olympiad (Forecasting India's Weather)
#     - Achieved high accuracy (R²: 0.9844) by comparing & selecting the best regression model (XGBoost, Gradient Boosting, Linear Regression, Decision Tree, etc)
#     - Performed EDA showcasing diverse graphs and model evaluation metrics
    
#     :computer: [**SQl AI**](https://github.com/PATELOM925/SQL-AI) - Access Database In Your Language
#     - Allows Users to upload SQL databases and Access them in Natural Language prompts.
#     - Transforms input into precise SQL queries with  an accuracy over *80%*.

#     :computer: [**ChatPDF AI**](https://chatpdf-ai-om-m-patel.streamlit.app/) - Talk With Your PDFs
#     - let's user retrieve necessary information from PDF (Q/A chatbot).
#     - Accuracy rate over 80% and Empowers them to make informed discussion.

#     :computer: [**Autograder**](https://github.com/PATELOM925/AutoGrader) - Precision In Every Grade
#     - Automated grading system for teachers and professors.
#     - Integration of BERT-Uncased for NLP-based grading, along with Spacy & PyTessearch for Image processing.
#     - Ensures accuracy in assessing diverse exam formats.

#     :computer: [**Meme App**](https://github.com/PATELOM925/MemeApp) - Laughter Just A Click Away
#     - Innovative and fun Android application developed using Kotlin and Sourced from Reddit's API through Retrofit.
#     - Utilizes Android development tools and Glide library to Deliver a never-ending stream of hilarious memes. 
#     '''
# )

# # --- CO-CURRICULAR ACTIVITIES ---
# st.write('#')
# st.subheader('Co-Curricular Activities')
# st.write(
#     '''
# - **President** @ *[Tattvam](https://www.instagram.com/tattvam.pdeu/)- The Sanskrit Club of PDEU*(June 2023 - June 2024)
# - **Graphic Head** @ *[Tattvam](https://www.instagram.com/tattvam.pdeu/) - The Sanskrit Club of PDEU*(May 2022 - May 2023)

# '''
# )

# # --- CERTIFICATIONS ---
# st.write('#')
# st.subheader('Certifications')
# st.write(
#     '''
# - [Generative AI Project](https://learn.ineuron.ai/certificate/fa40c5f4-fe71-42a6-8557-9a8a1abdb7d4)
# - [NPTEL](https://internalapp.nptel.ac.in/NOC/NOC24/SEM1/Ecertificates/107/noc24-de06/Course/NPTEL24DE06S55570004730616807.pdf)
# - [Generative AI with Large Language Models](https://www.coursera.org/account/accomplishments/certificate/XGBDJAYXTEF7)
# - [Langchain Chat With Your Data](https://coursera.org/share/4b21792f6551d0c5096f1d761417278f)
# - [Excel](https://www.sololearn.com/certificates/CT-S9OKVGDH)

# '''
# )

# # --- LEARNT FROM ---
# st.write('#')
# st.subheader('Learnt From')
# for mentor, link in Learnt_From.items():
#     st.write(f'[{mentor}]({link})')



# # ---

