import pyrebase
from aiogram import types
from create import dp
from create import bot

firebaseConfig = {
  'apiKey': "AIzaSyAnn4DrW2ixhH49ebkZvZ6Xx5S1QlilfFw",
  'databaseURL': "https://arvazbase-default-rtdb.firebaseio.com",
  'authDomain': "arvazbase.firebaseapp.com",
  'storageBucket': "arvazbase.appspot.com",
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
    # await bot.send_message(message.from_user.id, url)
    await bot.send_audio(message.from_user.id, url, performer="Performer", title="Title")


@dp.message_handler(lambda message: 'S1' in message.text)
async def text(message: types.Message):
  data = db.child('song').child('s1').get()
  cloudfilename = data.val()['title']
  url = storage.child('songs').child(cloudfilename).get_url(None)
  # await bot.send_message(message.from_user.id, 'url')
  await bot.send_audio(message.from_user.id, url, performer = "Performer", title = "Title")

@dp.message_handler(lambda message: 'S2' in message.text)
async def text(message: types.Message):
  data = db.child('song').child('s2').get()
  cloudfilename = data.val()['title']
  url = storage.child('songs').child(cloudfilename).get_url(None)
  await bot.send_audio(message.from_user.id, url, performer = "Performer", title = "Title")

@dp.message_handler(lambda message: 'S3' in message.text)
async def text(message: types.Message):
  data = db.child('song').child('s1').get()
  cloudfilename = data.val()['title']
  url = storage.child('songs').child(cloudfilename).get_url(None)
  await bot.send_audio(message.from_user.id, url, performer = "Performer", title = "Title")
