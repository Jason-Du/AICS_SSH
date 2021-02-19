import paramiko
import os
username = "pi"
password = "raspberry"
hostname = "140.116.164.33"
port =2225

# COMMAMD EXE
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

except Exception:
    print ('Exception!!')
    raise
#SSH UPLOAD
try:
    t2 = paramiko.Transport((hostname, 2225))
    t2.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    LOCALPATH=os.path.join(os.path.dirname(__file__),"Desktop_Message.log")
    sftp.put(localpath=LOCALPATH, remotepath="Desktop_Message.log")
    # sftp.get(localpath="RASPBERRARY_MSEEAGE.txt", remotepath=os.path.join(os.path.dirname(__file__),"\RASPBERRARY_MSEEAGE.txt"))
    t2.close()
except Exception as e:
    print (e)
    raise
# SSH DOWNLOAD
try:
    t2 = paramiko.Transport((hostname, 2225))
    t2.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.get(localpath=os.path.join(os.path.dirname(__file__),"RASPBERRARY_MSEEAGE.log"), remotepath="RASPBERRARY_MSEEAGE.log")
    t2.close()
except Exception as e:
    print (e)
    raise