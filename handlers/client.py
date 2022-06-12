import pyrebase
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create import dp, bot
from keyboard.client_k import kb_client
from keyboard.song_k import kb_song
from keyboard.album_k import kb_album
from keyboard.genre_k import kb_genre
from keyboard.singer_k import kb_singer


firebaseConfig = {
  'apiKey': "XXX",
  'databaseURL': "https://mireathing-default-rtdb.europe-west1.firebasedatabase.app",
  'authDomain': "mireathing.firebaseapp.com",
  'storageBucket': "mireathing.appspot.com",
}


def firebase_start():
  global firebase, db, storage
  firebase = pyrebase.initialize_app(firebaseConfig)
  db=firebase.database()
  storage=firebase.storage()
  if db:
    print('Data base connected OK!')
  if storage:
    print('Storage connected OK!')


class FSMMusic(StatesGroup):
    song = State()
    artist = State()
    album = State()
    genre = State()


async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Испоьзуйте кнопки ниже,\nчтобы сделать выбор', reply_markup=kb_client)
    except:
        await message.reply('https://t.me/musicprojectmirea_bot')

async def menue_start(message : types.Message):
    await bot.send_message(message.from_user.id, 'Разделы:', reply_markup=kb_client)


async def search_song(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберите песню', reply_markup=kb_song)
    await FSMMusic.song.set()

async def search_singer(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите исполнителя', reply_markup=kb_singer)
    await FSMMusic.artist.set()

async def search_genre(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите жанр', reply_markup=kb_genre)
    await FSMMusic.genre.set()

async def search_album(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите альбом', reply_markup=kb_album)
    await FSMMusic.album.set()


def builder(typing, number, posit, folder):
    data = db.child(typing).child(number).get()
    cloudfilename = data.val()[posit]
    url = storage.child(folder).child(cloudfilename).get_url(None)
    return url


async def find_song(message: types.Message, state: FSMContext):
    if message.text == 'The Nights\U0001F319':
        url = builder('song', 's1', 'title_1', 'songs')
        await bot.send_audio(message.from_user.id, url)

    elif message.text == 'Shape of You\U0001F498':
        url = builder('song', 's1', 'title_2', 'songs')
        await bot.send_audio(message.from_user.id, url)

    elif message.text == 'Enemy\U0001F480':
        url = builder('song', 's1', 'title_3', 'songs')
        await bot.send_audio(message.from_user.id, url)

    elif message.text == 'Youre Gonna Go Far, Kid\U0001F92C':
        url = builder('song', 's1', 'title_4', 'songs')
        await bot.send_audio(message.from_user.id, url)

    elif message.text == 'Главное меню\U0001F3E0':
        await state.finish();

    else:
        await bot.send_message(message.from_user.id, "Простите, я не знаю такой команы")


async def find_genre(message: types.Message, state: FSMContext):
    if message.text == 'Rock\U0001FAA8':
        await message.reply("Три самых популярных трека этого жанра:")
        url = builder('genre', 'g1', 'title_1', 'genres')
        await bot.send_audio(message.from_user.id, url)

        url = builder('genre', 'g1', 'title_2', 'genres')
        await bot.send_audio(message.from_user.id, url)

        url = builder('genre', 'g1', 'title_3', 'genres')
        await bot.send_audio(message.from_user.id, url)

    elif message.text == 'Главное меню\U0001F3E0':
        await state.finish();

    else:
        await bot.send_message(message.from_user.id, "Простите, я не знаю такой команы")


async def find_singer(message: types.Message, state: FSMContext):
    if message.text == 'AJR\U0001F604':
        await message.reply("Три самых популярных трека этого исполнителя:")

        url = builder('singer', 'i1', 'title_1', 'singers')
        await bot.send_audio(message.from_user.id, url)

        url = builder('singer', 'i1', 'title_2', 'singers')
        await bot.send_audio(message.from_user.id, url)

        url = builder('singer', 'i1', 'title_3', 'singers')
        await bot.send_audio(message.from_user.id, url)

    elif message.text == 'Главное меню\U0001F3E0':
        await state.finish();
        
    else:
        await bot.send_message(message.from_user.id, "Простите, я не знаю такой команы")


async def find_album(message: types.Message, state: FSMContext):
    if message.text == 'Scaled And Icy\U0001F432':
        await message.reply("Три самых популярных трека из этого альбома:")

        url = builder('album', 'a1', 'title_1', 'albums')
        await bot.send_audio(message.from_user.id, url)

        url = builder('album', 'a1', 'title_2', 'albums')
        await bot.send_audio(message.from_user.id, url)

        url = builder('album', 'a1', 'title_3', 'albums')
        await bot.send_audio(message.from_user.id, url)

    elif message.text == 'Главное меню\U0001F3E0':
        await state.finish();
        
    else:
        await bot.send_message(message.from_user.id, "Простите, я не знаю такой команы")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'], state = "*")
    dp.register_message_handler(menue_start, text=['Главное меню\U0001F3E0'], state = "*")
    dp.register_message_handler(search_song, text=['Песня\U0001F3B5'], state = "*")
    dp.register_message_handler(search_singer, text=['Исполнитель\U0001F60E'], state = "*")
    dp.register_message_handler(search_genre, text=['Жанр\U0001F3AD'], state = "*")
    dp.register_message_handler(search_album, text=['Альбом\U0001F4C1'], state = "*")
    dp.register_message_handler(find_song, state=FSMMusic.song)
    dp.register_message_handler(find_genre, state=FSMMusic.genre)
    dp.register_message_handler(find_singer, state=FSMMusic.artist)
    dp.register_message_handler(find_album, state=FSMMusic.album)
