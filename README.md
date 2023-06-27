# Primitive
* This is a personal project and I did not choose a suitable name for it but it will be upgraded in the future.
* currently users can sign up/in and do crud operations for their posts.


# Technologies used

* [Python 3.9](https://www.python.org) , Programming Language.
* [Django 4.0](https://docs.djangoproject.com/en/4.0/) , Web Framework.
* [Django Rest Framework 3.13](https://www.django-rest-framework.org/) , Web API's.
* [Docker](https://docker.com/) , Container Platform.
* [Git](https://git-scm.com/doc) , Version Control System.
* [Celey](https://docs.celeryq.dev/en/stable/) , Distributed Task Queue.
* [Redis](https://redis.io/docs/) , Cache Database and message broker.
* [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) , Authentication Manager.
* [PostgreSQL](https://www.postgresql.org/) , Database.


# Requirements

* **install [Docker](https://www.docker.com/)**  
You must install Docker to run **Redis and PostgreSQL** container on it.
  * [install Docker on Linux](https://docs.docker.com/engine/install/)
  * [install Docker on Windows](https://docs.docker.com/desktop/windows/install/)
  * [install Docker on Mac](https://docs.docker.com/desktop/mac/install/)

* **install [Postman](https://www.postman.com/)(recommended) _or_ [Thunder Client](https://www.thunderclient.com)**  
To test api, you need to use postman app **or** thunder client extension on vscode  

  Postman  
  * [install postman on Linux](https://learning.postman.com/docs/getting-started/installation-and-updates/#installing-postman-on-linux)
  * [install postman on Windows](https://learning.postman.com/docs/getting-started/installation-and-updates/#installing-postman-on-windows)
  * [install postman on Mac](https://learning.postman.com/docs/getting-started/installation-and-updates/#installing-postman-on-mac)

  > use this [Guide](https://learning.postman.com/docs/sending-requests/requests/) on how to send request via **postman**. 

  Thunder Client(**note**: you won't need this, if you've installed Postman)  
       
  Launch VS Code Extensions tab (Ctrl+Shift+X), search for _Thunder Client_ and install it.

  > use this [Guide](https://developers.refinitiv.com/en/article-catalog/article/how-to-test-http-rest-api-easily-with-visual-studio-code---thund) on how to send request via **thunder client**.


# Installation

1. **clone the project**  
   ```  
   git clone git@github.com:mr-ghodsiniya/primitive.git
   ```  

2. **rename .sample.env to .env and fill the variables**.  
   Pay attention that in this project we're using [SMS.IR](https://sms.ir/) APIs to send OTP.  
   **note**: you will need an API_KEY which is accessible in your dashboard.
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

# Testing APIs

The login senario would be like this:  
1. Client's phone number would be sent by a post request to 'user/login/' endpoint. Then user will receive an sms containing OTP code.
2. Client's phone number and delivered OTP code must be sent by a Post request to 'user/verify/' endpoint. If client provides the correct information, it's request would be Responsed by an access and refresh token for further usages(authentication).

**Login** <br/>
send a post request to (https://localhost:8000/user/login/) including "phone_number" in it's body.  
you will receive an sms containig OTP code asap.(you would see it in the celery logs if you are not using an SMS provider as explained in step2.)

**Verify**  
send a post request to (https://localhost:8000/user/verify/) including "phone_number" and "otp" in it's body.  
you will Responded by an access and refresh token if you provide correct information.

**if you provide correct credentials, with access token you can do CRUD.**

**Create**  
send a post request to (https://localhost:8000/user/create-post/) including "text" and "title" in it's body and including access token in Headers like below:  
```
# key: Authorization
# value: Bearer your-access-token-without-quotation-marks
```


**Retrieve**  
send a get request to (https://localhost:8000/user/user/get-post/3/)
3 = id of your post that create in Create API.


**Patch or Update**  
send a patch request to (https://localhost:8000/user/update-post/3/) including "text" or "title" or both of them in it's body and including access token in Headers like below:  
```
# key: Authorization
# value: Bearer your-access-token-without-quotation-marks
```
3 = The id of the post you want to edit


**Delete**  
send a delete request to (https://localhost:8000/user/delete-post/3/) including access token in Headers like below:
```
# key: Authorization
# value: Bearer your-access-token-without-quotation-marks
```
3 = The id of the post you want to delete

























