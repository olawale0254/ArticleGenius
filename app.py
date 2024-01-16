import streamlit as st
from src.article_generator import ArticleGenerator

def main():
    # Streamlit page configuration
    st.set_page_config(page_title="Generate Articles", page_icon="📰", layout="centered")

    st.header("Generate Articles 📰")

    # User input fields
    input_topic = st.text_input("Enter the Article Topic")
    col1, col2 = st.columns([5, 5])

    with col1:
        word_count = st.text_input('Number of Words')
    with col2:
        article_style = st.selectbox('Writing Style', 
                                     ('Academic', 'Professional', 'General Public'), 
                                     index=0)
        
    submit = st.button("Generate Article")

    # Article generation
    if submit:
        article_gen = ArticleGenerator()
        generated_article = article_gen.generate(input_topic, word_count, article_style)
        st.write(generated_article)

if __name__ == "__main__":
    main()
