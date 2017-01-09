# comp4560museum

## Dev
**Vagrant** and **virtual box** are required
`vagrant up` to start up the local dev vm
`vagrant ssh` to login into the vm  

the system of the virtual box is ubuntu. provision shell script is all written in the file `provision.sh`. This script will install all the python dev environment and mysql database into the vm. Also it will install all required python library listed in `requirements.txt`

### Web Frontend

For the project, frontend is developed by using **Angular2**  

**Nodejs** and **npm or yarn** are required

All the frontend end part code are placed in **mzm-frontend** folder.

Before start development, need to run `npm install` inside the forlder to install all dependences.
To run live-reload dev server, run the command `npm start`.

More infomation please have a look at the readme file in that folder.

### mobile

please checkout the readme inside **mzm-mobile** folder

### Backend

The Backend framework for this project is Django web framework.

To run the dev server, go to the **mzm** folder then run the command `python manage.py runserver 0.0.0.0:8000` inside the vagrant machine. You can then visit the api at **192.168.66.88:8000** (e.g. the admin page is at 192.168.66.88:8000/admin)

In the **mzm** folder, need to create a new file named **.env** to store environment variables such as database config.

### database
All the database config should be finished at provision phase. But you still need to run the **data_importer_fish.py** to import initial data into database with python3.5 inside the vm.

## Deploy

This project is using frontend-backend separate architecture. So we can have both web and mobile side to use the same backend. Therefore, web and backend could be deployed to different server. In current case, frontend and backend are on same server but on different domain (http://ebony.cs.umanitoba.ca/ and http://penguin.cs.umanitoba.ca/).

The web server used by this project in production is nginx. the config example is **museum_nginx.conf.example** in the **mzm** folder.

Django and nginx are bridged by **uwsgi**, everytime after deploy need to run `uwsgi -x uwsgi_conf.xml` to pull up the django server.

For frontend, run `npm build:prod` to build the project. The root folder in nginx config should point to the **dist** folder.






