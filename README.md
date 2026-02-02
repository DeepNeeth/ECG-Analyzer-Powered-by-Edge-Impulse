# ECG-Analyzer-Powered-by-Edge-Impulse
An Edge AI cardiac diagnostic gateway powered by the Arduino Uno Q and AD8232 ECG sensor. This project utilizes a heterogeneous architecture (STM32 + AARCH64) to perform local, real-time ECG morphology analysis and arrhythmia detection (AFib) via quantized neural networks—ensuring patient privacy and zero-latency processing

Key Features
Real-Time Processing: Detects heart irregularities instantly using the Uno Q’s dual-core power.

100% Privacy: All biometric data stays on the device—no cloud uploads, no data breaches.

Edge AI Engine: Uses a quantized CNN (Convolutional Neural Network) optimized for AARCH64.

Mission-Critical Reliability: Functions perfectly in network "dead zones" (airplanes, rural areas, etc.).

System Architecture :
1.This project utilizes a Heterogeneous Compute strategy to ensure maximum signal fidelity:

2.The Senses (STM32 MCU): The AD8232 sensor is sampled at 100Hz on the real-time core.

3.The Bridge: Data is passed via the high-speed internal serial link to the Linux core.

4.The Brain (AARCH64 MPU): The Linux core collects a 10-second "batch" and runs the model.eim inference.

1. Hardware Setup
Connect AD8232 OUTPUT to Uno Q Pin A0.

Connect GND and 3.3V.

Place electrodes in a standard 3-lead configuration (Right Arm, Left Arm, Left Leg).

2. Deployment
Flash the Sketch: Upload the sketch/ folder using the Arduino App Lab to the STM32 core.

Run the App: Launch the Python application via the App Lab dashboard.

Monitor: Watch the Linux console for real-time classification results.

The model was trained on the MIT-BIH Arrhythmia Database and quantized for edge performance.

Accuracy: 92%+ on AFib classification.

Inference Time: < 150ms on the Uno Q Linux core.

![device image](https://github.com/user-attachments/assets/8e30dc09-87fe-4653-8683-5b467ef59c83)

