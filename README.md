# Evaluation Platform for FG-AI4H.
![AI4H Logo](Logo-FG-AI4H.png)
## Features

- **Custom evaluation protocols and phases**: We allow creation of an arbitrary number of evaluation phases and dataset splits, compatibility using any programming language, and organizing results in both public and private leaderboards.

- **Remote evaluation**: Certain large-scale challenges need special compute capabilities for evaluation. If the challenge needs extra computational power, challenge organizers can easily add their own cluster of worker nodes to process participant submissions while we take care of hosting the challenge, handling user submissions, and maintaining the leaderboard.

- **Evaluation inside environments**: EvalAI lets participants submit code for their agent in the form of docker images which are evaluated against test environments on the evaluation server. During evaluation, the worker fetches the image, test environment, and the model snapshot and spins up a new container to perform evaluation.

- **CLI support**: [evalai-cli](https://github.com/Cloud-CV/evalai-cli) is designed to extend the functionality of the EvalAI web application to your command line to make the platform more accessible and terminal-friendly.

- **Portability**: EvalAI is designed with keeping in mind scalability and portability of such a system from the very inception of the idea. Most of the components rely heavily on open-source technologies – Docker, Django, Node.js, and PostgreSQL.

- **Faster evaluation**: We warm-up the worker nodes at start-up by importing the challenge code and pre-loading the dataset in memory. We also split the dataset into small chunks that are simultaneously evaluated on multiple cores. These simple tricks result in faster evaluation and reduces the evaluation time by an order of magnitude in some cases.

## Project Structure
```
├── apps                                                      #Django applications   
│   ├── challenges                                            #Handles creating, modifying and deleting challenges
│   ├── hosts                                                 #Functionalities for challenge hosts
│   ├── participants                                          #Functionalities for challenge participants
│   ├── jobs                                                  #Handles processing and evaluating submission
│   ├── web
│   ├── accounts
│   └── base
├── docker                                                    #Contains Dockerfiles, environment variables and settings
│   ├── dev
│   └── prod
├── frontend                                                 
│   └── src
│       ├── css
│       ├── fonts
│       ├── js                                                #Important for Angular Controllers and hosting settings
│       └── views
├── scripts                                                   #Scripts provided by EvalAi that make your life easier
│   ├── deployment
│       ├── deploy
│       └── push
│   ├── migration
│   ├── tools
│   └── workers                                               #Contains important code for the submission/code_upload workers
├── settings                                                  #Backend settings for the entire project, depending on environment
│   ├── common.py
│   ├── dev.py
│   ├── prod.py
│   └── test.py
├── docker-compose-production.yml                             #Necessary for starting production environment
├── manage.py                                                 #Very important Django tool; allows admin access, DB migration etc.
└── README.md
```
## Installation instructions

We are currently running three instances on AWS (EC2) hosting three different environments: dev, staging and production. To access those instances you need an AWS account and access permission granted by us. Cloning this repo will not reproduce the working project, as key configurations are not pushed here. 

1. **Demo** - 18.158.39.173:8888 (EvalAi), 18.158.39.173:8000/admin (admin view, requires auth)
2. **Production-Staging** - health.aiaudit.org (EvalAi), health.aiaudit.org/admin
3. **Production** - 18.158.223.90 (EvalAi), 18.158.223.90:8000/admin

The staging instance corresponds with the staging branch, whereas the production environment corresponds with the master branch. We recently decided to update the staging branch with the new EvalAi version (as of Feb 21) and have created a temporary updated staging brach. We are working on merging the two soon. The old staging still contains the updated frontend, while the new one has been updated to enable SSL.

### How do I access the instances?

Once you have been granted access on AWS, you should be able to view all instances at the Cloud9 IDE. Connect to the desired instance and you will see the file system as well as the terminal access. We usually keep the projects running on the instances, but you can manually start them up again. Change into the project folder and run:

```
docker-compose up 
```
or
```
sudo docker-compose -f docker-compose-production.yml up

```
depending on which environment you are using.

### How do I access the project itself?

The project is structured into multiple docker containers, separating backend, frontend and worker nodes. Once the containers are built and are running, simply changing the source code won't so anything. There are two options:

1. **Access the running containers** and change the source code from within:
```
sudo docker exec -it <CONTAINER_ID> /bin/bash
```
2. **Re-build the project**. This option is useful should one or more containers repeatedly fail to execute. 
```
sudo docker-compose -f docker-compose-production.yml build
```
Once the project is re-build you will have a completely new set of images. Depending on how often you re-build, Docker will start to take up a lot of disk space. To solve this, run:
 ```
sudo docker system prune -a
```
Note, that this **will delete all containers, images and networks within Docker**. 

### How do I submit a docker image to a challenge?
To submit to the platform, you need to log in as a verified user. For testing purposes this is the user **participant**. 
As all of our Audits are docker-based, you will have to use the command-line tool [EvalAi-Cli](https://github.com/Cloud-CV/evalai-cli) for submission.
1. The client is by default configured to submit to the original EvalAi platform. Thus, the submission host needs to be change before sumission:
```
evalai host -sh <HOST_IP:8000>
```
2. Sign up for Challenge and Participant Team on the plaftorm
3. Submission.
```
evalai login
evalai set_token <usr_token>
evalai push <image>:<tag> --phase <phase_name> 
```

## Task Overview

Task | Description | Stage | Assigned To
--- | --- | --- | --- 
Debug Worker| The worker nodes in staging and production aren't starting. | DOING | Elora
Fix Static Files| The static files in AWS cannot be accessed. | DOING | Steffen
Integrate Model Zoo | Integrate the model zoo (HPI) into EvalAi | DOING | Kamran
Write Eval Script | Write an eval. script for diabetic retiopathy and offer as Auditing | TODO | Danny, Elora
Adapt the questionnaire | Adapt questions and frontend of questionnaire | TODO | ----
Configure K8s | Configure the cluster in AWS to connect with workers and run evaluation | TODO | ----
Integrate Data Package | Make datasets stored accessible for evaluation in AWS. Configure EvalAi to use them. | TODO | ----
Change EvalAi Auth | Change the Auth system to AWS Cognito for universal user management over all packages. | TODO | ----
Set up email server | Set up an email server on EvalAi, so people can register. | TODO | ----
Integrate EvalAi Cli in UI | Currently the image upload is made through a command-line tool. Integration into UI would be good. | TODO | ----

##Testing
