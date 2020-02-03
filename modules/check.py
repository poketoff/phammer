from time import sleep
import socket, ipaddress, threading

max_threads = 50
final = {}
def check_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
        #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        socket.setdefaulttimeout(2.0) # seconds (float)
        result = sock.connect_ex((ip,port))
        if result == 0:
            # print ("Port is open")
            final[ip] = "OPEN"
        else:
            # print ("Port is closed/filtered")
            final[ip] = "CLOSED"
        sock.close()
    except:
        pass
port = 80
for ip in ipaddress.IPv4Network('192.168.1.0/24'):
    threading.Thread(target=check_port, args=[str(ip), port]).start()
    #sleep(0.1)

# limit the number of threads.
while threading.active_count() > max_threads :
    sleep(1)

print(final)