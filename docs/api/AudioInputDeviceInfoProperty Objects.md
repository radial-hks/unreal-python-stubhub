## AudioInputDeviceInfoProperty Objects

```python
class AudioInputDeviceInfoProperty(StructBase)
```

Encapsulates audio device properties which are utilized by UI facing classes such as FAudioInputDeviceProperty.

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakesCore
- **File**: TakeRecorderSourceProperty.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``device_id`` (str):  [Read-Only] The unique id used to identify the device
- ``device_name`` (str):  [Read-Only] User friendly name of the audio device
- ``input_channels`` (int32):  [Read-Only] The number input channels this device supports
- ``is_default_device`` (bool):  [Read-Only] Boolean indicating if this device is the currently the system selected input device
- ``preferred_sample_rate`` (int32):  [Read-Only] The preferred sample rate for this audio device

<a id="unreal.AudioInputDeviceInfoProperty.__init__"></a>

#### __init__

```python
def __init__(device_name: str = "",
             device_id: str = "",
             input_channels: int = 0,
             preferred_sample_rate: int = 0,
             is_default_device: bool = False) -> None
```

<a id="unreal.AudioInputDeviceInfoProperty.device_name"></a>

#### device_name

```python
@property
def device_name() -> str
```

(str):  [Read-Only] User friendly name of the audio device

<a id="unreal.AudioInputDeviceInfoProperty.device_id"></a>

#### device_id

```python
@property
def device_id() -> str
```

(str):  [Read-Only] The unique id used to identify the device

<a id="unreal.AudioInputDeviceInfoProperty.input_channels"></a>

#### input_channels

```python
@property
def input_channels() -> int
```

(int32):  [Read-Only] The number input channels this device supports

<a id="unreal.AudioInputDeviceInfoProperty.preferred_sample_rate"></a>

#### preferred_sample_rate

```python
@property
def preferred_sample_rate() -> int
```

(int32):  [Read-Only] The preferred sample rate for this audio device

<a id="unreal.AudioInputDeviceInfoProperty.is_default_device"></a>

#### is_default_device

```python
@property
def is_default_device() -> bool
```

(bool):  [Read-Only] Boolean indicating if this device is the currently the system selected input device

<a id="unreal.AudioInputDeviceProperty"></a>