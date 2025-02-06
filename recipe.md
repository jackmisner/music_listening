## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Function Signature

class music_listener(person)

Arguments:
person is the user who listens to the music

Variables:
List of available songs (with artist/album/track info)
songs_listened_dict -> Dict of songs listened to in the format {Artist:{Album:[Track]}}


Functions:
listen_to(track)
    add track to songs_listened_dict

return_listened_to()
    return f"{user} listened to {track} by {artist} from the album {album}"

return_not_listened_to_yet()
    return [songs not listened to yet]

