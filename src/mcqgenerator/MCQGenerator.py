import os
import json
import pandas as pd
import traceback
from dotenv import load_dotenv
from src.mcqgenerator.logger import logging

# Install the package if not already installed
# %pip install --upgrade --quiet langchain-google-genai

from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
# from langchain_core.chains import LLMChain, SequentialChain
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables
api_key = os.getenv('GOOGLE_GENAI_API_KEY')

# Initialize the LLM
llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=api_key)

# Define the prompt template for quiz generation
TEMPLATE = """
Text{text}
You are an expert MCQ maker. Given the above text, it is your job to \
create a quiz of {number} multiple choice questions for {subject} students in {tone} tone.
Make sure the questions are not repeated and verify all questions against the text.
Ensure to format your response like RESPONSE_JSON below and use it as a guide. \
Ensure to create {number} MCQs.
### RESPONSE_JSON
{response_json}
"""

quize_generation_prompt = PromptTemplate(
    input_variables=['text', 'number', 'subject', 'tone', 'response_json'],
    template=TEMPLATE
)

quiz_chain = LLMChain(llm=llm, prompt=quize_generation_prompt, output_key='quiz', verbose=True)

# Define the prompt template for quiz evaluation
TEMPLATE2 = """
You are an expert English grammarian and writer. Given a Multiple Choice Quiz for {subject} students,\
evaluate the complexity of the questions and provide a complete analysis of the quiz. Use at most 50 words for complexity analysis. 
If the quiz does not meet the cognitive and analytical abilities of the students,\
update the questions as needed and adjust the tone to better suit the students' abilities.
Quiz_MCQs:
{quiz}

Check by an expert English Writer of the above quiz:
"""

quize_evaluation_prompt = PromptTemplate(
    input_variables=['subject', 'quiz'], 
    template=TEMPLATE2
)

review_chain = LLMChain(llm=llm, prompt=quize_evaluation_prompt, output_key='review', verbose=True)

# Combine quiz_chain and review_chain into a single sequential chain
generate_evaluate_chain = SequentialChain(
    chains=[quiz_chain, review_chain], 
    input_variables=['text', 'number', 'subject', 'tone', 'response_json'],
    output_variables=['quiz', 'review'],
    verbose=True
)

# Example usage
