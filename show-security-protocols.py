import subprocess

def show_security_protocols():
    try:
        # اجرای دستور netsh برای نمایش وضعیت فایروال
        result = subprocess.run("netsh advfirewall show allprofiles", shell=True, capture_output=True, text=True)
        
        if result.stdout:
            print("Firewall settings and security protocols:")
            print(result.stdout)
        else:
            print("No security protocols found or no output.")
    
    except Exception as e:
        print(f"Error while fetching security protocols: {e}")

if __name__ == "__main__":
    show_security_protocols()
