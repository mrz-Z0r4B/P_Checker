# Password_Strength_Checker

**Password_Strength_Checker** is a powerful Python-based tool designed to assess the strength of passwords in real-time. Built with a modern graphical user interface using Tkinter, this application evaluates passwords based on various criteria, including length, the inclusion of uppercase and lowercase letters, numbers, and special characters. It provides users with instant feedback and suggestions to enhance password security.

## Features
- Real-time password strength evaluation
- Color-coded visual strength meter
- Feedback and suggestions for creating stronger passwords
- Dark-themed user interface for enhanced visibility
- Uses **zxcvbn** for accurate password strength analysis

## Installation Instructions

### Step 1: Clone the Repository
Clone the repository using the following command:
```bash
git clone https://github.com/mrz-Z0r4B/P_Checker.git
cd P_Checker
```

### Step 2: Install Dependencies
Ensure that Python is installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/). Follow the instructions for your operating system.

- For **Tkinter** (if not included with your Python installation):
  - **Ubuntu/Debian**:
    ```bash
    sudo apt-get install python3-tk
    ```
  - **Windows**: Tkinter is usually included with Python installations.

- To install **zxcvbn**, run the following command:
  ```bash
  pip install zxcvbn
  ```

### Step 3: Run the Application
You can run the application using the following command:
```bash
python P_Checker.py
```

### Step 4: Test Password Strength
Once the application is running, enter passwords into the interface to check their strength. The tool will provide instant feedback on how to improve your password.

## Contributing
If you would like to contribute to this project, please feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
