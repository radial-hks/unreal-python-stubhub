## AudioVolumeSubmixSendSettings Objects

```python
class AudioVolumeSubmixSendSettings(StructBase)
```

Struct to determine dynamic submix send data for use with audio volumes.

**C++ Source:**

- **Module**: Engine
- **File**: AudioVolume.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``listener_location_state`` (AudioVolumeLocationState):  [Read-Write] The state the listener needs to be in, relative to the audio volume, for this submix send list to be used for a given sound
- ``submix_sends`` (Array[SoundSubmixSendInfo]):  [Read-Write] Submix send array for sounds that are in the ListenerLocationState at the same time as the listener

<a id="unreal.AudioVolumeSubmixSendSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        listener_location_state:
    AudioVolumeLocationState = AudioVolumeLocationState.INSIDE_THE_VOLUME,
        submix_sends: Array[SoundSubmixSendInfo] = []) -> None
```

<a id="unreal.AudioVolumeSubmixSendSettings.listener_location_state"></a>

#### listener\_location\_state

```python
@property
def listener_location_state() -> AudioVolumeLocationState
```

(AudioVolumeLocationState):  [Read-Write] The state the listener needs to be in, relative to the audio volume, for this submix send list to be used for a given sound

<a id="unreal.AudioVolumeSubmixSendSettings.listener_location_state"></a>

#### listener\_location\_state

```python
@listener_location_state.setter
def listener_location_state(value: AudioVolumeLocationState) -> None
```

<a id="unreal.AudioVolumeSubmixSendSettings.submix_sends"></a>

#### submix\_sends

```python
@property
def submix_sends() -> Array[SoundSubmixSendInfo]
```

(Array[SoundSubmixSendInfo]):  [Read-Write] Submix send array for sounds that are in the ListenerLocationState at the same time as the listener

<a id="unreal.AudioVolumeSubmixSendSettings.submix_sends"></a>

#### submix\_sends

```python
@submix_sends.setter
def submix_sends(value: Array[SoundSubmixSendInfo]) -> None
```

<a id="unreal.SoundSubmixSendInfo"></a>