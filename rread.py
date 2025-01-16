import streamlit as st
import PyPDF2
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import nltk
import re

# Download NLTK stopwords
to_download = True
try:
    stop_words = set(stopwords.words('english'))
    to_download = False
except:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

# Streamlit app
def main():
    st.title("PDF Word Cloud Generator")
    st.write("Upload a PDF file to extract text, preprocess it, and generate a word cloud.")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        # Extract text from the PDF
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = "".join(page.extract_text() for page in pdf_reader.pages)

        st.subheader("Extracted Text")
        st.text_area("Extracted Text", text, height=200)

        if st.button("Generate Word Cloud"):
            # Preprocess text
            processed_text = preprocess_text(text)

            # Generate word cloud
            generate_word_cloud(processed_text)


def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation and special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Tokenize and remove stop words
    words = text.split()
    cleaned_words = [word for word in words if word not in stop_words]

    return ' '.join(cleaned_words)


def generate_word_cloud(text):
    wordcloud = WordCloud(width=800, height=400, max_words=500, background_color='white').generate(text)
    
    # Display the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    st.pyplot(plt)


if __name__ == "__main__":
    main()
