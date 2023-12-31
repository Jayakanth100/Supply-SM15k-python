import pyvisa
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('10.0.0.165', 8462))
# s.sendall('*IDN?\n'.encode())
try:
    rm = pyvisa.ResourceManager()
    # print(rm.list_resources())
    print(rm.list_resources())
    dev = 'TCPIP0::10.0.0.165::8462::SOCKET'
    session = rm.open_resource(dev)
    print("\nOpen successful")
    session.read_termination = '\n'
    session.write_termiantion = '\n'
#   print("IDN:" + str(session.query('*IDN?')))
#   print("Maximum voltage: " + session.query('SOURce:VOLtage:MAXimum?'))
#   session.write('SOURce:VOLtage 1.2')
#   print("The voltage is : " + str(session.query('SOURce:VOLtage?')))

    session.write('SYSTem:COMmunicate:LOGging ETH,RX,ON')
    session.write('SYSTem:COMmunicate:LOGging ETH,TX,ON')
    print("RX: " + session.query('SYSTem:COMmunicate:LOGging ETH,RX?'))
    print("TX: " + session.query('SYSTem:COMmunicate:LOGging ETH,TX?'))
    session.write('SYSTem:COMmunicate:LOGging ETH,EXCLUDE,ON')
    print("Excluded: " + str(session.query('SYSTem:COMmunicate:LOGging ETH,EXCLUDE?')))

   #hour = currentTime.hour
   #minute = currentTime.minute
   #second = currentTime.second
    #session.write('SYSTem:TIMe 11,33,0')#set the current time
    # session.write('SYSTem:COMmunicate:LOGging ETH,CLEAR') #This command is use for clearing the log file
    
    print("Current time: " + str(session.query('SYSTem:TIMe?')))
    #writing phase
    # session.write('SOURce:VOLtage 1.4')
    # session.write('SOURce:CURrent 0.1')
    # session.write('SOURce:POWer 0.1')

    # print("Start time: " + str(session.query('SYSTem:TIMe?')))
    #reading phase
    for i in range(100):
        print(str(session.query('SYSTem:TIMe?')) + str(session.query('MEASure:CURrent?')) + str(session.query('MEASure:VOLtage?')) )
        print("\n")
        # print("Power : " + str(session.query('MEASure:POwer?')))
    # print("End time: " + str(session.query('SYSTem:TIMe?')))
    print("The excluded content: " + str(session.query('SYSTem:COMmunicate:LOGging ETH,READ?')))

except Exception as e:
    print('[!] Exception: ' + str(e))