from pycaw.pycaw import AudioUtilities
from time import sleep


def unmute():
    """
    Detect every audio output session and unmute it!
    """
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        interface = session.SimpleAudioVolume
        interface.SetMute(0, None)


def mute():
    """
    Detect every audio output session and mute it!
    """
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        interface = session.SimpleAudioVolume
        interface.SetMute(1, None)


def mute_unmute(delay):
    """
    delay -> int: delay between mute and unmute\n
    Detect every audio output session, mute it and after (delay) unmute it
    Note: The while loop is to make sure you didn't unmute manually!
    """
    i = 0
    while i < delay:
        mute()
        sleep(1)
        i += 1
    unmute()
