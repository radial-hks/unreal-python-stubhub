## SoundWaveSpectralDataPerSound Objects

```python
class SoundWaveSpectralDataPerSound(StructBase)
```

Sound Wave Spectral Data Per Sound

**C++ Source:**

- **Module**: Engine
- **File**: SoundWave.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``playback_time`` (float):  [Read-Write] The current playback time of this sound wave
- ``sound_wave`` (SoundWave):  [Read-Write] The sound wave this spectral data is associated with
- ``spectral_data`` (Array[SoundWaveSpectralData]):  [Read-Write] The array of current spectral data for this sound wave

<a id="unreal.SoundWaveSpectralDataPerSound.__init__"></a>

#### \_\_init\_\_

```python
def __init__(spectral_data: Array[SoundWaveSpectralData] = [],
             playback_time: float = 0.000000,
             sound_wave: SoundWave = None) -> None
```

<a id="unreal.SoundWaveSpectralDataPerSound.spectral_data"></a>

#### spectral\_data

```python
@property
def spectral_data() -> Array[SoundWaveSpectralData]
```

(Array[SoundWaveSpectralData]):  [Read-Write] The array of current spectral data for this sound wave

<a id="unreal.SoundWaveSpectralDataPerSound.spectral_data"></a>

#### spectral\_data

```python
@spectral_data.setter
def spectral_data(value: Array[SoundWaveSpectralData]) -> None
```

<a id="unreal.SoundWaveSpectralDataPerSound.playback_time"></a>

#### playback\_time

```python
@property
def playback_time() -> float
```

(float):  [Read-Write] The current playback time of this sound wave

<a id="unreal.SoundWaveSpectralDataPerSound.playback_time"></a>

#### playback\_time

```python
@playback_time.setter
def playback_time(value: float) -> None
```

<a id="unreal.SoundWaveSpectralDataPerSound.sound_wave"></a>

#### sound\_wave

```python
@property
def sound_wave() -> SoundWave
```

(SoundWave):  [Read-Write] The sound wave this spectral data is associated with

<a id="unreal.SoundWaveSpectralDataPerSound.sound_wave"></a>

#### sound\_wave

```python
@sound_wave.setter
def sound_wave(value: SoundWave) -> None
```

<a id="unreal.SoundWaveEnvelopeDataPerSound"></a>