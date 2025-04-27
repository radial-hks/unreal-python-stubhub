## AudioOutputDeviceInfo Objects

```python
class AudioOutputDeviceInfo(StructBase)
```

Platform audio output device info, in a Blueprint-readable format

**C++ Source:**

- **Module**: AudioMixer
- **File**: AudioMixerBlueprintLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``device_id`` (str):  [Read-Write] ID of the device.
- ``format`` (AudioMixerStreamDataFormatType):  [Read-Write] The data format of the audio stream
- ``is_current_device`` (bool):  [Read-Write] Whether or not this device is the device currently in use
- ``is_system_default`` (bool):  [Read-Write] Whether or not this device is the system default
- ``name`` (str):  [Read-Write] The name of the audio device
- ``num_channels`` (int32):  [Read-Write] The number of channels supported by the audio device
- ``output_channel_array`` (Array[AudioMixerChannelType]):  [Read-Write] The output channel array of the audio device
- ``sample_rate`` (int32):  [Read-Write] The sample rate of the audio device

<a id="unreal.AudioOutputDeviceInfo.__init__"></a>

#### __init__

```python
def __init__(
        name: str = "",
        device_id: str = "",
        num_channels: int = 0,
        sample_rate: int = 0,
        format: AudioMixerStreamDataFormatType = AudioMixerStreamDataFormatType
    .UNKNOWN,
        output_channel_array: Array[AudioMixerChannelType] = [],
        is_system_default: bool = False,
        is_current_device: bool = False) -> None
```

<a id="unreal.AudioOutputDeviceInfo.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Only] The name of the audio device

<a id="unreal.AudioOutputDeviceInfo.device_id"></a>

#### device_id

```python
@property
def device_id() -> str
```

(str):  [Read-Only] ID of the device.

<a id="unreal.AudioOutputDeviceInfo.num_channels"></a>

#### num_channels

```python
@property
def num_channels() -> int
```

(int32):  [Read-Only] The number of channels supported by the audio device

<a id="unreal.AudioOutputDeviceInfo.sample_rate"></a>

#### sample_rate

```python
@property
def sample_rate() -> int
```

(int32):  [Read-Only] The sample rate of the audio device

<a id="unreal.AudioOutputDeviceInfo.format"></a>

#### format

```python
@property
def format() -> AudioMixerStreamDataFormatType
```

(AudioMixerStreamDataFormatType):  [Read-Only] The data format of the audio stream

<a id="unreal.AudioOutputDeviceInfo.output_channel_array"></a>

#### output_channel_array

```python
@property
def output_channel_array() -> Array[AudioMixerChannelType]
```

(Array[AudioMixerChannelType]):  [Read-Only] The output channel array of the audio device

<a id="unreal.AudioOutputDeviceInfo.is_system_default"></a>

#### is_system_default

```python
@property
def is_system_default() -> bool
```

(bool):  [Read-Only] Whether or not this device is the system default

<a id="unreal.AudioOutputDeviceInfo.is_current_device"></a>

#### is_current_device

```python
@property
def is_current_device() -> bool
```

(bool):  [Read-Only] Whether or not this device is the device currently in use

<a id="unreal.SwapAudioOutputResult"></a>