# START CODING

from functions import *


@dp.message(Command("start"))
async def start(message: Message, state: FSMContext):
    print(message.text.split())
    if len(message.text.split()) > 1:
        code = message.text.split()[1]
        res = kino_info(code, "code")
        if res == False:
            await message.answer("Kino topilmadi")
        else:
            await message.answer_video(
                video=f"{res[3]}", caption=f"{res[1]}\n\n{res[2]}"
            )
    else:

        await bot.send_message(
            chat_id=message.from_user.id,
            text=f"Salom {message.from_user.full_name}, botga kino kodini yuboring yoki @{channel} kanalidagi sizga kerakli kino ostidagi tugmanga bosing:",
            reply_markup=menu,
        )
        

@dp.callback_query(F.data == "check")
async def st(callback: CallbackQuery):
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer(
            text=f"Salom {callback.message.from_user.full_name}, botga kino kodini yuboring yoki @{channel} kanalidagi sizga kerakli kino ostidagi tugmanga bosing:",
            reply_markup=menu,
    )


@dp.message(Command("panel"))
async def pnl(message: Message):
    id = message.from_user.id
    if f"{id}" == f"{admin}":
        await bot.send_message(
            chat_id=f"{admin}",
            text="Admin panelga xush kelibsiz",
            reply_markup=panel,
        )


@dp.message(F.text == "Bekor qilish")
async def add_bac(message: Message, state: FSMContext):
    id = message.from_user.id
    if f"{id}" == f"{admin}":
        await bot.send_message(
            chat_id=f"{admin}", text="Admin panelga xush kelibsiz", reply_markup=panel
        )
        await state.clear()


@dp.message(F.text == "Kinoni o'chirish")
async def kino_qosh(message: Message, state: FSMContext):
    await bot.send_message(
        chat_id=f"{admin}",
        text="Kino kodini kiriting",
        reply_markup=add_back,
    )
    await state.set_state(delKino.cod)


@dp.message(delKino.cod)
async def add3(message: Message, state: FSMContext):
    text = message.text
    if kino_info(text, "code") != False:
        if delete(text) == True:
            await bot.send_message(
                chat_id=f"{admin}",
                text="Yaxshi, kino muvaffaqiyatli olib tashlandi",
                reply_markup=panel,
            )
            await state.clear()
        else:
            await bot.send_message(
                chat_id=f"{admin}", text="Xatolik yuz berdi", reply_markup=panel
            )
            await state.clear()
    else:
        await bot.send_message(
            chat_id=f"{admin}",
            text="Ushbu koddagi kino bazada mavjud emas.\n\nQaytadan urinib ko'ring.",
            reply_markup=add_back,
        )
        await state.set_state(delKino.cod)


@dp.message(F.text == "Kino yuklash")
async def kino_qosh(message: Message, state: FSMContext):
    await bot.send_message(
        chat_id=f"{admin}",
        text="Kanalga yuborish uchun rasm yoki video yuboring:",
        reply_markup=add_back,
    )
    await state.set_state(addKino.inf)


@dp.message(addKino.inf)
async def kino_qosh(message: Message, state: FSMContext):
    if message.video or message.photo:
        if message.video:
            await bot.send_message(
                chat_id=f"{admin}",
                text="Kino uchun nom yuboring:",
                reply_markup=add_back,
            )
            await state.update_data({"to": "video"})
            await state.update_data({"info": message.video.file_id})
            await state.set_state(addKino.name)
        elif message.photo:
            await bot.send_message(
                chat_id=f"{admin}",
                text="Kino uchun nom yuboring:",
                reply_markup=add_back,
            )
            await state.update_data({"to": "photo"})
            await state.update_data({"info": message.photo[-1].file_id})
            await state.set_state(addKino.name)
    else:
        await bot.send_message(
            chat_id=f"{admin}",
            text="Faqat video yoki rasm yuboring.\n\nQaytadan urining.",
        )
        await state.set_state(addKino.inf)


@dp.message(addKino.name)
async def add2(message: Message, state: FSMContext):
    text = message.text
    if kino_info(text, "name") == False:
        await state.set_state(addKino.desc)
        await bot.send_message(
            chat_id=f"{admin}",
            text="Yaxshi, endi kino haqida barcha ma'lumotlarni yuboring:",
            reply_markup=add_back,
        )
        await state.update_data({"knomi": text})
    else:
        await bot.send_message(
            chat_id=f"{admin}",
            text="Xatolik, Bunday nomdagi kino mavjud yoki bazaga ulanishda xatolik yuz berdi.\n\nBoshqa nom kiritib ko'ring: ",
            reply_markup=add_back,
        )
        await state.set_state(addKino.name)


@dp.message(addKino.desc)
async def add3(message: Message, state: FSMContext):
    text = message.text

    await bot.send_message(
        chat_id=f"{admin}",
        text="Yaxshi, endi botga kinoni yuboring",
        reply_markup=add_back,
    )
    await state.update_data({"discr": text})
    await state.set_state(addKino.kino)


@dp.message(addKino.kino)
async def add4(message: Message, state: FSMContext):
    if message.video:
        data = await state.get_data()
        r = data.get("to")
        i = data.get("info")
        n = data.get("knomi")
        d = data.get("discr")
        vid = message.video.file_id
        if add_information(n, d, vid) == True:
            res = kino_info(vid, "url")
            await bot.send_message(
                chat_id=f"{admin}",
                text=f"OK, kino bazaga yuklandi.\n\nKino kodi: <code>{res[0]}</code>",
                reply_markup=panel,
            )
            await state.clear()
            down = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text="🎬 Filmi yuklab olish",
                            url=f"https://t.me/{bot_user}?start={res[0]}",
                        )
                    ]
                ]
            )
            if r == "photo":
                await bot.send_photo(
                    photo=f"{i}",
                    chat_id=f"@{channel}",
                    caption=f"""<b>✅ Aynan shu rasmni kinosi to'liq xolda @{bot_user} ga joylandi !
                    
🎬 Kino kodi: <code>{res[0]}</code>

⚠️ Kinoni yuklab olish uchun botimizga kirib kino kodini kiriting yoki pastdagi rugma orqali kirib yuklab oling !</b>""",
                    reply_markup=down,
                )
            elif r == "video":
                await bot.send_video(
                    video=f"{i}",
                    chat_id=f"@{channel}",
                    caption=f"""<b>✅ Aynan shu videoni kinosi to'liq xolda @{bot_user} ga joylandi !
                    
🎬 Kino kodi: <code>{res[0]}</code>

⚠️ Kinoni yuklab olish uchun botimizga kirib kino kodini kiriting yoki pastdagi rugma orqali kirib yuklab oling !</b>""",
                    reply_markup=down,
                )
        else:
            await bot.send_message(
                chat_id=f"{admin}",
                text=f"Jarayon muvaffaqiyatli amalga oshmadi\n\nQayadan urinib ko'ring.",
                reply_markup=panel,
            )
            await state.clear()
    else:
        await bot.send_message(
            chat_id=f"{admin}",
            text="Faqat video yuboring:",
            reply_markup=add_back,
        )
        await state.set_state(addKino.kino)


@dp.message(F.text)
async def kino_search(message: Message):
    text = message.text
    if str(text).isdigit() == True:
        res = kino_info(text, "code")
        if res == False:
            await message.answer("Kino topilmadi")
        else:
            await message.answer_video(
                video=f"{res[3]}", caption=f"{res[1]}\n\n{res[2]}"
            )


async def main() -> None:
    dp.message.middleware.register(ThrottlingMiddleware())
    dp.update.middleware.register(joinchat())
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except:
        print("Jarayon yakunlandi")
