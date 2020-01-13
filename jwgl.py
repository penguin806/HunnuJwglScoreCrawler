import requests
from requests_html import HTMLSession
import time

def crawlGradeFromGwgl():
    session = HTMLSession()
    jar = requests.cookies.RequestsCookieJar()

    jar.set('JSESSIONID', '6BA651B6212F486ECA797A5DDC7ED5B9.node1')
    jar.set('C2RT', '752a8a3bea43ee86559ed1ee5c815f18')
    jar.set('bocms_visite_user_session', 'C816B689B1A91CC278FD5FCD7CD1CD61')
    jar.set('SERVERNAME', 'xk5')
    jar.set('GSESSIONID', '6BA651B6212F486ECA797A5DDC7ED5B9.node1')
    session.cookies = jar

    courseIdToFind = ['12160007.08', '22163171.01', '22163219.01', '22163280.01']
    # request_toJWGL = session.get('http://jwglnew.hunnu.edu.cn/eams/teach/grade/course/person!search.action?semesterId=82&projectType=&_=1578409087439')
    result = session.get('http://jwglnew.hunnu.edu.cn/eams/teach/grade/course/person!historyCourseGrade.action')
    gradeRows = result.html.find('div.grid>table.gridtable>tbody tr', containing = courseIdToFind)

    if len(gradeRows) > 0:
        textBuffer = ''
        for item in gradeRows:
            courseId = item.find('td:nth-child(3)')[0].text
            courseName = item.find('td:nth-child(4)')[0].text
            courseScore = item.find('td:nth-last-child(3)')[0].text
            textBuffer += courseId + ' ' + courseName + ': ' + courseScore + '\n'
        print(textBuffer)
    else:
        print('[' + ','.join(courseIdToFind) + '] Not Found')



while True:
    print(time.strftime('%Y-%m-%d %X',time.localtime()))
    crawlGradeFromGwgl()
    time.sleep(180)
