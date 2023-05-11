import socket
import subprocess
from datetime import datetime


subprocess.call('clear', shell=True)


target = input("Enter the target IP address or hostname: ")


def port_scan(target):
    try:
   
        ip = socket.gethostbyname(target)


        print("-" * 50)
        print("Scanning target:", ip)
        print("Time started:", datetime.now())
        print("-" * 50)

        for port in range(1, 65635):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Set a timeout for the connection attempt
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("Port {}: Open".format(port))
            sock.close()

    except socket.gaierror:
        print("Hostname could not be resolved.")

    except socket.error:
        print("Could not connect to the server.")


port_scan(target)
