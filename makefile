.PHONY: login build deploy

DEFAULT_TAG = latest
TAG ?= $(DEFAULT_TAG)

login:
	docker login

build:
	docker build . -t dockliu/chatgpt-token-calculator:$(TAG)

deploy: login build
	docker push dockliu/chatgpt-token-calculator:$(TAG)
