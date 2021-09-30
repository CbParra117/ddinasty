NAME=dynasty
TAG=$$(git log --pretty=format:"%h" -1)
ENV?=staging
CURRENT_DATE=$(shell date +%Y%m%d%H)
IMG?=${NAME}:${ENV}-${CURRENT_DATE}-${TAG}
LATEST=${NAME}:latest

build:
	docker build --no-cache -t ${IMG}  .

tag:
	docker tag ${IMG} 352631681906.dkr.ecr.us-east-1.amazonaws.com/${IMG}

push:
	docker push 352631681906.dkr.ecr.us-east-1.amazonaws.com/${IMG}

deploy-staging:
	make build
	make tag
	make push

deploy-production:
	$(eval ENV=production)
	make build
	make tag
	make push
