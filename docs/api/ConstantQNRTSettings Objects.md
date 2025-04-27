## ConstantQNRTSettings Objects

```python
class ConstantQNRTSettings(AudioSynesthesiaNRTSettings)
```

UConstantQNRTSettings

Settings for a UConstantQNRT analyzer.

**C++ Source:**

- **Plugin**: AudioSynesthesia
- **Module**: AudioSynesthesia
- **File**: ConstantQNRT.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``analysis_period`` (float):  [Read-Write] Number of seconds between cqt measurements
- ``band_width_stretch`` (float):  [Read-Write] Stretching factor to control overlap of adjacent bands.
- ``cqt_normalization`` (ConstantQNormalizationEnum):  [Read-Write] Normalization scheme used to generate band windows.
- ``downmix_to_mono`` (bool):  [Read-Write] If true, multichannel audio is downmixed to mono with equal amplitude scaling. If false, each channel gets it's own CQT result.
- ``fft_size`` (ConstantQFFTSizeEnum):  [Read-Write] Size of FFT.
- ``noise_floor_db`` (float):  [Read-Write] Noise floor to use when normalizing CQT
- ``num_bands`` (int32):  [Read-Write] Total number of resulting constant Q bands.
- ``num_bands_per_octave`` (float):  [Read-Write] Number of bands within an octave.
- ``spectrum_type`` (AudioSpectrumType):  [Read-Write] Type of spectrum to use.
- ``starting_frequency`` (float):  [Read-Write] Starting frequency for first bin of CQT
- ``window_type`` (FFTWindowType):  [Read-Write] Type of window to be applied to input audio

<a id="unreal.ConstantQNRTSettings.starting_frequency"></a>

#### starting_frequency

```python
@property
def starting_frequency() -> float
```

(float):  [Read-Only] Starting frequency for first bin of CQT

<a id="unreal.ConstantQNRTSettings.num_bands"></a>

#### num_bands

```python
@property
def num_bands() -> int
```

(int32):  [Read-Only] Total number of resulting constant Q bands.

<a id="unreal.ConstantQNRTSettings.num_bands_per_octave"></a>

#### num_bands_per_octave

```python
@property
def num_bands_per_octave() -> float
```

(float):  [Read-Only] Number of bands within an octave.

<a id="unreal.ConstantQNRTSettings.analysis_period"></a>

#### analysis_period

```python
@property
def analysis_period() -> float
```

(float):  [Read-Only] Number of seconds between cqt measurements

<a id="unreal.ConstantQNRTSettings.downmix_to_mono"></a>

#### downmix_to_mono

```python
@property
def downmix_to_mono() -> bool
```

(bool):  [Read-Only] If true, multichannel audio is downmixed to mono with equal amplitude scaling. If false, each channel gets it's own CQT result.

<a id="unreal.ConstantQNRTSettings.fft_size"></a>

#### fft_size

```python
@property
def fft_size() -> ConstantQFFTSizeEnum
```

(ConstantQFFTSizeEnum):  [Read-Only] Size of FFT.

<a id="unreal.ConstantQNRTSettings.window_type"></a>

#### window_type

```python
@property
def window_type() -> FFTWindowType
```

(FFTWindowType):  [Read-Only] Type of window to be applied to input audio

<a id="unreal.ConstantQNRTSettings.spectrum_type"></a>

#### spectrum_type

```python
@property
def spectrum_type() -> AudioSpectrumType
```

(AudioSpectrumType):  [Read-Only] Type of spectrum to use.

<a id="unreal.ConstantQNRTSettings.band_width_stretch"></a>

#### band_width_stretch

```python
@property
def band_width_stretch() -> float
```

(float):  [Read-Only] Stretching factor to control overlap of adjacent bands.

<a id="unreal.ConstantQNRTSettings.cqt_normalization"></a>

#### cqt_normalization

```python
@property
def cqt_normalization() -> ConstantQNormalizationEnum
```

(ConstantQNormalizationEnum):  [Read-Only] Normalization scheme used to generate band windows.

<a id="unreal.ConstantQNRTSettings.noise_floor_db"></a>

#### noise_floor_db

```python
@property
def noise_floor_db() -> float
```

(float):  [Read-Only] Noise floor to use when normalizing CQT

<a id="unreal.ConstantQNRT"></a>