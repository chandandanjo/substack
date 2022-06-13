import requests
import json
from bs4 import BeautifulSoup


class Substack:
    def __init__(self):
        self.session = requests.Session()

    def login_from_mail(self, mail, password):
        url = "https://substack.com/api/v1/login"
        headers = {"content-type": "application/json", "referer": "https://substack.com/sign-in?redirect=%2F"}
        data_ = f'"redirect":"/","for_pub":"","email":"{mail}","password":"{password}","captcha_response":null'
        data = '{' + data_ + '}'
        self.session.post(url, headers=headers, data=data)
        try:
            self.two_factor_auth()
            self.user_name()
            self.save_cookie()
            return 'Connected Successfully'
        except AttributeError:
            return 'Wrong Credentials'

    def login_from_saved_cookie(self, cookie_file_name):
        try:
            with open(f'{cookie_file_name}', 'r') as f:
                cookies = json.loads(f.read())
                self.session.cookies.update(cookies)
                try:
                    self.user_name()
                    return 'Connected Successfully'
                except AttributeError:
                    return 'Wrong Cookie'
        except FileNotFoundError:
            return 'File Not Found'

    def login_from_uploaded_cookie(self, cookie_name):
        cookies = json.loads(cookie_name)
        self.session.cookies.update(cookies)
        try:
            self.user_name()
            self.save_cookie()
            return 'Connected Successfully'
        except AttributeError:
            return 'Wrong Cookie'

    def save_cookie(self):
        cookies = str(self.session.cookies.get_dict()).replace("'", '"')
        if len(cookies) == 0:
            return 'No Cookies in the session currently.'
        else:
            print(cookies, file=open("output.txt", "w"))
            return 'Cookies saved in output.txt file.'

    def user_name(self):
        url = 'https://substack.com/account/settings?utm_source=user-menu'
        resp = self.session.get(url)
        soup = BeautifulSoup(resp.content, 'html5lib')
        name = soup.find('h1').get_text()
        return name

    def enable_recovery_questions(self):
        # data may vary from user to user according to recovery question and answers set by the user.
        url = "https://substack.com/api/v1/settings/questions"
        headers = {"content-type": "application/json", "referer": "https://substack.com/account/security-questions"}
        data = '{"question_one":"In what city or town did your parents meet?","answer_one":"faizabad","question_two":"What was the make and model of your first car?","answer_two":"no","question_three":"What is your earliest memory?","answer_three":"zezuz"}'
        resp = self.session.post(url, headers=headers, data=data)
        response = json.loads(resp.content.decode('utf-8').replace("'", '"').strip())
        if len(response) == 0:
            response = {'Recovery questions': 'Enabled'}

        print(response)

    def disable_recovery_questions(self):
        # data may vary from user to user according to recovery question and answers set by the user.
        url = "https://substack.com/api/v1/settings/questions"
        headers = {"content-type": "application/json", "referer": "https://substack.com/account/security-questions"}
        data = '{"answer_one":"faizabad","answer_two":"no","answer_three":"zezuz"}'
        resp = self.session.delete(url, headers=headers, data=data)
        response = json.loads(resp.content.decode('utf-8').replace("'", '"').strip())
        if len(response) == 0:
            response = {'Recovery questions': 'Disabled'}

        print(response)

    def two_factor_auth(self):
        url = "https://substack.com/api/v1/mfa-challenge"
        headers = {"content-type": "application/json", "referer": "https://substack.com/sign-in/mfa"}
        data_test = '{"code":"{123456}"}'
        resp_ = self.session.post(url, headers=headers, data=data_test)
        response_ = json.loads(resp_.content.decode('utf-8').replace("'", '"').strip())["error"]
        if response_ == "We were unable to verify this code.":
            pass
        else:
            totp_token = input("Enter the six digit TOTP: ")
            while len(totp_token) != 6:
                print('Enter TOTP correctly.')
                totp_token = input("Enter the six digit TOTP: ")
            data_ = f'"code":"{totp_token}"'
            data = '{' + data_ + '}'
            resp = self.session.post(url, headers=headers, data=data)
            response = json.loads(resp.content.decode('utf-8').replace("'", '"').strip())

            print(response)

    def disable_two_factor_auth(self):

        totp_token = int(input("Enter the six digit TOTP: "))
        while 6 < len(str(totp_token)) > 6:
            print('Enter TOTP correctly.')
            totp_token = input("Enter the six digit TOTP: ")

        url = "https://substack.com/api/v1/settings/mfa"
        headers = {"content-type": "application/json", "referer": "https://substack.com/account/mfa"}
        data_ = f'"totp_token":"{totp_token}"'
        data = '{' + data_ + '}'
        resp = self.session.delete(url, headers=headers, data=data)
        response = json.loads(resp.content.decode('utf-8').replace("'", '"').strip())
        if len(response) == 0:
            response = {'Two factor authentication': 'Disabled'}

        print(response)
    
    def profile_image(self):

        url = 'https://substack.com/account/settings?utm_source=user-menu'
        resp = self.session.get(url)
        soup = BeautifulSoup(resp.content, 'html5lib')
        img = soup.find('div', class_='profile-img-wrap').find('img')['src']
        return img



session = Substack()
session.login_from_mail(' ', ' ')
