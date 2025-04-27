## SynesthesiaSpectrumAnalysisSettings Objects

```python
class SynesthesiaSpectrumAnalysisSettings(AudioSynesthesiaSettings)
```

USynesthesiaSpectrumAnalysisSettings

Settings for a USynesthesiaSpectrumAnalysisAnalyzer.

**C++ Source:**

- **Plugin**: AudioSynesthesia
- **Module**: AudioSynesthesia
- **File**: SynesthesiaSpectrumAnalysis.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``analysis_period`` (float):  [Read-Write] Number of seconds between SynesthesiaSpectrumAnalysis measurements
- ``downmix_to_mono`` (bool):  [Read-Write] If true, multichannel audio is downmixed to mono with equal amplitude scaling. If false, each channel gets its own FFT result.
- ``fft_size`` (FFTSize):  [Read-Write] Size of FFT.
- ``spectrum_type`` (AudioSpectrumType):  [Read-Write] Type of spectrum to use.
- ``window_type`` (FFTWindowType):  [Read-Write] Type of window to use.

<a id="unreal.SynesthesiaSpectrumAnalysisSettings.analysis_period"></a>

#### analysis_period

```python
@property
def analysis_period() -> float
```

(float):  [Read-Only] Number of seconds between SynesthesiaSpectrumAnalysis measurements

<a id="unreal.SynesthesiaSpectrumAnalysisSettings.fft_size"></a>

#### fft_size

```python
@property
def fft_size() -> FFTSize
```

(FFTSize):  [Read-Only] Size of FFT.

<a id="unreal.SynesthesiaSpectrumAnalysisSettings.spectrum_type"></a>

#### spectrum_type

```python
@property
def spectrum_type() -> AudioSpectrumType
```

(AudioSpectrumType):  [Read-Only] Type of spectrum to use.

<a id="unreal.SynesthesiaSpectrumAnalysisSettings.window_type"></a>

#### window_type

```python
@property
def window_type() -> FFTWindowType
```

(FFTWindowType):  [Read-Only] Type of window to use.

<a id="unreal.SynesthesiaSpectrumAnalysisSettings.downmix_to_mono"></a>

#### downmix_to_mono

```python
@property
def downmix_to_mono() -> bool
```

(bool):  [Read-Only] If true, multichannel audio is downmixed to mono with equal amplitude scaling. If false, each channel gets its own FFT result.

<a id="unreal.SynesthesiaSpectrumAnalyzer"></a>