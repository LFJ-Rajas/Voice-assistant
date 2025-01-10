fileopen=open("api.txt","r")
a=fileopen.read()
fileopen.close()

import openai #pip install openai
from dotenv import load_dotenv #pip install python-dotenv

openai.api_key = a
load_dotenv()

completion = openai.Completion()

def Reply(question, chat_log=None):
    filelog = open("chat_log.txt","r")
    chat_log_template = filelog.read()
    filelog.close()

    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}You : {question}\nJarvis : '
    response=completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty= 0)
    
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nYou : {question} \nJarvis : {answer}"

    filelog=open("chat_log.txt","w")
    filelog.write(chat_log_template_update)
    filelog.close()

    return answer