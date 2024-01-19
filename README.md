# ArticleGenius: AI-Powered Article Generation Tool

## Overview:
ArticleGenius is an innovative web application that utilizes the power of AI to assist in generating high-quality articles. It's built using Streamlit, a popular framework for building data applications, and integrates a language model (LLaMa 2) for content creation. This tool is tailored for users who need quick, intelligent, and customized article writing, such as content creators, marketers, researchers, and educators.

## Features
- **Custom Topic Selection:** Users can input any topic for article generation.
- **Word Count Customization:** Allows specifying the length of the article.
- **Writing Style Options:** Choose from academic, professional, or general public writing styles.

## Requirements
- Python 3.8
- Streamlit
- Other dependencies listed in `requirements.txt`

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/olawale0254/ArticleGenius.git
   cd ArticleGenius
2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
3. **Download Llama model from Huggingface**
    Download the Llamma model and export it into the model folder. i.e src/model/llama-2-7b.ggmlv3.q8_0.bin

3. **Run the App:**
    ```bash
    streamlit run app.py




