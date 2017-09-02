# api-demo

### Requirements

* docker
* docker-machine
* docker-swarm
* git
* docker account


### Local install and developent


1.
```
    git clone git@github.com:cornelv/api-demo.git
```

2. 

```
    cd api-demo
```

3.
```
    cp env .env
```

4. 

edit .env file, add random credentials, if local switch to DEBUG=1

5.

```
    docker-compose build
```

5.

```
    docker-compose up
```

6. 

In a new terminal
```
    docker exec -ti apidemo_web_1 bash
```

7.
```
    python api.py
```

### stage install 

TODO:
- add Oauth 2 to API 
- create a docker image
- deploy to digital ocean with docker-swarm