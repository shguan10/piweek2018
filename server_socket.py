import io
import socket
import _thread
import struct
import tempfile
import datetime
import pathlib
from db_ops import update_django


def on_new_client(conn, addr):
    connection = conn.makefile('rb')
    directory = tempfile.TemporaryDirectory()
    user_id = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
    print(directory)
    print(user_id)

    while True:
        # Read the length of the image as a 32-bit unsigned int. If the length is zero, quit the loop
        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        if not image_len:
            break
            
        dt = datetime.datetime.now()
        file = directory.name + "/" + dt.strftime("%s")
               
        # Construct a stream to hold the image data and read the image data from the connection
        with open(file, 'wb') as file_stream:
            file_stream.write(connection.read(image_len))

    # Hit the Tensor

    # Update DB (uncomment below line)
    # update_django(item_name, is_insert, user_id)

    connection.close()


# Start a socket listening for connections on 0.0.0.0:8000
server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)

try:
    while True:
        conn, addr = server_socket.accept()
        _thread.start_new_thread(on_new_client, (conn, addr))
        
finally:
    server_socket.close()
