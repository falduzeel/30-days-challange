name = input("What is your name? ").strip().title()

if name:
    print(f"Hello, {name}! Great to meet you.")
    print(f"Informative tidbit: Your name is {len(name)} letters long.")
else:
    print("Hello, mystery guest! You didn't type a name.")