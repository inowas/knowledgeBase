# Knowledge base docker-compose project

# Installation

* clone this repo
* clone the knowledgebase repo
* copy .env.dist file to .env and adapt it

* connect to web-container

`docker-compose exec web bash`

* Run fixtures

`./build/loadInitialFixtures.sh`

* Create Users

`python manage.py createsuperuser`
