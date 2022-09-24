import sys
from functions import (
    exec_commands,
    set_connection,
    bot
)
import vars


def run_stand_configuring_script(target_host, mount_path):
    ssh = set_connection(target_host)
    msg = exec_commands(ssh, монтирование_общего_ссд=f'sudo mount -t virtiofs {vars.ssd_name} {mount_path}',
                        проверка_устройства='df -T',
                        добавление_устройства_в_fstab=f'echo <имя устройства> {mount_path} virtiofs rw 0 0 >> /etc/fstab')
    if msg:
        bot.send_message(vars.tg_chat_id, msg)


if __name__ == '__main__':
    run_stand_configuring_script(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]))