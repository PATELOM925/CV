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
resume_file = current_directory / 'details' / 'Om_Resume_Canada.pdf'
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
    # 'https://www.svgrepo.com/show/303115/twitter-3-logo.svg': 'https://twitter.com/om_m_patel',
    'https://www.svgrepo.com/show/349422/kaggle.svg': 'https://www.kaggle.com/iamommpatel',
}

# ----------------------------
# CSS STYLING
# ----------------------------
st.markdown(
    """
    <style>
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
    .stImage > img {
      border-radius: 0 !important;
      width: 250px !important;
      height: 250px !important;
      object-fit: cover;
    }
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
    @media screen and (max-width: 768px) {
      .nav-links a {
         font-size: 14px;
         margin: 5px;
      }
    }
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
    .less-space ul {
        margin-top: 0px;
        margin-bottom: 5px;
        padding-left: 20px;
    }
    .less-space li {
        margin-top: 0.5px
        margin-bottom: 0.5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# NAV BAR 
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
# HERO SECTION: PROFILE PIC, TITLE, DESCRIPTION & CV DOWNLOAD
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
# SOCIAL LINKS 
# ----------------------------
st.write("")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (icon_url, link_url) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].markdown(
        f'<a href="{link_url}"><img src="{icon_url}" alt="icon" style="width:42px;height:42px;"></a>',
        unsafe_allow_html=True
    )

# ----------------------------
# SKILLS 
# ----------------------------
st.write("")
st.subheader("Skills", anchor="skills")
skills_data = [
    ('Programming Languages', 'Python, JavaScript, SQL, HTML+CSS'),
    ('Databases', 'MySQL, MongoDB, PostgreSQL, Firebase'),
    ('Libraries/Frameworks', 'NumPy, Scipy, Pandas, Matplotlib, OpenCV, PIL, Tensorflow, Keras, NLTK, Streamlit, Flask, Pytesseract'),
    ('Developer Tools', 'Git, Github, Docker, AWS, Microsoft Office, Asana, Confluence, JIRA, AI Tools, Compass, Workbench, Postman'),
    ('Areas of Interest', 'AI Democratization, NLP, LLMs, Deep Generative Models, Prompt engineering'),
    ('Soft Skills', 'Avid listener, Critical Thinker, Problem-Solver'),
]
index_labels = ['A', 'B', 'C', 'D', 'E', 'F']
skills_df = pd.DataFrame(skills_data, columns=['Category', 'Skills'], index=index_labels)
st.table(skills_df)

# ----------------------------
# EXP 
# ----------------------------
st.write("")
st.subheader("Experience", anchor="experience")
st.markdown(
    """
    :pushpin: **Backend & Data Engineer Intern @ Sharperly(Zaza Tech Ltd.) (Dec 2024 -- Aug 2025)**
     - Designed Airflow-powered ETL pipelines for geospatial datasets (Geopandas, Python), increasing throughput around 25%.
     - Worked with messy real-world data, developing robust pipelines using ETL/ELT stack.
     - Containerized services on AWS and Render via CI/CD pipelines and GitHub Actions, ensuring scalability and consistent performance.
     - Optimized MongoDB schemas and indexing for real-time lookups used by downstream ML components.
     - Collaborated with teams and stakeholders, used GitHub, Jira, & Confluence to drive technical documentation.

    :pushpin: **Data Science Intern @ Sharperly (March 2024 -- July 2024)**
     - Developed geocoding APIs with Python (Flask, Geopandas) to reduce dependency on GMaps API and cutting costs upto 45% (approx 350 USD) monthly.
     - Scraped and pre-processed 20k+ addresses to create robust training datasets, producing versioned datasets for ML training
     - Performed exploratory data analysis (EDA) on geospatial datasets.
     - Trained and evaluated models (RNNs, K-Means, GNNs, Autoencoders) to predict user behaviour, optimize routes and detect anomalies.
     
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
# PROJECTS 
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
    - Analyzed architecture and hyperparameters searches, achieving almost 12% lower RMSE vs. baseline.
    - Visualized factors impacting Uber driver pay through features like date, time, location, and other trip details using Tableau.
    
    :computer: [**Indian Weather Prediction**](https://www.kaggle.com/code/iamommpatel/indian-weather-predictor) - Ranked in Top-5 for Kaggle's ML Olympiad (Forecasting India's Weather)
    - Achieved high accuracy (R²: 0.9844) by comparing & selecting the best regression model (XGBoost, Gradient Boosting, Linear Regression, Decision Tree, etc.).
    - Performed EDA showcasing diverse graphs and model evaluation metrics.
    
    :computer: [**SQL AI**](https://github.com/PATELOM925/SQL-AI) - Access Database In Your Language
    - Allows users to upload SQL databases and access them in natural language prompts. 
    - Transforms input into precise SQL queries with an accuracy over 80%.

    :computer: [**ChatPDF AI**](https://chatpdf-ai-om-m-patel.streamlit.app/) - Talk With Your PDFs
    - Built a Proof Of Concept for Conversational AI using RAG architecture with 80% accuracy using Sentence Transformers, LangChain, PyPDF2 and FAISS by optimizing search and analysis
    - Deployed the advanced system on Streamlit Cloud and enhancing the retrieval process.

    :computer: [**Autograder**](https://github.com/PATELOM925/AutoGrader) - Precision In Every Grade
    - Led a six-member team to develop an automated grading system, using React for the front-end, Python with Flask for model integration, backend logic, and MongoDB for data storage.
    - Achieved over 63% grading accuracy by developing a custom pipeline combining BERT-Uncased with NLP; leveraged SpaCy and PyTesseract for image-based answer sheet processing.

    :computer: [**Meme App**](https://github.com/PATELOM925/MemeApp) - Laughter Just A Click Away
    - Innovative and fun Android application developed using Kotlin and sourced from Reddit's API through Retrofit.
    - Utilizes Android development tools and Glide library to deliver a never-ending stream of hilarious memes. 
    """,
    unsafe_allow_html=True
)

# ----------------------------
# EXTRACURRICULARS 
# ----------------------------
st.write("")
st.subheader("Extracurriculars", anchor="extracurricular")
st.markdown(
    """
    - **Vector AI 2025-2026 Scholarship Recipient**, York University (May 2025)
    - **Published Research Paper** @*ADCIS 2024, BITS Pilani*- "Automated Sleep Stage Classification Using Machine Intelligence Techniques" (September 2024) <br> [@Springer Journal](https://link.springer.com/chapter/10.1007/978-981-96-3652-5_14)
    - **Top-10 Rank** @ *Kaggle's ML Olympiad* - Forecasting India’s Weather (April 2024 - May 2024)
    - **AI/ML Mentor** Guided 10+ students on projects including Autograder and Legal Clarity
    - **President** @*[Tattvam](https://www.instagram.com/tattvam.pdeu/)- The Sanskrit Club of PDEU* (June 2023 - June 2024)
    - **Graphic Head** @*[Tattvam](https://www.instagram.com/tattvam.pdeu/)- The Sanskrit Club of PDEU* (May 2022 - May 2023)
    - **Volunteer** @ *Vardaan Foundation, Vadodara* - Civic and Social Internship: Taught digital literacy to underprivileged students (June 2022 - July 2022)
    """,
    unsafe_allow_html=True
)

# ----------------------------
# CERTIFICATIONS 
# ----------------------------
st.write("")
st.subheader("Certifications", anchor="certifications")
st.markdown(
    """
    <div class="less-space">
      <ul>
        <li><a href="https://learn.ineuron.ai/certificate/fa40c5f4-fe71-42a6-8557-9a8a1abdb7d4" target="_blank">Generative AI Project</a></li>
        <li><a href="https://internalapp.nptel.ac.in/NOC/NOC24/SEM1/Ecertificates/107/noc24-de06/Course/NPTEL24DE06S55570004730616807.pdf" target="_blank">NPTEL</a></li>
        <li><a href="https://credsverse.com/credentials/477d05ad-f429-46d3-94b7-2c7dc8695a52" target="_blank">LLMs: RAG with LLamaIndex & AzureOpenA</a></li>
        <li><a href="https://drive.google.com/file/d/18Sz-wRGKDv-6jrAU1IxtofAjchoHLu14/view?usp=sharing" target="_blank">Applications of AI/ML in Biomedical Signal Processing & Computer Vision</a></li>
        <li><a href="https://www.coursera.org/account/accomplishments/certificate/XGBDJAYXTEF7" target="_blank">Generative AI with Large Language Models</a></li>
        <li><a href="https://coursera.org/share/4b21792f6551d0c5096f1d761417278f" target="_blank">Langchain Chat With Your Data</a></li>
        <li><a href="https://www.sololearn.com/certificates/CT-S9OKVGDH" target="_blank">Excel</a></li>
        <li><a href="https://www.mygreatlearning.com/certificate/PWEPYSNT" target="_blank">C Language</a></li>
      </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# LEARNT FROM :
# ----------------------------
st.write("")
st.subheader("Learnt From")
st.markdown(
    """
    <div class="less-space">
      <ul>
            <li><a href="https://www.youtube.com/@krishnaik06" target="_blank">Krish Naik</a></li>
            <li><a href="https://x.com/svpino" target="_blank">Santiago</a></li>
            <li><a href="https://x.com/karpathy" target="_blank">Andrej Karpathy</a></li>
            <li><a href="https://www.youtube.com/@statquest" target="_blank">StatQuest with Josh Starmer</a></li>
            <li><a href="https://towardsdatascience.com/" target="_blank">Towards Data Science</a></li>
            <li><a href="https://www.deeplearning.ai/" target="_blank">DeepLearning.AI</a></li>
            <li><a href="https://ineuron.ai/" target="_blank">iNeuron</a></li>
      </ul>
    </div>
    """,
    unsafe_allow_html=True
)
# ----------------------------
# CONTACT 
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
