import json
import traceback
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
from langchain_community.callbacks import get_openai_callback
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain
from src.mcqgenerator.logger import logging

# Load the environment variables
load_dotenv()

# Load the JSON file
try:
    with open('Response.json', 'r', encoding='utf-8') as file:
        RESPONSE_JSON = json.load(file)
        print("Loaded RESPONSE_JSON:", RESPONSE_JSON)  # Debugging: Print the loaded JSON
except Exception as e:
    print(f"Error loading JSON file: {e}")
    RESPONSE_JSON = {}

# Create a title for the app
st.title('MCQ Generator Application with Langchain')

# Create a form using st.form
with st.form('user_inputs'):
    # File upload
    uploaded_file = st.file_uploader('Upload a PDF or txt file')

    # Input fields
    mcq_count = st.number_input('No. of MCQs.', min_value=3, max_value=50)
    subject = st.text_input('Insert Subject', max_chars=40)
    tone = st.text_input('Complexity Level of Questions', max_chars=20, placeholder='Simple')

    # Add button
    button = st.form_submit_button('Create MCQs')

    # Check if the button is clicked and all fields have input
    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner('Loading...'):
            try:
                text = read_file(uploaded_file)
                print("File content:", text)  # Debugging: Print the file content

                # Count tokens and the cost of API call
                with get_openai_callback() as cb:
                    response = generate_evaluate_chain({
                        'text': text,
                        'number': mcq_count,
                        'subject': subject,
                        'tone': tone,
                        'response_json': json.dumps(RESPONSE_JSON)
                    })
                
                print(f"Total Tokens: {cb.total_tokens}")
                print(f"Prompt Tokens: {cb.prompt_tokens}")
                print(f"Completion Tokens: {cb.completion_tokens}")
                print(f"Total Cost: {cb.total_cost}")
                print("API response:", response)

                if isinstance(response, dict):
                    quiz = response.get('quiz', None)
                    if quiz is not None:
                        try:
                            print("Received JSON string:", quiz)
                            table_data = get_table_data(quiz)
                            print(table_data)
                            print("Table data:", table_data)
                            if table_data:
                                df = pd.DataFrame(table_data)
                                df.index = df.index + 1
                                st.table(df)
                                st.text_area(label='Review', value=response.get('review', ''))
                            else:
                                st.error('Error in the table data.')
                        except Exception as e:
                            st.error(f"Error processing table data: {e}")
                    else:
                        st.error('Quiz data not found in response.')
                else:
                    st.write(response)
            except Exception as e:
                st.error(f"Error during processing: {e}")