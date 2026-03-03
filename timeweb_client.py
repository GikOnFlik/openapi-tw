import requests

class TimewebCloudMailClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.timeweb.cloud/mail/'

    def create_mailbox(self, domain, mailbox, password):
        url = f'{self.base_url}mailboxes/'
        data = {
            'domain': domain,
            'mailbox': mailbox,
            'password': password
        }
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.post(url, json=data, headers=headers)
        return response.json()

    def update_mailbox(self, mailbox_id, new_password):
        url = f'{self.base_url}mailboxes/{mailbox_id}/'
        data = {'password': new_password}
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.put(url, json=data, headers=headers)
        return response.json()