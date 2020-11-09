import pyrebase

config = {
    "apiKey": "AIzaSyCsfxYkeZspL3jqgiRTVau8Ib6MrP-c55Q",
    "authDomain": "enstock-f376c.firebaseapp.com",
    "databaseURL": "https://enstock-f376c.firebaseio.com",
    "projectId": "enstock-f376c",
    "storageBucket": "enstock-f376c.appspot.com",
    "messagingSenderId": "164380283319",
    "appId": "1:164380283319:web:e18dd141988bc816d39832"
}
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

path_on_cloud = "logo3.png"
path_local = "logo3.png"
url_up = storage.child(path_on_cloud).put(path_local)
url_down = storage.child("logo3.png").get_url(url_up['downloadTokens'])
print(url_down)