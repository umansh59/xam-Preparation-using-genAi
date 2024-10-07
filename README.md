
# 📚 MCQ Generator Application with Langchain & Google Generative AI

[![Python Version](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/licenses/MIT)

## 📝 Description

The MCQ Generator is a Python application that generates multiple-choice questions (MCQs) using the powerful Langchain library and Google Generative AI (Gemini 1.5). This application allows users to create customized MCQs based on input text, making it suitable for various subjects and complexity levels. The interface, built with Streamlit, provides a seamless way to generate and review MCQs.

## 🎯 Features

- 📂 **File Upload**: Users can upload PDF or text files containing the input text for MCQ generation.
- 🎛️ **Customization**: Specify the number of MCQs, subject, and complexity level of questions.
- 🧠 **Advanced Natural Language Processing**: Leverages the Langchain library and Google Generative AI API for intelligent question generation.
- 📊 **Review Generated MCQs**: View and evaluate the generated MCQs in a table format within the Streamlit app.
- 📝 **Logging**: Logs application events to track errors and usage.

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Google Generative AI API key

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/umansh59/xam-Preparation-using-genAi
   cd mcqgen
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python3 -m venv env
   source env/bin/activate  # On Windows: `env\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the API key:
   - Obtain an API key from Google Generative AI.
   - Create a `.env` file in the project root directory.
   - Add the following line to the `.env` file:
     ```
     GOOGLE_GENAI_API_KEY=your_api_key_here
     ```

## 🏃‍♂️ Usage

1. Run the Streamlit application:
   ```
   streamlit run StreamlitAPP.py
   ```

2. Open your browser and navigate to `http://localhost:8501`.

3. Upload a PDF or text file containing the content for MCQ generation.

4. Set the desired number of MCQs, subject, and tone.

5. Click the "Create MCQs" button to generate the MCQs.

6. Review the MCQs in the Streamlit app and see the evaluation analysis.

## 📁 File Descriptions

- `StreamlitAPP.py`: Main script that runs the Streamlit app for the MCQ Generator.
- `mcqgenerator.py`: Script for generating and evaluating MCQs using Langchain and Google Generative AI.
- `utils.py`: Contains utility functions to read files and process the generated MCQs.
- `requirements.txt`: Lists all the required Python packages.



This application uses the [Langchain](https://github.com/hwchase17/langchain) library and [Google Generative AI API](https://cloud.google.com/ai/generative-ai) for natural language processing. We are grateful to the developers of these tools.


