from pypsexec.client import Client
import os
import time
import sys
import paramiko


primer_comando = "docker exec -it bowint_judiciales_int_1 bash"
segundo_comando = "cd /var/www/html/judiciales"
tercer_comando = "php bin/console judiciales:core:actualizar-avisos "
cuarto_comando = "php bin/console judiciales:core:procesar-avisos-pagados"


def conectarse():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("conectandomeee")
    ssh.connect(hostname='10.2.1.112', username='root', password='Factory.07')
    print('listo')
    shell = ssh.invoke_shell()
    shell.send(primer_comando + '\n')
    shell.send(segundo_comando + '\n')
    shell.send(tercer_comando + '\n')
    shell.send(cuarto_comando + '\n')
    ssh.close()


if __name__ == '__main__':
    conectarse()
