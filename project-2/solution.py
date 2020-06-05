import json
import datetime
import time

class LoadTracks:

    def __init__(self):
        with open('track.txt', 'r') as f:
            data_new = json.loads(str(f.read()))
        self.data_new = data_new

    def __str__(self):
        return str(self.data_new)

    def __repr__(self):
        return self.data_new


class PlayMusic(LoadTracks):

    def __init__(self):
        LoadTracks.__init__(self)

    def select_song(self):

        self.status_song = False

        print('\nЭТИ АРТИСТЫ ЕСТЬ В ВАШЕЙ МЕДИАТЕКЕ\n')
        print(f'∆∆∆ {" | ".join(list((self.data_new["tr"]).keys()))} ∆∆∆\n')
        artist = input('∆∆∆ Введите имя артиста - ')
        try:
            selected_artist = dict(self.data_new['tr'][artist])
        except KeyError:
            print('Такого артиста нету в вашей медиатеке')
            self.select_song()
        for i in list(selected_artist.keys()):
            if i == 'Single':
                print(f'\n▁ ▂ ▃ ▅ ▆ █ Синглы Артиста {artist}')
                for b in list(selected_artist['Single'].keys()):
                    print(f"\n♬ {b} - {selected_artist['Single'][b]}")
            elif i == 'Albums':
                for alb in list(selected_artist['Albums'].keys()):
                    print(f'\n▁ ▂ ▃ ▅ ▆ █ Песни из альбома ✖ {alb} ✖')
                    for song in list(selected_artist['Albums'][alb].keys()):
                        print(f"\n♬ {song}  - {selected_artist['Albums'][alb][song]}")
        ch_song = input(
            'Введите название песни, \nЕсли песня из альбома , то введите название альбома и название песни через запятую').split(
            ' ')
        if len(ch_song) == 1:
            song_len = selected_artist['Single'][ch_song[0]]
            x = round(datetime.datetime.timestamp(datetime.datetime.now()))
            now = x + PlayMusic.min_to_sec(song_len)
            print('Песня играет')
            while True:
                if round(datetime.datetime.timestamp(datetime.datetime.now())) == now:
                    print('Песня закончилась')
                    break
                time.sleep(1)



    @staticmethod
    def min_to_sec(time:str):
        time = time.split(':')
        min = int(time[0])
        sec = int(time[1])
        total_sec = 60*min + sec
        return total_sec




