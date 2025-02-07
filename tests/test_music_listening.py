import pytest
from lib.music_listening import *

ml = Music_Listener("Jackseph")
# Is there a music listener?

def test_is_there_a_listener():
    ml = Music_Listener("Jackseph")

# Check for list of available songs

def test_are_there_songs_to_listen_to():
    assert len(ml.available_albums_list) > 0

# Check that listened to songs starts out empty

def test_listened_to_dict_starts_empty():
    assert len(ml.listened_to_dict) == 0 

def test_listen_to_track_lovesong():
    ml.listen_to("Lovesong")
    assert "The Cure" in ml.listened_to_dict.keys()
    assert "Disintigration" in ml.listened_to_dict["The Cure"].keys()
    assert "Lovesong" in ml.listened_to_dict["The Cure"]["Disintigration"]

def test_listen_to_track_taxman():
    ml.listened_to_dict = {}
    ml.listen_to("Taxman")
    assert "The Beatles" in ml.listened_to_dict.keys()
    assert "Revolver" in ml.listened_to_dict["The Beatles"].keys()
    assert "Taxman" in ml.listened_to_dict["The Beatles"]["Revolver"]

def test_return_listened_to():      # Test adding 1 song from a fresh start, then adding a song from a different album, then a song from the same album, then a song from the first album again,
    ml.listened_to_dict = {}        # then a song from an entirely new album before 
    ml.listen_to('Taxman') 
    assert ml.return_listened_to() == {"The Beatles": {"Revolver": ["Taxman"]}}
    ml.listen_to('No Surprises')
    assert ml.return_listened_to() == {"The Beatles": {"Revolver": ["Taxman"]}, "Radiohead": {"OK Computer": ["No Surprises"]}}
    ml.listen_to('Lucky')
    assert ml.return_listened_to() == {"The Beatles": {"Revolver": ["Taxman"]}, "Radiohead": {"OK Computer": ["No Surprises", "Lucky"]}}
    ml.listen_to('Eleanor Rigby')
    assert ml.return_listened_to() == {"The Beatles": {"Revolver": ["Taxman", "Eleanor Rigby"]}, "Radiohead": {"OK Computer": ["No Surprises", "Lucky"]}}
    ml.listen_to('Lovesong')
    assert ml.return_listened_to() == {"The Beatles": {"Revolver": ["Taxman", "Eleanor Rigby"]}, "Radiohead": {"OK Computer": ["No Surprises", "Lucky"]}, "The Cure": {"Disintigration": ["Lovesong"]}}
    ml.listened_to_dict = {}
    ml.listen_to('Lovesong')
    assert ml.return_listened_to() == {"The Cure": {"Disintigration": ["Lovesong"]}}

