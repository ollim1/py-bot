# Python bot

Forks `-n` independent Chromium instances for location `-l` at interface scale `-s`. Requires ChromeDriver 98 in the directory `ext`.

## Setup
Download ChromeDriver 98 at [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads)
```
pip3 install virtualenv
virtualenv env
source env/bin/activate
python3 bot.py -l [full url] -n [instances] (-s [scale])
```
