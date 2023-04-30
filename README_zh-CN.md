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
1、 clone项目
```shell
git clone https://github.com/CelestialRipple/Midjourney-Web-API
cd Midjourney-Web-API
```
2、 获取Cookie（请确认你可以在discord中使用Midjourney绘图）
- 进入Discord中与Midjourney Bot的对话框-
- 打开任一浏览器的开发者工具（右键/F12），选中网络（network）选项
- 发送任意绘图请求
- 开发者工具中搜索interaction，查看请求头部与负载


example：
![weixin](https://user-images.githubusercontent.com/115361435/235084018-32aaad31-45f6-447d-b854-f92241c927e8.png)
![weixin-2](https://user-images.githubusercontent.com/115361435/235084031-3948e15c-f48f-41c8-aa43-9712cb310909.png)

3、 将请求头部中的信息填入sender_params.json。
值得注意的时，如果你需要多线程画图，请将不同频道抓取的channelid填入channelid数组中（Standard计划最大并发数为3，PRO计划为12）

4、 启动Web-API
```shell
pip -r requirements.txt
python app.py
```

5、(可选)进入APP.py配置跨域
```shell
nano app.py
```
## （更新）外部API使用介绍：
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
## 解答
Q：sender_params.json中的信息隔多久更新？
A：项目运行以来已经有两周，目前仍未过期。

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
