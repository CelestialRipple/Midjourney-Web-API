[中文版本](https://github.com/CelestialRipple/Midjourney_api/blob/main/README_zh-CN.md)
# Midjourney-Web-API
Unofficial Midjourney-Web-API, for learning and research purposes only.

## :sparkles: Features
* ✨ Simple and easy to deploy
* 👋 Support for caching images, mainland China access friendly
* 💾 Support image Upscale function, get HD large image
* 📚 Multi-threaded concurrency, high-speed drawing
* 💻 Automatic database cleanup and error handling functions are perfect
* 🔐 Cross-domain restrictions can be set, anti-theft

## QuickStart fast start


## (Updated) Introduction to the use of external APIs:
- To use external API, nano app.py (configure cross-domain with sender_params.json file path)
- python app.py
### Request method
- post request: http://localhost:5000/api/send_and_receive"
- Optional parameter: cdn=true (default false, when enabled the server will cache the image before sending, continental access is more friendly)
Example:
```python
import requests
import json

payload = {
    "prompt": "your_prompt_here"
}

url = "http://localhost:5000/api/send_and_receive";

response = requests.post(url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

print(response.json())
```
- get request: http://localhost:5000/upscale"
- Mandatory parameter: file_name(string), the name of the file that needs to be executed upscale (e.g. rockgifinrock1971_link_and_zelda_33e8886f-adae-4579-9882-bae644005f5b.png)
- Mandatory parameter: number (number), the serial number of the image that needs to be executed upscale (example 1/2/3/4).
- Optional parameters: cdn=true (default false, after enabling the server will cache pictures before sending, continental access more friendly)
Example:
```python
import requests

base_url = 'http://localhost:5000' # Replace with the URL your Flask application is actually running on
file_name = 'rockgifinrock1971_link_and_zelda_33e8886f-adae-4579-9882-bae644005f5b.png' # Replace with your actual file name
number = 3 # Replace with the number you want to use

response = requests.get(f'{base_url}/upscale', params={'file_name': file_name, 'number': number})

if response.status_code == 200.
    print('Success!')
    print(response.json())
else.
    print(f'Error: {response.status_code}')
    print(response.text)
```


## Update plan

- Model switching
- Multi-account concurrency
- Faster cookie retrieval

## Contact:
For suggestions and cooperation: Me@hiripple.com
Ask the author to eat Crazy Thursday to speed up the project: https://afdian.net/a/hiripple/plan

## License
MIT

## Additions
Sender.py and Receiver.py are based on https://github.com/George-iam/Midjourney_api
