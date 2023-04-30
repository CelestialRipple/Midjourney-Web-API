[中文版本](https://github.com/CelestialRipple/Midjourney-Web-API/blob/main/README_zh-CN.md)
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
1. clone project
```shell
git clone https://github.com/CelestialRipple/Midjourney-Web-API
cd Midjourney-Web-API
```
2、 Get Cookie (make sure you can use Midjourney drawing in Discord)
- Go to the dialog box in Discord with Midjourney Bot -
- Open the developer tools of any browser (right click/F12) and check the network option
- Send any drawing request
- Search for interaction in Developer Tools and check the request header and load
example:
! [weixin](https://user-images.githubusercontent.com/115361435/235084018-32aaad31-45f6-447d-b854-f92241c927e8.png)
! [weixin-2](https://user-images.githubusercontent.com/115361435/235084031-3948e15c-f48f-41c8-aa43-9712cb310909.png)

3. Fill the information in the request header into sender_params.json.
It is worth noting that if you need multi-threaded drawing, please fill in the channelid array with the channelid of different channels (the maximum number of concurrency is 3 for Standard plan, 12 for PRO plan)

4、 Start Web-API
```shell
pip -r requirements.txt
python app.py
```

5. (Optional) Go to app.py to configure cross-domain
```shell
nano app.py
```
## (Updated) Introduction to external API usage:
### Request method
- post request: http://localhost:5000/api/send_and_receive"
- Optional parameter: cdn=true (default false, after enabling the server will cache the image before sending, continental access is more friendly)
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
## Q&A
Q: How often is the information in sender_params.json updated?
A: It has been two weeks since the project was run, and it is still not expired.

## Future plan

- Model switching
- Multi-account concurrency
- easier cookie retrieval

## Contact:
For suggestions and cooperation: Me@hiripple.com
Ask the author to eat Crazy Thursday to speed up the project: https://afdian.net/a/hiripple/plan

## License
MIT

## Additions
Sender.py and Receiver.py are based on https://github.com/George-iam/Midjourney_api二次开发
