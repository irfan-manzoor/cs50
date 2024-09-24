from fpdf import FPDF

def create_shirtificate(name):
    # Create instance of FPDF class
    pdf = FPDF(orientation='P', unit='mm', format='A4')

    # Add a page
    pdf.add_page()

    # Set font for "CS50 Shirtificate" text
    pdf.set_font("Arial", size=24)

    # Calculate the position for "CS50 Shirtificate" text to be centered horizontally
    text_width = pdf.get_string_width("CS50 Shirtificate")
    center_x = (210 - text_width) / 2

    # Add "CS50 Shirtificate" text at the top, centered horizontally
    pdf.text(x=center_x, y=20, txt="CS50 Shirtificate")

    # Add shirt's image centered horizontally
    pdf.image("shirtificate.png", x=(210 - 150) / 2, y=40, w=150)

    # Set font for user's name and "took CS50" text
    pdf.set_text_color(255, 255, 255)  # White text color
    pdf.set_font("Arial", size=16)

    # Calculate the position for the combined text to be centered horizontally on the shirt
    combined_text = f"{name} Took CS50"
    text_width = pdf.get_string_width(combined_text)
    center_x = (210 - text_width) / 2

    # Add combined text on top of the shirt, centered horizontally
    pdf.text(x=center_x, y=100, txt=combined_text)

    # Save the PDF as "shirtificate.pdf"
    pdf.output("shirtificate.pdf")

# Prompt the user for their name
user_name = input("Enter your name: ")

# Create the shirtificate with the user's name
create_shirtificate(user_name)
