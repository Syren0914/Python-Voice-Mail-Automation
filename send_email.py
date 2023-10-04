
import os
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv, dotenv_values




load_dotenv()

Sending_email = os.environ.get("EMAIL")
email_password = os.environ.get("PASSWORD")
PORT = 587
EMAIL_SERVER = "smtp.gmail.com"


listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()



def get_info():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass








def send_email(receiver, subject, content):
    
    

    server =  smtplib.SMTP(EMAIL_SERVER, PORT)
    server.starttls()
    server.login(Sending_email,email_password)

    email = EmailMessage()
    email["From"] = Sending_email
    email["To"] = receiver
    email["Subject"] = subject
    email["BCC"] = "Syren0914"
    email.set_content(content)
    server.send_message(email)


email_list = { "programmer":"erdenebatbayar5@gmail.com",
              "dude":"erdenebatbayar5@gmail.com",
                "girlfriend":"erdenebatbayar5@gmail.com",

}



def get_email_info():
    talk("Who do you want to send email ?")
    name =get_info()
    receiver = email_list[name]
    print(receiver)
    talk("What is the Subject of your email?")
    subject = get_info()
    talk("Tell me the text in your email?")
    content = get_info()


    send_email(receiver, subject, content)
    talk("The Email was sent succesfully ")
    talk("Do you want to write a another email ?")
    send_more = get_info()
    if "yes" in send_more:
        get_email_info()
    else:
        talk("Thank you for using our service")





get_email_info()
