from curses import killchar
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import math
import numpy as np
from src.dashed_image_draw import DashedImageDraw
from src.data import Data
import textwrap

A4WIDTH = 2479
A4HEIGHT = 3508


class CardManager:
    def __init__(self):
        # dpi 300 with dynamic margins
        # self.page_margin = 80  # from all sides
        self.vertical_page_margin = 160
        self.horizontal_page_margin = 80
        height_with_margins = A4HEIGHT - (2 * self.vertical_page_margin)
        width_with_margins = A4WIDTH - (2 * self.horizontal_page_margin)

        self.a9_vertical_step = math.floor(height_with_margins / 8)
        self.a9_horizontal_step = math.floor(width_with_margins / 4)
        self.card_left_margin = 80

        # dpi 300 with margins to accomodate smaller cardboard
        # 2479x3508 px => 2319x3348
        # page_margin = 80  # from all sides
        # a9_vertical_step = 418
        # a9_horizontal_step = 580
        # card_left_margin = 80

        # dpi 300
        # a9_vertical_step = 438
        # a9_horizontal_step = 620
        # card_left_margin = 80

        # dpi 72
        # a9_vertical_step = 105 * 4
        # a9_horizontal_step = 149 * 4

    size_to_orientation_map = {
        'a8': 'vertical',
        'a9': 'horizontal',

    }
    size_to_cards_number_map = {
        'a8': 16,
        'a9': 32,
    }

    '''portrait'''
    size_to_cards_in_a_row_map = {
        'a8': 4,
        'a9': 4,
    }

    # public

    def add_card_to_image(self, image: Image, size: str, index: int, resource_key: str) -> Image:
        x, y = self.get_coordinates_by_size(size, index)
        image = self.insert_card(image, x, y, resource_key)
        return image

    def get_coordinates_by_size(self, size: str, index: int):
        in_a_row = self.size_to_cards_in_a_row_map[size]
        horizontal_coefficient = self.a9_horizontal_step * (index % in_a_row)
        vertical_coefficient = self.a9_vertical_step * \
            math.floor(index / in_a_row)

        return self.horizontal_page_margin + horizontal_coefficient, self.vertical_page_margin + vertical_coefficient

    def get_coordinates_a8(self, index: int):
        in_a_row = self.size_to_cards_in_a_row_map['a8']
        horizontal_coefficient = self.a9_horizontal_step * (index % in_a_row)
        vertical_coefficient = self.a9_vertical_step * 2 * \
            math.floor(index / in_a_row)

        return self.horizontal_page_margin + horizontal_coefficient, self.vertical_page_margin + vertical_coefficient


    def insert_card(self, image: Image, x: int, y: int, resource_key: str) -> Image:
        assert (image != None)
        image = self.draw_border(image, x, y)
        image = self.write_card(image, x, y, resource_key)
        return image

    def make_blank(self, image: Image) -> Image:
        white = (255, 255, 255)
        draw = ImageDraw.Draw(image)
        draw.rectangle(
            [(0, 0), image.size],
            fill=white
        )
        return image

    def draw_border(self, image: Image, x: int, y: int) -> Image:
        d = DashedImageDraw(image)

        d.dashed_rectangle(
            [(x, y), (x + self.a9_horizontal_step, y + self.a9_vertical_step)],
            dash=(5, 40),
            outline='black',
            width=1
        )

        return image


    def draw_border_a8(self, image: Image, x: int, y: int)->Image:
        d = DashedImageDraw(image)

        d.dashed_rectangle(
            [(x, y), (x + self.a9_horizontal_step, y + self.a9_vertical_step * 2)],
            dash=(5, 40),
            outline='black',
            width=1
        )

        return image
    
    def write_card(self, image: Image, x: int, y: int, resource_key: str) -> Image:
        image_draw = ImageDraw.Draw(image)
        font_path = '/Users/gena/Library/Fonts/NotoSansMono-Regular.ttf'
        my_font = ImageFont.truetype(font_path, 70)

        black = (0, 0, 0)
        resource = Data.get_resources()[resource_key]
        image_draw.text(
            (x + self.card_left_margin, y),
            resource_key,
            font=my_font,
            fill=black
        )

        i = 0
        for key, value in resource.items():
            if key == 'quantity':
                continue
            width_in_chars = 12
            spaces = width_in_chars - 1 - len(key)
            if value != 0:
                image_draw.text(
                    (x + self.card_left_margin + 30, y + (110 + (i * 70))),
                    key + ' ' * spaces + str(value),
                    font=ImageFont.truetype(font_path, 44),
                    fill=black
                )
            i += 1
        return image
    
    
    def write_multiline_text(self, image: Image, x: int, y: int, text:str, font:ImageFont, wrap_after:int=20, line_spacing:int=40) -> Image:
        image_draw = ImageDraw.Draw(image)
        black = (0, 0, 0)
        lines = textwrap.wrap(text, width=wrap_after)
        for index, line in enumerate(lines):
            image_draw.text(
                (x, y + index * line_spacing),
                line,
                font=font,
                fill=black
            )
        return image
    # private
