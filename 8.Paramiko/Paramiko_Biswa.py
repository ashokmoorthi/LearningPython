import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("172.17.240.11",port=22,username='idirect',password='iDirect')
stdin, stdout,stderr = ssh.exec_command('su -')
stdin, stdout,stderr = ssh.exec_command('iDirect')
stdin, stdout,stderr = ssh.exec_command('cd /tmp')
stdin, stdout,stderr = ssh.exec_command('ls -ltr')
output = stdout.readlines()
print('\n'.join(output))
stdin, stdout,stderr = ssh.exec_command('cd /root')
stdin, stdout,stderr = ssh.exec_command('ls -ltr')
output = stdout.readlines()
print('\n'.join(output))
stdin, stdout,stderr = ssh.exec_command('exit')
stdin, stdout,stderr = ssh.exec_command('mkdir /tmp/test')
stdin, stdout,stderr = ssh.exec_command('cd /tmp/test')
stdin, stdout,stderr = ssh.exec_command('cd ..')
stdin, stdout,stderr = ssh.exec_command('ls -ltr')
output = stdout.readlines()
print('\n'.join(output))
# stdin, stdout,stderr = ssh.exec_command('rm -rf test')
# testing push