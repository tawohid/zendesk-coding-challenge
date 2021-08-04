# zendesk-coding-challenge
A command line Python application for interacting with the Zendesk API specifcaly for https://zccsupport.zendesk.com/ 

## Prerequisite
- Python 3


# Instructions 

1. Download via Github via git clone (below) or download zip


```
$ git clone https://github.com/voscra/zendesk-coding-challenge
```

2. Authorize with correct API token. Either replace the 'bearer_token' variable with given token in email or add to unix envoriment variables to not change any part of the code

```
$ export BEARER_TOKEN={given token in accompanying email}
```

3. Install required packages
- This applicaiton only requires one external package 'requests'

```
$ pip install requests
```
4. Navigate to app directory in terminal run main with python3

```
$ python3 main.py
```

![Preview](https://i.imgur.com/HxY6nKp.png)

