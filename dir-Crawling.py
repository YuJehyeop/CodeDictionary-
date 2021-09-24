# 1. 패키지 기본 틀
    import requests  # requests 라이브러리 설치 필요
    r = requests.get('API')
    rjson = r.json()
    ex = rjson['a']['b']

# 2. 크롤링
#   1) 기본 세팅
    import requests
    from bs4 import BeautifulSoup

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('url',headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    title = soup.select_one('경로 copy > copy selector')
    title = soup.select_one('경로').text  # -> 출력에서 text만 가져온다.
    title = soup.select_one('경로')['href']  # -> href 값을 가져온다. (다른것도 가능)
    title = soup.select('경로')  # -> 리스트 형식으로 가져온다(여러개 가져옴)

  # 2) 활용
    import requests
    from bs4 import BeautifulSoup

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    trs = soup.select('#old_content > table > tbody > tr')
    for tr in trs:
        a_tag = tr.select_one('td.title > div > a')
        if a_tag is not None:
            rank = tr.select_one('td:nth-child(1) > img')['alt']
            title = a_tag.text
            star = tr.select_one('td.point').text
            print(rank,title,star)


