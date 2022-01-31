from twitchAPI.twitch import Twitch
from twitchAPI.twitch import Twitch
import requests

while True:
    try:
        twitch = Twitch('your app client id','your app client secret')
        break
    except:
        apc=input("Please Enter Your App Client ID: ")
        aps=input("Please Enter Your App Client Secret: ")
        twitch = Twitch(apc,aps)
        break

def twitchfolowing(user):
    try:
        chatters = requests.get(f"https://tmi.twitch.tv/group/user/{user}/chatters").json()
        streamerid=twitch.get_users(logins=user)["data"][0]["id"]
        viewers=chatters["chatters"]["viewers"]
        for v in viewers:
            personid=twitch.get_users(logins=v)["data"][0]["id"]
            followstatus=twitch.get_users_follows(from_id=personid,to_id=streamerid)["total"]
            with open(f"{user}.txt",'a') as f:
                if followstatus != 1:
                    f.write(v+" -----> Yes \n")
                else:
                    f.write (v+" -----> No \n") 
            print(f"saved in {user}.txt")
    except Exception as e:
        print(f"somthing went wrong: {e}")

streamer=input("please Enter Streamer Name: ")
twitchfolowing(streamer)
