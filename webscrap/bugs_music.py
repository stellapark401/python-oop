from bs4 import BeautifulSoup
from urllib.request import urlopen


class BugsMusic(object):
    url = ''

    def to_string(self) -> str:
        return f'입력한 URL: {self.url}'

    @staticmethod
    def main():
        bugs = BugsMusic()
        while True:
            menu = int(input("Input\t\t\t1\nGet rank\t\t2\nSearch rank\t\t3\ndiv tags?\t\t4\nTesting\t\t\t5\nExit\t\t\t0"))
            if menu == 1:
                url = input('URL 입력: ')
                bugs.url = url
            elif menu == 2:
                soup = BeautifulSoup(urlopen(bugs.url), 'lxml')
                artist = list()
                title = list()
                lst_rank = list()
                for link in soup.find_all(name='p', attrs={'class': 'artist'}):
                    artist.append(link.find('a').text)
                    print(type(link))
                for link in soup.find_all(name='p', attrs={'class': 'title'}):
                    title.append(link.find('a').text)
                for i in range(len(artist)):
                    lst_rank.append((artist[i], title[i]))
            elif menu == 3:
                search = int(input('몇 위?: ')) - 1
                print(f'{search + 1}위 곡: \'{lst_rank[search][0]}\'(이)가 부른 \'{lst_rank[search][1]}\'')
            elif menu == 4:
                soup = BeautifulSoup(urlopen(bugs.url), 'lxml')
                for link in soup.find_all(name='div', attrs={'class': 'ranking'}):
                    print(link.find('strong').text)
            elif menu == 5:
                lst_rank = list()
                soup = BeautifulSoup(urlopen(bugs.url), 'lxml')
                for link in soup.find_all(name='tr', attrs={'rowtype': 'track'}):
                    # print(link)
                    rank = int(link.find('strong').text)
                    rank_artist = ''
                    rank_title = ''
                    print(link.find('p', {'class': 'title'}))
            elif menu == 0:
                break
            else:
                print('입력이 바르지 않습니다.')
                continue


BugsMusic.main()
