import requests
from bs4 import BeautifulSoup
import time
from telegram import Bot

# 이전에 확인한 상품 갯수
previous_count = 0

# 텔레그램 봇 토큰
telegram_token = "token"

# 텔레그램 채팅 ID
telegram_chat_id = "id"

# 웹 페이지 URL
url = "https://www.hermes.com/kr/ko/category/women/bags-and-small-leather-goods/bags-and-clutches/#|"

# 텔레그램 봇 초기화
bot = Bot(token=telegram_token)

while True:
    # 웹 페이지 요청
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 상품 요소 추출
    products = soup.select("div.product-item")
    
    # 현재 상품 갯수
    current_count = len(products)
    
    # 상품 갯수가 변화한 경우 알림 전송
    if current_count != previous_count:
        message = f"상품 갯수가 변경되었습니다!\n이전 상품 갯수: {previous_count}\n현재 상품 갯수: {current_count} \n {url} "
        bot.send_message(chat_id=telegram_chat_id, text=message)
    
    # 이전 상품 갯수 업데이트
    previous_count = current_count
    
    # 2분마다 웹 페이지 확인
    time.sleep(120)
