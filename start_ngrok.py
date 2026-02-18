import subprocess
import time
import os

# Set ngrok authtoken
authtoken = "39WWKz1t3uBHjAtQBmAJDaO8DFc_3evevEHLsKcnbFLcoCUS7"
subprocess.run(f"ngrok config add-authtoken {authtoken}", shell=True)

print("🚀 Starting Streamlit app...")
print("⏳ Please wait...")

# Start ngrok tunnel
print("\n🌐 Creating public URL with ngrok...")
subprocess.Popen("ngrok http 8501", shell=True)

time.sleep(3)

print("\n✅ Setup complete!")
print("\n📊 Your dashboard is now publicly accessible!")
print("\n🔗 To get your public URL:")
print("   1. Open: http://localhost:4040")
print("   2. Copy the 'Forwarding' URL (https://xxxx.ngrok.io)")
print("\n💡 Or run in another terminal: curl http://localhost:4040/api/tunnels")
print("\n⚠️  Keep this window open to maintain the tunnel")
print("\n🛑 Press Ctrl+C to stop")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n\n🛑 Shutting down ngrok tunnel...")
