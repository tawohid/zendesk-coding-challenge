import requests
import textwrap as tr
from config import api, header

# Dictionary for storing tickets, preventing API calls for specific tickets at the expense of negligible storage
ticket_store = dict()


# Generic requests handler, returns exact API errors therefore allowing the backend to process error handling and
# Returns exact error from server to CLI user
def req(url, api, header):
    response = requests.get(api + url, headers=header)  # Using API recommended secure bearer token
    data = response.json()
    if response.status_code != 200: # Only GETs are made in this application, anything other than 200 is an error
        print('Status:', response.status_code, '| Problem with the request:')
        print(data, "\nExiting..")
        exit(-1)
    data = response.json()
    return data


# Creates the URL for the fetch of tickets, only function that calls the API
def fetch_tickets(after_cursor=None):
    page_size = 25
    url = f'tickets.json?page[size]={page_size}'   # Allows server to handle pagination using API recommended style
    if after_cursor:
        url += f'&page[after]={after_cursor}'      # Condition allows only one function for both first and next pages
    data = req(url, api, header)
    return data


def display_tickets(tickets):
    for ticket in tickets:
        ticket_store[ticket['id']] = ticket         # Stores entire ticket object for ticket id, allowing extensibility
        print(f"ID:{ticket['id']:<4}| {ticket['subject']}")  # Consistent spacing for each line
    print(f"Total Tickets: {len(ticket_store)}")    # Prints total tickets to allow users to see total data retrieved


def display_ticket(ticket_id):
    ticket = ticket_store[ticket_id]  # Gets ticket information from already fetched tickets, preventing extra calls
    print(f" -------------------- \n "  # Separators for readability
          f"TICKET ID: {ticket['id']} \n "
          f"SUBJECT: {ticket['subject']} \n "
          f"STATUS: {ticket['status']} \n "
          f"REQUESTER: {ticket['requester_id']} \n "
          f"ASSIGNEE: {ticket['assignee_id']} \n "
          f"CREATED: {ticket['created_at']} \n "
          f"UPDATED: {ticket['updated_at']} \n "
          f"TAGS: {ticket['tags']} \n ")
    for line in tr.wrap(ticket['description']):  # Built-in wrap library used resulting in easier paragraph readability
        print(" " + line)
    print(" --------------------")


if __name__ == '__main__':
    choice = ''
    # Client side page-tracking due to cursor based pagination recommended by API documentations lacking page number
    page = 1
    after = None
    end = False

    print("\nWelcome to ZCC Supports Ticket Viewer CLI App")
    while choice != 'q':  # Using only one 2 'button' menu, no nested menus for simplicity and ease of use

        if page == 1:
            print("\nEnter 'n' to view page of tickets")

        elif page > 1 and after:
            print("\nEnter {ticket's id #} to view a tickets information")
            print("Enter 'n' to scroll to next page of tickets")

        elif page > 1 and not after:
            end = True
            print("\nYou have gathered all available tickets")
            print("Enter {ticket's id #} to view a tickets information")

        print("Enter 'q' to quit.")

        choice = input()

        if choice == "n" and not end:
            results = fetch_tickets(after)
            print(f"Page {page}: ")
            display_tickets(results['tickets'])
            if results['meta']['has_more']:
                after = results['meta']['after_cursor']
            else:
                after = None
            page += 1

        elif choice.isnumeric():    # Automatically filters out invalid negative IDs as isnumeric returns false for '-'
            entered_id = int(choice)
            if entered_id in ticket_store.keys():
                display_ticket(entered_id)
            else:
                print("Invalid Ticket ID")  # Informs user on specific error

        elif choice == 'q':
            print("Exiting...")

        else:
            print("Invalid Command. Try again!")
