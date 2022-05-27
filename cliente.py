from datetime import date
from send_email import send_mail

class Cliente():
    def __init__(self, email: list, nome_cliente: str, empresa: list, all_paths: list, assinatura: str):
        self.email = email
        self.nome_cliente = nome_cliente
        self.empresa = empresa
        self.assinatura = assinatura
        self.subject = self.generate_subject()
        self.texto = self.generate_text()
        self.paths = self.set_path(all_paths)
        self.paths = list(set(self.paths))
        self.data_envio = date.today().strftime("%Y-%m-%d")

    def to_dict(self):
        obj = {
            "recipients": self.email,
            "body": self.texto,
            "paths": self.paths,
            "subject": self.subject
        }
        return obj

    def to_tuple(self):
        email = str(self.email)[1:-1].replace("'", "").replace(', ', ' ')
        paths = str(self.paths)[1:-1].replace("'", '"').replace(', ', ' ')
        return email, self.subject, self.texto, paths, len(self.paths), str(self.empresa), len(self.empresa), self.data_envio

    def generate_text(self, mes=None, ano=None):
        if not mes:
            mes = date.today().strftime("%B").capitalize()

        if not ano:
            ano = date.today().year

        texto = f"<p>Bom dia,<br /> {self.nome_cliente}.<br /><br />Segue em anexo o boleto e a NFS-e referente ao honor&aacute;rio cont&aacute;bil da compet&ecirc;ncia {mes}/{ano}.<br /><br />Qualquer d&uacute;vida, fico &agrave; disposi&ccedil;&atilde;o.</p><br/>{self.assinatura}"
        return texto

    def generate_subject(self, mes=None, ano=None):
        if not mes:
            mes = date.today().strftime("%B").capitalize()

        if not ano:
            ano = date.today().year

        return f"HONORÁRIO CONTÁBIL {mes}/{ano}"

    def set_path(self, all_paths):
        files = []
        for f in self.empresa:
            files.extend(list(filter(lambda x: f in x, all_paths)))
        return files
