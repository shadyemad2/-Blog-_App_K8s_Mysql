apiVersion: v1
kind: Service
metadata:
  name: blog-service
spec:
  selector:
    app: blog-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 5000
  type: ClusterIP

