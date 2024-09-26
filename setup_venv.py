import os
import subprocess
import sys

venv_path = ".venv"

print(f"Creating virtual environment at '{venv_path}'...")
subprocess.run([sys.executable, "-m", "venv", venv_path], check=True)

pip_executable = os.path.join(venv_path, "bin", "pip") if os.name != "nt" else os.path.join(venv_path, "Scripts", "pip")

if os.path.isfile("requirements.txt"):
    print("Installing dependencies from requirements.txt...")
    subprocess.run([pip_executable, "install", "-r", "requirements.txt"], check=True)
    print("Dependencies installed successfully.")
else:
    print("No requirements.txt file found. Skipping installation.")

print("Setup completed successfully.")
print("Run the following command to activate it\n\tsource .venv/bin/activate\n")
print("If you want to deactivate, simply run\n\tdeactivate")
