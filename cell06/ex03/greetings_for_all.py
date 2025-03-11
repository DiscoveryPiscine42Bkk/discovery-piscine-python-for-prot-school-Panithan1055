def greetings(name="noble stranger"):
    if not isinstance(name, str):
        print("Error! It was not a name.")
    else:
        print(f"Hello, {name}.")

if __name__ == "__main__":
    greetings('Alexandra')
    greetings('Wil')
    greetings()
    greetings(42)