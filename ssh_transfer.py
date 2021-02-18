import paramiko
import os
username = "pi"
password = "raspberry"
hostname = "140.116.164.33"
port =2225

try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port, username, password)
    t = client.get_transport()
    # sftp=paramiko.SFTPClient.from_transport(t)
    # d = sftp.stat("/Users/allen/Dropbox/python/ssh.txt")
    # print (d)
    stdin, stdout, stderr=client.exec_command('source test.sh')
    # stdin, stdout, stderr = client.exec_command('ls -al')
    result = stdout.readlines()
    print (result)
    print(os.path.dirname(__file__))

except Exception:
    print ('Exception!!')
    raise
try:
    t2 = paramiko.Transport((hostname, 2225))
    t2.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    # sftp.put(localpath='sentfromdesktop.txt', remotepath=os.path.join(os.path.dirname(__file__),"\sentfromdesktop.txt"))
    sftp.get(localpath='sentfromdesktop.txt', remotepath=os.path.join(os.path.dirname(__file__),"\sentfromdesktop.txt"))
    t2.close()
except Exception as e:
    print (e)
    raise
