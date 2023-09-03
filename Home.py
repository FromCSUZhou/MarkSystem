import streamlit as st
import openai

import json
import requests
import datetime

api_keys = st.secrets["API_KEYS"]
openai.api_key = api_keys
MONGO_URL_findOne = st.secrets["MONGO_URL_findOne"]
MONGO_URL_updateOne = st.secrets["MONGO_URL_updateOne"]
MONGO_KEY = st.secrets["MONGO_KEY"]


def find_one(user_key):
    payload = json.dumps({
        "collection": "email_info",
        "database": "email_monitoring_db",
        "dataSource": "ChatgptUsing",
        "filter": {"email_address": user_key},
    })
    headers = {
                  'Content-Type': 'application/json',
                  'Access-Control-Request-Headers': '*',
                  'api-key': MONGO_KEY,
    }
    response = requests.request("POST", MONGO_URL_findOne, headers=headers, data=payload)
    print(response.text)
    return json.loads(response.text)


def email_check(user_key, check_date=True):
    email_data = find_one(user_key)
    if email_data["document"] and check_date:
        expiry_date_str = email_data["document"]["expiry_date"]
        expiry_date = datetime.datetime.strptime(expiry_date_str, "%Y-%m-%d").date()

        # 判断 expiry_date 是否在今天之前
        if expiry_date >= datetime.date.today():
            return True
        else:
            return False
    elif email_data["document"] and not check_date:
        return True
    else:
        return False

st.set_page_config(page_title="GPT 学习助手", page_icon=":guardsman:", layout="wide")

user_key = st.text_input("请在这儿输入您的邮箱后按回车键(或使用下方链接激活邮箱)～")

if email_check(user_key):
    user_info = find_one(user_key)
    expire_date = user_info["document"]["expiry_date"]
    # used_tokens = user_info["document"]["used_tokens"]
    st.success("""验证成功，欢迎使用GPT学习助手 👋\n
    您GPT学习助手的有效期限至：{}""".format(expire_date))
    if "shared" not in st.session_state:
        st.session_state["shared"] = True
    if "user_key" not in st.session_state:
        st.session_state["user_key"] = user_key
else:
    st.error("请输入您的邮箱或检查您的邮箱是否正确～")

# st.sidebar.success("欢迎大家使用GPT学习助手 👋")
st.info("邮箱激活链接：https://uaf0q0145e5gy8rw.mikecrm.com/O1jAWJ5")
st.info("""
亲爱的用户🌟，\n
感谢您一直以来对我们智能问答网站的支持和信任💖。自从推出基于ChatGPT API接口的免费智能问答网站以来，我们为您和众多用户提供了一个多月的免费服务。然而，鉴于近期大范围封号风险、恶意举报以及服务器成本压力，我们迫不得已决定从4月4日下午6时起对网站服务进行收费。\n
请谅解，这一决定并非轻率做出。我们的初衷始终是为大家提供免费服务，所以收费标准不会过高，仅需3元一周，并且赠送您一次GPT-4模型的使用机会。您依旧可在规定日期内继续无限量使用我们的网站。\n
尽管转向收费服务，我们仍将致力于网站的维护和新功能开发。在付费界面留下邮箱并成功支付后，您的邮箱将会被立马激活，并可以扫描群二维码进入微信群。在群里，您可以随时反馈意见和需求，我们会尽最大努力满足您的期望。\n
再次感谢您对我们智能问答网站的支持。我们珍视您的每一次使用体验，将继续为您提供更优质的服务。期待与您携手共创美好的未来🌈！\n
意见/建议以及各种需求欢迎反馈到邮箱：englishtool@hotmail.com\n
衷心感谢🌹，\n
Openai在逃员工团队
""")
