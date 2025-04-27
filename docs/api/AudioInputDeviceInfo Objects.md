## AudioInputDeviceInfo Objects

```python
class AudioInputDeviceInfo(StructBase)
```

Platform audio input device info, in a Blueprint-readable format

**C++ Source:**

- **Plugin**: AudioCapture
- **Module**: AudioCapture
- **File**: AudioCaptureBlueprintLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``device_id`` (str):  [Read-Write] ID of the device.
- ``device_name`` (str):  [Read-Write] The name of the audio device
- ``input_channels`` (int32):  [Read-Write] The number of channels supported by the audio device
- ``preferred_sample_rate`` (int32):  [Read-Write] The preferred sample rate of the audio device
- ``supports_hardware_aec`` (bool):  [Read-Write] Whether or not the device supports Acoustic Echo Canceling

<a id="unreal.AudioInputDeviceInfo.__init__"></a>

#### __init__

```python
def __init__(device_name: str = "",
             device_id: str = "",
             input_channels: int = 0,
             preferred_sample_rate: int = 0,
             supports_hardware_aec: bool = False) -> None
```

<a id="unreal.AudioInputDeviceInfo.device_name"></a>

#### device_name

```python
@property
def device_name() -> str
```

(str):  [Read-Only] The name of the audio device

<a id="unreal.AudioInputDeviceInfo.device_id"></a>

#### device_id

```python
@property
def device_id() -> str
```

(str):  [Read-Only] ID of the device.

<a id="unreal.AudioInputDeviceInfo.input_channels"></a>

#### input_channels

```python
@property
def input_channels() -> int
```

(int32):  [Read-Only] The number of channels supported by the audio device

<a id="unreal.AudioInputDeviceInfo.preferred_sample_rate"></a>

#### preferred_sample_rate

```python
@property
def preferred_sample_rate() -> int
```

(int32):  [Read-Only] The preferred sample rate of the audio device

<a id="unreal.AudioInputDeviceInfo.supports_hardware_aec"></a>

#### supports_hardware_aec

```python
@property
def supports_hardware_aec() -> bool
```

(bool):  [Read-Only] Whether or not the device supports Acoustic Echo Canceling

<a id="unreal.AudioCaptureDeviceInfo"></a>