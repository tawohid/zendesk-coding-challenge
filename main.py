from creds import CREDENTIALS
from zenpy import Zenpy

zenpy_client = Zenpy(**CREDENTIALS)

if __name__ == '__main__':
    for ticket in zenpy_client.tickets():
        print(ticket.subject)
