### Setup

- Create python virtual environment 
- install python requirements: pip install -r requirements.txt
- Run server: python3 main.py
### Test with CURL: 

- curl -X POST -H "Content-Type: text/plain" --data $'2\nSun 10 May 2015 13:54:36 -0700\nSun 10 May 2015 13:54:36 -0000\nSat 02 May 2015 19:54:36 +0530\nFri 01 May 2015 13:54:36 -0000' http://127.0.0.1:5000/calculate