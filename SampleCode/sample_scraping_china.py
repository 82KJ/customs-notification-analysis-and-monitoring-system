'''
FileName : scraper/scraping/scrap_china.py
Summary : 중국 문서 크롤링 및 키워드 추출 모듈
'''

# ===================================================================
#  Sample Code of China Scraper
# ===================================================================

'''
Description: 영어로 번역된 중국 문서의 데이터프레임을 전처리(구두점, 숫자, 월, 불용어 등을 제거 및 소문자화)하기 위한 함수
Parameter: removed
return: removed
'''
def preprocess(): pass

'''
Description: 크롤링해온 중국 문서의 본문 내용을 영어로 번역하는 함수
Parameter: removed
Return: removed
'''
def china_trans_text(): pass

'''
Description: 새롭게 올라온 중국의 세관고시가 있을 경우, 문서를 크롤링하여 date, link, title, content를 뽑아낸 후 제목 번역, 
본문 내용 영어 번역, 중국 내부 문서에 .xls이 존재하는지 파악 후 그 xls에 hscode가 있는지 파악, 키워드 추출 및 모니터링 품목 매칭 진행 후 DB에 저장
Parameter: cur_title(DB에 저장된 가장 최신 문서의 제목, 제목이 같은 경우가 있기 떄문에 link로 비교 수정하는 것이 더 좋음)
Return: True = DB에 최신 문건이 추가됨 / False = DB에 변화가 없음
'''
def scrap_china(cur_title):
    
    # 1. 동적 scraping을 위한, selenium 동작
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_argument('User-Agent=Input Your useragent')
    browser = webdriver.Chrome(options=options)

    browser.get('http://www.customs.gov.cn/customs/302249/302266/index.html')

    # 2. html parsing 진행
    soup = BeautifulSoup(browser.page_source, 'lxml')
    
    titles = []
    dates = []
    links = []
  
    # 3. 제목, 링크, 날짜 list 변환 저장 수행
    try:
        ul = soup.find('ul', attrs = {'class' : 'conList_ull'}).find_all('li')
    except:
        print('중국 서버 통신 문제로 크롤링을 중단합니다. 추후 다시 시도 부탁드립니다')
        return False

    for li in ul:
        title = li.a.get_text().strip()
        link = 'http://www.customs.gov.cn'+li.a['href']
        date = li.span.get_text().strip()

        titles.append(title)
        links.append(link)
        dates.append(date)

    if len(titles) != 0:
        if cur_title == titles[0]:
            return False
        else:
            idx = titles.index(cur_title)
    else:
        return False

    #===============================================================================================================================#
    # All the code below has been removed as a private area.

    # 4. 세관고시 본문 내용 크롤링 수행
    # 5. 제목 한국어 번역 수행
    # 6. 본문 내용 영어 번역 수행
    # 7. 중국 내부 .xls에 hscode가 있는지 파악 수행
    # 8. 핵심 키워드 추출 및 모니터링 품목 매칭 수행
    # 8. DataBase 갱신 수행

    return True