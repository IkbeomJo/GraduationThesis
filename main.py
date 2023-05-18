from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import sys

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    login_url = "https://sso2.hs.ac.kr/" # 로그인 URL 정보
    driver.get(login_url) # 로그인 URL로 접속
    driver.implicitly_wait(3) # URL 접속후 브라우저 로딩을 위해 3초 대기

    # 한신대 포털을 들어가기 위한 로그인 데이터 입력
    login_Data = {
        'id' : 'ib0113',
        'pwd' : 'whdlrqja13!'
    }

    driver.find_element(By.ID, 'userId').send_keys(login_Data['id']) # ID FORM에 id 입력
    sleep(0.5)
    driver.find_element(By.ID, 'userPwd').send_keys(login_Data['pwd']) # PWD FORM에 pwd 입력
    sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="ssoLoginFrm"]/div[1]/div/input[3]').click() # 로그인 버튼 클릭

    if driver.current_url != "https://sso2.hs.ac.kr/loginSuccess.do":
        print("로그인에 실패하였습니다.")
        sys.exit()
    sleep(2)
    driver.get("https://hsctis.hs.ac.kr/app-nexa/index.html")



    ###########################  아래코드는 과목 데이터가 있는 테이블까지 가는 경로  ########################################
    sleep(2)
    driver.find_element(By.XPATH,'//*[@id="mainframe.HFrameSet00.LeftFrame.form.div_left_wrap2.form.menulist_wrap.form.menu_dep01_1"]').click()
    sleep(0.5)
    driver.find_element(By.XPATH,'//*[@id="mainframe.HFrameSet00.LeftFrame.form.div_left_wrap2.form.menulist_wrap.form.menu_dep02_wrap_1.form.menu_dep02_1"]').click()
    sleep(0.5)
    driver.find_element(By.XPATH,'//*[@id="mainframe.HFrameSet00.LeftFrame.form.div_left_wrap2.form.menulist_wrap.form.menu_dep02_wrap_1.form.menu_dep03_wrap_1.form.menu_dep03_1"]').click()
    sleep(0.5)
    driver.find_element(By.XPATH,'//*[@id="mainframe.HFrameSet00.LeftFrame.form.div_left_wrap2.form.menulist_wrap.form.menu_dep02_wrap_1.form.menu_dep03_wrap_1.form.menu_dep04_wrap_1.form.menu_dep04_14"]').click()
    sleep(0.5)
    #################################################################################################################

    ##################### 학교 시스템 개인 브라우저의 고유 코드를 추출하는 코드 #################################
    element = driver.find_element(By.CSS_SELECTOR,
                                  '#mainframe\\.HFrameSet00\\.VFrameSet00\\.WorkFrame > div:first-child > div:first-child')
    element_id = element.get_attribute('id')
    element_id = element_id.split('.')[-1]
    print(element_id)
    ####################################################################################################
    # 찾고자 하는 데이터의 값 설정
    lecture_Data_CF = {
        'year': 2022,
        'Semester': '2학기',  # 1학기, 2학기, 여름계절학기, 겨울계절학기, 입학전특별교육
    }
    Semester_tabel = [None, '1학기', '2학기', '여름계절학기', '겨울계절학기', '입학전특별교육']
    sleep(1)


    # 찾고자 하는 데이터의 학년도 값을 변경 하는 코드
    spin_edit_elem = driver.find_element(By.XPATH, f'//*[@id="mainframe.HFrameSet00.VFrameSet00.WorkFrame.{element_id}.form.div_content.form.div_search.form.spn_shyr"]')
    spin_edit_elem.click()  # SpinEdit 컴포넌트 클릭하여 선택
    spin_edit_input = spin_edit_elem.find_element(By.CSS_SELECTOR, '.spinedit input')
    spin_edit_input.clear()  # SpinEdit 컴포넌트 입력 값 초기화
    spin_edit_input.send_keys(lecture_Data_CF['year'])  # SpinEdit 컴포넌트 입력 값 변경

    # 찾고자 하는 데이터의 학기 값을 변경 하는 코드
    input_box = driver.find_element(By.ID,f'mainframe.HFrameSet00.VFrameSet00.WorkFrame.{element_id}.form.div_content.form.div_search.form.cbo_smstGbcd.comboedit')
    action = ActionChains(driver)
    action.move_to_element(input_box).click().perform()
    sleep(0.3)
    action.move_to_element_with_offset(input_box, 0, input_box.size['height']*Semester_tabel.index(lecture_Data_CF['Semester'])).click().perform()

    # 변경한 값으로 결과를 출력 하는 버튼
    driver.find_element(By.XPATH,f'//*[@id="mainframe.HFrameSet00.VFrameSet00.WorkFrame.{element_id}.form.div_content.form.div_search.form.btn_search"]').click()


    scroll_bnt = driver.find_element(By.XPATH,'//*[@id="mainframe.HFrameSet00.VFrameSet00.WorkFrame.2429.form.div_content.form.Grid00.vscrollbar.incbutton:icontext"]')
    for i in range(20):
        scroll_bnt.click()
        sleep(0.5)

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
