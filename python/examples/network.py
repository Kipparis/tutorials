# function given data for transmit and if it have to wait for result
def handle_request(*items, wait_for_reply=True):
    SizeStruct = struct.Struct("!I")# holding unsigned integer in network byte
    data = picle.dumps(items, 3)    # last namber - pickle version
    
    try:
        with SocketManager(tuple(Address)) as sock:
            sock.sendall(SizeStruct.pack(len(data)))
            sock.sendall(data)
            if not wait_for_reply:
                return
            # get size of return
            size_data = sock.recv(SizeStruct.size)
            size = SizeStruct.unpack(size_data)[0]
            # fetch result with 4000 blocks
            result = bytearray()
            while True:
                data = sock.recv(4000)
                if not data:
                    break
                result.extend(data)
                if len(result) >= size:
                    break
        return pickle.loads(result)
    except socket.error as err:
        print("{0}: is the server running?".format(err))
        sys.exit(1)

