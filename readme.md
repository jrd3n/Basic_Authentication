```bash 

mkdir Basic_auth

wget https://github.com/jrd3n/XSS-comment-box-example/archive/refs/heads/main.zip

unzip main.zip

pip install flask  --break-system-packages

(crontab -l 2>/dev/null; echo "@reboot /usr/bin/python3 /home/pi/Basic_auth/XSS-comment-box-example-main/app.py") | crontab -

sudo reboot -n


```