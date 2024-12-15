import os, shutil
import subprocess
import time

def check_dependencies():
    #Ensure required tools (QEMU/Android emulator) are installed.
    required_tools = ["qemu-system-x86_64", "adb"]
    for tool in required_tools:
        if not shutil.which(tool):
            raise EnvironmentError(f"Required tool {tool} is not installed.")

def start_virtual_android():
    """Start a virtual Android system using QEMU."""
    android_img = "C:/Users/Harsh/AppData/Local/Android/system-images/android-34/default/x86_64/system.img"  #Use your OWN android system image path
    if not os.path.exists(android_img):
        raise FileNotFoundError(f"Android image file '{android_img}' not found.")

    qemu_command = [
        "qemu-system-x86_64",
        "-avd", "test_avd_1",  #Use your OWN avd name 
        "-no-snapshot",
        "-qemu",
        "-m", "2048",  
        "-cpu", "host",
    ]

    process = subprocess.Popen(qemu_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(30)  # Offset the boot time for the emulator
    return process

def install_apk(apk_path):
    """Install an APK file into the virtual Android system using adb."""
    if not os.path.exists(apk_path):
        raise FileNotFoundError(f"APK file '{apk_path}' not found.")

    install_command = ["adb", "install", apk_path]
    result = subprocess.run(install_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(f"Successfully installed APK: {apk_path}")
    else:
        raise RuntimeError(f"Failed to install APK. Error: {result.stderr.decode()}")

def retrieve_system_info():
    """Retrieve and log system information from the Android system."""
    commands = {
        "OS Version": ["adb", "shell", "getprop", "ro.build.version.release"],
        "Device Model": ["adb", "shell", "getprop", "ro.product.model"],
        "Available Memory": ["adb", "shell", "free", "-h"]
    }

    info = {}
    for key, cmd in commands.items():
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            info[key] = result.stdout.decode().strip()
        else:
            info[key] = "Error retrieving information"

    for key, value in info.items():
        print(f"{key}: {value}")

    with open("system_info.log", "w") as log_file:
        for key, value in info.items():
            log_file.write(f"{key}: {value}\n")

    print("System information logged in 'system_info.log'.")

def main():
    try:
        check_dependencies()
        process = start_virtual_android()
        print("Virtual Android system launched.")
        apk_path = "webtoon.apk" #This is a test apk file, you can use whatever you want to.
        install_apk(apk_path)

        retrieve_system_info()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        input("Press Enter to terminate the virtual Android system...")
        process.terminate()
        print("Virtual Android system terminated.")

if __name__ == "__main__":
    main()
