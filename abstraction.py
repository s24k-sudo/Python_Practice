class Email_service:
    def _connect(self):
        print("Connecting to the email server")
    
    def _authenticate(self):
        print("Authenticating")

    def send_mail(self):
        self._connect()
        self._authenticate()
        print("Sending the mail....")
        self._disconnect()


    def _disconnect(self):
        print("Disconnecting from the email server....")

email=Email_service()

email.send_mail()