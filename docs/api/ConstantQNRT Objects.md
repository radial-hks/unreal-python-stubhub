## ConstantQNRT Objects

```python
class ConstantQNRT(AudioSynesthesiaNRT)
```

UConstantQNRT

UConstantQNRT calculates the temporal evolution of constant q transform for a given
sound. ConstantQ is available for individual channels or the overall sound asset.

**C++ Source:**

- **Plugin**: AudioSynesthesia
- **Module**: AudioSynesthesia
- **File**: ConstantQNRT.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``duration_in_seconds`` (float):  [Read-Write] The duration of the analyzed audio in seconds.
- ``settings`` (ConstantQNRTSettings):  [Read-Write] The settings for the audio analyzer.
- ``sound`` (SoundWave):  [Read-Write] The USoundWave which is analyzed.

<a id="unreal.ConstantQNRT.settings"></a>

#### settings

```python
@property
def settings() -> ConstantQNRTSettings
```

(ConstantQNRTSettings):  [Read-Only] The settings for the audio analyzer.

<a id="unreal.ConstantQNRT.get_normalized_channel_constant_q_at_time"></a>

#### get_normalized_channel_constant_q_at_time

```python
def get_normalized_channel_constant_q_at_time(seconds: float,
                                              channel: int) -> Array[float]
```

x.get_normalized_channel_constant_q_at_time(seconds, channel) -> Array[float]
Get a specific channel cqt of the analyzed sound at a given time.

Args:
    seconds (float): 
    channel (int32): 

Returns:
    Array[float]: 

    out_constant_q (Array[float]):

<a id="unreal.ConstantQNRT.get_channel_constant_q_at_time"></a>

#### get_channel_constant_q_at_time

```python
def get_channel_constant_q_at_time(seconds: float,
                                   channel: int) -> Array[float]
```

x.get_channel_constant_q_at_time(seconds, channel) -> Array[float]
Get a specific channel cqt of the analyzed sound at a given time.

Args:
    seconds (float): 
    channel (int32): 

Returns:
    Array[float]: 

    out_constant_q (Array[float]):

<a id="unreal.LoudnessSettings"></a>