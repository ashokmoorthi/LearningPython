import paramiko
import time
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.56.101",port=22,username='bak',password='iDirect')
shell = ssh.invoke_shell()

shell.send("sudo bash\n")
# stdin, stdout, stderr = ssh.exec_command(
#     "sudo dmesg")
# stdin.write('lol\n')

time.sleep(1)
shell.send("iDirect\n")
time.sleep(1)
shell.send("cd /tmp/ \n")
shell.send("ls -ltr\n")
time.sleep(1)
shell.send("cd /root/ \n")
shell.send("ls -ltr\n")
time.sleep(1)
shell.send("mkdir -p /tmp/test\n")
time.sleep(1)
shell.send("cd /tmp/test/\n")
time.sleep(1)
shell.send("cd .. \n")
# shell.send("mkdir test\n")
# time.sleep(1)
# shell.send("cd test\n")
shell.send("pwd\n")
shell.send("rm -rf test\n")
time.sleep(1)

output = ''
log = open("C:\\python_test\\abc.txt","w")
# time.sleep(1)
while not shell.recv_ready():
    time.sleep(2)
output = shell.recv(9999)
# if shell.recv_ready():
#     output = shell.recv(9999)
# print(output)
for ln in output.decode("utf-8").split('\n'):
    print (ln)
    log.writelines(ln)

shell.close()
ssh.close()
log.close()
# #time.sleep(1)
# shell.send("ls -ltr \n")
# time.sleep(1)
# while not shell.recv_ready():
#     time.sleep(2)
# results = ''
# while shell.recv_ready():
#     results = results + shell.recv(1).decode("utf-8")
# # shell.send("su -n")
# # shell.send("su -n")
# print(results)
# test
