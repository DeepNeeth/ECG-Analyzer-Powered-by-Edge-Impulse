import serial
import os
import subprocess

# Set up the internal bridge to the STM32
# Note: Device path may vary; commonly /dev/ttyHS1 on Uno Q
ser = serial.Serial('/dev/ttyHS1', 115200, timeout=1)

def run_inference(file_path):
    print(f"--- Running Edge AI Inference on {file_path} ---")
    # Execute the Edge Impulse .eim model locally
    # Usage: ./model.eim <data_file>
    result = subprocess.run(['./model.eim', file_path], capture_output=True, text=True)
    print(result.stdout)

try:
    print("Starting ECG Data Capture...")
    while True:
        # Buffer 100 samples (roughly 1 second of data)
        samples = []
        for _ in range(100):
            line = ser.readline().decode('utf-8').strip()
            if line:
                samples.append(line)
        
        # Save to temporary file for the model to read
        with open('live_data.txt', 'w') as f:
            f.write('\n'.join(samples))
            
        run_inference('live_data.txt')

except KeyboardInterrupt:
    ser.close()
    print("Monitoring stopped.")
