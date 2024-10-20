import random
from PIL import Image, ImageDraw, ImageFont

# Lists of options with corresponding emojis
options_with_emojis = {
    "positive": [
        ("Great job!", "🎉"),
        ("You're amazing!", "🌟"),
        ("Keep up the good work!", "👍"),
        ("You're doing fantastic!", "👏"),
        ("You've got this!", "💪"),
        ("Excellent progress!", "🚀"),
        ("You're a star!", "⭐"),
        ("Awesome effort!", "✨"),
        ("Keep shining!", "🌞"),
        ("You're unstoppable!", "🔥"),
    ],
    "negative": [
        ("Not your best day.", "😞"),
        ("Could use some improvement.", "🔧"),
        ("Try harder next time.", "🤔"),
        ("Don't give up!", "💔"),
        ("Keep pushing forward.", "🏃‍♂️"),
        ("Learn from this.", "📚"),
        ("Stay positive!", "😊"),
        ("It's okay to fail.", "🙁"),
        ("You can do better!", "⚠️"),
        ("Keep trying!", "💪"),
    ],
}

# Combine options with emojis
all_options = [f"{text} {emoji}" for text, emoji in options_with_emojis["positive"]] + \
              [f"{text} {emoji}" for text, emoji in options_with_emojis["negative"]]

# Function to display options
def display_options():
    print("Here are your options:")
    for i, option in enumerate(all_options, start=1):
        print(f"{i}: {option}")

# Function to get user choice
def get_user_choice():
    while True:
        try:
            choice = int(input("Pick a number between 1 and 20, or enter 0 for a computer pick: "))
            if 0 <= choice <= 20:
                return choice
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

# Function to create an image with text and a background
def create_image_with_text(text):
    # Load the background image
    background = Image.open('background.jpg')
    img = background.resize((400, 200))  # Resize if needed
    d = ImageDraw.Draw(img)
    
    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except IOError:
        font = ImageFont.load_default()

    # Add text to the image
    text_bbox = d.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = (img.width - text_width) / 2
    text_y = (img.height - text_height) / 2
    d.text((text_x, text_y), text, fill="black", font=font)

    # Save the image
    img.save('output.png')
    print("Image saved as 'output.png'")

# Main program
def main():
    
    
    choice = get_user_choice()
    
    if choice == 0:
        computer_choice = random.randint(1, 20) - 1
        selected_option = all_options[computer_choice]
        print(f"\nComputer picked: {selected_option}")
    else:
        selected_option = all_options[choice - 1]
        print(f"\nYou picked: {selected_option}")
    
    # Create an image with the selected option
    create_image_with_text(selected_option)

if __name__ == "__main__":
    main()
