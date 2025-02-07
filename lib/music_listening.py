from lib.album import *

revolver = Album("The Beatles", "Revolver", ["Taxman","Eleanor Rigby","Here, There and Everywhere","Tomorrow Never Knows","Good Day Sunshine"])
wtsmg = Album("Oasis", "What's The Story, Morning Glory", ["Wonderwall","Don't Look Back in Anger","Champagne Supernova","Roll with It","Some Might Say"])
disintigration = Album("The Cure", "Disintigration", ['Lovesong','Pictures of You','Lullaby','Fascination Street','Prayers for Rain'])
ok_computer = Album("Radiohead", "OK Computer", ["Paranoid Android","No Surprises","Karma Police","Exit Music (For a Film)","Lucky"])
wpsiatwin = Album('Arctic Monkeys', "Whatever People Say I Am: That's What I'm Not", ["I Bet You Look Good on the Dancefloor","Fake Tales of San Francisco","When the Sun Goes Down","The View from the Afternoon","A Certain Romance"])

class Music_Listener():
    def __init__(self, name):
        self.name = name
        self.listened_to_dict = {}
        self.available_albums_list = [disintigration, wpsiatwin, revolver,wtsmg, ok_computer]
   
    def listen_to(self, listened_to_song):
        self.listened_to_song = listened_to_song
        self.listened_to_song_list = []
        for item in self.available_albums_list:
            for song in item.song_list:
                if song == listened_to_song:
                    entry = list(self.listened_to_dict.values())
                    if any(item.album in d for d in entry):
                        self.listened_to_song_list = self.listened_to_dict[item.artist][item.album]
                    self.listened_to_song_list.append(listened_to_song)
                    self.album_and_songs = {item.album:self.listened_to_song_list}
                    self.listened_to_dict[item.artist] = self.album_and_songs

    def return_listened_to(self):
        return self.listened_to_dict