1. Installation
		**Python dependencies**:
			- Pyvisa
			**Code:**
				`pip install PyVISA` 
			PyVISA is a Python package that enables you to control all kinds of measurement devices independently of the interface (e.g. GPIB, RS232, USB, Ethernet).
			- pyvisa-py
			**Code:**
				`pip install pyvisa-py`
			PyVISA-py is **a backend for PyVISA**. It implements most of the methods for Message Based communication (Serial/USB/GPIB/Ethernet) using Python and some well developed, easy to deploy and cross platform libraries.
			 - psutil
			**Code:**
				`pip install psutil`
			psutil (process and system utilities) is a cross-platform library for retrieving information on **running processes** and **system utilization** (CPU, memory, disks, network, sensors) in Python.
			- zeroconf
			Code:
				`pip install zeroconf`
			A pure python implementation of multicast DNS service discovery.
2. Usage
		**Establish communication (TCP/IP):**
			+ port number: 8462
			+ Ip address: 10.0.0.165
			Combining both components, we can form a unified address format: `TCPIP0::10.0.0.165::8462::SOCKET`. This address includes the following elements:
						- Protocol: TCPIP0
						- IP Address: 10.0.0.165
						- Port: 8462
						- Socket Type: SOCKET
			+ Using the PyVISA library, you can establish a connection to an external power supply through the TCP/IP protocol.
			Code:
			```rm = pyvisa.ResourceManager() 
			dev = 'TCPIP0::10.0.0.165::8462::SOCKET'
			session = rm.open_resource(dev)
			```
3. Critical Data's
			- Voltage
			- Current
			- Power
			- Time
4. Commands (SM15000):
			**Write Data:**
						<NR2 - floating point: 3.22, 0.06, etc.... >
						- Set time:
				``session.write('SYSTem:TIMe 11,33,0')``
						- Set current:
				``session.write('SOURce:CURrent <NR2>')`` 
						- Set voltage:
				`` session.write('SOURce:VOLtage <NR2>')``
						- Set power:
				``session.write('SOURce:POWer <NR2>')``
			**Read Data:**
						- Read time:
				``session.query('SYSTem:TIMe?')``
						- Read current:
				``session.query('MEASure:CURrent?')``
						- Read voltage:
				``session.query('MEASure:VOLtage?')``

			
		