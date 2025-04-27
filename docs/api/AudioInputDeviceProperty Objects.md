## AudioInputDeviceProperty Objects

```python
class AudioInputDeviceProperty(StructBase)
```

Encapsulates the array of audio input devices which is populated by UTakeRecorderMicrophoneAudioManager and
utilized by the audio input device list in FAudioInputDevicePropertyCustomization.

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakesCore
- **File**: TakeRecorderSourceProperty.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``audio_input_buffer_size`` (int32):  [Read-Write] The desired buffer size used for audio callbacks during record
- ``device_id`` (str):  [Read-Write] The unique id of the currently selected audio device
- ``device_info_array`` (Array[AudioInputDeviceInfoProperty]):  [Read-Only] Holds device information for each of the audio devices available on this system.
- ``use_system_default_audio_device`` (bool):  [Read-Write] Boolean indicating if the system selects audio device should be used or to use the selected device from the details panel

<a id="unreal.AudioInputDeviceProperty.__init__"></a>

#### __init__

```python
def __init__(use_system_default_audio_device: bool = False,
             device_info_array: Array[AudioInputDeviceInfoProperty] = [],
             device_id: str = "",
             audio_input_buffer_size: int = 0) -> None
```

<a id="unreal.AudioInputDeviceProperty.use_system_default_audio_device"></a>

#### use_system_default_audio_device

```python
@property
def use_system_default_audio_device() -> bool
```

(bool):  [Read-Write] Boolean indicating if the system selects audio device should be used or to use the selected device from the details panel

<a id="unreal.AudioInputDeviceProperty.use_system_default_audio_device"></a>

#### use_system_default_audio_device

```python
@use_system_default_audio_device.setter
def use_system_default_audio_device(value: bool) -> None
```

<a id="unreal.AudioInputDeviceProperty.device_info_array"></a>

#### device_info_array

```python
@property
def device_info_array() -> Array[AudioInputDeviceInfoProperty]
```

(Array[AudioInputDeviceInfoProperty]):  [Read-Only] Holds device information for each of the audio devices available on this system.

<a id="unreal.AudioInputDeviceProperty.device_id"></a>

#### device_id

```python
@property
def device_id() -> str
```

(str):  [Read-Write] The unique id of the currently selected audio device

<a id="unreal.AudioInputDeviceProperty.device_id"></a>

#### device_id

```python
@device_id.setter
def device_id(value: str) -> None
```

<a id="unreal.AudioInputDeviceProperty.audio_input_buffer_size"></a>

#### audio_input_buffer_size

```python
@property
def audio_input_buffer_size() -> int
```

(int32):  [Read-Write] The desired buffer size used for audio callbacks during record

<a id="unreal.AudioInputDeviceProperty.audio_input_buffer_size"></a>

#### audio_input_buffer_size

```python
@audio_input_buffer_size.setter
def audio_input_buffer_size(value: int) -> None
```

<a id="unreal.AudioInputDeviceChannelProperty"></a>