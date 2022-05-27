

import win32com.client

def see_accounts():

    outlook = win32com.client.Dispatch('outlook.application')
    mapi = outlook.GetNamespace("MAPI")

    for account in mapi.Accounts:
        print(account.DeliveryStore.DisplayName)


if __name__ == '__main__':
    see_accounts()
    input()