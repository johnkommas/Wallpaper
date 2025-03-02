import asyncio
import aioping
import os
import time
import pandas as pd
from Files import minimalist_write
# from dotenv import load_dotenv
#
# load_dotenv()


async def ping(name, ip, retries=2, timeout=1):
    """Ping a device and return status with response time, with retries."""
    last_exception = None
    for _ in range(retries):
        try:
            start = time.time()
            await aioping.ping(ip, timeout=timeout)  # Increased timeout
            end = time.time()
            response_time = (end - start) * 1000  # Convert to milliseconds
            return {
                "Device": name,
                "IP": ip,
                "Status": "Alive",
                "Response Time (ms)": round(response_time, 2),
            }
        except TimeoutError:
            last_exception = "Timeout"
        except Exception as e:
            last_exception = str(e)

    # After retries, if still down, return as down
    return {
        "Device": name,
        "IP": ip,
        "Status": "Down",
        "Response Time (ms)": None,
        "Error": last_exception,
    }


async def check_devices():
    """Ping all devices asynchronously and store results in a DataFrame."""
    # Define device names and fetch IPs from environment variables
    device_mapping = {
        "A": os.getenv("RETAIL_PC_A"),
        "B": os.getenv("RETAIL_PC_B"),
    }

    # Remove None values in case an environment variable is missing
    devices = {name: ip for name, ip in device_mapping.items() if ip}

    results = await asyncio.gather(*[ping(name, ip) for name, ip in devices.items()])
    return pd.DataFrame(results)  # Convert results to a DataFrame and return it


# Run every 10 minutes
async def main(images, path):
    df = await check_devices()
    # print(df)
    PCA = df.loc[df["Device"] == "A", "Status"].values[0]
    PCB = df.loc[df["Device"] == "B", "Status"].values[0]

    def handle_image(path, status, offset, image):
        path_a = f"{path}/switch-on.png" if status == 'Alive' else f"{path}/switch-off.png"
        box_ = (2250 + offset, 1950)
        image = minimalist_write.paste_image(image, path_a, box_, resize=2)

    for image in images:
        # Εικόνα για pos_a
        handle_image(path, PCA, 0, image)
        # Εικόνα για pos_b
        handle_image(path, PCB, 1550, image)


def run(images, path):
    print("Running Network Devices Check", end='')
    asyncio.run(main(images, path))

