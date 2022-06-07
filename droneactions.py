import paramiko
import time
p = paramiko.SSHClient()
p.set_missing_host_key_policy(paramiko.AutoAddPolicy())   # This script doesn't work for me unless this line is added!
p.connect("192.168.43.24", port=22, username="pi", password="raspberry")
def startup():
    stdin, stdout, stderr = p.exec_command("pigs SERVO 17 1505")
    stdin, stdout, stderr = p.exec_command("pigs SERVO 22 1505")
    stdin, stdout, stderr = p.exec_command("pigs SERVO 27 1000")
    stdin, stdout, stderr = p.exec_command("pigs SERVO 18 1500")
    return 
def default():
    stdin, stdout, stderr = p.exec_command("pigs SERVO 17 1505")
    stdin, stdout, stderr = p.exec_command("pigs SERVO 22 1505")
    stdin, stdout, stderr = p.exec_command("pigs SERVO 27 1550")
    stdin, stdout, stderr = p.exec_command("pigs SERVO 18 1500")
    #stdin, stdout, stderr = p.exec_command("python ledon.py")
    opt = stdout.readlines()
    opt = "".join(opt)
    print(opt)
    return

def arm():
    stdin, stdout, stderr = p.exec_command("pigs SERVO 22 1000")
    time.sleep(1)
    stdin, stdout, stderr = p.exec_command("pigs SERVO 22 1500")
    time.sleep(1)
    return

def disarm():
    stdin, stdout, stderr = p.exec_command("pigs SERVO 22 2000")
    time.sleep(1)
    stdin, stdout, stderr = p.exec_command("pigs SERVO 22 1500")
    return

def up():
    stdin, stdout, stderr = p.exec_command("pigs SERVO 27 1580")
    return

def down():
    stdin, stdout, stderr = p.exec_command("pigs SERVO 27 1400")
    return

def left():
    stdin, stdout, stderr = p.exec_command("pigs SERVO 17 1450")
    return

def right():
    stdin, stdout, stderr = p.exec_command("pigs SERVO 17 1550")
    return

def front():
    stdin, stdout, stderr = p.exec_command("pigs SERVO 18 1520")
    return

def back():
    stdin, stdout, stderr = p.exec_command("pigs SERVO 18 1480")
    return

def gradup():
    for i in range(1155,1500,50):
        stdin, stdout, stderr = p.exec_command("pigs SERVO 27 " + str(i))
        time.sleep(1)
    return

def graddown():
    for i in range(1500,1100,-50):
        stdin, stdout, stderr = p.exec_command("pigs SERVO 27 " + str(i))
        time.sleep(0.01)
    return

def start():
    print("sehsfb")
    return

startup()
back()
    
