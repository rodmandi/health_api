# Health API

Contains scripts for handling data flow

### Prerequisite

This module uses a number of open source projects to work properly:

* [Docker](https://www.docker.com/get-started)
* [Docker-compose](https://docs.docker.com/compose/install/)

### Introduction

This project contains an API that determines the true insurance value of a Patient comparing and selecting information from other sources.
The project has the following structure:
```
health_api
│   README.md
│   .gitignore  
│
└───main
│   │   run.py
│   │   requirements.txt
│   │   ...
│   └───tests
│   │   
│   │   ...
│   └───routing
│   │   
│   │   ...
│   └───core
│       │   
│       │   ...
│       
│   
└───insurers_api
    │   run.py
    │   requirements.txt    
    └───tests
        └───insurers_api 
            │   TestBaseApp.py
            │   ...
```
This Repository contains an API that uses Python, Flask and Docker for determine the true insurance value of a patient,
considering information from multiple sources.

In the folder main contains all the files that uses the "main API", the directory tests, 
contains the unit tests cases, for test the application, routing the blueprint for the Flask app, 
the core all the code that we the application is going to use in order to select the "true" insurance value.

The application will call the and endpoint that contains three different APIs located in the directory (insurers_api).
Considering that this type of projects can increase of each API can have multiple ways to received or return information, 
I proposed to use a Factory Method that helps to create and Abstract APIObject that will assist in the process for send a request.

In the directory insurers_api is demo API for testing purposes that accepts requests in three different methods
* http://localhost:6000/api1
* http://localhost:6000/api2
* http://localhost:6000/api3

Each method will return the default values proposed in the document https://docs.google.com/document/d/1fSVdED879ugvASeMNw1MfM9ymtlklUWaJjb0GDLprTo/edit
```
API1: {deductible: 1000, stop_loss: 10000, oop_max: 5000}
API2: {deductible: 1200, stop_loss: 13000, oop_max: 6000}
API3: {deductible: 1000, stop_loss: 10000, oop_max: 6000}
```
The main project will call the three apis and then considering the method on the directory core/algorithms/select_best_insurer.py 
the application will determine the true insurance value.

In order to understand how is working and the design of the application please check the following link:
https://docs.google.com/document/d/1HpQGBo2utfwI20xY3VHuoNh00dDW-oY2f4QrRzOii50/edit

### Setup 

1. Open a terminal and clone the repository
2. Use this command to build. This process will take around 10 minutes, this process will build the two applications
```sh
$ sudo make build
```

### Run the project

Considering the previous steps from the Setup section, in the same terminal go to directory called "insurers_api"
and run the following command

```sh
$ sudo make run
```

This will create a container with two enpoints one pointing to the port 7000 (The main project) 
and another one that contains 3 API's liven in the same endpoint but with the PORT 6000.

In order to check that the application is working is important to send the following request, via postman,
 or run in the terminal in the directory of the project  the following command
 
```sh
$ python3 test_request.py
```

The expected value considering the smoke tests will be the following result
```sh
{"result": {"deductible": "1000", "oop_max": "5000", "stop_loss": "10000"}, "status": "ok"}
```


### Stop process and clean 

Use this command to stop.
```sh
$ sudo make stop
```

Use this command to stop and remove all containers.
```sh
$ sudo make clean
```

Use this command to clean all images.
(this is usefull for developing new images and test with fresh)
```sh
$ sudo make purge
```


#### Resource API Endpoints 

In the following tables there is a description of each endpoint

| Endpoint Name | API 1 Insurance                                         |
|---------------|---------------------------------------------------------|
| Description   | Fetch a proposed insurance value related to the patient |
| HTTP Method   | POST                                                    |
| API URI       | http://localhost:6000/api1                              |
| Headers       | {  "Content-Type": "application/json" }                 |
| URL Params    | {}                                                      |


| Endpoint Name | API 2 Insurance                                         |
|---------------|---------------------------------------------------------|
| Description   | Fetch a proposed insurance value related to the patient |
| HTTP Method   | POST                                                    |
| API URI       | http://localhost:6000/api2                              |
| Headers       | {  "Content-Type": "application/json" }                 |
| URL Params    | {}                                                      |


| Endpoint Name | API 3 Insurance                                         |
|---------------|---------------------------------------------------------|
| Description   | Fetch a proposed insurance value related to the patient |
| HTTP Method   | POST                                                    |
| API URI       | http://localhost:6000/api3                              |
| Headers       | {  "Content-Type": "application/json" }                 |
| URL Params    | {}                                                      |


Change fetching emails date

* Go to *mongo-seed/import.sh* 
* In line 2, change the parameter --date  **5 minutes ago**

### Installing on Windows 10
First, you need to download [Ubuntu WSL](https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6#activetab=pivot:overviewtab)
and of course [Docker for Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows)

After installing docker, please expose the daemon by checking:
> Expose daemon on tcp://localhost:2375

and then, open Ubuntu WSL terminal, and run the commands below:
```sh
$ sudo apt-get update
$ sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
$ sudo apt-get update
$ sudo apt-get install docker-ce
$ sudo apt-get install build-essential
$ echo "export DOCKER_HOST=localhost:2375" >> ~/.bash_profile
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
```

and then, add this line using "sudo visudo"
> Defaults        env_keep += "DOCKER_HOST"

and you may need to run this command once your computer starts
```sh
sudo mount --bind /mnt/c /c
```
