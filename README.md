# PDF Chatbot using Streamlit and LangChain

This application utilizes Streamlit and LangChain to create a chatbot capable of extracting text from PDFs and answering user questions based on the content of the PDF.

## Overview

The chatbot functionality is powered by the following components:

- **Streamlit:** Used for the web application interface.
- **LangChain:** Provides text processing, including text splitting, vectorization, and question-answering capabilities.
- **Hugging Face's `google/flan-t5-xxl` Language Model:** Utilized for generating responses to user queries.

## Installation

To run this application, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd pdf-chatbot
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application:**
    ```bash
    streamlit run app.py
    ```

## Usage

1. Upon running the application, you'll be presented with an interface to upload a PDF file.
2. Upload a PDF file containing text.
3. Ask questions related to the content of the uploaded PDF using the chat input.
4. The chatbot will extract information from the PDF and provide relevant answers using the language model.

## Files and Components

- **`app.py`:** Main application file containing the Streamlit interface and chatbot logic.
- **`requirements.txt`:** File listing all required dependencies for the application.
