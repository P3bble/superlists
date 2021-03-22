Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.6
* virtualenv + pip
* Git
  
  eg, on Ubuntu:

    sudo add-apt-repository ppa:fkrull/deadsnakes
    sudo apt-get install nginx git python36 python3.6-venv

## Nginx Virtual Host config

* see nginx.tempalate.conf
* replace SITENAME with, e.g., stating.my-domain.com

## System service

* see gunicorn-systemd.template.service
* replace SITENAME with, e.g., staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

```
/home/username
|__sites
   |__SITENAME
       |-- database
       |-- source
       |-- static
       |-- virtualenv
```