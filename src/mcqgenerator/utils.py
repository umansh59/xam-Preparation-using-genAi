import os
import traceback
import PyPDF2
import json

def read_file(file):
    """Reads the content from a PDF or text file and returns the text."""
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()  # Accumulate text from all pages
            return text  # Return the entire content after processing all pages
        
        except Exception as e:
            raise Exception('Error reading the PDF file') from e
    
    elif file.name.endswith(".txt"):
        return file.read().decode('utf-8')  # Read and decode text file content
    
    else:
        raise Exception(
            'Unsupported file format, only PDF and Text files are supported.'
        )


def get_table_data(quiz_str):
    """Extracts MCQs from the quiz string, converts it to a table-friendly format."""
    try:
        # Locate the JSON object in the string using curly braces
        start_index = quiz_str.find('{')
        end_index = quiz_str.rfind('}') + 1

        if start_index == -1 or end_index == -1:
            raise ValueError("The input string does not contain a valid JSON object.")

        # Extract and clean the JSON string
        json_str = quiz_str[start_index:end_index].strip()
        print(f"Extracted JSON string (first 500 chars): {json_str[:500]}")  # Log a portion of the string for debug

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
