import os 
import traceback
import PyPDF2
import json

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
                return text
        
        except Exception as e:
            raise Exception('Error reading the PDF file')
    
    elif file.name.endswith(".txt"):
        return file.read().decode('utf-8')
    
    else:
        raise Exception(
            'Unsupported file format only PDF and Text file supported.'
        )


def get_table_data(quiz_str):
    try:
        # Extract the JSON from the string by locating `{}` directly rather than searching for markdown syntax
        start_index = quiz_str.find('{')
        end_index = quiz_str.rfind('}') + 1

        if start_index == -1 or end_index == -1:
            raise ValueError("The input string does not contain a valid JSON object.")

        # Extract and clean the JSON string
        json_str = quiz_str[start_index:end_index].strip()
        print(f"Extracted JSON string: {json_str}")

        if not json_str:
            raise ValueError("The extracted JSON string is empty.")
        
        # Convert the JSON string to a Python dictionary
        quiz_dict = json.loads(json_str)
        quiz_table_data = []

        # Iterate over the quiz dictionary and extract the required information
        for key, value in quiz_dict.items():
            mcq = value.get('mcq', 'N/A')
            options = " \n ".join(
                [
                    f"{option} -> {option_value}" for option, option_value in value.get('options', {}).items()
                ]
            )
            correct = value.get('correct', 'N/A')
            quiz_table_data.append({'MCQ': mcq, 'Choices': options, 'Correct': correct})
        
        return quiz_table_data

    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        traceback.print_exception(type(e), e, e.__traceback__)
        return False 
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exception(type(e), e, e.__traceback__)
        return False
