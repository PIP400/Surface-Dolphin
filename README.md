# SURFING DOLPHIN PE v6.1.0
A Simple Hardware Specs Scanner

# How to Download & Run
1. Download: Download the project as a ZIP file from the GitHub repository.
2. Locate: The application exe.
3. Run: Double-click the executable to start the application.
4. Troubleshooting: If you encounter errors such as "STDN missing" or other startup issues, please follow the VS Code setup instructions below.

# Running via VS Code (Development Mode)
If the executable fails to run, you can launch the application directly using Python:
1. Setup: Open VS Code and ensure the Python extension is installed.
2. Import: Open the uncompressed "Surface Dolphin" folder in VS Code.
3. Terminal: Open a new terminal window within VS Code.
# Environment: Create a virtual environment by typing:
python -m venv venv
# Activation: Activate the virtual environment:
venv\Scripts\Activate
# Dependencies: Install the required libraries:
pip install psutil WMI pywin32 requests
# Updates: Ensure your package manager is up to date:
python.exe -m pip install --upgrade pip
# Launch: Start the application by typing:
python dolphin.py
# Operating live advisor
1. Launch: Run the application (either via .exe or python main.py).
2. Live Monitoring: Upon opening, the "Live Load" bars will immediately begin tracking your current CPU, RAM, and Storage usage in real-time.
3. Deep Audit: Click the RUN DEEP AUDIT button in the top-right corner.
4. Permissions: The program uses WMI (Windows Management Instrumentation) to talk to your hardware. Ensure you are running as an Administrator for the most accurate results.
5. Hardware Review: Scroll through the various sections:
6. Processor: Identify your exact socket type for future CPU upgrades.
7. Memory: View individual RAM slot data, including brand and speed (MHz).
8. Storage: Check if your drives are using high-speed NVMe or older SATA interfaces.
9. Advisor Tips: Read the yellow "ADVICE" text in each section. The program analyzes your current specs and suggests modern standards (e.g., suggesting 16GB of RAM for 2026 standards).
10: Note: Advisor Tips is not accurate, it was a test i didnt add a function to know what you should buy.
8. Tool: It run a deep audit to show few specs.
