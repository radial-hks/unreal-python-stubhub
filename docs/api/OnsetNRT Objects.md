## OnsetNRT Objects

```python
class OnsetNRT(AudioSynesthesiaNRT)
```

UOnsetNRT

UOnsetNRT calculates the temporal evolution of constant q transform for a given
sound. Onset is available for individual channels or the overall sound asset.

**C++ Source:**

- **Plugin**: AudioSynesthesia
- **Module**: AudioSynesthesia
- **File**: OnsetNRT.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``duration_in_seconds`` (float):  [Read-Write] The duration of the analyzed audio in seconds.
- ``settings`` (OnsetNRTSettings):  [Read-Write] The settings for the audio analyzer.
- ``sound`` (SoundWave):  [Read-Write] The USoundWave which is analyzed.

<a id="unreal.OnsetNRT.settings"></a>

#### settings

```python
@property
def settings() -> OnsetNRTSettings
```

(OnsetNRTSettings):  [Read-Only] The settings for the audio analyzer.

<a id="unreal.OnsetNRT.get_normalized_channel_onsets_between_times"></a>

#### get_normalized_channel_onsets_between_times

```python
def get_normalized_channel_onsets_between_times(
        start_seconds: float, end_seconds: float,
        channel: int) -> Tuple[Array[float], Array[float]]
```

x.get_normalized_channel_onsets_between_times(start_seconds, end_seconds, channel) -> (out_onset_timestamps=Array[float], out_onset_strengths=Array[float])
Get a specific channel cqt of the analyzed sound at a given time.

Args:
    start_seconds (float): 
    end_seconds (float): 
    channel (int32): 

Returns:
    tuple: 

    out_onset_timestamps (Array[float]): 

    out_onset_strengths (Array[float]):

<a id="unreal.OnsetNRT.get_channel_onsets_between_times"></a>

#### get_channel_onsets_between_times

```python
def get_channel_onsets_between_times(
        start_seconds: float, end_seconds: float,
        channel: int) -> Tuple[Array[float], Array[float]]
```

x.get_channel_onsets_between_times(start_seconds, end_seconds, channel) -> (out_onset_timestamps=Array[float], out_onset_strengths=Array[float])
Returns onsets which occured between start and end timestamps.

Args:
    start_seconds (float): 
    end_seconds (float): 
    channel (int32): 

Returns:
    tuple: 

    out_onset_timestamps (Array[float]): 

    out_onset_strengths (Array[float]):

<a id="unreal.SynesthesiaSpectrumAnalysisSettings"></a>