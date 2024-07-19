A really really basic webpage with really basic authendication, this can be broken so easy

```bash 

mkdir Basic_auth

cd Basic_auth

wget https://github.com/jrd3n/Basic_Authentication/archive/refs/heads/main.zip

unzip main.zip

pip install flask  --break-system-packages

(crontab -l 2>/dev/null; echo "@reboot /usr/bin/python3 /home/pi/Basic_auth/Basic_Authentication-main/app.py") | crontab -

sudo reboot -n

```