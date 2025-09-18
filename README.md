# 📝 Mini Blog App (Kubernetes + MySQL)

**Mini Blog App** is a simple web application deployed on **Kubernetes**. It allows users to submit and view blog posts through a web interface. The backend is built with **Flask** (Python), and the data is stored in a **MySQL** database. This project demonstrates key Kubernetes concepts such as Deployments, StatefulSets, Headless Services, Secrets, ConfigMaps, Services, and Ingress.

---

## 💡 Application Overview

- **Frontend & Backend:** Flask app handles HTTP requests, displays posts, and allows new submissions.  
- **Database:** MySQL stores all blog posts in the `blogdb` database.  
- **Persistence:** MySQL uses a **StatefulSet** with a **headless service** for stable network identity and persistent storage.  
- **Secrets Management:** Database credentials are stored securely using Kubernetes **Secrets**.  
- **Networking:** The Flask app is exposed inside the cluster via a **Service** and externally through an **Ingress** at `blog.local`.  

---

## 📂 Project Structure

k8s-blog-app/
├─ app/ # Flask application code
│ ├─ app.py
│ └─ requirements.txt
├─ k8s/ # Kubernetes manifests
│ ├─ app-deployment.yaml
│ ├─ mysql-statefulset.yaml
│ ├─ secrets.yaml
│ ├─ configmap.yaml
│ ├─ headless.yaml
│ ├─ service.com
│ └─ ingress.yaml
├─ Dockerfile # Builds Flask app image
└─ README.md # Project documentation


---

## 🚀 Deployment Steps

1. Build the Flask Docker image:  

docker build -t mini-blog-app:latest ./app



2. Deploy MySQL with StatefulSet:  

kubectl apply -f k8s/secrets.yaml
kubectl apply -f k8s/mysql-statefulset.yaml
kubectl apply -f k8s/headless.yam

3. Deploy the Blog App:  
kubectl apply -f k8s/app-deployment.yaml
kubectl apply -f k8s/service.com

4. Configure Ingress:  
kubectl apply -f k8s/ingress.yaml



5. Map `blog.local` to the cluster IP in `/etc/hosts`.

---

## 🔍 Testing the Application

- Check Pods and Services:  
kubectl get pods
kubectl get svc

- Access the app in browser or via curl:  
curl http://blog.local

- Verify database:  
kubectl exec -it mysql-0 -- mysql -u root -p
USE blogdb;
SHOW TABLES;

---

## 🛠️ Troubleshooting

- **503 Service Temporarily Unavailable:**  
  Check Ingress rules, ensure service name and port match the backend deployment.

- **Database connection errors:**  
  Verify MySQL Pod is running.  
  Check endpoints: `kubectl get endpoints mysql`  
  Ensure Secrets and environment variables in the Deployment match MySQL credentials.

---

## ✅ Tech Stack

- Kubernetes (Minikube)  
- Flask (Python)  
- MySQL (StatefulSet with persistent storage)  
- Nginx Ingress Controller  
- Docker (Containerization)  
- Kubernetes Objects: Deployment, StatefulSet, Headless Service, Service, ConfigMap, Secret, Ingress  

---

## 👤 Author

**Shady Emad** – DevOps / Kubernetes / Cloud Enthusiast

