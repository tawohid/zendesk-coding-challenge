import pytest
import main
from config import api, header


def test_req_invalid_token():
    mock_url = f'tickets.json?page[size]=25'
    wrong_header = {'Authorization': 'Bearer ' + 'wrongtoken'}
    assert main.req(api, mock_url, wrong_header) == pytest.exit("Application Exits")


def test_req_invalid_url():
    wrong_url = f'tickets.json?pag[size]=25'
    assert main.req(wrong_url, api, header) == pytest.exit("Application Exits")


def test_valid_config():
    mock_url = f'tickets.json?page[size]=25'
    assert main.req(mock_url, api, header)


def test_fetch_tickets_no_after():
    assert main.fetch_tickets()


def test_fetch_tickets_after():
    mock_after =  "eyJvIjoibmljZV9pZCIsInYiOiJhUm9BQUFBQUFBQUEifQ=="
    assert main.fetch_tickets(mock_after)