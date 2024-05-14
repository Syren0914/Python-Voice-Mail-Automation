# Voice-Controlled Email Sender

Voice-Controlled Email Sender is a Python script that allows you to send emails using voice commands. You can dictate the recipient, subject, and content of the email, and the script will send it for you.

## Features

- **Voice Recognition**: Utilizes the SpeechRecognition library to recognize voice commands.
- **Text-to-Speech**: Employs the pyttsx3 library to convert text to speech for interaction.
- **Email Sending**: Sends emails via SMTP using the smtplib library.
- **Environment Variables**: Utilizes environment variables for email credentials to enhance security.

## Requirements

- Python 3.x
- SpeechRecognition library (`pip install SpeechRecognition`)
- pyttsx3 library (`pip install pyttsx3`)
- dotenv library (`pip install python-dotenv`)

## Setup

1. Clone the repository or download the script.

2. Install the required libraries: pip install SpeechRecognition pyttsx3 python-dotenv



3. Create a `.env` file in the same directory as the script. Add your email credentials:

```plaintext
EMAIL=your_email@gmail.com
PASSWORD=your_email_password

```

Allow less secure apps access to your Gmail account if necessary.

Run the script: python voice_email_sender.py

Follow the instructions prompted by the script to send emails using voice commands.

Usage
Speak the name of the recipient to whom you want to send the email.
Dictate the subject of the email.
Speak the content of the email.
Confirm if you want to send more emails or exit the program.
Limitations
This script currently only supports sending emails via Gmail.
It might have limitations with recognizing certain accents or speech patterns.
The email account used must allow less secure apps access.
It's not secure to store the email password directly in a file, even if it's a .env file. Consider more secure options if deploying this in production.
Contributing
Contributions are welcome! If you have any improvements, bug fixes, or feature implementations, feel free to open an issue or create a pull request.




