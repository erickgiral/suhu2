import pyrebase
from pusher_push_notifications import PushNotifications

config = {
    'apiKey': "AIzaSyAVy30wClxCZ2s6zeMEX1BEEm8muw1_BO8",
    'authDomain': "datasuhu-8d46e.firebaseapp.com",
    'databaseURL': "https://datasuhu-8d46e.firebaseio.com",
    'projectId': "datasuhu-8d46e",
    'storageBucket': "datasuhu-8d46e.appspot.com",
    'messagingSenderId': "1028790303658"
  }
firebase = pyrebase.initialize_app(config)

db=firebase.database()
pn_client = PushNotifications(
    instance_id='cae714a5-ba66-4c41-a5f3-e4675e2a6439',
    secret_key='D8796D2B7704CB5785EC46E830F895E48DC1590399C5527DEC47DC595B760430',
)

def stream_handler(message):
    print(message)
    if(message['data'] >= 38):
        response = pn_client.publish(
            interests=['hello'],
            publish_body={
                'apns': {
                    'aps': {
                        'alert': 'Hello!',
                    },
                },
                'fcm': {
                    'notification': {
                        'title': 'Suhu menunjukan lebih dari 38°C',
                        'body': 'Mohon periksa keadaan bayi!',
                    },
                },
            },
        )

        print(response['publishId'])

my_stream = db.child("suhu").stream(stream_handler,None)