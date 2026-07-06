from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL

devices = AudioUtilities.GetSpeakers()

interface = devices.Activate(
    IAudioEndpointVolume._iid_,
    CLSCTX_ALL,
    None
)

volume = cast(interface, POINTER(IAudioEndpointVolume))

# Get actual volume range of your system
min_vol, max_vol, _ = volume.GetVolumeRange()
print("Volume Range:", volume.GetVolumeRange())


def set_volume(percent):

    percent = max(0, min(100, percent))

    level = min_vol + ((max_vol - min_vol) * (percent / 100))

    volume.SetMasterVolumeLevel(level, None)