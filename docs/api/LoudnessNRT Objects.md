## LoudnessNRT Objects

```python
class LoudnessNRT(AudioSynesthesiaNRT)
```

ULoudnessNRT

ULoudnessNRT calculates the temporal evolution of perceptual loudness for a given
sound. Loudness is available for individual channels or the overall sound asset. Normalized
loudness values convert the range to 0.0 to 1.0 where 0.0 is the noise floor and 1.0 is the
maximum loudness of the particular sound.

**C++ Source:**

- **Plugin**: AudioSynesthesia
- **Module**: AudioSynesthesia
- **File**: LoudnessNRT.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``duration_in_seconds`` (float):  [Read-Write] The duration of the analyzed audio in seconds.
- ``settings`` (LoudnessNRTSettings):  [Read-Write] The settings for the audio analyzer.
- ``sound`` (SoundWave):  [Read-Write] The USoundWave which is analyzed.

<a id="unreal.LoudnessNRT.settings"></a>

#### settings

```python
@property
def settings() -> LoudnessNRTSettings
```

(LoudnessNRTSettings):  [Read-Only] The settings for the audio analyzer.

<a id="unreal.LoudnessNRT.get_normalized_loudness_at_time"></a>

#### get_normalized_loudness_at_time

```python
def get_normalized_loudness_at_time(seconds: float) -> float
```

x.get_normalized_loudness_at_time(seconds) -> float
Get the normalized overall loudness of the analyzed sound at a given time. Normalized loudness
is always between 0.0 to 1.0. 0.0 refers to the noise floor while 1.0 refers to the maximum
loudness in the sound.

Args:
    seconds (float): 

Returns:
    float: 

    out_loudness (float):

<a id="unreal.LoudnessNRT.get_normalized_channel_loudness_at_time"></a>

#### get_normalized_channel_loudness_at_time

```python
def get_normalized_channel_loudness_at_time(seconds: float,
                                            channel: int) -> float
```

x.get_normalized_channel_loudness_at_time(seconds, channel) -> float
Get a specific channel normalized loudness of the analyzed sound at a given time. Normalized
loudness is always between 0.0 to 1.0. 0.0 refers to the noise floor while 1.0 refers to the
maximum loudness in the sound.

Args:
    seconds (float): 
    channel (int32): 

Returns:
    float: 

    out_loudness (float):

<a id="unreal.LoudnessNRT.get_loudness_at_time"></a>

#### get_loudness_at_time

```python
def get_loudness_at_time(seconds: float) -> float
```

x.get_loudness_at_time(seconds) -> float
Get the overall loudness of the analyzed sound at a given time.

Args:
    seconds (float): 

Returns:
    float: 

    out_loudness (float):

<a id="unreal.LoudnessNRT.get_channel_loudness_at_time"></a>

#### get_channel_loudness_at_time

```python
def get_channel_loudness_at_time(seconds: float, channel: int) -> float
```

x.get_channel_loudness_at_time(seconds, channel) -> float
Get a specific channel loudness of the analyzed sound at a given time.

Args:
    seconds (float): 
    channel (int32): 

Returns:
    float: 

    out_loudness (float):

<a id="unreal.MeterSettings"></a>