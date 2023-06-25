import socket, threading

DEFAULT = 0.5


def TCP_connect(ip, port_number, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, port_number))
        output[port_number] = 'Listening'
    except:
        output[port_number] = 'Occupied'


def scan_ports(host_ip, delay=DEFAULT):
    threads = []
    output = {}

    for i in range(10000):
        t = threading.Thread(target=TCP_connect,
                             args=(host_ip, i, delay, output))
        threads.append(t)

    for i in range(10000):
        threads[i].start()

    for i in range(10000):
        threads[i].join()

    for i in range(10000):
        if output[i] == 'Listening':
            print(str(i) + ': ' + output[i])


def main():
    ip = input("Enter host IP: ")
    delay = input("Enter timeout, or skip to use default: ")
    if len(delay) == 0:
        scan_ports(ip)
    else:
        scan_ports(ip, int(delay))


if __name__ == "__main__":
    main()
