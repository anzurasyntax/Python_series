# 1) import - using Python modules
# Python has built-in modules you can use
import math

print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)

# You can also import only specific things
from math import ceil, floor

print("Ceil of 3.2:", ceil(3.2))
print("Floor of 3.8:", floor(3.8))

print("-" * 40)

# 2) pip - install external libraries
# Example (run in terminal, not in Python file):
# pip install requests

# Using installed library example
import requests

response = requests.get("https://api.github.com")
print("GitHub API Status Code:", response.status_code)

print("-" * 40)

# 3) Virtual Environments (basic idea)
# Run in terminal (not Python file):
# python -m venv myenv   -> creates a new virtual environment
# source myenv/bin/activate  -> activate (Linux/Mac)
# myenv\Scripts\activate     -> activate (Windows)
# pip install <package>      -> install packages inside env
# deactivate                 -> exit virtual environment

print("Virtual environments help keep project libraries separate.")
