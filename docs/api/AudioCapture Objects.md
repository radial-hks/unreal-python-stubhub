## AudioCapture Objects

```python
class AudioCapture(AudioGenerator)
```

Class which opens up a handle to an audio capture device.
Allows other objects to get audio buffers from the capture device.

**C++ Source:**

- **Plugin**: AudioCapture
- **Module**: AudioCapture
- **File**: AudioCapture.h

<a id="unreal.AudioCapture.stop_capturing_audio"></a>

#### stop_capturing_audio

```python
def stop_capturing_audio() -> None
```

x.stop_capturing_audio() -> None
Stops capturing audio

<a id="unreal.AudioCapture.start_capturing_audio"></a>

#### start_capturing_audio

```python
def start_capturing_audio() -> None
```

x.start_capturing_audio() -> None
Starts capturing audio

<a id="unreal.AudioCapture.is_capturing_audio"></a>

#### is_capturing_audio

```python
def is_capturing_audio() -> bool
```

x.is_capturing_audio() -> bool
Returns true if capturing audio

Returns:
    bool:

<a id="unreal.AudioCapture.get_audio_capture_device_info"></a>

#### get_audio_capture_device_info

```python
def get_audio_capture_device_info() -> Optional[AudioCaptureDeviceInfo]
```

x.get_audio_capture_device_info() -> AudioCaptureDeviceInfo or None
Returns the audio capture device info

Returns:
    AudioCaptureDeviceInfo or None: 

    out_info (AudioCaptureDeviceInfo):

<a id="unreal.AudioCaptureFunctionLibrary"></a>