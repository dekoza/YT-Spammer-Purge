# yt-spam-purge

[![ci](https://github.com/dekoza/yt-spam-purge/workflows/ci/badge.svg)](https://github.com/dekoza/yt-spam-purge/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://dekoza.github.io/yt-spam-purge/)
[![pypi version](https://img.shields.io/pypi/v/yt-spam-purge.svg)](https://pypi.org/project/yt-spam-purge/)
[![gitter](https://badges.gitter.im/join%20chat.svg)](https://gitter.im/yt-spam-purge/community)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Easily scan for and delete scam comments on your YouTube channel.

This is REWRITE of the tool made by ThioJoe. I want to refactor it into a proper library with CLI and utilizing async for blazing-fast operation.


<hr>
Part of original README:

**What Is This?** - Allows you to filter and search for spammer comments on your channel and other's channel(s) in many different ways AND delete/report them all at once (see features below).

**How to Download:** Click the "[Releases](https://github.com/ThioJoe/YouTube-Spammer-Purge/releases)" link on the right, then on the latest release, under 'Assets' click to download "YTSpammerPurge.exe". (You might have to click "Assets" to view the files for the release)
> * [Linux Setup Instructions](https://github.com/ThioJoe/YouTube-Spammer-Purge/wiki/Linux-Installation-Instructions)
> * [MacOS Setup Instructions](https://github.com/ThioJoe/YouTube-Spammer-Purge/wiki/MacOS-Instructions)
> * (Windows installation not necessary if using exe file. But see how to set up required API key [on this page](https://github.com/ThioJoe/YT-Spammer-Purge/wiki/Instructions:-Obtaining-an-API-Key))

### **Detailed Info & Documentation →** Visit the wiki [(Click Here)](https://github.com/ThioJoe/YT-Spammer-Purge/wiki) for more detailed writeups on the program

## Features

* 15 Different Filtering Methods
  * **Auto-Smart Mode (Recommended)**: Automatically detects multiple spammer techniques
  * **Sensitive-Smart Mode**: More likely to catch elusive spammers, but with more false positives
  * **Scan by Channel ID**: Enter a known spammer's channel link or ID directly
  * **Scan Usernames** for: Individual special characters, individual strings, or using a custom Regex expression
  * **Scan Comment Text**: (Same 3 options as above)
  * **Scan Usernames and Comment Text** simultaneously: (Same 3 options as above)
  * **ASCII Mode**: Scan Usernames for non-ASCII special characters (three different sensitivities)
* 4 Different Scanning Modes
  * Scan a **single video**
  * Scan **Recent Videos** (Up to 5)
  * Scan recent comments across **entire channel** (all videos)
  * *Experimental*: Scan a **community post**
* Automatic deletion of all found comments (after confirmation), as well as the option to ban them
* Options to instead Report spam comments or 'Hold For Review'
* Ability to create config file to skip pre-set options
* Rich text log files
* 'Recovery Mode' option to re-instate previously deleted comments
* Displays "match samples" after printing comments list to easily spot false positives
* Ability to exclude selected authors before deletion / reporting

## Purpose

Recently, there has been a massive infestation of spam on YouTube where fake impersonator accounts leave spam/scam replies to hundreds of users on a creator's videos. For some god-forsaken reason, YouTube offers no way to delete all comments by a specific user at once, meaning you must delete them one by one BY HAND.

YouTube offers a functionality to ban a user, but it does NOT delete previous comments. Therefore I created this script to allow you to instantly purge their spam replies, and since then it has evolved into a fully featured spam scanner as well. **IT DOES NOT PREVENT SPAMMERS - It only makes it easier to delete them when they show up!** YouTube still must implement better native tools for dealing with spammers.

## 🤔 Pro-Tip If This Seems Sketchy: Limiting The App's Access 🤔

If you feel sketched out about giving the app the required high level permissions to your channel (very understandable), you could instead use the app in 'moderator mode' (set in the config file). First, some context: When you grant access to another channel to be a moderator for your channel, they are able to mark comments for 'held for review', and this permission works through the API as well.

_Therefore,_ what you could do is create an _blank dummy-google-account_ with nothing on it except a empty new channel. Then you can grant _that_ channel permission to be a moderator, and use the app through _the dummy moderator account_. **This way, you know that the app will never have the ability to do more than mark comments as held for review** (which the app supports) on your main channel, and have no other access to your account's data. You just won't be able to ban the spammers through this app directly, but you can still remove/hide their comments instead of deleting them. Just make sure to create the google cloud API project on the dummy account instead.

Read some additional details about 'moderator mode' on the [wiki page here](https://github.com/ThioJoe/YT-Spammer-Purge/wiki/Moderator-Mode-&-Limiting-Permissions).

## Usage Notes -READ THIS

1. To use this script, you will need to obtain your own API credentials file by making a project via the Google Developers Console (aka 'Google Cloud Platform'). The credential file should be re-named `client_secret.json` and be placed in the same directory as this script. [See Instructions Here](https://github.com/ThioJoe/YT-Spammer-Purge/wiki/Instructions:-Obtaining-an-API-Key).

2. **IF IT FREEZES** while scanning, it is probably because you clicked within the command prompt window and entered "selection mode" which pauses everything. **To unfreeze it, simply right click within the window, or press the Escape key.**

3. I'm a total amateur, so if something doesn't work I'll try to fix it but might not even know how, so don't expect too much. Therefore **I OFFER NO WARRANTY OR GUARANTEE FOR THIS SCRIPT. USE AT YOUR OWN RISK.** I tested it on my own and implemented some failsafes as best as I could, but there could always be some kind of unexpected bug. You should inspect the code yourself.



<hr>


## Requirements

yt-spam-purge requires Python 3.10 or above.

<details>
<summary>To install Python 3.10, I recommend using <a href="https://github.com/pyenv/pyenv"><code>pyenv</code></a>.</summary>

```bash
# install pyenv
git clone https://github.com/pyenv/pyenv ~/.pyenv

# setup pyenv (you should also put these three lines in .bashrc or similar)
export PATH="${HOME}/.pyenv/bin:${PATH}"
export PYENV_ROOT="${HOME}/.pyenv"
eval "$(pyenv init -)"

# install Python 3.10
pyenv install 3.10.0

# make it available globally
pyenv global system 3.10.0
```
</details>

## Installation

With `pip`:
```bash
python3.10 -m pip install yt-spam-purge
```

With [`pipx`](https://github.com/pipxproject/pipx):
```bash
python3.10 -m pip install --user pipx

pipx install --python python3.10 yt-spam-purge
```

