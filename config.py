import os


class Config(object):
    API_HASH = os.environ.get("API_HASH", "96985c2aaea6c75408528909b7e18879")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    TELEGRAM_API = os.environ.get("TELEGRAM_API", "26728872")
    OWNER = os.environ.get("OWNER", "1705634892")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "Itsme123i")
    PASSWORD = os.environ.get("PASSWORD", "123i")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://python21java:<8ZFGYMKJCqAPwsiO>@cluster0.4ieuy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOGCHANNEL = os.environ.get("LOGCHANNEL", "-1002288135729") 
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
