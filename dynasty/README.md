# Dynasty
> This microservice is for sending emails, which allows us to customize different brands, templates and keep track of them.

### Stack
* gunicorn
* Django 3.2

> Ready-To-Deploy
> Getting a `Django` 3.2 app up in no time. In this project, gunicorn is used as a WSGI. 

### Requirements

* [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) - Docker Container

### Getting Started

In the root level of this repository, create a file named `.env` and add environment variables. For example:

```bash
##############################
#    Environment
##############################

# This will let the script at `./django/config/start.sh` what django commands
# need to be executed. For this is a development environment we will flush
# the database. When creating a production configuration set this variable
# to true.

PRODUCTION=False

##############################
#    Django Framework
##############################

DEBUG=True
SECRET_KEY=#cn!!#$m+xt!v3mg9m&m513u@=nslx1ooh)7np!$7@6s2)vi44#E%#
LANGUAGE_CODE=es-MX
TIME_ZONE=America/Mexico_City
USE_I18N=True
USE_L10N=True
USE_TZ=False

DATABASE_ENGINE=django.db.backends.mysql
DATABASE_HOST=
DATABASE_PORT=3306
DATABASE_NAME=dynasty_db
DATABASE_USER=dynasty_db
DATABASE_PASSWORD=dynasty_db

# SendGrid
SENDGRID_API_KEY=

ADMIN_USERNAME=dynasty_admin
ADMIN_EMAIL=dynasty@myproject.com
ADMIN_PASSWORD=yourpassword

##############################
#    MEDIA
##############################

IMAGE_FOLDER=/images/

##############################
#    DJANGO ADMIN INTERFACE
#    https://github.com/fabiocaccamo/django-admin-interface
##############################

INSTALL_ADDITIONAL_THEMES=True
```

### HOW TO USE

**Get token authentication (JWT)**

```sh
curl -X POST http://localhost:5004/api/token/ \
-H "Content-Type: application/json" \
-d '{
    "username": "<user>",
    "password": "<yourpassword>"
}'
```

### Know More?

* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Editor Config](https://editorconfig.org/) The EditorConfig project consists of a file format for defining coding styles
* [JWT](https://jwt.io/introduction/) JWT Documentation
* [Git Flow](https://danielkummer.github.io/git-flow-cheatsheet/) Git Flow
* [Git Flow Bitbucket](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) Git Flow Bitbucket

### Technologies

| Name              | README                                   |
| ----------------- | ---------------------------------------- |
| MySQL             | [https://www.mysql.com/](https://www.mysql.com/) |
| Python 3.8        | [https://docs.python.org/3.7](https://docs.python.org/3.8) |
| Django            | [https://docs.djangoproject.com/en/3.2/](https://docs.djangoproject.com/en/3.2/) |
| Docker Compose    | [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/) |
| Docker            | [https://docs.docker.com/install/linux/docker-ce/ubuntu/](https://docs.docker.com/install/linux/docker-ce/ubuntu/) |

### Change Logs
- **1.0.0**
  - Initial release
