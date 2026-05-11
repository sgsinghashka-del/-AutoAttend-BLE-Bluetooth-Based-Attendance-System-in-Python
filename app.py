import asyncio
from bleak import BleakScanner
from datetime import datetime

TARGET_DEVICE_ADDRESS = "A4:4B:D5:51:D0:8D"  # replace with real address
device_detected = False

def detection_callback(device, advertisement_data):
    global device_detected

    if device.address.lower() == TARGET_DEVICE_ADDRESS.lower():
        if not device_detected:
            device_detected = True
            time_now = datetime.now().strftime("%H:%M:%S")

            print("ALERT!")
            print(f"Device detected: {device.address}")
            print(f"Time: {time_now}")

async def scan():
    print("📡 Scanning for device...\n")
    scanner = BleakScanner(detection_callback=detection_callback)
    await scanner.start()
    await asyncio.sleep(30)
    await scanner.stop()
    print("🛑 Scan stopped")

asyncio.run(scan())
