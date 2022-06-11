import pyrebase
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create import dp, bot
from keyboard.client_k import kb_client


firebaseConfig = {
  'apiKey': "AIzaSyA2yicK3GAEpkkDOfLweKanJh2rJYi0mIg",
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

async def firebase_read(message):
  data = db.child('song').get()
  for item in data.each():
    cloudfilename=item.val()['title']
    url = storage.child('songs').child(cloudfilename).get_url(None)
    await bot.send_audio(message.from_user.id, url)


class FSMMusic(StatesGroup):
    song = State()
    artist = State()
    album = State()
    genre = State()


async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Команды:\n\nЖанр\nИсполнитель\nПесня\nАльбом', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('https://t.me/musicprojectmirea_bot')

async def search_song(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберите песню:\nThunder\nShape_of_You\nThe_Nights')
    await FSMMusic.song.set()

async def search_singer(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите исполнителя:\nDaft_Punk')
    await FSMMusic.artist.set()

async def search_style(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите жанр:\nPop')
    await FSMMusic.genre.set()

async def search_album(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите альбом:\nThe_works')
    await FSMMusic.album.set()


async def find_song(message: types.Message, state: FSMContext):
	if message.text == 'Thunder':
		data = db.child('song').child('s1').get()
		cloudfilename = data.val()['title']
		url = storage.child('songs').child(cloudfilename).get_url(None)
		await bot.send_audio(message.from_user.id, url)
	if message.text == 'Shape_of_You':
		data = db.child('song').child('s2').get()
		cloudfilename = data.val()['title']
		url = storage.child('songs').child(cloudfilename).get_url(None)
		await bot.send_audio(message.from_user.id, url)
	if message.text == 'The_Nights':
		data = db.child('song').child('s3').get()
		cloudfilename = data.val()['title']
		url = storage.child('songs').child(cloudfilename).get_url(None)
		await bot.send_audio(message.from_user.id, url)
	await state.finish();


async def find_genre(message: types.Message, state: FSMContext):
    if message.text == 'Pop':
        await message.reply("Подборка популярных треков из данного жанра")
        await bot.send_audio(message.chat.id,'https://s413sas.storage.yandex.net/get-mp3/463d5dfff9e691696c90256868f6300ff4385d34dd6ea76f56a646547d038fa9/0005df4fd2570682//rmusic/U2FsdGVkX1-ONNXNhTkmJULLOI1vsMZimBm0SSzOEk1JclHSE_ItkpGlLkWA2IDuG5LbQ9kamBl4PDEzYPFk5lkaIJyhRvUw2123rCxeVfI/463d5dfff9e691696c90256868f6300ff4385d34dd6ea76f56a646547d038fa9/26595?track-id=89081846&play=false')
        await bot.send_audio(message.chat.id,'https://s246sas.storage.yandex.net/get-mp3/b174fc68fa356a15ae874e57aa39d3a09e8ff648f1ad2e54ca943e929f4b19d0/0005df4fd256ec80//rmusic/U2FsdGVkX18sFVYEeP0AI-jVs8F-5wM7j89G9XFyuZ6N1p03iH56GEDs8wGACkvTiy1YRL-H2bMesSFkYzFcZAuOfsSr4cs0SjCg97G92Es/b174fc68fa356a15ae874e57aa39d3a09e8ff648f1ad2e54ca943e929f4b19d0?track-id=27094549&play=false')
        await bot.send_audio(message.chat.id, 'https://s293myt.storage.yandex.net/get-mp3/0f227555e12e150f69ec64cd4d03192141e3c22c4a705d0f23e547e0e40add53/0005df4f4d331388//rmusic/U2FsdGVkX1_oaSe5BuwKI-h1eTof7yGGMswexexfbqgwfZwbDg-IDNh7bodw8n_5KWNd5di0hMPaljOKpdO31lqB5hryVRkq4b4_-3U713w/0f227555e12e150f69ec64cd4d03192141e3c22c4a705d0f23e547e0e40add53/27667?track-id=104294880&play=false')
    await state.finish();

async def find_artist(message: types.Message, state: FSMContext):
    if message.text == 'Daft_Punk':
        await message.reply("Лучшие треки")
        await bot.send_audio(message.chat.id,'https://s56sas.storage.yandex.net/get-mp3/05c5644b1df4c67e44e3c21790d7c41c11acccb318d2ec4f662c3b29af98f5e2/0005df4fd8d5d66d//rmusic/U2FsdGVkX1_LPKl3FAFfqmsUUUFxlMLzIZO2WhqeYJBCUd73YtTBPJVMAPfq_eADSGOH6_l9_aw3aj9oTzo7bw/05c5644b1df4c67e44e3c21790d7c41c11acccb318d2ec4f662c3b29af98f5e2/35119?track-id=270953&play=false')
        await bot.send_audio(message.chat.id,'https://s592sas.storage.yandex.net/get-mp3/a354ba4061a82c21de4ff263b8feaa6d212357e9beab6b8b0c6bc18d5883c48d/0005df4fd8d62664//rmusic/U2FsdGVkX19mViGBKx1hJPCpdVxvkA9hKB8stX-quOkP8ViLpQL-0uIXWW6jtGbt_vyPUblAo9n3ZqN6Id-aTg/a354ba4061a82c21de4ff263b8feaa6d212357e9beab6b8b0c6bc18d5883c48d/37419?track-id=270950&play=false')
        await bot.send_audio(message.chat.id, 'https://s154vla.storage.yandex.net/get-mp3/df179aefac1ecb74ed0badd512a63248f926e881f54b05488c1eace13b343c98/0005df4f47d289ec//rmusic/U2FsdGVkX1-8mQWVC5Mfm2Tjx_VTlUrrTuNh6tw0XKbKnedyA8nL_fHgN2neG6Dh4WTXGHvgEtMVTZJ70sM_QK09Tu9gRCqurauzps0BSmc/df179aefac1ecb74ed0badd512a63248f926e881f54b05488c1eace13b343c98/38811?track-id=10277791&play=false')
    await state.finish();

async def find_album(message: types.Message, state: FSMContext):
    if message.text == 'The_works':
        await message.reply("Три самых популярных трека из данного альбома")
        await bot.send_audio(message.chat.id,'https://s124iva.storage.yandex.net/get-mp3/80fd6e6b176b1916734610da8b50e8de505418c115fe97f7d43dafeff15beb14/0005df4fc702e44e//rmusic/U2FsdGVkX18697aeqPWkxp9vV9s9U8iqojROmM6M-bGiN-ve6qtEKa13Z1_pgGz4VEDkdkdi9WKx7bjdKBwLSwrPE8DA9jW_GLts4_TY7ok/80fd6e6b176b1916734610da8b50e8de505418c115fe97f7d43dafeff15beb14/41423?track-id=2758002&play=false')
        await bot.send_audio(message.chat.id,'https://s680sas.storage.yandex.net/get-mp3/4411db4e17ea2fd9eac283a3786a11fdcf99e2a09dcfbb0d9abb2351b4a716d5/0005df4fc700ccad//rmusic/U2FsdGVkX1-YNlefdT5lZk4l0Z1NhyXzRys-vSUGlA_u4DiYmfA_MbMcf6KznYrUZb1sSZ4AkVM9sVztmEo_TTqwzFR2zKAFWJPHD8Alec4/4411db4e17ea2fd9eac283a3786a11fdcf99e2a09dcfbb0d9abb2351b4a716d5/54015?track-id=1710804&play=false')
        await bot.send_audio(message.chat.id,'https://s209iva.storage.yandex.net/get-mp3/c3d112bcec595427daf631c328ab85773f33591d6678485a87ee1eb4e2cde9a3/0005df4f379d87d5//rmusic/U2FsdGVkX1_HVPMwJ__kSLcgF01mbmzupMMYpdEypTlOBKKhKmHdbAGHYCrlJLu0WSCr5_A1yBx9p3Hfz1pjIscxXScnTT0mwo_VFFW_RPY/c3d112bcec595427daf631c328ab85773f33591d6678485a87ee1eb4e2cde9a3/31559?track-id=2758001&play=false')
    await state.finish();



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'], state = "*")
    dp.register_message_handler(search_song, text=['Песня'], state = "*")
    dp.register_message_handler(search_singer, text=['Исполнитель'], state = "*")
    dp.register_message_handler(search_style, text=['Жанр'], state = "*")
    dp.register_message_handler(search_album, text=['Альбом'], state = "*")
    dp.register_message_handler(find_song, state=FSMMusic.song)
    dp.register_message_handler(find_genre, state=FSMMusic.genre)
    dp.register_message_handler(find_artist, state=FSMMusic.artist)
    dp.register_message_handler(find_album, state=FSMMusic.album)
