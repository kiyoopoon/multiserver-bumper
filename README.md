# Multiserver Auto Bump Bot

**Note: Ignore the first error for now, I will update this code later and give it sometime if it doesn't send right bump command make sure only disboard is allowed in the bump channel but it should work with all bots. Keep it deployed it will send all bump command but will take a few hours to work properly**

🌠 - Consider giving a star if it helped you

Bump all your servers automatically. It will send bump messages to each server with a 20 min intreval between each bump.
This bot is written in python using discord.py-self library.

**Note: Using this bot for more than 4 servers might cause some problems**

Consider joining https://discord.gg/8C98Tqkspq if you want to support me!

- How to configure it?

First download the repo. Then go to the main.py file and replace `TOKEN` with your account token, then put your channel IDs in the `CHANNEL_IDS`. Finally change the `LOG_CHANNEL` with your log channel ID the bot will send the bump logs in that channel.

**Make sure you have python and discord.py-self installed if you want to do test run. But discord.py-self might break your regular discord.py lib**

- How to host it?

There is no trusted site that hosts self-bots. But you can use replit and uptime robot but it will not stay online always you will need to monitor it. You can use PolyNode but I don't have that much exprerience using it, so use at your own risk! I recommend using a vps.

PolyNode - https://polynode.works/
( PolyNode might be down sometimes, keep an eye on their discord server to get updates )

## discord.py-self error
If you installed discord.py-self library using pip you git get an error saying `API down` so I recommend you installing it from the github repo.

```
$ git clone https://github.com/dolfies/discord.py-self
$ cd discord.py-self
$ python3 -m pip install -U .
```

Run these command and it will install or replace your discord.py-self library. I ran into the issue but luckly there was this [issue here](https://github.com/dolfies/discord.py-self/issues/597) where I got the solve to it.

**Please not that discord.py-self library might break your original discord.py library so I recommend using codespace for testing**

### Note: Self bots are against Discord TOS and we do not encourage you to use self bots. This project was just done for educational pourpose

![Screenshot 2023-11-02 133736](https://github.com/kiyoopon/multiserver-bumper/assets/87245088/eb842b7b-205e-474a-a004-a26fb2972395)
