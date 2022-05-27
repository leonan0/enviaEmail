from see_accounts import see_accounts
import json

assinatura = "<br/><p><strong>Att.</strong></p><p><strong>Gabriela Andreoli Pedro</strong><strong> <br/strong>Departamento Financeiro <br/><img src=\"https://raw.githubusercontent.com/leonan0/files/main/logoacn.jpg\" alt=\"\" /> <br/>Avenida Rio de Janeiro, 1765 &ndash; Londrina/PR <br/>Telefone: (43) 3324-4373 <br/>E-mail:&nbsp;<a href=\"mailto:office01@acncon.com.br\">financeiro@acncon.com.br</a></p>"


caminho_raiz_anexos = input("Qual o caminho da raiz dos anexos?\n")

planilha_base = input("Qual o caminho da planilha base?\n")
if input("Quer ver as contas disponiveis?\n") == "s":
    print(see_accounts())


email_de_envio = input("Qual o email de envio?\n")

paths_finais = input("Quais os paths finais dos anexos?\n")

config = {'caminho_raiz_anexos': caminho_raiz_anexos,
          'paths_finais':paths_finais,
          'email_de_envio':email_de_envio,
          'planilha_base':planilha_base,
          'assinatura':assinatura
}

with open('config.json', 'w') as f:
    json.dump(config, f, indent=2)

print(config)
input()