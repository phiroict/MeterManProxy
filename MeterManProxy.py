from flask import Flask
import urllib
import urllib.request
import urllib.parse
import datetime

app = Flask(__name__)




@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'This path: %s no longer leads to the lands in the west. Take a boat. ' % path

@app.route('/pvoutput/getstatus/<sysid>/<key>')
def getStatus(sysid, key):
    url='http://pvoutput.org/service/r2/getstatus.jsp'
    params = {'d': datetime.date.today().strftime("%Y%m%d")}
    querystring = urllib.parse.urlencode(params)
    request = urllib.request.Request(url, data=querystring.encode('utf-8'), headers={'X-Pvoutput-Apikey':key, 'X-Pvoutput-SystemId': sysid})
    response = urllib.request.urlopen(request)
    return response.read()

@app.route('/pvoutput/getstatusByDate/<sysid>/<key>/<date>')
def getStatusByDate(sysid, key, date):
    url='http://pvoutput.org/service/r2/getstatus.jsp'
    params = {'d': date}
    querystring = urllib.parse.urlencode(params)
    request = urllib.request.Request(url, data=querystring.encode('utf-8'), headers={'X-Pvoutput-Apikey':key, 'X-Pvoutput-SystemId': sysid})
    response = urllib.request.urlopen(request)
    return response.read()



if __name__ == '__main__':
    app.run()
