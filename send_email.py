import win32com.client as win32


def send_mail(sender, **email):
    outlook_app = win32.Dispatch('Outlook.Application')

    # choose sender account
    send_account = None
    for account in outlook_app.Session.Accounts:
        if account.SmtpAddress == sender:
            send_account = account
            break

    mail_item = outlook_app.CreateItem(0)   # 0: olMailItem

    # mail_item.SendUsingAccount = send_account not working
    # the following statement performs the function instead
    mail_item._oleobj_.Invoke(*(64209, 0, 8, 0, send_account))

    for em in email['recipients']:
        mail_item.Recipients.Add(em)
    
    mail_item.Subject = email['subject']
    mail_item.BodyFormat = 2   # 2: Html format
    mail_item.HTMLBody = email['body']

    if email['paths']:
        for path in email['paths']:
            mail_item.Attachments.Add(path)

    print(f"Enviado emails para {email['recipients']}")
    mail_item.Send()


if __name__ == '__main__':
    email = {'subject':'teste', 'recipients':['usa30-0@hotmail.com'], 'paths':[], 'body':''}
    send_mail(sender='gmail', **email)
