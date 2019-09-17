import socket,json

HOST, PORT = '127.0.0.1', 7777

listen_socket = socket.socket(socket.AF_INET,
                              socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET,
                         socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(3)
print('Serving HTTP on port %s ...' % PORT)
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print(request)
    test_dict = {'a':"a"}
    json_response= json.dumps(test_dict,ensure_ascii=False)
    http_response = b"""
	HTTP/1.1 200 OK
    Access-Control-Allow-Origin:http://127.0.0.1:7777
	"""
    b_json_response= bytes(json_response,encoding='utf8')
    print(b_json_response,'sfssfs')
    client_connection.send(http_response+b_json_response)
    client_connection.close()
