from bs4 import BeautifulSoup
import requests


class MelonMusic(object):
    tags = ''

    @staticmethod
    def main():
        mm = MelonMusic()
        rank_dict = dict()
        while True:
            mn = int(input('Input the url\t1\nGet the rank\t2\nSearch the rank\t3\nExit\t\t\t0'))
            if mn == 1:
                url = input('URL 입력: ')
                header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
                mm.tags = requests.get(url, headers=header).text
            elif mn == 2:
                soup = BeautifulSoup(mm.tags, 'html.parser')
                cnt = 0
                for link in soup.find('form', {'id': 'frm'}).find('table').find('tbody').find_all('tr'):
                    rank_dict[cnt] = (link.find('div', {'class': 'ellipsis rank01'}).find('a').text, link.find('div', {'class': 'ellipsis rank02'}).find('a').text)
                    cnt += 1
                if len(rank_dict) == 100:
                    print('Top 100 songs have been brought successfully.')
            elif mn == 3:
                search = int(input('몇 위?: ')) - 1
                print(f"{search + 1}위 곡: \'{rank_dict[search][1]}\'의 \'{rank_dict[search][0]}\'")
            elif mn == 0:
                break
            else:
                print("You've entered the wrong number.")
                continue


MelonMusic.main()
