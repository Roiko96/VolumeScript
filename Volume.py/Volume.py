import keyboard
import comtypes
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, comtypes.CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

def increase_volume():
    current_volume = volume.GetMasterVolumeLevel()
    new_volume = min(current_volume + 2.0, 0.0)
    volume.SetMasterVolumeLevel(new_volume, None)
    print("Volume increased. Current level:", new_volume)

def decrease_volume():
    current_volume = volume.GetMasterVolumeLevel()
    new_volume = max(current_volume - 2.0, -65.25)
    volume.SetMasterVolumeLevel(new_volume, None)
    print("Volume decreased. Current level:", new_volume)

keyboard.add_hotkey('-', decrease_volume)
keyboard.add_hotkey('+', increase_volume)

print("Script is running. Press ESC to exit.")
keyboard.wait('esc')
