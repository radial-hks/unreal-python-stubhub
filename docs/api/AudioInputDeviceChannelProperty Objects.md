## AudioInputDeviceChannelProperty Objects

```python
class AudioInputDeviceChannelProperty(StructBase)
```

This class is used by Microphone sources to track the currently selected channel. It aslo
contains a local cache of the max channel count for the currently selected audio device.

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakesCore
- **File**: TakeRecorderSourceProperty.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``audio_input_device_channel`` (int32):  [Read-Write] The currently selected channel from the details panel for this source

<a id="unreal.AudioInputDeviceChannelProperty.__init__"></a>

#### __init__

```python
def __init__(audio_input_device_channel: int = 0) -> None
```

<a id="unreal.AudioInputDeviceChannelProperty.audio_input_device_channel"></a>

#### audio_input_device_channel

```python
@property
def audio_input_device_channel() -> int
```

(int32):  [Read-Write] The currently selected channel from the details panel for this source

<a id="unreal.AudioInputDeviceChannelProperty.audio_input_device_channel"></a>

#### audio_input_device_channel

```python
@audio_input_device_channel.setter
def audio_input_device_channel(value: int) -> None
```

<a id="unreal.TakeRecorderUserParameters"></a>