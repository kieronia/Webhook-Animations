import requests,time
order = "1"
link1 = "https://ptb.discord.com/api/webhooks/777/dwakjADWDdwkadjadfwhoa" #make 2 webhooks and copy the link
link2 = "https://ptb.discord.com/api/webhooks/777/wdawaddaWEaDW" #you need 2 to seperate it otherwise itll show the previous pfp
message = "Demonstration from **https://github.com/kieronia/Webhook-Animations**" #honestly  - while ik this is simple please , if your gonna change it, don't claim you made this, I've put so many hours into my work and It breaks my heart to see it get around 5 stars, copied and pasted and sold etc
username = "OooooOooooOooo"
while True:
    with open("avatarlinks.txt", 'r') as f:
        for line in f.readlines():
            avatar = line.strip()
            data = {
                'content': message,
                'username': username,
                'avatar_url': avatar
            }
            if order == "1":
                webhook = link1
                order = "2"
            elif order == "2":
                webhook = link2 
                order = "1"

            e = requests.post(webhook, data=data).status_code
            if e != 204:
                time.sleep(15)
            time.sleep(1)
