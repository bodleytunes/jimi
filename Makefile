.PHONY: start

default: start

start:
	docker-compose build && docker-compose up -d

start-foreground:
	docker-compose build && docker-compose up