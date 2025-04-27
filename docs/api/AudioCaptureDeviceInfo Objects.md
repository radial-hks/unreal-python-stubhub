## AudioCaptureDeviceInfo Objects

```python
class AudioCaptureDeviceInfo(StructBase)
```

Struct defining the time synth global quantization settings

**C++ Source:**

- **Plugin**: AudioCapture
- **Module**: AudioCapture
- **File**: AudioCapture.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``device_name`` (Name):  [Read-Write] The name of the audio capture device
- ``num_input_channels`` (int32):  [Read-Write] The number of input channels
- ``sample_rate`` (int32):  [Read-Write] The sample rate of the audio capture device

<a id="unreal.AudioCaptureDeviceInfo.__init__"></a>

#### __init__

```python
def __init__(device_name: Name = "None",
             num_input_channels: int = 0,
             sample_rate: int = 0) -> None
```

<a id="unreal.AudioCaptureDeviceInfo.device_name"></a>

#### device_name

```python
@property
def device_name() -> Name
```

(Name):  [Read-Only] The name of the audio capture device

<a id="unreal.AudioCaptureDeviceInfo.num_input_channels"></a>

#### num_input_channels

```python
@property
def num_input_channels() -> int
```

(int32):  [Read-Only] The number of input channels

<a id="unreal.AudioCaptureDeviceInfo.sample_rate"></a>

#### sample_rate

```python
@property
def sample_rate() -> int
```

(int32):  [Read-Only] The sample rate of the audio capture device

<a id="unreal.MovieSceneGeometryCacheParams"></a>