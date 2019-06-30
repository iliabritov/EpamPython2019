import bs4
import requests


class PikabuGrabber():

    HOMEPAGE = 'https://pikabu.ru/'
    HEADERS = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36', 
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://pikabu.ru",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cache-Control": 'max-age=0',
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "TE": "Trailers",
    "Host": 'pikabu.ru',
    "X-Requested-With": 'XMLHttpRequest',
    "Upgrade-Insecure-Requests": "1"
    }
    DATA = {
        'twinmode': '1',
        'of': 'v2',
        'page': '1'
        }

    def __init__(self):
        self.session = requests.Session()
        self.headers = self.HEADERS
        self.data = self.DATA
        with open('Cookie.txt') as file:
            cookies = file.read()
        cookies = [(elem.split('=')[0], elem.split('=')[1]) for elem in cookies.split('; ')]
        cookies = requests.cookies.cookiejar_from_dict({key:val for key, val in cookies})
        self.session.cookies = cookies

    def getPages(self, url, page_quantity):
        result = []
        for num in range(page_quantity):
            self.data['page'] = num
            result.append(self.session.get(url,
                        data=self.data, headers=self.headers).text) 
        return result


if __name__ == '__main__':
    curr_pikabu_tags = {}
    new = PikabuGrabber()  
    pages = new.getPages(url='https://pikabu.ru/subs', page_quantity=15)
    for page in pages:
        soup = bs4.BeautifulSoup(page, features="lxml")
        result = soup.find_all('div', attrs = {'class': 'story__tags tags'})
        for tag in result:
            a_objs = tag.find_all('a')
            for elem in a_objs:
                if 'data-tag' in elem:
                    pikabu_tag = elem['data-tag']
                else:
                    pikabu_tag = elem.text
                if pikabu_tag in curr_pikabu_tags:
                    curr_pikabu_tags[pikabu_tag] += 1
                else:
                    curr_pikabu_tags[pikabu_tag] = 1

    # printing in file 10 first elements
    result = sorted(curr_pikabu_tags.items(),
                    key= lambda i: i[1], reverse=True)[:10]
    with open('result.txt', 'w') as file:
        file.write('Top-Tags:\n')
        for tag in result:
            file.write('{0:30} - {1:1} \n'.format(tag[0], str(tag[1])))

    
    
    
