# app.py
def greet(name):
    return f"Hello, {name}! Welcome to Docker & Kubernetes."

if __name__ == "__main__":
    name = "Mariam"
    message = greet(name)
    print(message)
