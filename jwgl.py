import requests
from requests_html import HTMLSession

session = HTMLSession()
jar = requests.cookies.RequestsCookieJar()

jar.set('JSESSIONID', '484D0BF3ACAE818F485245B722641601.node1')
jar.set('C2RT', 'b435f32d05e0ff4cf87d0edf16a417e6')
jar.set('bocms_visite_user_session', 'C816B689B1A91CC278FD5FCD7CD1CD61')
jar.set('SERVERNAME', 'xk3')
jar.set('GSESSIONID', '484D0BF3ACAE818F485245B722641601.node1')
session.cookies = jar

courseIdToFind = ['嵌入式系统', 'Web应用系统设计']
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