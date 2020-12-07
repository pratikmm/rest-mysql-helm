## REST API MYSQL Kubernetes

### Description
This repository contains application code, Dockerfile and Helm charts to deploy REST application and Mysql DB on kubernetes where REST api which connects to Mysql DB.

#### Kubernetes Resoruces
* **Kubernetes Secret**
    * MYSQL_ROOT_PASSWORD is getting created using Helm charts.
    * Using Autogenerate function of Helm to create this Alphanumeric password of length 20.
    * Mounting this secret on REST application and MYSQL DB microservice as Environment variable
* **REST application**
    * Application is written in Python using Flask framework to create REST API.
    * API makes ```SELECT 'Hello World!``` query on MYSQL DB.
* **MYSQL DB**
    * MYSQL DB(5.6) deployed on Persistant volume to retain the data in case of pod failure.
    * MYSQL DB deployment is done in stateful manner.

#### Folder structure
```
rest-mysql-helm
|───helm
|   ├───flask-mysql
|   │   ├───charts
|   │   └───templates
|   |───secret-pvc
|   |   ├───charts
|   |   └───templates
|───src
|   |───main.py
|   |───db_connection.py
|   └───gunicorn.py
|───Dockerfile
|───requirements.txt
└───README.md
```

#### Deployment

##### Pre-requisites
* **Git client**
Install the Git client to clone the repository on local.
* **Kubernetes Environemnt**
Please make sure kubernetes environment is up and kubectl client is configured with the cluster. You can use Minikube cluster on your local.
* **Helm client**
    * Configure Helm v3 to deploy application Helm charts. 

##### Deployment Steps
Below steps are for kubernetes environment is created using minikube.
**Clone the repository**
```
git clone https://github.com/pratikmm/rest-mysql-helm.git
```
**Deploy Secret, PV and PVC using Helm chart**
```
helm install secret-pv rest-mysql-helm/helm/secret-pvc
```
**Deploy REST application and MYSQL DB**
```
helm install rest-w-mysql rest-mysql-helm/helm/flask-mysql
```
**Check if Helm charts are successfully deployed**
```
helm list
```
**Check Application and DB status**
```
kubectl get pods
```
Once all Pods are running. User below command to access REST API from browser.(for minikube enviroment)
```
minikube service rest-flask-application-service
```
It should automatically open the default browser and hit the Node IP and port to access REST application which makes query on MYSQL DB in the backend.

To get URL use below command and it can be used with curl command from terminal.
```
minikube service --url rest-flask-application-service
> x.x.x.x
curl x.x.x.x
```
Your should see below output on browser or terminal after above commands.
> {"result": \[["Hello World!"]]}

