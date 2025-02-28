import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from apscheduler.schedulers.background import BackgroundScheduler

def send_email(subject, body, to_email):
    from_email = "ton_email@gmail.com"
    password = "ton_mot_de_passe"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

def job():
    send_email("Rappel", "Il est temps de mettre à jour votre projet", "responsable@example.com")

# Planification du job pour envoyer un e-mail tous les 15 jours
scheduler = BackgroundScheduler()
scheduler.add_job(job, 'interval', days=15)
scheduler.start()
