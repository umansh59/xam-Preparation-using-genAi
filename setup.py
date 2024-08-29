from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Umansh Bansal',
    author_email='umansh5959@gmail.com',
    install_requirement = ['openai','langchain','streamlit','python-dotenv','PyPDF'],
    packages=find_packages()
)