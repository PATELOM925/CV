from pathlib import Path
import streamlit as st
from PIL import Image
import pandas as pd
import requests 

# ----------------------------
# PAGE CONFIGURATION & PATHS
# ----------------------------
st.set_page_config(page_title="CV | OM M. PATEL", page_icon=":rocket:")

current_directory = Path(__file__).parent if '__file__' in locals() else Path.cwd()
resume_file = current_directory / 'details' / 'Om_Resume.pdf'
profile_pic_path = current_directory / 'details' / 'Profile Photo - Om Patel.png'

with open(resume_file, 'rb') as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic_path)

NAME = "OM M. PATEL"
DESCRIPTION = "Diving Deep in Data"
EMAIL = "iampatelom@gmail.com"

SOCIAL_MEDIA = {
    'https://upload.wikimedia.org/wikipedia/commons/a/ae/Github-desktop-logo-symbol.svg': 'https://github.com/PATELOM925',
    'https://www.svgrepo.com/show/110195/linkedin.svg': 'https://www.linkedin.com/in/om-m-patel/',
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

# ----------------------------
# CSS STYLING
# ----------------------------
st.markdown(
    """
    <style>
    /* Global Dark Theme Styles */
    body {
      font-family: 'Arial', sans-serif;
      color: #e0e0e0;
      background: linear-gradient(180deg, #030f4f, #5d3d94 100%);
      background-attachment: fixed;
      margin: 0;
      padding: 0;
    }
    .stApp {
      background: transparent;
      color: #e0e0e0;
      overflow: visible;
    }
    /* Force profile pic to be a 250x250 square */
    .stImage > img {
      border-radius: 0 !important;
      width: 250px !important;
      height: 250px !important;
      object-fit: cover;
    }
    /* Navigation Bar */
    .nav-container {
      background: rgba(93, 61, 148, 0.9);
      padding: 0.75rem;
      width: 100%;
      position: sticky;
      top: 0;
      z-index: 100;
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
    }
    .nav-links {
      display: flex;
      gap: 1.5rem;
      flex-wrap: wrap;
    }
    .nav-links a {
      color: white;
      text-decoration: none;
      font-size: 16px;
      font-weight: bold;
    }
    .nav-links a:hover {
      color: #ffd700;
    }
    /* Responsive adjustments for the nav bar */
    @media screen and (max-width: 768px) {
      .nav-links a {
         font-size: 14px;
         margin: 5px;
      }
    }
    /* Hero Section */
    .hero-col2 {
      margin-left: 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 250px; /* same height as the profile pic */
    }
    .hero-col2 h1 {
      margin-bottom: 20px;
    }
    .hero-col2 h5 {
      margin-bottom: 20px;
    }
    /* Download Button adjustments */
    .stDownloadButton {
      margin-left: 20px;
      margin-top: -57px;
    }
    .stDownloadButton > button {
      color: #222;
      background-color: #ffffff;
      border: none;
      border-radius: 8px;
      padding: 8px 16px;
      font-size: 16px;
      font-weight: bold;
    }
    .stDownloadButton > button:hover {
      background-color: #222;
      color: #ffd700;
    }
    /* Table Styling */
    .stTable {
      background-color: #030f4f;
      color: #e0e0e0;
      border-collapse: collapse;
    }
    .stTable th {
      color: #ffd700;
    }
    .stTable td {
      color: #e0e0e0;
      border-top: 1px solid #0b3d91;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# NAVIGATION BAR 
# ----------------------------
st.markdown(
    """
    <div class="nav-container">
      <div class="nav-links">
        <a href="#contact">Contact</a>
        <a href="#skills">Skills</a>
        <a href="#experience">Experience</a>
        <a href="#projects">Projects</a>
        <a href="#extracurricular">Extracurricular</a>
        <a href="#certifications">Certifications</a>
      </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# HERO SECTION: PROFILE PICTURE, TITLE, DESCRIPTION & RESUME DOWNLOAD
# ----------------------------
col1, col2 = st.columns([1, 2])
with col1:
    st.image(profile_pic, width=250)
with col2:
    st.markdown(
        f"""
        <div class="hero-col2">
            <div>
                <h1>{NAME}</h1>
                <h5>{DESCRIPTION}</h5>
            </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)
    st.download_button(
        label="📄 Download My Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    

# ----------------------------
# SOCIAL LINKS SECTION
# ----------------------------
st.write("")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (icon_url, link_url) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].markdown(
        f'<a href="{link_url}"><img src="{icon_url}" alt="icon" style="width:42px;height:42px;"></a>',
        unsafe_allow_html=True
    )

# ----------------------------
# SKILLS SECTION
# ----------------------------
st.write("")
st.subheader("Skills", anchor="skills")
skills_data = [
    ('Programming Languages', 'Python, Java, C, HTML+CSS'),
    ('Databases', 'MySQL, MongoDB, PostgreSQL, Firebase'),
    ('Libraries/Frameworks', 'NumPy, Scipy, Pandas, Matplotlib, OpenCV, PIL, Tensorflow, Keras, NLTK, Streamlit, Flask, Pytesseract'),
    ('Developer Tools', 'Git, Github, Docker, AWS, Microsoft Office, Asana, Confluence, JIRA, AI Tools, Compass, Workbench, Postman'),
    ('Areas of Interest', 'Natural Language Processing (NLP), LangChain,  LLMs,  Generative AI'),
    ('Soft Skills', 'Avid listener, Critical Thinking, Problem-Solving'),
]
index_labels = ['A', 'B', 'C', 'D', 'E', 'F']
skills_df = pd.DataFrame(skills_data, columns=['Category', 'Skills'], index=index_labels)
st.table(skills_df)

# ----------------------------
# EXPERIENCE SECTION
# ----------------------------
st.write("")
st.subheader("Experience", anchor="experience")
st.markdown(
    """
    :pushpin: **Data Engineer @ Sharperly (August 2024 -- Present)**
     - Enhanced and managed scalable data pipelines for geospatial data processing, improving ETL processes for data flows increasing training efficiency by 36%
     - Containerized the application with Docker and deployed it on cloud platforms (Render/AWS), achieving consistent performance and scalability
     - Led integration efforts to support the platform’s credit management and routing workflows
     - Collaborated with cross-functional teams and stakeholders using GitHub, Jira, & Confluence to drive technical documentation and business needs

    :pushpin: **Data Science Intern @ Sharperly (March 2024 -- July 2024)**
     - Developed a geocoding solution using Python (Flask, Geopandas, etc.), reducing dependency on Google Cloud API and cutting costs up to 55%.
     - Scraped and processed 10,000 plus address data using Overpass Turbo, Beautiful Soup, and Selenium.
     - Performed exploratory data analysis (EDA) on geospatial datasets, contributed to training machine learning models for geospatial analysis by leveraging KNN and other algorithms.
     - Optimized MongoDB databases to store data, and further contributed to authentication and credit management systems for APIs.
     
    :pushpin: **Android Developer (Intern) @ Patchmax pvt ltd. (May 2023 -- July 2023)**
     - Assisted in UI improvements and API integration, leading to a 23% increase in user engagement.
     - Implemented web scraping using Python, Beautiful Soup, and Selenium, increasing data acquisition efficiency by 18%.
     - Created apps in Kotlin, integrated libraries like Glide, Retrofit and Firebase resulting in a 20% reduction of crash rates and improved asynchronous operations.
     - Major Skills Used: REST APIs, Firebase, Kotlin, Azure Blob, MySQL.

    :pushpin: **Creator @ ASK OM PATEL (Nov 2021 -- July 2022)**
     - Spread financial and startup knowledge and gained more than 55,000 eyeballs on [Instagram](https://www.instagram.com/askompatel/).
     - Used [YouTube](https://www.youtube.com/@iampatelom) to spread startup knowledge in the native language (Gujarati).
     - Major Skills Used: Adobe Premiere Pro, Canva, Social Media Marketing.

    :pushpin: **Graphic Designer @ Aasan Study (Mar 2020 -- Feb 2022)**
     - Created engaging educational content for the [website](https://aasanstudy.com/).
     - Designed graphics for educational posts for Instagram, YouTube, and website.
     - Major Skills Used: Adobe Photoshop, Adobe Illustrator, Web Content Writing.
    """,
    unsafe_allow_html=True
)

# ----------------------------
# PROJECTS SECTION
# ----------------------------
st.write("")
st.subheader("Projects", anchor="projects")
st.markdown(
    """
    :computer: [**Legal Clarity**](https://github.com/PATELOM925/Legal_Clarity) - Simplifying Legal Documents
    - Developed and deployed a containerized NLP Flask application for legal document processing.
    - Implemented advanced transformer-based models (Pegasus, T5, IndicBARTSS) using PyTorch and Hugging Face Transformers to enable multi-language legal text summarization and translation.
    - Optimized model inference and API performance by integrating tokenization with SentencePiece, efficient caching, and asynchronous Flask request handling.
    
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
    - Enhanced productivity and decision-making in document analysis with 77% accuracy using NLP, Streamlit, LangChain, PyPDF2, and FAISS for an efficient retrieval system (RAG System).
    - Transformed document analysis with Google Generative AI, deploying the advanced system on Streamlit Cloud and enhancing the retrieval process.

    :computer: [**Autograder**](https://github.com/PATELOM925/AutoGrader) - Precision In Every Grade
    - Assisted a six-member team to develop an automated grading system, using React for the front end, Python with Flask for model integration, backend logic, and MongoDB for data storage.
    - Achieved over 63% accuracy in grading by analyzing NLP with BERT-Uncased and employing Spacy and PyTesseract for image processing

    :computer: [**Meme App**](https://github.com/PATELOM925/MemeApp) - Laughter Just A Click Away
    - Innovative and fun Android application developed using Kotlin and sourced from Reddit's API through Retrofit.
    - Utilizes Android development tools and Glide library to deliver a never-ending stream of hilarious memes. 
    """,
    unsafe_allow_html=True
)

# ----------------------------
# EXTRACURRICULARS SECTION
# ----------------------------
st.write("")
st.subheader("Extracurriculars", anchor="extracurricular")
st.markdown(
    """
    - **President** @ *[Tattvam](https://www.instagram.com/tattvam.pdeu/)- The Sanskrit Club of PDEU* (June 2023 - June 2024)
    - **Graphic Head** @ *[Tattvam](https://www.instagram.com/tattvam.pdeu/)- The Sanskrit Club of PDEU* (May 2022 - May 2023)
    - **Research Presenter** @ *ADCIS 2024, BITS Pilani* - Presented paper titled "Automated Sleep Stage Classification using Machine Intelligence Techniques" (September 2024, accepted/presented/under press in Springer Journal)
    - **Top-5 Rank** @ *Kaggle's ML Olympiad* - Forecasting India’s Weather (April 2024 - May 2024)
    - **Volunteer** @ *Vardaan Foundation, Vadodara* - Civic and Social Internship: Taught digital literacy to underprivileged students (June 2022 - July 2022)
    """,
    unsafe_allow_html=True
)

# ----------------------------
# CERTIFICATIONS SECTION
# ----------------------------
st.write("")
st.subheader("Certifications", anchor="certifications")
st.markdown(
    """
    - [Generative AI Project](https://learn.ineuron.ai/certificate/fa40c5f4-fe71-42a6-8557-9a8a1abdb7d4)
    - [NPTEL](https://internalapp.nptel.ac.in/NOC/NOC24/SEM1/Ecertificates/107/noc24-de06/Course/NPTEL24DE06S55570004730616807.pdf)
    - [LLMs: RAG with LLamaIndex & AzureOpenA](https://credsverse.com/credentials/477d05ad-f429-46d3-94b7-2c7dc8695a52)
    - [Applications of AI/ML in Biomedical Signal Processing & Computer Vision](https://drive.google.com/file/d/18Sz-wRGKDv-6jrAU1IxtofAjchoHLu14/view?usp=sharing)
    - [Generative AI with Large Language Models](https://www.coursera.org/account/accomplishments/certificate/XGBDJAYXTEF7)
    - [Langchain Chat With Your Data](https://coursera.org/share/4b21792f6551d0c5096f1d761417278f)
    - [Excel](https://www.sololearn.com/certificates/CT-S9OKVGDH)
    - [C Language](https://www.mygreatlearning.com/certificate/PWEPYSNT)
    """,
    unsafe_allow_html=True
)

# ----------------------------
# LEARNT FROM SECTION
# ----------------------------
st.write("")
st.subheader("Learnt From")
for mentor, link in Learnt_From.items():
    st.markdown(f"[{mentor}]({link})", unsafe_allow_html=True)

# ----------------------------
# CONTACT SECTION
# ----------------------------
st.write("")
st.subheader("Contact Me", anchor="contact")
with st.form(key='contact_form'):
    st.write("## Send me a message")
    name_input = st.text_input("Name")
    email_input = st.text_input("Email")
    message_input = st.text_area("Message")
    submit_button = st.form_submit_button(label='Send Message')
    
    if submit_button:
        if not name_input or not email_input or not message_input:
            st.error("Please fill out all fields.")
        else:
            form_data = {
                "name": name_input,
                "email": email_input,
                "message": message_input
            }
            response = requests.post(
                "https://formspree.io/f/xnnjbpve",  
                data=form_data
            )
            if response.status_code == 200:
                st.success(f"Thank you {name_input}! Your message has been sent. I'll respond to you at {email_input} soon.")
            else:
                st.error("Failed to send the message. Please try again later.")
