#!/usr/bin/env python
# encoding: utf-8
import paramiko


def get_server_log():
    hostname = ""
    port = 22
    username = ""
    password = ""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port, username, password, compress=True)
    remote_command = "tail -n100 /opt/xxx/logs/error_log"
    stdin, stdout, stderr = client.exec_command(remote_command)
    last_line = stdout.read()
    try:
        count = 0
        for line in last_line:
            if 'Traceback' in line:
                print(line)
                count = count + 1
        print(count)
    finally:
        last_line.close()


if __name__ == "__main__":
    get_server_log()

