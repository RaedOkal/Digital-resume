import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from pathlib import Path


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
resume_file = current_dir / "images" / "Raed-CV.pdf"
profile_pic = current_dir / "images" / "profile-pic (6).png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Raed Okal"
PAGE_ICON = ":bar_chart:"
NAME = "Raed Okal"
DESCRIPTION = """
Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "raedokal33@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/raed-okal-31390b247",
    "GitHub": "https://github.com/RaedOkal",
    "kaggle": "https://www.kaggle.com/raedokal",
    "Tableau": "https://public.tableau.com/app/profile/raed.okal",
}

   


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)



# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Degrees,Licenses and Qualifications")
st.write(
    """
- ✔️ Bachelor degree in information system
- ✔️ Completed the Google Data Analyst Professional Certification Program
- ✔️ Completed the python for everybody from University of Michigan Program
- ✔️ Strong knowledge in Python and Excel and sql
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Good knowledge in building and developing applications with python  
- ✔️ Familiar with all principles of computer science, oop, Data structures & Algorithms  
- ✔️ Good data engineering knowledge with python
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn,Pandas,Numpy), SQL
- 📊 Data Visulization: Tableau, MS Excel,Python(Matplotlib,Seaborn)
- 🗄️ Databases: Sql Server, Sqlite, Bigquery
"""
)





#st.set_page_config(page_title='RAED OKAL PORTFOLIO',page_icon=':bar_chart:',layout='wide')
#st.subheader("Hello there, i'm Raed :wave:")
#st.title('Data Analyst from the Middle East :bar_chart:')
#st.write('well versed analyst in Ecxel, SQL, Python and Tableau ')
#st.write("Learn More >> https://2u.pw/39UTI") 


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


 #Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_3rwasyjy.json")
img_python = Image.open("C:\\Users\\lenovo ideapad130\OneDrive\\المستندات\\practical python proj\\images\\pytonE.jpg")
img_Excel = Image.open("C:\\Users\\lenovo ideapad130\\OneDrive\\المستندات\\practical python proj\\images\\ExcelP.jpg")
sqlimg= Image.open("C:\\Users\\lenovo ideapad130\\OneDrive\\المستندات\\practical python proj\\images\\office.jpg")
tt=Image.open("C:\\Users\\lenovo ideapad130\\OneDrive\\المستندات\\practical python proj\\images\\Tableau.jpg")




# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do:-")
        #st.write("##")
        st.write(
            """

         I'm a data analyst get the job done with :
          - SQL or pandas (which I prefer)
          - Excel 
          - Tableau 

        I look every day for new challenges and projects to hone my skills and
          increase my expertise in more than one field 
          such as: " finance & Real estate , tech & e-commerce."

        As Harvey Spector says: 
                 "I win that's what I do" :necktie: 
        
        
            """)

with right_column:
        st_lottie(lottie_coding, height=300, key="coding")




# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects :-")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_python)
    with text_column:
        st.subheader("country's GDP analysis with python ")
        st.write(
            """
            After I have learned some python , 
            I recently came up with this idea 
            to use my web scraping skills and find and scrape my dataset from the web 
            to do some exploratory Exploratory data analysis
            and answer some questions about the data after cleaning it up in Excel
            """
        )
        st.markdown("[view project...](https://2u.pw/uA8BZ)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_Excel)
    with text_column:
        st.subheader("Bike sales analysis")
        st.write(
            """
            in this specific project I did some analysis and data cleaning
             on the bike sales data and 
             I have created a beautiful dashboard.
            """
        )
        st.markdown("[view project...](https://2u.pw/JQchm)")


with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(sqlimg)
    with text_column:
        st.subheader("The Office With SQL")
        st.write(
            """
            a small project from the office series I created a small data set
             and I started to analyze it and answer some questions 
             after I cleaned it
            """
        )
        st.markdown("[view project...](https://github.com/RaedOkal/The-office-SQL-project)")


with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(tt)
    with text_column:
        st.subheader("My Tableau project")
        st.write(
            """
            a small project containe beautiful dashboard
             for a specific analysis
            """
        )
        st.markdown("[view project...](https://public.tableau.com/app/profile/raed.okal/viz/dashboard2_16606436432870/Dashboard2)")

       

       
 # ---- CONTACT ----
with st.container():
    st.write("---")
    st.header(":mailbox:Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/raedokal33@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()