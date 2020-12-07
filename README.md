# rest-mysql-helm



helm install rest-flask-w-mysql helm/flask-mysql-minikube/

minikube service rest-flask-application-service


mysql -h localhost -u root -p
HdFE7Z3D3IaU3H4kpHUe


mysql -h mysql -u root -p

kubectl run -i -t --rm ephemeral --image=mysql -- /bin/sh -l

docker run -d --name mysql1 -p 3306:3306 -e MYSQL_ROOT_PASSWORD:'password' -e MYSQL_USER:'user1' -e MYSQL_PASSWORD:'user1' -e MYSQL_DATABASE:'test' mysql:5.7



docker run -d --name mysql1 -p 3306:3306 -e MYSQL_ROOT_PASSWORD:password1 mysql:8.0.22

mysql -u root mysql