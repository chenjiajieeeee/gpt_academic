# [step 1]>> 例如： API_KEY = "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" （此key无效）
import os
API_KEY = os.getenv("OPENAI_API_KEY") #使用系统环境变量
WEB_PORT = 8000 #自定义固定端口，如8000
# [step 2]>> 改为True应用代理，如果直接在海外服务器部署，此处不修改
USE_PROXY = False
if USE_PROXY:
    # 填写格式是 [协议]://  [地址] :[端口]，填写之前不要忘记把USE_PROXY改成True，如果直接在海外服务器部署，此处不修改
    # 例如    "socks5h://localhost:11284"
    # [协议] 常见协议无非socks5h/http; 例如 v2**y 和 ss* 的默认本地协议是socks5h; 而cl**h 的默认本地协议是http
    # [地址] 懂的都懂，不懂就填localhost或者127.0.0.1肯定错不了（localhost意思是代理软件安装在本机上）
    # [端口] 在代理软件的设置里找。虽然不同的代理软件界面不一样，但端口号都应该在最显眼的位置上

    # 代理网络的地址，打开你的*学*网软件查看代理的协议(socks5/http)、地址(localhost)和端口(11284)
    proxies = {
        #          [协议]://  [地址]  :[端口]
        "http":  "socks5h://localhost:11284",  # 再例如  "http":  "http://127.0.0.1:7890",
        "https": "socks5h://localhost:11284",  # 再例如  "https": "http://127.0.0.1:7890",
    }
else:
    proxies = None

# [step 3]>> 多线程函数插件中，默认允许多少路线程同时访问OpenAI。Free trial users的限制是每分钟3次，Pay-as-you-go users的限制是每分钟3500次
# 一言以蔽之：免费用户填3，OpenAI绑了信用卡的用户可以填 16 或者更高。提高限制请查询：https://platform.openai.com/docs/guides/rate-limits/overview
DEFAULT_WORKER_NUM = 3


# [step 4]>> 以下配置可以优化体验，但大部分场合下并不需要修改
# 对话窗的高度
CHATBOT_HEIGHT = 1115

# 代码高亮
CODE_HIGHLIGHT = True

# 窗口布局
LAYOUT = "LEFT-RIGHT"  # "LEFT-RIGHT"（左右布局） # "TOP-DOWN"（上下布局）
DARK_MODE = True  # "LEFT-RIGHT"（左右布局） # "TOP-DOWN"（上下布局）

# 发送请求到OpenAI后，等待多久判定为超时
TIMEOUT_SECONDS = 30

# 网页的端口, -1代表随机端口
#WEB_PORT = -1

# 如果OpenAI不响应（网络卡顿、代理失败、KEY失效），重试的次数限制
MAX_RETRY = 2

# 模型选择是 (注意: LLM_MODEL是默认选中的模型, 同时它必须被包含在AVAIL_LLM_MODELS切换列表中 )
LLM_MODEL = "gpt-3.5-turbo" # 可选 ↓↓↓
AVAIL_LLM_MODELS = ["gpt-3.5-turbo-16k", "gpt-3.5-turbo", "api2d-gpt-3.5-turbo", "gpt-4", "api2d-gpt-4", "chatglm", "moss", "newbing", "newbing-free", "stack-claude"]
# P.S. 其他可用的模型还包括 ["newbing-free", "jittorllms_rwkv", "jittorllms_pangualpha", "jittorllms_llama"]

# 本地LLM模型如ChatGLM的执行方式 CPU/GPU
LOCAL_MODEL_DEVICE = "cpu" # 可选 "cuda"

# 设置gradio的并行线程数（不需要修改）
CONCURRENT_COUNT = 100

# 加一个live2d装饰
ADD_WAIFU = False

# 设置用户名和密码（不需要修改）（相关功能不稳定，与gradio版本和网络都相关，如果本地使用不建议加这个）
# [("username", "password"), ("username2", "password2"), ...]
AUTHENTICATION = []

# 重新URL重新定向，实现更换API_URL的作用（常规情况下，不要修改!!）
# （高危设置！通过修改此设置，您将把您的API-KEY和对话隐私完全暴露给您设定的中间人！）
# 格式 {"https://api.openai.com/v1/chat/completions": "在这里填写重定向的api.openai.com的URL"} 
# 例如 API_URL_REDIRECT = {"https://api.openai.com/v1/chat/completions": "https://ai.open.com/api/conversation"}
API_URL_REDIRECT = {}

# 如果需要在二级路径下运行（常规情况下，不要修改!!）（需要配合修改main.py才能生效!）
CUSTOM_PATH = "/"

# 如果需要使用newbing，把newbing的长长的cookie放到这里
NEWBING_STYLE = "creative"  # ["creative", "balanced", "precise"]
# 从现在起，如果您调用"newbing-free"模型，则无需填写NEWBING_COOKIES
NEWBING_COOKIES = """
[
    {
        "domain": ".bing.com",
        "expirationDate": 1718355612.140664,
        "hostOnly": false,
        "httpOnly": false,
        "name": "SnrOvr",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "X=rebateson"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1721293034.992386,
        "hostOnly": false,
        "httpOnly": false,
        "name": "SRCHUSR",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "DOB=20230606&T=1686733026000"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1686747522.724491,
        "hostOnly": false,
        "httpOnly": true,
        "name": "SUID",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "A"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1720520428.79929,
        "hostOnly": false,
        "httpOnly": false,
        "name": "_TTSS_OUT",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "hist=WyJ6aC1IYW5zIl0="
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1721293214.986316,
        "hostOnly": false,
        "httpOnly": false,
        "name": "SRCHHPGUSR",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "SRCHLANG=zh-Hans&PV=15.0.0&BRW=W&BRH=M&CW=1434&CH=714&SCW=1417&SCH=3216&DPR=1.3&UTC=480&DM=0&EXLTT=31&HV=1686733213&PRVCW=1434&PRVCH=714&cdxtone=Precise&cdxtoneopts=h3precise,clgalileo,gencontentv3&BZA=0"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1721292461.011129,
        "hostOnly": false,
        "httpOnly": false,
        "name": "ANON",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "A=8949274253613C01A9E57402FFFFFFFF&E=1c65&W=1"
    },
    {
        "domain": ".bing.com",
        "hostOnly": false,
        "httpOnly": false,
        "name": "_SS",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": true,
        "storeId": null,
        "value": "SID=2B6D2B476AF460D13D3538776B8E6117&PC=ACTS&R=3123&RB=3123&GB=0&RG=0&RP=3123"
    },
    {
        "domain": ".bing.com",
        "hostOnly": false,
        "httpOnly": false,
        "name": "ipv6",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": true,
        "storeId": null,
        "value": "hit=1686736649186&t=4"
    },
    {
        "domain": ".bing.com",
        "hostOnly": false,
        "httpOnly": false,
        "name": "dsc",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": true,
        "storeId": null,
        "value": "order=News"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1687942061.011098,
        "hostOnly": false,
        "httpOnly": false,
        "name": "_U",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "1aBb8nc6PMg_hM3dmmLCljNIL6H-cQ5qEzR1snESeSlSSpeht2020Pfj0rjTr6PVXx3-1EEtcSj-0kTDBufNsUiiGk1eg89HYS8LNDfd9ovUM56-qNHffxEXoYB_6-OEJnBV79mMwxYQOaavQz2g9U5a2RCTMoG1kNPSUH-NObUZCDP2u9AdyvR78pl2G8kxUo3sRTv-v38x74_l8JfNJDA"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1719461460.383792,
        "hostOnly": false,
        "httpOnly": false,
        "name": "SRCHD",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "AF=NOFORM"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1688995783,
        "hostOnly": false,
        "httpOnly": false,
        "name": "ANIMIA",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "FRE=1"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1718597460.383778,
        "hostOnly": false,
        "httpOnly": true,
        "name": "_EDGE_V",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "1"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1701002587.327416,
        "hostOnly": false,
        "httpOnly": false,
        "name": "NAP",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "V=1.9&E=1c0b&C=BXeZKkTePWVMpCLqoA_isNWJQgU345_wJV1sLEHtyldkwqp2Rqlj0A&W=1"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1718355612.140592,
        "hostOnly": false,
        "httpOnly": false,
        "name": "_RwBf",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "r=1&mta=0&rc=3123&rb=3123&gb=0&rg=0&pc=3123&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=2&l=2023-06-14T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&o=0&p=bingcopilotwaitlist&c=MY00IA&t=8435&s=2023-02-17T03:41:34.0636946+00:00&ts=2023-06-14T09:00:12.9822481+00:00&rwred=0&wls=2&lka=0&lkt=0&TH=&e=Vb16uL7IeXRQMYBvOu6GfrQkMB0W6qPmATIosCO2ON_y__nrHmd7a1sL1q2B_TAZ1aC5M5-wweDs0NQ1LXXWvA&A="
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1721293208.860687,
        "hostOnly": false,
        "httpOnly": false,
        "name": "_UR",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "QS=0&TQS=0"
    },
    {
        "domain": ".bing.com",
        "hostOnly": false,
        "httpOnly": true,
        "name": "_EDGE_S",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": true,
        "storeId": null,
        "value": "SID=2B6D2B476AF460D13D3538776B8E6117&mkt=ja-jp"
    },
    {
        "domain": "www.bing.com",
        "expirationDate": 1720429216.433595,
        "hostOnly": true,
        "httpOnly": true,
        "name": "MUIDB",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "38BA37C370616E8E07B824D8717A6FCB"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1721293213.365084,
        "hostOnly": false,
        "httpOnly": true,
        "name": "USRLOC",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "HS=1&ELOC=LAT=35.728973388671875|LON=107.63307189941406|N=%E8%A5%BF%E5%B3%B0%E5%8C%BA%EF%BC%8C%E7%94%98%E8%82%83%E7%9C%81|ELT=4|&BLOCK=TS=230614090014"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1721293209.156239,
        "hostOnly": false,
        "httpOnly": false,
        "name": "_HPVN",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "CS=eyJQbiI6eyJDbiI6MywiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MywiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MywiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMy0wNi0xNFQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6MTB9"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1720520428.797461,
        "hostOnly": false,
        "httpOnly": false,
        "name": "_tarLang",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "default=zh-Hans"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1720520428.798672,
        "hostOnly": false,
        "httpOnly": false,
        "name": "_TTSS_IN",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "hist=WyJlbiIsImF1dG8tZGV0ZWN0Il0="
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1719495911.149074,
        "hostOnly": false,
        "httpOnly": false,
        "name": "MMCASM",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "ID=D8C848050E514C47BF66A6BF3F490ACC"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1719832975.986741,
        "hostOnly": false,
        "httpOnly": false,
        "name": "MUID",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "38BA37C370616E8E07B824D8717A6FCB"
    },
    {
        "domain": ".bing.com",
        "hostOnly": false,
        "httpOnly": false,
        "name": "SRCHS",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": true,
        "storeId": null,
        "value": "PC=ACTS"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1719461460.383799,
        "hostOnly": false,
        "httpOnly": false,
        "name": "SRCHUID",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "V=2&GUID=4A90C11C46264DB5A30D5880E7AA1944&dmnchg=1"
    },
    {
        "domain": ".bing.com",
        "hostOnly": false,
        "httpOnly": false,
        "name": "WLS",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": true,
        "storeId": null,
        "value": "C=88fcc172d977f981&N=jiajie"
    }
]
"""

# 如果需要使用Slack Claude，使用教程详情见 request_llm/README.md
SLACK_CLAUDE_BOT_ID = ''   
SLACK_CLAUDE_USER_TOKEN = ''
