import vars
import paramiko
import telebot

bot = telebot.TeleBot(vars.TG_API_TOKEN)


def mount_common_ssd():
    pass


def set_connection(target_host):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=target_host, username=vars.user, key_filename=vars.pkey)

    return ssh


def exec_commands(ssh, **commands):
    for command in commands:
        stdin, stdout, stderr = ssh.exec_command(commands[command])
        error = stderr.readlines()
        if len(error) > 0:
            print(error)
            return f'Ошибка при выполнении {command} на сервере балансера'
