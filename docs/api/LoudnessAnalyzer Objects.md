## LoudnessAnalyzer Objects

```python
class LoudnessAnalyzer(AudioAnalyzer)
```

ULoudnessAnalyzer

ULoudnessAnalyzer calculates the temporal evolution of perceptual loudness for a given
audio bus in real-time. Loudness is available for individual channels or the overall audio bus. Normalized
loudness values convert the range to 0.0 to 1.0 where 0.0 is the noise floor and 1.0 is the
maximum loudness of the particular sound.

**C++ Source:**

- **Plugin**: AudioSynesthesia
- **Module**: AudioSynesthesia
- **File**: Loudness.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_latest_overall_loudness_results`` (OnLatestOverallLoudnessResults):  [Read-Write] Delegate to receive the latest overall loudness results.
- ``on_latest_per_channel_loudness_results`` (OnLatestPerChannelLoudnessResults):  [Read-Write] Delegate to receive the latest per-channel loudness results.
- ``on_overall_loudness_results`` (OnOverallLoudnessResults):  [Read-Write] Delegate to receive all overall loudness results since last delegate call.
- ``on_per_channel_loudness_results`` (OnPerChannelLoudnessResults):  [Read-Write] Delegate to receive all loudness results, per-channel, since last delegate call.
- ``settings`` (LoudnessSettings):  [Read-Write] The settings for the audio analyzer.

<a id="unreal.LoudnessAnalyzer.settings"></a>

#### settings

```python
@property
def settings() -> LoudnessSettings
```

(LoudnessSettings):  [Read-Write] The settings for the audio analyzer.

<a id="unreal.LoudnessAnalyzer.settings"></a>

#### settings

```python
@settings.setter
def settings(value: LoudnessSettings) -> None
```

<a id="unreal.LoudnessAnalyzer.on_overall_loudness_results"></a>

#### on_overall_loudness_results

```python
@property
def on_overall_loudness_results() -> OnOverallLoudnessResults
```

(OnOverallLoudnessResults):  [Read-Write] Delegate to receive all overall loudness results since last delegate call.

<a id="unreal.LoudnessAnalyzer.on_overall_loudness_results"></a>

#### on_overall_loudness_results

```python
@on_overall_loudness_results.setter
def on_overall_loudness_results(value: OnOverallLoudnessResults) -> None
```

<a id="unreal.LoudnessAnalyzer.on_per_channel_loudness_results"></a>

#### on_per_channel_loudness_results

```python
@property
def on_per_channel_loudness_results() -> OnPerChannelLoudnessResults
```

(OnPerChannelLoudnessResults):  [Read-Write] Delegate to receive all loudness results, per-channel, since last delegate call.

<a id="unreal.LoudnessAnalyzer.on_per_channel_loudness_results"></a>

#### on_per_channel_loudness_results

```python
@on_per_channel_loudness_results.setter
def on_per_channel_loudness_results(
        value: OnPerChannelLoudnessResults) -> None
```

<a id="unreal.LoudnessAnalyzer.on_latest_overall_loudness_results"></a>

#### on_latest_overall_loudness_results

```python
@property
def on_latest_overall_loudness_results() -> OnLatestOverallLoudnessResults
```

(OnLatestOverallLoudnessResults):  [Read-Write] Delegate to receive the latest overall loudness results.

<a id="unreal.LoudnessAnalyzer.on_latest_overall_loudness_results"></a>

#### on_latest_overall_loudness_results

```python
@on_latest_overall_loudness_results.setter
def on_latest_overall_loudness_results(
        value: OnLatestOverallLoudnessResults) -> None
```

<a id="unreal.LoudnessAnalyzer.on_latest_per_channel_loudness_results"></a>

#### on_latest_per_channel_loudness_results

```python
@property
def on_latest_per_channel_loudness_results(
) -> OnLatestPerChannelLoudnessResults
```

(OnLatestPerChannelLoudnessResults):  [Read-Write] Delegate to receive the latest per-channel loudness results.

<a id="unreal.LoudnessAnalyzer.on_latest_per_channel_loudness_results"></a>

#### on_latest_per_channel_loudness_results

```python
@on_latest_per_channel_loudness_results.setter
def on_latest_per_channel_loudness_results(
        value: OnLatestPerChannelLoudnessResults) -> None
```

<a id="unreal.LoudnessNRTSettings"></a>