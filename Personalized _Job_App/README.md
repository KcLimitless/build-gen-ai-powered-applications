# Your Personalized Job Application Coach Based on LLM

Embark on a journey to master the integration of cutting-edge Large Language Models (LLM) into user-friendly applications. This project leverages the capabilities of **watsonx.ai** and **Gradio** to create practical, AI-driven tools for job seekers.

## Project Overview

This project provides hands-on experience in building advanced applications using LLM technology. We developed sample applications with **Gradio**, a framework for building machine learning interfaces, and the capabilities of **watsonx.ai**, utilizing its large language models to power real-world applications. 

In the project, three specialized tools to enhance the job application process was developed:
1. **AI-Driven Resume Enhancer**: Optimize resumes for better visibility and relevance.
2. **Personalized Cover Letter Generator**: Craft tailored cover letters for specific job applications.
3. **Strategic Job Hunting Advisor**: Receive expert advice on job search strategies, application tips, and career guidance.

## Getting Started

- I have included a jupyter notebook implementation: career_assistant.ipynb

### Prerequisites
- Basic understanding of Python programming.
- IBM Cloud account with access to **watsonx.ai** services.
- Familiarity with job application components (e.g., resumes, cover letters).
- watsonx_API 
- project_id 

```bash
pip install virtualenv 
virtualenv my_env # create a virtual environment named my_env
source my_env/bin/activate # activate my_env
```

```bash
# installing necessary pacakges in my_env
python3.11 -m pip install gradio==4.44.1 ibm-watson-machine-learning==1.0.349 email-validator==2.1.1 numpy==1.23.5 pandas==1.5.3
```
### Clone the Repository

```bash
git clone ...
cd the-repo-name
```
## Create a Q&A bot
Created a Q&A chatbot leveraging the llama-2-13b-chat model developed by Meta. This powerful foundation model has been seamlessly integrated into IBM's watsonx.ai platform and integrated into Gradio.

The following code in the llm_chat.py script shows this integration process. It includes three components:

- Initializing the model.
- Defining the function that generates responses from the LLM.
- Constructing the Gradio interface, enabling interaction with the LLM.

### Execute the code in the terminal to run the application:

'''
python3.11 simple_llm.py
'''
After it has excuted successfully, you will see message in the terminal with a url to display  the Gradio app.

## Resume polisher
create an LLM-based application tool that can help you to make your resume the best it can be. 
- It checks your resume, suggests improvements, and makes sure it shines.

#### Execute the script by entering the following command in the terminal:

'''
python3.11 resume_polisher.py
'''

Launch the gradio application by clicking the link provided in your terminal.

## Customized cover letter
This innovative tool based on LLMs is designed to help you write cover letters that not only highlight your unique skills and experiences but also tailor them to the specific job and the company you’re applying for. By inputting intended company, position, job description, and your resume, the generator will provide you with a cover letter that is both professional and personalized.

### In the terminal, run:

'''
python3.11 cover_letter.py
'''

Launch the gradio application by clicking the link provided in your terminal.

## Career advisor
Created a cool tool based on LLMs that helps with your career questions. All you need to do is put in the job you're interested in, what the job is about, and your resume. Our smart tool will look at all that and give you some solid advice on how to move forward in your career.

### In the terminal, run:

'''
python3.11 career_advisor.py
'''

Launch the gradio application by clicking the link provided in your terminal.

## Resources
- [IBM Watsonx Documentation](https://www.ibm.com/cloud/watsonx)
- [Gradio Documentation](https://gradio.app/)
- [Coursera Lab Page](https://www.coursera.org/learn/building-gen-ai-powered-applications/ungradedLti/mr4Il/lab-your-personalized-job-application-coach-based-on-llm)
























































































































































































































































































































































































































































































































































