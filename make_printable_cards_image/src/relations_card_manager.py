from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import math
import random
from src.card_manager import CardManager
from src.dashed_image_draw import DashedImageDraw
from src.data import Data

A4WIDTH = 2479
A4HEIGHT = 3508


class RelationsCardManager:
    def __init__(self):
        self.card_manager = CardManager()
        # dpi 300 with dynamic margins
        # self.page_margin = 80  # from all sides
        self.vertical_page_margin = 160
        self.horizontal_page_margin = 80
        height_with_margins = A4HEIGHT - (2 * self.vertical_page_margin)
        width_with_margins = A4WIDTH - (2 * self.horizontal_page_margin)

        self.a9_vertical_step = math.floor(height_with_margins / 8)
        self.a9_horizontal_step = math.floor(width_with_margins / 4)
        self.card_left_margin = 230

    # public

    def add_cards(self, image: Image, size: str, orientation: str) -> Image:
        if (self.card_manager.size_to_orientation_map[size] != orientation):
            image = self.card_manager.rotate_image_90(image)
        image = self.card_manager.make_blank(image)

        cards_count = self.card_manager.size_to_cards_number_map[size]
        relations_keys = self.get_relations_keys()
        relations_keys_len = len(relations_keys)
        relations_keys_effective_order = []
        for index in range(cards_count):
            relations_keys_effective_order.append(
                relations_keys[index % relations_keys_len])
            image = self.add_card_to_image(
                image, size, index, relations_keys[index % relations_keys_len])
        relations_keys_effective_order.reverse()

        image = self.rotate_image_180(image)

        for index, relations_key in enumerate(relations_keys_effective_order):
            image = self.add_recipient_card_to_image(
                image, size, index, relations_key)
        return image

    # private

    def rotate_image_180(self, image: Image) -> Image:
        image = image.rotate(180)
        return image

    def add_recipient_card_to_image(self, image, size, index, relation_key) -> Image:
        x, y = self.card_manager.get_coordinates_a8(index)

        image = self.write_recipient_part(image, x, y, relation_key, index)

        return image

    def add_card_to_image(self, image: Image, size: str, index: int, relation_key: str) -> Image:
        x, y = self.card_manager.get_coordinates_a8(index)
        image = self.insert_card(image, x, y, relation_key, index)
        return image

    def insert_card(self, image: Image, x: int, y: int, relation_key: str, index: int) -> Image:
        assert (image != None)
        image = self.card_manager.draw_border_a8(image, x, y)
        image = self.write_card(image, x, y, relation_key, index)
        return image

    def write_card(self, image: Image, x: int, y: int, relation_key: str, index: int) -> Image:
        image = self.write_agent_part(image, x, y, relation_key, index)
        # image = self.write_recipient_part(image, x, y, relation_key, index)
        return image

    def write_agent_part(self, image: Image, x: int, y: int, relation_key: str, index: int) -> Image:

        middle_x, middle_y = x + \
            (self.a9_horizontal_step // 2), y + self.a9_vertical_step
        image_draw = ImageDraw.Draw(image)
        font_path = '/Users/gena/Library/Fonts/NotoSansMono-Regular.ttf'
        my_font = ImageFont.truetype(font_path, 80)
        number_font = ImageFont.truetype(font_path, 100)

        black = (0, 0, 0)

        w, h = 220, 190
        shape = [(x, middle_y), (x + self.a9_horizontal_step, middle_y)]
        image_draw.line(shape, fill=black, width=3)

        relation = Data.get_relations()[relation_key]
        agent_bonus = relation["agent_bonus"]
        plus = '+' if agent_bonus > 0 else ''
        image_draw.text(
            (x + self.card_left_margin, middle_y+50),
            'WE',
            font=my_font,
            fill=black
        )
        image_draw.text(
            (x + self.card_left_margin, middle_y+200),
            f'{plus} {agent_bonus}',
            font=number_font,
            fill=black
        )
        return image

    def write_recipient_part(self, image: Image, x: int, y: int, relation_key: str, index: int) -> Image:

        relation = Data.get_relations()[relation_key]
        recipient_bonus = relation["recipient_bonus"]

        middle_x, middle_y = x + \
            (self.a9_horizontal_step // 2), y + self.a9_vertical_step
        image_draw = ImageDraw.Draw(image)
        font_path = '/Users/gena/Library/Fonts/NotoSansMono-Regular.ttf'
        my_font = ImageFont.truetype(font_path, 80)
        number_font = ImageFont.truetype(font_path, 100)

        black = (0, 0, 0)
        white = (255, 255, 255)

        # temp_text_image = Image.new('RGBA', (self.a9_horizontal_step, self.a9_vertical_step), (50, 50, 50,50))

        # temp_text_image_draw = ImageDraw.Draw(temp_text_image)
        # temp_text_image_draw.text((self.card_left_margin, 0), relation_key.upper(), font=my_font, fill=black)
        # temp_text_image_draw.text((self.card_left_margin, 10), f'{recipient_bonus}', font=my_font, fill=black)

        # temp_text_image = temp_text_image.rotate(180, expand=1)

        # px, py = 10, 10
        # sx, sy = temp_text_image.size
        # image.paste(temp_text_image, (x, y, x+self.a9_horizontal_step, y + self.a9_vertical_step), temp_text_image)
        # image.paste(temp_text_image, (x - self.a9_horizontal_step, y - self.a9_vertical_step, x, y), temp_text_image)
        # image.paste(temp_text_image, (x - 10, y - 10, x, y), temp_text_image)
        # image.paste(temp_text_image, (x, y, x+self.a9_horizontal_step, y + self.a9_vertical_step), temp_text_image)
        # image.paste(temp_text_image, (x, y, x+tempsz, y + tempsz),)

        # image.show()

        margin = 500 // len(relation_key)


        image_draw.text(
            (x + margin, middle_y+50),
            relation_key.upper(),
            font=my_font,
            fill=black
        )
        image_draw.text(
            (x + self.card_left_margin+50, middle_y+200),
            f'{recipient_bonus}',
            font=number_font,
            fill=black
        )
        return image

    def get_relations_keys(self) -> list:
        return list(Data.get_relations().keys())
