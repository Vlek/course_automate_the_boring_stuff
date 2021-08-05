# This program says hello and asks the user for their name


def main() -> None:
    """Say hello, ask user for their name."""
    print("Hello world!")

    userName = input("Enter your name: ")
    print(f"Thank you, {userName}")
    print(f"The length of your name is: {len(userName)}")

    userAge = input("Enter your age: ")
    print(f"Next year you will be {int(userAge) + 1} old!")


if __name__ == "__main__":
    main()
