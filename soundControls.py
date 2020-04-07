from pycaw.pycaw import AudioUtilities


def unmute():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        interface = session.SimpleAudioVolume
        interface.SetMute(0, None)


def mute():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        interface = session.SimpleAudioVolume
        interface.SetMute(1, None)
