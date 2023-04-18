# In[ ]:
import smtplib
import email.message

def enviar():
    estrutura = """
    <p>AQUI VAI A MENSAGEM A SER ENVIADA</p>
    <p>OU OS DADOS A SEREM ENVIADOS</p>
    """    
    msg = email.message.Message()
    msg ['Subject'] = input("Insira o assunto do E-MAIL: ")
    msg ['From'] = "alisson.cel.09@gmail.com"
    msg ['To'] = input("Digite o email de destino ex: seuemail@gmail.com ")
    password = 'izijbrfwsolsvktc'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(estrutura )
    
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    
    print("Seu Email foi enviado com sucesso!!!")



# In[ ]:

enviar()
# %%
