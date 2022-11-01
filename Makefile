tunel:
	minkube tunnel

build:
	docker build -t data-generator:1.0.2 .

restart:
	kubectl rollout restart deploy -n jarvis

see:
	kubectl get pods -n jarvis

all: build restart see