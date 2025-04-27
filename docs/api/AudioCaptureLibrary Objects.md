## AudioCaptureLibrary Objects

```python
class AudioCaptureLibrary(BlueprintFunctionLibrary)
```

Audio Capture Blueprint Library

**C++ Source:**

- **Plugin**: AudioCapture
- **Module**: AudioCapture
- **File**: AudioCaptureBlueprintLibrary.h

<a id="unreal.AudioCaptureLibrary.get_available_audio_input_devices"></a>

#### get_available_audio_input_devices

```python
@classmethod
def get_available_audio_input_devices(
        cls, world_context_object: Object,
        on_obtain_devices_event: OnAudioInputDevicesObtained) -> None
```

X.get_available_audio_input_devices(world_context_object, on_obtain_devices_event) -> None
Gets information about all audio output devices available in the system

Args:
    world_context_object (Object): 
    on_obtain_devices_event (OnAudioInputDevicesObtained): the event to fire when the audio endpoint devices have been retrieved

<a id="unreal.AudioCaptureLibrary.conv_audio_input_device_info_to_string"></a>

#### conv_audio_input_device_info_to_string

```python
@classmethod
def conv_audio_input_device_info_to_string(cls,
                                           info: AudioInputDeviceInfo) -> str
```

X.conv_audio_input_device_info_to_string(info) -> str
Returns the device info in a human readable format

Args:
    info (AudioInputDeviceInfo): The audio device data to print

Returns:
    str: The data in a string format

<a id="unreal.AudioCaptureComponent"></a>