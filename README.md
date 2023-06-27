# [![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=34&duration=3000&color=ADBAC7&center=false&vCenter=true&repeat=true&width=700&lines=Primitive+👋)](https://git.io/typing-svg)

* This is a personal project that will be **upgraded in the future** also I didn't choose a suitable name for it.
* Currently, users can **Sign up/in** and do **CRUD** operations for their posts.


# 💻 Technologies used

* [Python](https://www.python.org) , Programming Language. ![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

* [Django](https://docs.djangoproject.com/en/4.0/) , Web Framework. ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)

* [Django Rest Framework](https://www.django-rest-framework.org/) , Web API's. ![DRF](https://img.shields.io/badge/DRF-%2300BFFF.svg?style=for-the-badge&logo=django&logoColor=white)

* [Docker](https://docker.com/) , Container Platform. ![Docker](https://img.shields.io/badge/Docker-0db7ed?style=for-the-badge&logo=docker&logoColor=white)

* [Git](https://git-scm.com/doc) , Version Control System. ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

* [Celery](https://docs.celeryq.dev/en/stable/) , Distributed Task Queue. ![Celery](https://img.shields.io/badge/celery-%230C7BDC.svg?style=for-the-badge&logo=celery&logoColor=white)

* [Swagger](https://swagger.io/) , Test APIs inside of project. ![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)

* [Redis](https://redis.io/docs/) , Cache Database and message broker. ![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)

* [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) , Authentication Manager. ![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20Web%20Tokens)

* [PostgreSQL](https://www.postgresql.org/) , Database. ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)


# Requirements ;)

* **install [Docker](https://www.docker.com/)** <br/>
You must install Docker to run **Redis and PostgreSQL** container on it.

* **Docker** <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a>

  * [install Docker on Linux](https://docs.docker.com/engine/install/)
  * [install Docker on Windows](https://docs.docker.com/desktop/windows/install/)
  * [install Docker on Mac](https://docs.docker.com/desktop/mac/install/)

* **install [Postman](https://www.postman.com/)(recommended) or [Thunder Client](https://www.thunderclient.com) or [Swagger](https://swagger.io/)**  <br/>
To test API, you need to use postman app <br/>
**or** thunder client extension on VsCode **or** swagger.

* **Postman** <a href="https://postman.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a>

  * [install postman on Linux](https://learning.postman.com/docs/getting-started/installation-and-updates/#installing-postman-on-linux)
  * [install postman on Windows](https://learning.postman.com/docs/getting-started/installation-and-updates/#installing-postman-on-windows)
  * [install postman on Mac](https://learning.postman.com/docs/getting-started/installation-and-updates/#installing-postman-on-mac)
  > Use this [Guide](https://learning.postman.com/docs/sending-requests/requests/) on how to send request via **postman**. 
<br/>

* **Thunder Client** <br/>
  **Note**: You won't need this, if you've installed Postman.
       
  * Launch VsCode Extensions tab (Ctrl+Shift+X), search for _Thunder Client_ and install it.
  > Use this [Guide](https://developers.refinitiv.com/en/article-catalog/article/how-to-test-http-rest-api-easily-with-visual-studio-code---thund) on how to send request via **thunder client**.
<br/>

* **Swagger** <br/>
You can test APIs inside of project with the help of Google and localhost.
   ```
   http://127.0.0.1:8000/swagger/
   ```
   **or**
   ```
   http://127.0.0.1:8000/redoc/
   ```

# ⏳️ Installation

1. **clone the project**  
   ```  
   git clone git@github.com:mr-ghodsiniya/primitive.git
   ```  

2. **rename .sample.env to .env and fill the variables**.  
   Pay attention that in this project we're using [SMS.IR](https://sms.ir/) APIs to send OTP.  
   **Note**: You will need an API_KEY which is accessible in your dashboard.
   ```
   SECRET_KEY=Just fill in whatever you like
   API_KEY=API_KEY from sms.ir
   DEBUG=True
   ```

4. **create a python virtual environment**  
   ```
   python -m venv venv
   ```

5. **activate your venv**
  * on linux and mac
    ```
    source venv/bin/activate
    ```
  * on windows
    ```
    venv/Scripts/activate
    ```

5. **install dependencies**
   ```
   pip install -r requirements.txt
   ```

6. **run redis and postgresql container on docker**
   ```
   sudo docker run --name pri-rd -p 6381:6379 -d redis
   sudo docker run --name pri-sql -p 5435:5432 -e POSTGRES_PASSWORD=123456 -d postgres
   ```
   
7. **makemigrations**
   ```
   python manage.py makemigrations user
   ```

8. **migrate**
   ```
   python manage.py migrate
   ```

9. **run project**
   ```
   python manage.py runserver
   ```

# Testing APIs 💭

The login senario would be like this:  
1. Client's phone number would be sent by a post request to 'user/login/' endpoint. <br/>
Then user will receive an sms containing OTP code.
2. Client's phone number and delivered OTP code must be sent by a Post request to 'user/verify/' endpoint. <br/>
If client provides the correct information: <br/>
it's request would be Responsed by an access and refresh token for further usages(authentication).


# Login
send a post request to (http://127.0.0.1:8000/user/login/) <br/>
including "phone_number" in it's body.  
you will receive an sms containig OTP code asap. <br/>
(you would see it in the celery logs if you are not using an SMS provider as explained in step2)


# Verify  
send a post request to (http://127.0.0.1:8000/user/verify/) <br/>
including "phone_number" and "otp" in it's body.  
[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=34&duration=3400&color=ADBAC7&center=false&vCenter=true&repeat=true&width=700&lines=you+will+Responded+by+an+access+and+refresh+token;if+you+provide+correct+credentials+👥️;with+access+token+you+can+do+CRUD+operations+🤝🏻)](https://git.io/typing-svg)


# Create
send a post request to (http://127.0.0.1:8000/user/create-post/) <br/>
including "text" and "title" in it's body, <br/>
and including access token in Headers like below:  
```
# key: Authorization
# value: Bearer your-access-token-without-quotation-marks
```


# Retrieve  
send a get request to (http://127.0.0.1:8000/user/get-post/3/) <br/>
3 = id of your post that create in Create API.


# Patch or Update  
send a patch request to (http://127.0.0.1:8000/user/update-post/3/) <br/> 
including "text" or "title" or both of them in it's body, <br/>
and including access token in Headers like below:  
```
# key: Authorization
# value: Bearer your-access-token-without-quotation-marks
```
3 = The id of the post you want to edit.


# Delete
send a delete request to (http://127.0.0.1:8000/user/delete-post/3/) <br/>
including access token in Headers like below:
```
# key: Authorization
# value: Bearer your-access-token-without-quotation-marks
```
3 = The id of the post you want to delete.


# [![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=34&duration=3500&color=ADBAC7&center=false&vCenter=true&repeat=true&width=700&lines=✍️+Random+Dev+Quote:)](https://git.io/typing-svg)
![](https://quotes-github-readme.vercel.app/api?type=vertical&theme=dark&count=1)
