def get_positive_int(prompt: str) -> int:
    """Keep asking until the user enters an integer >= 0."""
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            # Original code would crash on non-integers; this makes it safer.
            print("Please enter a whole number.")
            continue

        if value < 0:
            prompt = "Age must be positive. Age: "
            continue

        return value


def get_non_empty_string(prompt: str) -> str:
    """Keep asking until the user enters a non-empty string."""
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        prompt = "Name can't be empty. Name: "


def main():
    age = get_positive_int("Age: ")
    name = get_non_empty_string("Name: ")
    print(name, age)


if __name__ == "__main__":
    main()