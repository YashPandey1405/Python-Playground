# Flask Backend Setup Guide

Flask is a lightweight and flexible web framework for Python. It is widely used for building web applications, RESTful APIs, and microservices. Flask is easy to set up and allows developers to focus on writing code rather than dealing with complex configurations.

## Flask Features and Uses

- **Lightweight and Minimalistic**: Flask is designed to be simple and easy to extend.
- **RESTful API Development**: Flask is ideal for building REST APIs.
- **Flexible**: It doesn’t enforce any particular project structure or dependencies.
- **Wide Ecosystem**: Flask supports extensions for database integration, authentication, and more.

Use Flask for:

- Building web applications
- Developing APIs for mobile or web apps
- Creating prototypes and MVPs (Minimum Viable Products)

---

## Steps to Set Up Flask

### 1. Open VS Code and Set Up the Virtual Environment

Create a virtual environment to isolate your project dependencies.

```bash
python -m venv flask<name>
```

### 2. Activate the Virtual Environment

Activate the virtual environment to start using it for your project.

```bash
flask<name>/scripts/activate
```

#### If the above command doesn’t work, follow these steps:

1. Check the current execution policy:
   ```bash
   Get-ExecutionPolicy
   ```
2. Temporarily bypass the execution policy:
   ```bash
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```
3. Activate the virtual environment:
   ```bash
   .\flask<name>\Scripts\Activate
   ```

### 3. Install Flask

Install Flask using pip, the Python package manager.

```bash
pip install flask
```

### 4. Verify the Directory

Ensure you’re in the correct project directory.

```bash
ls
```

### 5. Create and Run Your Flask App

1. Create a new Python file, e.g., `app.py`, and add the following basic Flask app code:

   ```python
   from flask import Flask

   app = Flask(__name__)

   @app.route('/')
   def home():
       return "Hello, Flask!"

   if __name__ == '__main__':
       app.run(debug=True)
   ```

2. Run the Flask app:
   ```bash
   python app.py
   ```

---

## To Generate Requirements.txt File

```bash
pip freeze > requirements.txt
```

---
