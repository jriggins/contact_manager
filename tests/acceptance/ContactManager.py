import threading
import time

import requests
from robot.libraries.BuiltIn import BuiltIn

import sys
sys.path.insert(0, '../../contact_manager')

import contact_manager.account.model.example as account_examples
import contact_manager.account.repo as account_repo
from contact_manager import app
from contact_manager.account import api


class WebClient:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self.session_token = None

    def get_url(self, path):
        return 'http://{host}:{port}{path}'.format(host=self._host, port=self._port, path=path)

    def post(self, path, data):
        url = self.get_url(path)
        print('POST to ', url, 'with data ', data)
        response = requests.post(url, json=data)
        print('Response: ', response.content)
        return response


class ContactManager:
    def __init__(self):
        self._repo = account_repo.InMemoryAccountRepository()
        self._api = api.Api(self._repo, 'adslk;jasdlk;ja;slkdj')
        self._host = 'localhost'
        self._port = 5005
        self._web_client = WebClient(self._host, self._port)
        self._process = None

    def start_app(self):
        self._start_app(self._api)

    def stop_app(self):
        if self._process:
            print('stoping app')
            response = self._web_client.post('/admin/shutdown', None)
            assert response.status_code == 200

    def clear_all_users(self):
        self._api._repo.clear_all()
        assert list(self._repo.all_accounts()) == [], 'There should be no Accounts in the system.'

    def register_user(self, user_key):
        user = account_examples.get(user_key)
        response = self._post('/api/account/register_user', dict(
            id=user.id,
            email_address=user.email_address,
            password='User1Password',
        ))
        assert 201 == response.status_code, 'Expected status code: {expected}  Received: {status_code}'.format(
            expected=201, status_code=response.status_code)

    def user_should_exist(self, user_key):
        user = account_examples.get(user_key)
        account = self._api._repo.find_by_email_address(user.email_address)
        assert account, 'Unable to find Account with email address {0}'.format(email_address)

    def log_in(self, user_key):
        user = account_examples.get(user_key)
        response = self.log_in2(user.email_address, 'User1Password')
        return response

    def log_in2(self, email_address, password):
        response = self._post('/api/auth/login', dict(
            email_address=email_address,
            password=password,
        ))
        if response.status_code == 200:
            self._web_client.session_token = response.json()['session_token']
        return response

    def _post(self, path: str, data: dict) -> requests.Response:
        response = self._web_client.post(path, data)
        BuiltIn().set_test_variable('${response}', response)
        return response

    def _start_app(self, api_: api.Api):
        if self._process:
            print('app already started')
            return
        print('starting app')
        self._process = threading.Thread(
            target=lambda: app.start_app(self._host, self._port, api_, debug=False)
        )
        self._process.start()
        time.sleep(.25)

