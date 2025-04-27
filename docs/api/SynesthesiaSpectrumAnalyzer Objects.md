## SynesthesiaSpectrumAnalyzer Objects

```python
class SynesthesiaSpectrumAnalyzer(AudioAnalyzer)
```

USynesthesiaSpectrumAnalysisAnalyzer

USynesthesiaSpectrumAnalysisAnalyzer calculates the current amplitude of an
audio bus in real-time.

**C++ Source:**

- **Plugin**: AudioSynesthesia
- **Module**: AudioSynesthesia
- **File**: SynesthesiaSpectrumAnalysis.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_latest_spectrum_results`` (OnLatestSpectrumResults):  [Read-Write] Delegate to receive the latest per-channel Spectrum results. If bDownmixToMono setting is true, results will be in channel index 0.
- ``on_spectrum_results`` (OnSpectrumResults):  [Read-Write] Delegate to receive all Spectrum results, per-channel, since last delegate call. If bDownmixToMono setting is true, results will be in channel index 0.
- ``settings`` (SynesthesiaSpectrumAnalysisSettings):  [Read-Write] The settings for the SynesthesiaSpectrumAnalysis audio analyzer.

<a id="unreal.SynesthesiaSpectrumAnalyzer.settings"></a>

#### settings

```python
@property
def settings() -> SynesthesiaSpectrumAnalysisSettings
```

(SynesthesiaSpectrumAnalysisSettings):  [Read-Write] The settings for the SynesthesiaSpectrumAnalysis audio analyzer.

<a id="unreal.SynesthesiaSpectrumAnalyzer.settings"></a>

#### settings

```python
@settings.setter
def settings(value: SynesthesiaSpectrumAnalysisSettings) -> None
```

<a id="unreal.SynesthesiaSpectrumAnalyzer.on_spectrum_results"></a>

#### on_spectrum_results

```python
@property
def on_spectrum_results() -> OnSpectrumResults
```

(OnSpectrumResults):  [Read-Write] Delegate to receive all Spectrum results, per-channel, since last delegate call. If bDownmixToMono setting is true, results will be in channel index 0.

<a id="unreal.SynesthesiaSpectrumAnalyzer.on_spectrum_results"></a>

#### on_spectrum_results

```python
@on_spectrum_results.setter
def on_spectrum_results(value: OnSpectrumResults) -> None
```

<a id="unreal.SynesthesiaSpectrumAnalyzer.on_latest_spectrum_results"></a>

#### on_latest_spectrum_results

```python
@property
def on_latest_spectrum_results() -> OnLatestSpectrumResults
```

(OnLatestSpectrumResults):  [Read-Write] Delegate to receive the latest per-channel Spectrum results. If bDownmixToMono setting is true, results will be in channel index 0.

<a id="unreal.SynesthesiaSpectrumAnalyzer.on_latest_spectrum_results"></a>

#### on_latest_spectrum_results

```python
@on_latest_spectrum_results.setter
def on_latest_spectrum_results(value: OnLatestSpectrumResults) -> None
```

<a id="unreal.SynesthesiaSpectrumAnalyzer.get_num_center_frequencies"></a>

#### get_num_center_frequencies

```python
def get_num_center_frequencies() -> int
```

x.get_num_center_frequencies() -> int32
Get Num Center Frequencies

Returns:
    int32:

<a id="unreal.SynesthesiaSpectrumAnalyzer.get_center_frequencies"></a>

#### get_center_frequencies

```python
def get_center_frequencies(sample_rate: float) -> Array[float]
```

x.get_center_frequencies(sample_rate) -> Array[float]
Get Center Frequencies

Args:
    sample_rate (float): 

Returns:
    Array[float]: 

    out_center_frequencies (Array[float]):

<a id="unreal.CableActor"></a>