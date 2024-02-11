import streamlit as st
import PyPDF2 as pdf
import google.generativeai as genai

GOOGLE_API_KEY = ""
genai.configure(api_key=GOOGLE_API_KEY)

def get_gemini_response(title, text, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([title, text[0], prompt])
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text


input_prompt = """
Please generate a summary of the following research paper:

Title: {title}

Paper Text: {text}

Please generate a summary on this research paper."""


# Streamlit APP
st.set_page_config(page_title="Research Paper Summarizer")
st.header("Lets Summarize!!")
input_text = st.text_area("Title of Research Paper", key="title")
uploaded_file = st.file_uploader("Upload Reasearch Paper",type=["pdf"], help="Please upload the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt, text, input_text)
        st.write(response)