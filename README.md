# 📝 Blog App (Kubernetes + MySQL)

**Blog App** is a simple web application deployed on **Kubernetes**. It allows users to submit and view blog posts through a web interface. The backend is built with **Flask** (Python), and the data is stored in a **MySQL** database. This project demonstrates key Kubernetes concepts such as Deployments, StatefulSets, Headless Services, Secrets, ConfigMaps, Services, and Ingress.

<img width="487" height="561" alt="app" src="https://github.com/user-attachments/assets/ce1eac84-1873-46dd-bcbf-d9a3c9aed0a3" />

<img width="946" height="647" alt="app2" src="https://github.com/user-attachments/assets/1704ec0d-ce76-4ae0-8903-3ff7e2a68952" />

---

## 💡 Application Overview

- **Frontend & Backend:** Flask app handles HTTP requests, displays posts, and allows new submissions.  
- **Database:** MySQL stores all blog posts in the `blogdb` database.  
- **Persistence:** MySQL uses a **StatefulSet** with a **headless service** for stable network identity and persistent storage.  
- **Secrets Management:** Database credentials are stored securely using Kubernetes **Secrets**.  
- **Networking:** The Flask app is exposed inside the cluster via a **Service** and externally through an **Ingress** at `blog.local`.  

---

## 📂 Project Structure

```plaintext
k8s-blog-app/
├─ app/              # Flask application code
│  ├─ app.py
│  └─ requirements.txt
├─ k8s/              # Kubernetes manifests
│  ├─ app-deployment.yaml
│  ├─ mysql-statefulset.yaml
│  ├─ secrets.yaml
│  ├─ configmap.yaml
│  ├─ headless.yaml
│  ├─ service.com
│  └─ ingress.yaml
├─ Dockerfile         # Builds Flask app image
└─ README.md          # Project documentation
ط
---
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

## ✅ Tech Stack

- Kubernetes (Minikube)  
- Flask (Python)  
- MySQL (StatefulSet with persistent storage)  
- Nginx Ingress Controller  
- Docker (Containerization)  
- Kubernetes Objects: Deployment, StatefulSet, Headless Service, Service, ConfigMap, Secret, Ingress  

---

## 👤 Author

**Shady Emad** – DevOps / Kubernetes / Cloud / Linux

