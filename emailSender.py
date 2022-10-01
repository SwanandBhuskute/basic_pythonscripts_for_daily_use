import smtplib
import ssl
import argparse

def sendEmail(Reciever, body):
     ctx = ssl.create_default_context()
     password = "jriajpwfcznsbhxy" #sender's app password
     sender = "riddheshpatil.jee@gmail.com"   #sender's mail ID
     receiver = Reciever
     message = body
     with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as server:
              server.login(sender, password)
              server.sendmail(sender, receiver, message)
     print("Mail sents successfully")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("reciever",type = str)
    parser.add_argument("message",type = str)

    args = parser.parse_args()
    sendEmail(args.reciever, args.message)
