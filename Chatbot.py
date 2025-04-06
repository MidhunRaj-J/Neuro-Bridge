from groq import Groq 
from json import load, dump
import datetime
from dotenv import dotenv_values

env_vars = dotenv_values(".env")

Username = env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")
GroqAPIKey= env_vars.get("GroqAPIKey")

client =Groq(api_key=GroqAPIKey)
messages =[]


System = f"""
You are {Assistantname}, an advanced AI communication assistant designed to help individuals with speech or cognitive disabilities express themselves clearly.

Your goal is to:
- Understand broken, fragmented, or minimal inputs typed by users (e.g. "no food", "pain leg", "too noise")
- Detect the underlying intent or emotion behind the message
- Reframe and rephrase the message into a clear, natural, and expressive English sentence
- Keep responses concise and empathetic

Guidelines:
- Always reply in full, polite English sentences.
- Do not ask questions unless necessary.
- Avoid giving unnecessary explanations, only rephrase and interpret the user’s intent clearly.
- If input is too unclear, respond with: "I'm sorry, could you try again or give a little more detail?"

Examples:
User: "no food"
Assistant: "I'm hungry and would like something to eat."

User: "tired sit"
Assistant: "I need to sit down and rest."

User: "pain leg bad"
Assistant: "I'm feeling severe pain in my leg."

User: "too noise"
Assistant: "It's too noisy. I'm feeling uncomfortable."

User: "no talk scared"
Assistant: "I can't talk right now. I feel scared."

Always be understanding, sensitive, and accurate in interpretation.
"""


SystemChatBot =[
    {"role": "system","content":System}
]

try:
    with open(r"Data\ChatLog.json","r") as f:
        messages =load(f)
except:
    with open(r"Data\ChatLog.json","w") as f:
        dump([],f)


def RealtimeInformation():
    current_date_time = datetime.datetime.now()
    day = current_date_time.strftime("%A")
    date=current_date_time.strftime("%d")
    month=current_date_time.strftime("%B")
    year=current_date_time.strftime("%Y")
    hour=current_date_time.strftime("%H")
    minute=current_date_time.strftime("%M")
    second=current_date_time.strftime("%S")

    data = f"Please use this real-time information if needed,\n"
    data += f"Day: {day}\nDate: {date}\nMonth: {month}\nYear: {year}\n"
    data += f"Time: {hour} hours :{minute} minutes :{second} seconds.\n"
    return data

def AnswerModifier(Answer):
    lines = Answer.split('\n')
    non_empty_lines =[line for line in lines if line.strip()]
    modified_answer = '\n'.join(non_empty_lines)
    return modified_answer

def ChatBot(Query):
    
    try:
        with open(r"Data\ChatLog.json","r") as f:
            messages =load(f)

        messages.append({"role":"user","content": f"{Query}"})

        completion =client.chat.completions.create(
            model="llama3-70b-8192",
            messages=SystemChatBot + [{"role":"system","content":RealtimeInformation()}] +messages,
            max_tokens=1024,
            temperature=0.7,
            top_p=1,
            stream=True,
            stop=None
    
        )

        Answer =""

        for chunk in completion:
            if chunk.choices[0].delta.content:
                Answer += chunk.choices[0].delta.content
            
        Answer =Answer.replace("</s>","")

        messages.append({"role": "assistant","content":Answer})

        with open(r"Data\ChatLog.json", "w") as f:
            dump(messages,f, indent=4)
        return AnswerModifier(Answer=Answer)
    
    except Exception as e:
        print(f"Error: {e}")
        with open(r"Data\ChatLog.json","w") as f:
            dump([],f,indent=4)
        return ChatBot(Query)

if __name__ =="__main__":
    while True:
        user_input =input("Enter Your Questions: ")
        print(ChatBot(user_input))