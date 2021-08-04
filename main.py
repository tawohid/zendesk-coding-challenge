import requests
from config import api, header

ticket_store = dict()


def req(url):
    response = requests.get(api + url, headers=header)
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()
    data = response.json()
    return data


def fetch_tickets(after_cursor=None):
    page_size = 25
    url = f'tickets.json?page[size]={page_size}'
    if after_cursor:
        url += f'&page[after]={after_cursor}'
    data = req(url)
    return data


def display_tickets(tickets):
    for ticket in tickets:
        ticket_store[ticket['id']] = ticket
        print(ticket['id'], ticket['subject'])


def display_ticket(ticket_id):
    ticket = ticket_store[ticket_id]
    print(ticket['subject'], ticket['description'])


if __name__ == '__main__':
    choice = ''
    page = 1
    after = None
    end = False

    while choice != 'q':

        if page == 1:
            print("\nEnter 'n' to view all tickets")
        elif page > 1 and after:
            print("\nEnter {ticket's id #} to view ticket information")
            print("Enter 'n' to scroll to next page of tickets")
        elif page > 1 and not after:
            end = True
            print("\nYou've reached the end")
            print("Enter {ticket's id #} to view ticket information")
        print("Enter 'q' to quit.")

        choice = input()

        if choice == "n" and not end:
            print(f"Page {page}: ")
            results = fetch_tickets(after)
            display_tickets(results['tickets'])
            if results['meta']['has_more']:
                after = results['meta']['after_cursor']
            else:
                after = None
            page += 1
        elif choice == 'q':
            print("Exiting...")
        elif choice.isnumeric():
            ticket_id = int(choice)
            if ticket_id in ticket_store.keys():
                display_ticket(ticket_id)
            else:
                print("Invalid Ticket ID")

        else:
            print("Invalid Selection")
