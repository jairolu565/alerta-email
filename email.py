import smtplib #módulo de e-mail do google
import os #módulo do cmd
import socket #módulo de ping TCP/UDP
from email.message import EmailMessage #módulo de envio de e-mail
from time import sleep #módulo de pause de script

#-----------testar a porta 80 no domínio python.org--------------
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('python.org',80))

iplist=['8.8.8.8','joaobelom.org'] #lista de ips a serem pingados no teste

#-----------estrutura do assunto do email--------------
SUBJECT = 'AVISO: QUEDA DE CONEXÃO'
TO = 'receberavisoo@gmail.com'
FROM = 'testedepingg@gmail.com'

msg=EmailMessage()
msg['Subject']='AVISO: QUEDA DE CONEXÃO'
msg['From']='Teste de ping'
msg['To']='receberavisoo@gmail.com'

#----------enviar email-------------
while True: #condição para loop infinito
    for ip in iplist:
        response = os.popen('ping ' + ip).read()
        if 'Recebidos = 4' in response: #se forem recebidos os 4 pacotes de volta
            print('O HOST: ', ip, 'ESTÁ ONLINE!')
        else: #se menos de 4 pacotes forem recebidos
            print('O HOST: ', ip, 'ESTÁ OFFLINE! UM E-MAIL DE AVISO SERÁ ENVIADO')
            msg.set_content('''A CONEXÃO COM O HOST ''' + ip + ''' FALHOU!''')
            servidor=smtplib.SMTP_SSL('smtp.gmail.com',465)
            servidor.login("testepingg@gmail.com","ravenclaw13")
            servidor.send_message(msg)
            servidor.quit()
    if result == 0:
        print ('A PORTA 80 NO HOST python.org ESTÁ ABERTA')
    else:
        print ('A PORTA 80 NO HOST python.org NÃO ESTÁ ABERTA')
    sock.close()               
# tempo em segundos para o loop ficar ocioso até voltar a rodar
    sleep(1)
    print("\n")