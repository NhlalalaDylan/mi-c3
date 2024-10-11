### Setup

- Create python virtual environment 
- install python requirements: pip install -r requirements.txt
- Build Docker image: docker build -t flask-app .
- Run Multiple Instances of the App:
   - docker run -d -p 5001:5000 --name flask-app-1 -e NODE_ID=node_1 flask-app
   - docker run -d -p 5002:5000 --name flask-app-2 -e NODE_ID=node_2 flask-app
   
### Test the application:

   - curl -X POST -H "Content-Type: text/plain" --data $'2\nSun 10 May 2015 13:54:36 -0700\nSun 10 May 2015 13:54:36 -0000\nSat 02 May 2015 19:54:36 +0530\nFri 01 May 2015 13:54:36 -0000' http://127.0.0.1:5001/calculate

   - curl -X POST -H "Content-Type: text/plain" --data $'2\nSun 10 May 2015 13:54:36 -0700\nSun 10 May 2015 13:54:36 -0000\nSat 02 May 2015 19:54:36 +0530\nFri 01 May 2015 13:54:36 -0000' http://127.0.0.1:5002/calculate

