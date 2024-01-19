from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

class ArticleGenerator:
    def __init__(self):
        self.llm = CTransformers(model='src/models/llama-2-7b.ggmlv3.q8_0.bin',
                                 model_type='llama',
                                 config={'max_new_tokens': 256, 'temperature': 0.01})

    def generate(self, topic, word_count, style):
        prompt_template = """
            As an expert content writer, craft a comprehensive and engaging article tailored for a {style} audience. 
            Topic: '{topic}'.

            Introduction:
            Provide a captivating overview of the topic, setting the stage for what the reader can expect.

            Body:
            Delve into the key aspects of '{topic}', presenting facts, insights, and analysis in a coherent and logical manner. 
            Include relevant examples, anecdotes, or case studies to make the article more relatable and impactful for the {style} audience.

            Conclusion:
            Summarize the main points and provide a thoughtful closing remark.

            Guidelines:
            - Word Count: Approximately {word_count} words.
            - Tone: Informative, well-researched, resonating with the {style} audience.
            - Structure: Clear introduction, body, and conclusion.
            - Objective: Aim for clarity, precision, and a narrative that keeps the reader engaged from start to finish.
        """

        prompt = PromptTemplate(input_variables=["style", "topic", "word_count"],
                                template=prompt_template)
        
        response = self.llm(prompt.format(style=style, topic=topic, word_count=word_count))
        return response
