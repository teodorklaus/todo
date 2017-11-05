import requests
import requests_mock


url = 'http://127.0.0.1:5000'

#r = requests.get(url)

# with open ('test.html', 'wb') as output_file:
#     output_file.write(r.text.encode('utf-8'))
#     print (r.text)


with requests_mock.Mocker() as m:
    m.register_uri('GET', url, real_http=True)
    print (requests.get(url).status_code)
    print (requests.get(url).content)

#todo assert
