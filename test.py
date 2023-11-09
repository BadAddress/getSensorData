import bluetooth

# 要连接的蓝牙设备的MAC地址
device_address = '48:E7:29:B6:76:7A'  # 用您要连接的设备的实际地址替换

try:
    # 创建一个BluetoothSocket对象
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    # 连接到设备
    sock.connect((device_address, 1))  # 第二个参数是通道号，通常为1

    # 发送数据
    while(1):
        sock.send("Hello, Bluetooth!")

    # 接收数据
    data = sock.recv(1024)
    print("Received:", data)

    # 关闭连接
    sock.close()
except Exception as e:
    print("Error:", str(e))

