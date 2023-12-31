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
    cd ChatPDF
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: .\env\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set the Hugging Face API token as an environment variable:**

    - If you haven't already, sign up on the Hugging Face website and get your API token.
    
    - Set the environment variable by replacing `"YOUR_HUGGINGFACE_API_KEY"` with your actual API key in the terminal:
        ```bash
        export HUGGINGFACEHUB_API_TOKEN="YOUR_HUGGINGFACE_API_KEY"
        ```
    
    - For Windows users, set the environment variable using:
        ```bash
        set HUGGINGFACEHUB_API_TOKEN="YOUR_HUGGINGFACE_API_KEY"
        ```

5. **Run the application:**
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

## Public Link

- Access the application using this public link: [PDF Chatbot Application](https://chatpdf-v1.streamlit.app)
