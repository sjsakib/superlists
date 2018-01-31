Provisioning a new site
=======================

## Required packages

* nginx
* python3.6
* virtualenv + pip
* Git

eg, on Ubuntu:

    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install nginx git python36 python3.6-venv

## Nginx virtual host config

* see nginx.template.conf
* replace DOMAIN and USERNAME

## Systemd service

* see gunicorn-systemd.template.service
* replace DOMAIN and USERNAME

## Folder Structure

Assuming we have a folder account at /home/USERNAME

/home/USERNAME
└── sites
    ├── DOMAIN1
    │    ├── .env
    │    ├── db.sqlite3
    │    ├── manage.py etc
    │    ├── static
    │    └── virtualenv
    └── DOMAIN2
         ├── .env
         ├── db.sqlite3
         ├── etc
