TEST ?= discover -s tests -p *Test*.py

build:
	docker-compose -p insurance_api build
run:
	docker-compose -p insurance_api up --build
stop:
ifeq ($(shell docker ps|grep health-algo| wc -l), 0)
	docker-compose down
else
	-docker stop `docker ps -q --filter ancestor=insurance_api_health-algo`
endif
test:
	export DOMAIN=localhost
	CMD_CLEAN="python3 -m unittest $(TEST) -v" DOMAIN="localhost" docker-compose -p insurance_api up
clean:
	docker-compose down
	-docker stop `docker ps -aq`
	-docker rm `docker ps -aq`
purge:
	docker-compose down
	docker system prune
	-docker stop `docker ps -aq`
	-docker rm `docker ps -aq`
	-docker image rm `docker images -q`