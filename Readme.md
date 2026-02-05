Smart ECU: Edge AI Anomaly Detection

This project implements a lightweight Machine Learning model designed for embedded automotive applications. It simulates an Engine Control Unit (ECU) environment to detect engine misfires and RPM anomalies in real-time using an ESP32 microcontroller. The system leverages micromlgen to port a Python-trained Random Forest classifier into optimized C++ code for "bare metal" inference.
Project Workflow

The development process is divided into four distinct stages, moving from data simulation to embedded deployment.
1. Environment Setup & Dependencies

The project relies on a specific set of Python libraries for data processing and model porting.

    numpy: Used for numerical operations and signal generation.

    scikit-learn: utilized for training the Random Forest Classifier.

    micromlgen: A critical tool for transpiling the trained Python model into C++ code, enabling direct integration with the Arduino IDE / ESP32.

Bash

pip install micromlgen scikit-learn numpy

2. Synthetic Data Generation

Due to the unavailability of raw telemetry from a physical vehicle during the initial development phase, a synthetic dataset was constructed to simulate engine behavior.

    Normal Operation: Simulated using continuous sine waves to represent smooth acceleration and deceleration.

    Anomaly Injection: Gaussian noise and random "spike" values were injected into the signal to simulate engine knocking, misfires, or sensor glitches.

    Output: The script generates labeled CSV files (normal.csv and anomaly.csv) distinguishing between healthy and erratic RPM patterns.

3. Model Training & Anomaly Detection

A Random Forest Classifier is employed to distinguish between normal and anomalous engine states.

    Feature Extraction: The model analyzes raw RPM values and signal variance.

    Classification: It predicts whether the current engine state is "Safe" (0) or "Anomaly Detected" (1).

    Rationale: Random Forest was selected for its robustness against noise and low computational complexity, making it suitable for low-power microcontrollers.

4. Embedded Deployment (Porting to C++)

Once the model achieves satisfactory accuracy in Python, it is exported for hardware implementation.

    The trained classifier is serialized into a C++ header file (model.h) using the micromlgen library.

    This header file contains the hard-coded decision logic of the model.

    Integration: The model.h file is included in the main Arduino sketch (SmartECU.ino), allowing the ESP32 to perform local inference without external connectivity.

Usage Instructions

    Generate Data: Run the data simulation script to create the dataset.
    Bash

    python generate_dataset.py

    Train & Export: Train the classifier and generate the C++ header.
    Bash

    python model.py

    Deploy: Move the generated model.h file to your Arduino project folder and upload the firmware to the ESP32.
