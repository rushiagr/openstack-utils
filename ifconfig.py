# Use those functions to enumerate all interfaces available on the system using Python.
# found on <http://code.activestate.com/recipes/439093/#c1>
 
# Works with Python 2.7
# Python 3.3's 'socket' module takes care of many of the functionalities coded here 
 
import socket
import fcntl
import struct
import array
 
def all_interfaces():
    """
    Returns list of two-tuples of interface name and IP address (unformatted)
    Example:
    >>> all_interfaces()
    >>> [('lo', '\x7f\x00\x00\x01'), ('wlan0', '\xc0\xa8\x01\x90')]
    
    TODO: Merge this and get_interface_dict()
    """
    max_possible = 128  # arbitrary. raise if needed.
    all_bytes = max_possible * 32
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    names = array.array('B', '\0' * all_bytes)
    outbytes = struct.unpack('iL', fcntl.ioctl(
        s.fileno(),
        0x8912,  # SIOCGIFCONF
        struct.pack('iL', all_bytes, names.buffer_info()[0])
    ))[0]
    namestr = names.tostring()
    lst = []
    for i in range(0, outbytes, 40):
        name = namestr[i:i+16].split('\0', 1)[0]
        ip   = namestr[i+20:i+24]
        lst.append((name, ip))
    return lst
 
def format_ip(addr):
    """
    Example:
    >>> format_ip('\x7f\x00\x00\x01')
    >>> '127.0.0.1'
    """
    return str(ord(addr[0])) + '.' + \
           str(ord(addr[1])) + '.' + \
           str(ord(addr[2])) + '.' + \
           str(ord(addr[3]))

def get_interface_dict():
    ifaces = all_interfaces()
    iface_dict = {}
    for iface in ifaces:
        iface_dict[iface[0]] = format_ip(iface[1])
    return iface_dict

if __name__ == '__main__':
    print get_interface_dict()