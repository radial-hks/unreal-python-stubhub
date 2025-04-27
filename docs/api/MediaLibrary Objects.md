## MediaLibrary Objects

```python
class MediaLibrary(BlueprintFunctionLibrary)
```

Blueprint library for Media related functions.

**C++ Source:**

- **Module**: MediaAssets
- **File**: MediaBlueprintFunctionLibrary.h

<a id="unreal.MediaLibrary.enumerate_webcam_capture_devices"></a>

#### enumerate_webcam_capture_devices

```python
@classmethod
def enumerate_webcam_capture_devices(cls,
                                     filter: int = -1
                                     ) -> Array[MediaCaptureDevice]
```

X.enumerate_webcam_capture_devices(filter=-1) -> Array[MediaCaptureDevice]
Enumerate available audio capture devices.

To filter for a specific subset of devices, use the MakeBitmask node
with EMediaWebcamCaptureDeviceFilter as the Bitmask Enum.

Args:
    filter (int32): The types of capture devices to return (-1 = all).

Returns:
    Array[MediaCaptureDevice]: 

    out_devices (Array[MediaCaptureDevice]): Will contain the available capture devices.

<a id="unreal.MediaLibrary.enumerate_video_capture_devices"></a>

#### enumerate_video_capture_devices

```python
@classmethod
def enumerate_video_capture_devices(cls,
                                    filter: int = -1
                                    ) -> Array[MediaCaptureDevice]
```

X.enumerate_video_capture_devices(filter=-1) -> Array[MediaCaptureDevice]
Enumerate available audio capture devices.

To filter for a specific subset of devices, use the MakeBitmask node
with EMediaVideoCaptureDeviceFilter as the Bitmask Enum.

Args:
    filter (int32): The types of capture devices to return (-1 = all).

Returns:
    Array[MediaCaptureDevice]: 

    out_devices (Array[MediaCaptureDevice]): Will contain the available capture devices.

<a id="unreal.MediaLibrary.enumerate_audio_capture_devices"></a>

#### enumerate_audio_capture_devices

```python
@classmethod
def enumerate_audio_capture_devices(cls,
                                    filter: int = -1
                                    ) -> Array[MediaCaptureDevice]
```

X.enumerate_audio_capture_devices(filter=-1) -> Array[MediaCaptureDevice]
Enumerate available audio capture devices.

To filter for a specific subset of devices, use the MakeBitmask node
with EMediaAudioCaptureDeviceFilter as the Bitmask Enum.

Args:
    filter (int32): The types of capture devices to return (-1 = all).

Returns:
    Array[MediaCaptureDevice]: 

    out_devices (Array[MediaCaptureDevice]): Will contain the available capture devices.

<a id="unreal.DefaultLevelSequenceInstanceData"></a>