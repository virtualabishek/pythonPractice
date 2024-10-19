import random

# Responses including both positive and negative ones
responses = [
    "You are lucky! 🍀",
    "You are brave! 🦸‍♂️",
    "You are a genius! 🤓",
    "You are beautiful! 🌈",
    "You are interesting but unique! 🎉",
    "You are the most joyful person! 😄",
    "You are kind-hearted! ❤️",
    "You are a superstar! ⭐",
    "You are so innocent and hardworking! 💪",
    "You spread happiness wherever you go! 😊",
    "You are a great friend! 🤝",
    "You have a wonderful imagination! ✨",
    "You are full of energy! ⚡",
    "You have a great sense of humor! 😂",
    "You are adventurous! 🌍",
    "You are a great listener! 👂",
    "You are a fantastic storyteller! 📖",
    "You are creative! 🎨",
    "You are brave enough to try new things! 🚀",
    "You make the world a better place! 🌟",
    "You are loved by everyone! 💖",
    "You are a ray of sunshine! ☀️",
    "You are a quick thinker! 🧠",
    "You are a true champion! 🏆",
    "You have a heart of gold! 💛",
    "You are a wonderful dreamer! 🌙",
    "You could try a little harder. 🤔",
    "Not everyone is perfect, and that's okay! 😌",
    "Sometimes, you might feel lost. 🌪️",
    "It's okay to have off days. 💭",
    "You can be a bit too hard on yourself. 💔",
    "You might be missing some opportunities. 🚫",
    "You have the potential to do better! 📈",
    "Don't forget that it's fine to ask for help! 🙏"
]

print("Hey! Welcome to the game created by Deepika! 🎉")
name = input("First, tell me your name: ")

print(f"Hello, {name}! ✋ Let's play a fun game!")
query = int(input("Do you want to enter a number yourself or let the computer choose? \nPress 1 to enter yourself, or 2 for the computer to choose: "))

# User-entered number
if query == 1:
    num = int(input("Enter a number between 1 and 30: "))  # Updated range
    if 1 <= num <= 30:
        print(responses[num - 1])  # List is 0-indexed
    else:
        print("Please enter a number between 1 and 30! ❌")
else:
    random_num = random.randint(1, 30)  
    print(f"The computer chose: {random_num}")
    print(responses[random_num - 1])  

print("Thanks for playing, and remember, you are awesome! 🌟")
