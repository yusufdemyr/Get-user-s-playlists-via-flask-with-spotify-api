from flask_spotify_auth import getAuth, refreshAuth, getToken

#Add your client ID
# YOU SHOULD USE os.environ['CLIENT']
CLIENT_ID = "YOUR-CLIENT-ID"

#aDD YOUR CLIENT SECRET FROM SPOTIFY
# YOU SHOULD USE os.environ['SECRET']
CLIENT_SECRET = "YOUR-CLIENT-SECRET"

#Port and callback url can be changed or ledt to localhost:5000
PORT = "5000"
CALLBACK_URL = "http://127.0.0.1"

#Add needed scope from spotify user
SCOPE = "playlist-read-private,playlist-read-collaborative"
#token_data will hold authentication header with access code, the allowed scopes, and the refresh countdown
TOKEN_DATA = []


def getUser():
    return getAuth(CLIENT_ID, "{}:{}/callback".format(CALLBACK_URL, PORT), SCOPE)

def getUserToken(code):
    global TOKEN_DATA
    TOKEN_DATA = getToken(code, CLIENT_ID, CLIENT_SECRET, "{}:{}/callback".format(CALLBACK_URL, PORT))
    return TOKEN_DATA

def refreshToken(time):
    time.sleep(time)
    TOKEN_DATA = refreshAuth()

def getAccessToken():
    return TOKEN_DATA
