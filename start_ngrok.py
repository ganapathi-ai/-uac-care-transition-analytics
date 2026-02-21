import os
import subprocess
import time


def main() -> None:
    authtoken = os.getenv("NGROK_AUTHTOKEN")
    if authtoken:
        subprocess.run(f"ngrok config add-authtoken {authtoken}", shell=True, check=False)
    else:
        print("NGROK_AUTHTOKEN is not set. Continuing without updating ngrok config.")

    print("Starting ngrok tunnel for Streamlit on port 8501...")
    subprocess.Popen("ngrok http 8501", shell=True)
    print("Open http://localhost:4040 to copy the public forwarding URL.")
    print("Keep this process running to keep the tunnel active.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping ngrok tunnel...")


if __name__ == "__main__":
    main()
