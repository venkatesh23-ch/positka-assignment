# positka-assignmen
===========================================================================================
Steps to Run the Flask Application on Windows
===========================================================================================
1. Install Python any version >=3 (I used 3.7.4)
2. Create a virtual environment and install all the required packages in requirements.txt.
   i) Install virtualenv using command:
       --> pip install virtualenv
   ii) Create a virtual environment using below command:
       --> virtualenv positka #you can use any name
   iii) Activate virtualenv using below command:
        --> <PATH_OF_YOUR_VIRTUAL_ENV>\Scripts\activate
   iv) Install Required Packages from requirements.txt as below:
        --> pip3 install -r requirements.txt
3. Set the gmail credentials in settings.ini to send JSON response mail.
      Ex: [SMTP]
          hostname=smtp.gmail.com # <Works only for google mails>
          sender_mail=<SENDER_GMAIL_ID>
          password=<GMAIL_PASSWORD>
   Note: Enable Less secure app access for allowing smtp mails using below link
         https://myaccount.google.com/lesssecureapps
4. Run the Flask Application using below command:
   --> python main.py (by default flask application will runn in 5000 Port)
5. Give the required inputs as below:
    Ex: Server IP: 13.126.96.126
        Username: XXXX
        Password: XXXX	
        Search Query: index=_internal | top sourcetype	
        Time Range: Last 24 <Select box>	
        Email: <RECIEVER_MAIL_ID>
6. Click Submit and check your mail id for results.
