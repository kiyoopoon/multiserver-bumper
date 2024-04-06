# Multi-server Auto Bump Bot
**Note: Ignore the first error for now, I will update this code later and give it sometime if it doesn't send right bump command make sure only disboard is allowed in the bump channel but it should work with all bots. Keep it deployed it will send all bump command but will take a few hours to work properly**

### Consider giving a star if it helped you 🌠
Bump all your servers automatically. It will send bump messages to each server with a 20 min interval between each bump.
This bot is written in python using discord.py-self library.

**Note: Using this bot for more than 4 servers might cause some problems**

**Consider joining https://discord.gg/8C98Tqkspq if you want to support me!**

### How to configure it?
First download the repo. Then go to the main.py file and replace `TOKEN` with your account token, then put your channel IDs in the `CHANNEL_IDS`. Finally change the `LOG_CHANNEL` with your log channel ID the bot will send the bump logs in that channel.

**Make sure you have python and discord.py-self installed if you want to do test run. But discord.py-self might break your regular discord.py lib**

### How to host it?
There is no trusted site that hosts self-bots. But you can use replit and uptime robot but it will not stay online always you will need to monitor it. You can use PolyNode but I don't have that much experience using it, so use at your own risk! I recommend using a vps.

PolyNode - https://polynode.works/
( PolyNode might be down sometimes, keep an eye on their discord server to get updates )

### How to host it in a VPS?
#### Easy way
If you already have a VPS then you just get my docker files and use those to build the bot easily. I maintain this docker container regularly.

First install docker.
**Linux VPS**
```
curl -fsSL https://get.docker.com -o install-docker.sh
sh install-docker.sh --dry-run
sudo sh install-docker.sh
```

All the commands are from the official docker install guide - [get.docker.com](https://get.docker.com/)

**Windows VPS**
If you have windows VPS then you just download the docker-cli
Download the installer using the download button at the top of the page, or from the [release notes](https://docs.docker.com/desktop/release-notes/). Open the `Docker Desktop Installer.exe` and follow the normal installation steps. Here is the official installation guide for windows - [Install Docker Desktop on Windows](https://docs.docker.com/desktop/install/windows-install/)

Run the command `docker version` to check if it's installed properly

After you have docker setup clone the repo, then cd inside the repo `cd multiserver-bumper`. Now you will need to build the docker container using `docker build -t multiserver-bumper`. Here the command uses the Dockerfile to build a new image, the `-t` flag tags your image which is `multiserver-bumper` in this case, and finally the `.` says that the Dockerfile is in the current folder. Wait for a while and after it's done run `docker run multiserver-bumper`. Done! Your self-bot should be online now :)

#### Manual way
If you don't want the docker way then you can go with the manual setup. First you will need to make sure you have the `venv` or `virtualenv` installed. Run `python3 -m venv --help` to check, if you don't have it installed then install it with this command
- For **linux** `sudo apt install python3-venv` [ Will install it globally, might face `externally-managed-environment` issue if you use `pip install virtualenv` ] or,
- For **windows** `pip install virtualenv`

After you have `venv` setup. You can now make the virtual environment run `python<version> -m venv <virtual-environment-name>` for example if you have `python version 3.12` and you want to name the virtual env `multiserver-bumper` then your command will be something like `python3.12 -m venv multiserver-bumper`. Use `python --version` to check your python versions.

Now we need to activate the virtual environment using this command
- For Unix/Linux based OS `source env/bin/activate`
- For Windows `env/Scripts/activate.bat`

Finally we now have our virtual environment so we can run `pip install -r requirements.txt` to install the discord.py-self [ Need the github version cause it's updated one ]

Now just run `python3 main.py` or `python main.py` to run the script :)

## Common errors
### discord.py-self error
If you installed discord.py-self library using pip you git get an error saying `API down` so I recommend you installing it from the github repo.

```
$ git clone https://github.com/dolfies/discord.py-self
$ cd discord.py-self
$ python3 -m pip install -U .
```

Run these command and it will install or replace your discord.py-self library. I ran into the issue but luckily there was this [issue here](https://github.com/dolfies/discord.py-self/issues/597) where I got the solve to it.

#### DeprecationWarning
If you get this error `DeprecationWarning: slash_commands is deprecated, use Messageable.application_commands instead.` after running the bot. Don't worry it will still work so just ignore it.

**To avoid all the issues I recommend you go with the docker container so that everything stays the same. Feel free to contact me on Discord or open an issue if you need any other help**

**Please not that discord.py-self library might break your original discord.py library so I recommend using codespace for testing**

### Note: Self bots are against Discord TOS and we do not encourage you to use self bots. This project was just done for educational purpose

![Preview](https://i.ibb.co/HrXrP0S/image-2.png)
