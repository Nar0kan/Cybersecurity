from email.header import Header
import smtplib
import time


def main():
    receiver = 'some@gmail.com'

    login = 'login'
    password = 'password'

    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(login, password)

    theme = "Hello."

    for i in range(5):
        header = 'To: ' + receiver + '\n' + 'From: ' + login + '\n' + 'Subject: ' + f"{theme + theme[-1]*i}" + '\n'
        print(header)
        message = header + '\nSimple gmail spammer, no worries.\n\n'

        smtpserver.sendmail(login, receiver, message)
        time.sleep(2)

    print('done!')
    smtpserver.quit()


if __name__ == "__main__":
    main()