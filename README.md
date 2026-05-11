AutoAttend BLE is a Python-based automated attendance tracking system that uses Bluetooth Low Energy (BLE) to mark attendance when registered devices are detected nearby. The program continuously scans for predefined Bluetooth device MAC addresses and records attendance once per day per device, ensuring accuracy and preventing duplicate entries.

Built using the Bleak library and Python’s asynchronous programming model, this project demonstrates a real-world application of proximity-based automation and BLE scanning.

✨ Key Features
Automatic attendance marking using Bluetooth MAC address detection
Prevents duplicate attendance entries for the same day
Supports multiple registered devices
Real-time timestamp logging
Asynchronous and efficient BLE scanning
Simple and extensible code structure


🛠️ Technologies Used
Python
Bleak (Bluetooth Low Energy scanning)
Asyncio
Datetime


📌 Use Cases
Classroom or training attendance systems
Office employee presence tracking
Contactless attendance solutions
IoT and Bluetooth learning projects


🚀 How It Works
Maintains a list of registered Bluetooth device MAC addresses
Scans nearby BLE devices asynchronously
Matches detected devices with registered entries
Mark's attendance is once per day per device
Displays attendance confirmation with a timestamp


⚠️ Important Notes
Works only with Bluetooth Low Energy (BLE) devices
MAC address detection is more reliable than device name detection
Bluetooth permissions must be enabled on the operating system
Classic Bluetooth devices (e.g., speakers, headphones) are not supported
