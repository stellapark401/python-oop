from bs4 import BeautifulSoup
from urllib.request import urlopen


class BugsMusic(object):
    url = ''

    @staticmethod
    def main():
        bugs = BugsMusic()
        dict_rank = dict()
        while True:
            menu = int(input("Input the url\t1\nGet ranks\t\t2\nSearch rank\t\t3\nExit\t\t\t0"))
            if menu == 1:
                bugs.url = input('URL 입력: ')
            elif menu == 2:
                soup = BeautifulSoup(urlopen(bugs.url), 'lxml')
                for link in soup.find_all(name='tr', attrs={'rowtype': 'track'}):
                    rank = int(link.find('strong').text)
                    dict_rank[rank] = (link.find('p', {'class': 'artist'}).find('a').text, link.find('p', {'class': 'title'}).find('a').text)
            elif menu == 3:
                search = int(input('몇 위?: ')) - 1
                print(f'{search + 1}위 곡: \'{dict_rank[search][0]}\'(이)가 부른 \'{dict_rank[search][1]}\'')
            elif menu == 0:
                break
            else:
                print('입력이 바르지 않습니다.')
                continue


BugsMusic.main()
