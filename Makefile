# Using $(lastword $(MAKEFILE_LIST)) and -f ... ensures that the $(MAKE) command uses the same makefile,
# even if that makefile was passed with an explicit path (-f ...) when make was originally invoked.
THIS_FILE := $(lastword $(MAKEFILE_LIST))

#### Parameters
RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(RUN_ARGS):;@:)

#### Tests
test: # Run all tests
	docker-compose exec bce-server pytest
	docker-compose exec bce-ui yarn test

test.server: # Run Server tests only
	docker-compose exec bce-server pytest

test.ui: # Run UI tests only
	docker-compose exec bce-ui yarn test

#### Django 
shell: # Access the Django Shell on the container
	docker-compose exec bce-server python manage.py shell

migrate: # Run migrations, accepts optional app name and migration name
	docker-compose exec bce-server python manage.py migrate $(RUN_ARGS)

migrations: # Generate migration files
	docker-compose exec bce-server python manage.py makemigrations

createsuperuser: # Create django super user
	docker-compose exec bce-server python manage.py createsuperuser

admin: # Open django admin in browser
	@make url.server | sed 's/$$/\/admin\//' | xargs open

#### Docker
url.server: # Print url for the API and copy it to clipboard
	@docker port bce_bce-server_1 | grep 8000 | sed 's/.*-> /http:\/\//' | pbcopy
	@echo `pbpaste`

url.ui: # Print url for the API and copy it to clipboard
	@docker port bce_bce-ui_1 | grep 8080 | sed 's/.*-> /http:\/\//' | pbcopy
	@echo `pbpaste`
