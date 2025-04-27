## SoundWaveSpectralData Objects

```python
class SoundWaveSpectralData(StructBase)
```

Sound Wave Spectral Data

**C++ Source:**

- **Module**: Engine
- **File**: SoundWave.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frequency_hz`` (float):  [Read-Write] The frequency (in Hz) of the spectrum value
- ``magnitude`` (float):  [Read-Write] The magnitude of the spectrum at this frequency
- ``normalized_magnitude`` (float):  [Read-Write] The normalized magnitude of the spectrum at this frequency

<a id="unreal.SoundWaveSpectralData.__init__"></a>

#### __init__

```python
def __init__(frequency_hz: float = 0.000000,
             magnitude: float = 0.000000,
             normalized_magnitude: float = 0.000000) -> None
```

<a id="unreal.SoundWaveSpectralData.frequency_hz"></a>

#### frequency_hz

```python
@property
def frequency_hz() -> float
```

(float):  [Read-Write] The frequency (in Hz) of the spectrum value

<a id="unreal.SoundWaveSpectralData.frequency_hz"></a>

#### frequency_hz

```python
@frequency_hz.setter
def frequency_hz(value: float) -> None
```

<a id="unreal.SoundWaveSpectralData.magnitude"></a>

#### magnitude

```python
@property
def magnitude() -> float
```

(float):  [Read-Write] The magnitude of the spectrum at this frequency

<a id="unreal.SoundWaveSpectralData.magnitude"></a>

#### magnitude

```python
@magnitude.setter
def magnitude(value: float) -> None
```

<a id="unreal.SoundWaveSpectralData.normalized_magnitude"></a>

#### normalized_magnitude

```python
@property
def normalized_magnitude() -> float
```

(float):  [Read-Write] The normalized magnitude of the spectrum at this frequency

<a id="unreal.SoundWaveSpectralData.normalized_magnitude"></a>

#### normalized_magnitude

```python
@normalized_magnitude.setter
def normalized_magnitude(value: float) -> None
```

<a id="unreal.SoundWaveSpectralDataPerSound"></a>