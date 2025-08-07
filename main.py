print("new hello")
import random
import datetime

def random_greeting():
    greetings = ["Hola", "Hello", "Bonjour", "Ciao", "Hallo", "Olá"]
    return random.choice(greetings)

def print_time():
    now = datetime.datetime.now()
    print(f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    print(random_greeting() + ", mundo!")
    print_time()

if __name__ == "__main__":
    main()