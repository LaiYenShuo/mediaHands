from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# 获取音量值，0.0代表最大，-65.25代表最小
vl = volume.GetMasterVolumeLevel()
print(vl)


# 设置静音，mute为1代表是静音，为0代表不是静音
volume.SetMute(0, None)
volume.SetMasterVolumeLevel(-65.25 + 8.26, None)

# 设置音量大小为60%
volume.SetMasterVolumeLevel(-7.63, None)