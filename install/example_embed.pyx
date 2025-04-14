"""
A simple example to test Python embedding functionality
"""

print("Hello from embedded Python!")

def greet(name):
    """Greet a user by name"""
    return f"Hello {name}!"

def main():
    """Main function to be called from C"""
    name = input("What's your name? ")
    message = greet(name)
    print(message)
    return message 