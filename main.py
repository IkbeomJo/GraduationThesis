from pymongo import MongoClient
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import pymysql

if __name__ == '__main__':
    login_url = 'http://www.hanbit.co.kr/member/login_proc.php'
    session = requests.session()

    params = dict()
    params['userId'] = 'ib0113'
    params['userPwd'] = 'whdlrqja13!'
    res = session.post(login_url, data=params)
    res.raise_for_status()

    # 응답코드가 200 즉, OK가 아닌 경우 에러를 발생시키는 메서드입니다.
    res.raise_for_status()

    # 'Set-Cookie'로 PHPSESSID 라는 세션 ID 값이 넘어옴을 알 수 있다.
    # print(res.headers)

    # cookie로 세션을 로그인 상태를 관리하는 상태를 확인해보기 위한 코드입니다.
    print(session.cookies.get_dict())

    # 여기서부터는 로그인이 된 세션이 유지됩니다. session 에 header에는 Cookie에 PHPSESSID가 들어갑니다.
    mypage_url = 'http://www.hanbit.co.kr/myhanbit/myhanbit.html'
    res = session.get(mypage_url)

    # con = pymysql.connect(host='localhost', user='root', password='dlrqja13',
    #                       db='Lecture_Recommend', charset='utf8',  # 한글처리 (charset = 'utf8')
    #                       autocommit=True,  # 결과 DB 반영 (Insert or update)
    #                       cursorclass=pymysql.cursors.DictCursor  # DB조회시 컬럼명을 동시에 보여줌
    #                       )
    # cur = con.cursor()

    # f = open(r"C:\Users\ikbum\PycharmProjects\university_lecture_extraction\class_row_data.txt", 'r',encoding='UTF8')
    #
    # data = f.read()
    # f.close()
    # soup = BeautifulSoup(data, "html.parser")  # html에 대하여 접근할 수 있도록
    #
    # element = soup.find(
    #     id='mainframe.HFrameSet00.VFrameSet00.WorkFrame.2429.form.div_content.form.Grid00.body.gridrow_0')
    # nexa_element = element.find(id='nexacontainer')
    # nexa_element = nexa_element.find(id='nexacontainer')
    #
    # cur.execute("SQL실행문")
    #
    # # 사용 예
    # sql = 'insert into departments values(280, "depth test", null, 1700)'
    # cur.execute(sql)
    # print(nexa_element)
