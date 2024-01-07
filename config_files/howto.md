# How To Use config files

This file is intended to help me remember what to do the day I change server.

- [How To Use config files](#how-to-use-config-files)
  - [Gunicorn](#gunicorn)
  - [Nginx](#nginx)

## Gunicorn

1. Move the gunicorn *service* file to `/etc/systemd/system/gunicorn.service`.
2. Move the gunicorn *socket* file to `/etc/systemd/system/gunicorn.socket`.
3. Start the socket : `sudo systemctl start gunicorn.socket` & `sudo systemctl enable gunicorn.socket`.
   1. Check for socket status : `sudo systemctl status gunicorn.socket`.
   2. Checl for socket file : `file /run/gunicorn.sock`
   3. Get log if needed : `sudo journalctl -u gunicorn.socket`
4. Update change to service :
   1. `sudo systemctl daemon-reload && sudo systemctl restart gunicorn`

## Nginx

1. Change the IP adress in the file to the new server at the 2 locations.
2. Copy the nginx file to `/etc/nginx/sites-available/blessedsleepseeker`.
3. Create a symlink to `sites-enabled` : `sudo ln -s /etc/nginx/sites-available/blessedsleepseeker /etc/nginx/sites-enabled`
4. Test then restart nginx : `sudo nginx -t`, `sudo systemctl restart nginx`
