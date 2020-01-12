import requests

session = requests.Session()
jar = requests.cookies.RequestsCookieJar()

jar.set('JSESSIONID', 'EC7D43D0C1C38A9D7216C9548BF01A72.node1')
jar.set('C2RT', 'fb2e46ee2c322709f4d18a908e81f9c3')
jar.set('bocms_visite_user_session', 'C816B689B1A91CC278FD5FCD7CD1CD61')
jar.set('SERVERNAME', 'xk3')
jar.set('GSESSIONID', 'EC7D43D0C1C38A9D7216C9548BF01A72.node1')
session.cookies = jar

# request_toJWGL = session.get('http://jwglnew.hunnu.edu.cn/eams/teach/grade/course/person!search.action?semesterId=82&projectType=&_=1578409087439')
request_toJWGL = session.get('http://jwglnew.hunnu.edu.cn/eams/teach/grade/course/person!historyCourseGrade.action')


print(request_toJWGL.text)