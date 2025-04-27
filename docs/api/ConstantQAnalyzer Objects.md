## ConstantQAnalyzer Objects

```python
class ConstantQAnalyzer(AudioAnalyzer)
```

UConstantQAnalyzer

UConstantQAnalyzer calculates the temporal evolution of constant q transform for a given
audio bus in real-time. ConstantQ is available for individual channels or the overall audio bus.

**C++ Source:**

- **Plugin**: AudioSynesthesia
- **Module**: AudioSynesthesia
- **File**: ConstantQ.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_constant_q_results`` (OnConstantQResults):  [Read-Write] Delegate to receive all Spectrum results, per-channel, since last delegate call. If bDownmixToMono setting is true, results will be in channel index 0.
- ``on_latest_constant_q_results`` (OnLatestConstantQResults):  [Read-Write] Delegate to receive the latest per-channel Spectrum results. If bDownmixToMono setting is true, results will be in channel index 0.
- ``settings`` (ConstantQSettings):  [Read-Write] The settings for the audio analyzer.

<a id="unreal.ConstantQAnalyzer.settings"></a>

#### settings

```python
@property
def settings() -> ConstantQSettings
```

(ConstantQSettings):  [Read-Write] The settings for the audio analyzer.

<a id="unreal.ConstantQAnalyzer.settings"></a>

#### settings

```python
@settings.setter
def settings(value: ConstantQSettings) -> None
```

<a id="unreal.ConstantQAnalyzer.on_constant_q_results"></a>

#### on_constant_q_results

```python
@property
def on_constant_q_results() -> OnConstantQResults
```

(OnConstantQResults):  [Read-Write] Delegate to receive all Spectrum results, per-channel, since last delegate call. If bDownmixToMono setting is true, results will be in channel index 0.

<a id="unreal.ConstantQAnalyzer.on_constant_q_results"></a>

#### on_constant_q_results

```python
@on_constant_q_results.setter
def on_constant_q_results(value: OnConstantQResults) -> None
```

<a id="unreal.ConstantQAnalyzer.on_latest_constant_q_results"></a>

#### on_latest_constant_q_results

```python
@property
def on_latest_constant_q_results() -> OnLatestConstantQResults
```

(OnLatestConstantQResults):  [Read-Write] Delegate to receive the latest per-channel Spectrum results. If bDownmixToMono setting is true, results will be in channel index 0.

<a id="unreal.ConstantQAnalyzer.on_latest_constant_q_results"></a>

#### on_latest_constant_q_results

```python
@on_latest_constant_q_results.setter
def on_latest_constant_q_results(value: OnLatestConstantQResults) -> None
```

<a id="unreal.ConstantQAnalyzer.get_num_center_frequencies"></a>

#### get_num_center_frequencies

```python
def get_num_center_frequencies() -> int
```

x.get_num_center_frequencies() -> int32
Get Num Center Frequencies

Returns:
    int32:

<a id="unreal.ConstantQAnalyzer.get_center_frequencies"></a>

#### get_center_frequencies

```python
def get_center_frequencies() -> Array[float]
```

x.get_center_frequencies() -> Array[float]
Get Center Frequencies

Returns:
    Array[float]: 

    out_center_frequencies (Array[float]):

<a id="unreal.ConstantQNRTSettings"></a>