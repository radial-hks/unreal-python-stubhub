## SoundSubmixSpectralAnalysisBandSettings Objects

```python
class SoundSubmixSpectralAnalysisBandSettings(StructBase)
```

Sound Submix Spectral Analysis Band Settings

**C++ Source:**

- **Module**: Engine
- **File**: SoundSubmixSend.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attack_time_msec`` (int32):  [Read-Write] The attack time for the FFT band interpolation for delegate callback
- ``band_frequency`` (float):  [Read-Write] The frequency band for the magnitude to analyze
- ``q_factor`` (float):  [Read-Write] The ratio of the bandwidth divided by the center frequency. Only used when the spectral analysis type is set to Constant Q.
- ``release_time_msec`` (int32):  [Read-Write] The release time for the FFT band interpolation for delegate callback

<a id="unreal.SoundSubmixSpectralAnalysisBandSettings.__init__"></a>

#### __init__

```python
def __init__(band_frequency: float = 0.000000,
             attack_time_msec: int = 0,
             release_time_msec: int = 0,
             q_factor: float = 0.000000) -> None
```

<a id="unreal.SoundSubmixSpectralAnalysisBandSettings.band_frequency"></a>

#### band_frequency

```python
@property
def band_frequency() -> float
```

(float):  [Read-Write] The frequency band for the magnitude to analyze

<a id="unreal.SoundSubmixSpectralAnalysisBandSettings.band_frequency"></a>

#### band_frequency

```python
@band_frequency.setter
def band_frequency(value: float) -> None
```

<a id="unreal.SoundSubmixSpectralAnalysisBandSettings.attack_time_msec"></a>

#### attack_time_msec

```python
@property
def attack_time_msec() -> int
```

(int32):  [Read-Write] The attack time for the FFT band interpolation for delegate callback

<a id="unreal.SoundSubmixSpectralAnalysisBandSettings.attack_time_msec"></a>

#### attack_time_msec

```python
@attack_time_msec.setter
def attack_time_msec(value: int) -> None
```

<a id="unreal.SoundSubmixSpectralAnalysisBandSettings.release_time_msec"></a>

#### release_time_msec

```python
@property
def release_time_msec() -> int
```

(int32):  [Read-Write] The release time for the FFT band interpolation for delegate callback

<a id="unreal.SoundSubmixSpectralAnalysisBandSettings.release_time_msec"></a>

#### release_time_msec

```python
@release_time_msec.setter
def release_time_msec(value: int) -> None
```

<a id="unreal.SoundSubmixSpectralAnalysisBandSettings.q_factor"></a>

#### q_factor

```python
@property
def q_factor() -> float
```

(float):  [Read-Write] The ratio of the bandwidth divided by the center frequency. Only used when the spectral analysis type is set to Constant Q.

<a id="unreal.SoundSubmixSpectralAnalysisBandSettings.q_factor"></a>

#### q_factor

```python
@q_factor.setter
def q_factor(value: float) -> None
```

<a id="unreal.StaticMaterial"></a>