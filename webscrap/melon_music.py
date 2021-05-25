from bs4 import BeautifulSoup
import requests


class MelonMusic(object):
    tags = ''
    rank_dict = dict()

    @staticmethod
    def get_ranks(tags):
        soup = BeautifulSoup(tags, 'html.parser')
        cnt = 0
        for link in soup.find('form', {'id': 'frm'}).find('table').find('tbody').find_all('tr'):
            MelonMusic.rank_dict[cnt] = (link.find('div', {'class': 'ellipsis rank01'})
                                         .find('a').text, link.find('div', {'class': 'ellipsis rank02'}).find('a').text)
            cnt += 1
        if len(MelonMusic.rank_dict) == 100:
            print('Top 100 songs have been brought successfully.')

    @staticmethod
    def search_rank():
        search = int(input('몇 위?: ')) - 1
        print(f"{search + 1}위 곡: \'{MelonMusic.rank_dict[search][1]}\'의 \'{MelonMusic.rank_dict[search][0]}\'")

    @staticmethod
    def main():
        while True:
            mn = int(input('Input the url\t1\nGet the rank\t2\nSearch the rank\t3\nExit\t\t\t0'))
            if mn == 1:
                url = input('URL 입력: ')
                header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
                MelonMusic.tags = requests.get(url, headers=header).text
            elif mn == 2:
                MelonMusic.get_ranks(MelonMusic.tags)
            elif mn == 3:
                MelonMusic.search_rank()
            elif mn == 0:
                break
            else:
                print("You've entered the wrong number.")
                continue


MelonMusic.main()
