# Midjourney-Web-API
非官方的Midjourney-Web-API,仅用于学习与研究。

## :sparkles: 特性
* ✨ 部署简单、易用
* 👋 支持缓存图片，中国大陆访问友好
* 💾 支持图片Upscale功能，获取高清大图
* 📚 多线程并发，高速绘图
* 💻 自动清理数据库、错误处理功能完善
* 🔐 可设置跨域限制，防盗用

## QuickStart快速开始


## （更新）外部API使用介绍：
- 要使用外部API，nano app.py（配置跨域与sender_params.json文件路径)
- python app.py
### 请求方式
- post请求：http://localhost:5000/api/send_and_receive"
- 可选参数：cdn=true(默认false，启用后服务器将缓存图片然后再发送，大陆访问更友好）
例子：
```python
import requests
import json

payload = {
    "prompt"： "your_prompt_here"
}

url = "http://localhost:5000/api/send_and_receive"；

response = requests.post(url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

print(response.json())
```
- get请求：http://localhost:5000/upscale"
- 必填参数：file_name(string），需要执行upscale的文件名（例如rockgifinrock1971_link_and_zelda_33e8886f-adae-4579-9882-bae644005f5b.png）
- 必填参数：number（number），需要执行upscale的图片序号（例1/2/3/4）。
- 可选参数：cdn=true(默认false，启用后服务器将缓存图片然后再发送，大陆访问更友好）
例子：
```python
import requests

base_url = 'http://localhost:5000'  # 替换为您的 Flask 应用实际运行的 URL
file_name = 'rockgifinrock1971_link_and_zelda_33e8886f-adae-4579-9882-bae644005f5b.png'  # 替换为您的实际文件名
number = 3  # 替换为您想要使用的数字

response = requests.get(f'{base_url}/upscale', params={'file_name': file_name, 'number': number})

if response.status_code == 200:
    print('Success!')
    print(response.json())
else:
    print(f'Error: {response.status_code}')
    print(response.text)
```


## 更新计划

- 模型切换
- 多账号并发
- 更快捷地获取cookie

## 联系方式：
如需建议和合作：Me@hiripple.com
请作者吃疯狂星期四，加快项目进度：https://afdian.net/a/hiripple/plan

## License
MIT

## 补充
Sender.py与Receiver.py基于https://github.com/George-iam/Midjourney_api二次开发
