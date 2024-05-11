import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

df = pd.read_excel("trading_cards.xlsx")

# Define card dimensions and layout
card_width = 200
card_height = 100
margin_x = 20
margin_y = 20
cards_per_row = 2
cards_per_column = 2
space_x = (letter[0] - 2 * margin_x - cards_per_row * card_width) / (cards_per_row - 1)
space_y = (letter[1] - 2 * margin_y - cards_per_column * card_height) / (cards_per_column - 1)

pdf_path = "trading_cards.pdf"
c = canvas.Canvas(pdf_path, pagesize=letter)

