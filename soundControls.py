from pycaw.pycaw import AudioUtilities
from time import sleep


def unmute():
    """
    Detect every audio output session and unmute it!
    params:
        none
    return:
        none
    """
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        interface = session.SimpleAudioVolume
        interface.SetMute(0, None)


def mute():
    """
    Detect every audio output session and mute it!\n
    params:
        none
    return
        none
    """
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        interface = session.SimpleAudioVolume
        interface.SetMute(1, None)


def mute_unmute(delay, allow_unmute=False):
    """
    Detect every audio output session, mute it and after (delay) unmute it\n
    params:
        delay (int): delay between mute and unmute
        allow_unmute (bool): Default=False
            True: User can unmute manually
            False: User can't unmute manually
    return:
        none
    """
    if allow_unmute:
        mute()
        sleep(delay)
    elif not allow_unmute:
        i = 0
        while i < delay:
            mute()
            sleep(1)
            i += 1
    unmute()
