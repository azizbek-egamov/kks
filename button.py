from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from config import channel

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🎥 Kinolar kanali", url=f"https://t.me/{channel}")]
    ]
)

add_back = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Bekor qilish")]
    ],
    resize_keyboard=True
)

panel = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kino yuklash")],
        [KeyboardButton(text="Kinoni o'chirish")]
    ],
    resize_keyboard=True
)

# menu = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Sherik kerak"), KeyboardButton(text="Ish joyi kerak")],
#         [KeyboardButton(text="Shogird kerak"), KeyboardButton(text="Ustoz kerak")],
#     ],
#     resize_keyboard=True,
# )

# ok = ReplyKeyboardMarkup(
#     keyboard=[[KeyboardButton(text="HA"), KeyboardButton(text="YO'Q")]],
#     resize_keyboard=True,
# )

# menu = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(
#                 text="Sherik kerak", callback_data="search--Sherik"
#             ),
#             InlineKeyboardButton(
#                 text="Ish joyi kerak", callback_data="search--Ish joyi"
#             ),
#         ],
#         [
#             InlineKeyboardButton(
#                 text="Hodim kerak", callback_data="search--Hodim"
#             ),
#             InlineKeyboardButton(
#                 text="Uztoz kerak", callback_data="search--Ustoz"
#             )
#         ],
#         [
#             InlineKeyboardButton(
#                 text="Shogird kerak", callback_data="search--Shogird"
#             )
#         ]
#     ]
# )
