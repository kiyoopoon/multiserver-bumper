# Multi-server Auto Bump Bot

~~**Note: Ignore the first error for now, I will update this code later and give it sometime if it doesn't send the right bump command. Make sure only Disboard is allowed in the bump channel, but it should work with all bots. Keep it deployed; it will send all bump commands but will take a few hours to work properly**~~ [ Fixed ]

### Consider giving a star if it helped you 🌠

Bump all your servers automatically. It will send bump messages to each server with a 20-minute interval between each bump. This bot is written in Python using the `discord.py-self` library.

**Note: Using this bot for more than 4 servers might cause some problems.**

**Wanna join my Discord server? [Join now!](https://discord.gg/8C98Tqkspq) :)**

**I might have missed something or maybe documented something wrong, so feel free to contact me on Discord if you face any problem/something needs to be corrected or open an issue here! My Discord: `kiyoopoon` or you can also ping me in my server**

## How to configure it?
1. First, download the repo.
2. Go to the `main.py` file and replace `TOKEN` with your account token.
3. Put your channel IDs in the `CHANNEL_IDS`.
4. Change the `LOG_CHANNEL` with your log channel ID where the bot will send the bump logs.

**Make sure you have Python and `discord.py-self` installed if you want to do a test run. Note that `discord.py-self` might break your regular `discord.py` library.**

## How to host it?
I don't know any trusted site that hosts self-bots. However, you can use Replit and Uptime Robot, but it will not stay online always; you will need to monitor it. You can use PolyNode, but I don't have much experience with it, so use it at your own risk! I recommend using a VPS.

- [PolyNode](https://polynode.works/)
(PolyNode might be down sometimes, keep an eye on their Discord server for updates.)

## How to host it on a VPS?

### Easy way

If you already have a VPS, you can use my Docker files to build a Docker container and the bot easily.

First, install Docker.

**Linux VPS**

```sh
curl -fsSL https://get.docker.com -o install-docker.sh
sh install-docker.sh --dry-run
sudo sh install-docker.sh
```

All the commands are from the official Docker install guide - [get.docker.com](https://get.docker.com/)

**Windows VPS**

If you have a Windows VPS, download the Docker CLI:
Download the installer using the download button at the top of the page, or from the [release notes](https://docs.docker.com/desktop/release-notes/). Open the `Docker Desktop Installer.exe` and follow the normal installation steps. Here is the official installation guide for Windows - [Install Docker Desktop on Windows](https://docs.docker.com/desktop/install/windows-install/)

Run the command `docker version` to check if it's installed properly.

After you have Docker set up, clone the repo, then navigate inside the repo `cd multiserver-bumper`. Now you will need to build the Docker container using `docker build -t multiserver-bumper .`. This command uses the Dockerfile to build a new image. The `-t` flag tags your image, which is `multiserver-bumper` in this case, and the `.` specifies that the Dockerfile is in the current folder. Wait for a while, and after it's done, run `docker run multiserver-bumper`. Done! Your self-bot should be online now :)

### Manual way

If you don't want to use Docker, you can go with the manual setup. First, ensure you have `venv` or `virtualenv` installed. Run `python3 -m venv --help` to check. If you don't have it installed, then install it with this command:

- For **Linux**:
  ```sh
  sudo apt install python3-venv
  ```
  This will install it globally. You might face the `externally-managed-environment` issue if you use `pip install virtualenv`.
  
- For **Windows**:
  ```
  pip install virtualenv
  ```

After you have `venv` set up, create the virtual environment by running:
```sh
python<version> -m venv <virtual-environment-name>
```
For example, if you have Python version 3.12 and you want to name the virtual environment `multiserver-bumper`, then your command will be:
```sh
python3.12 -m venv multiserver-bumper
```
Use `python --version` to check your Python version.

Now, activate the virtual environment using this command:
- For Unix/Linux-based OS:
  ```sh
  source multiserver-bumper/bin/activate
  ```
- For Windows:
  ```
  multiserver-bumper\Scripts\activate.bat
  ```
Replace `multiserver-bumper` with your virtual environment name.

Finally, install the required packages by running:
```sh
pip install -r requirements.txt
```
This will install `discord.py-self``
**Important Note: You need the GitHub version because it's the updated one. The PyPI one is outdated!**

Now, just run `python3 main.py` or `python main.py` to run the script :)


### Checking
To check if your bot is running you can run the `?bing` command yes it's bing not ping :) 

## Common errors

### discord.py-self error [ Fixed ]
~~If you installed the `discord.py-self` library using pip, you might get an error saying `API down`. I recommend installing it from a GitHub fork as it was fixed there.~~

~~`
git clone https://github.com/ye4241/discord.py-self
cd discord.py-self
python3 -m pip install -U .
`~~

~~Run these commands and it will install or replace your `discord.py-self` library. I ran into the issue but luckily found the solution [here](https://github.com/dolfies/discord.py-self/issues/597).~~

### DeprecationWarning [ Fixed ]
~~If you get this error `DeprecationWarning: slash_commands is deprecated, use Messageable.application_commands instead.` after running the bot, don't worry, it will still work, so just ignore it.~~

**To avoid issues, I recommend using the Docker container to ensure consistency. Feel free to contact me on Discord or open an issue if you need any help. Contributions and PRs are also welcome!**

**Please note that using self-bots is against Discord TOS, and we do not encourage you to use self-bots. This project was done for educational purposes only ;)**

![Preview](https://i.ibb.co/HrXrP0S/image-2.png)