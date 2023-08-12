from steam import Steam
from decouple import config

KEY = config("39864BB6D6F58565CFF414BD1280495D")

app_id = 782330
steam = Steam(KEY)

user = steam.apps.get_app_details(app_id)
print(user)