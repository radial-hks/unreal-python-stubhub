## PerlinNoiseShaker Objects

```python
class PerlinNoiseShaker(StructBase)
```

A perlin noise shaker for a single number.

**C++ Source:**

- **Plugin**: EngineCameras
- **Module**: EngineCameras
- **File**: PerlinNoiseCameraShakePattern.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``amplitude`` (float):  [Read-Write] Amplitude of the perlin noise.
- ``frequency`` (float):  [Read-Write] Frequency of the sinusoidal oscillation.

<a id="unreal.PerlinNoiseShaker.__init__"></a>

#### __init__

```python
def __init__(amplitude: float = 0.000000, frequency: float = 0.000000) -> None
```

<a id="unreal.PerlinNoiseShaker.amplitude"></a>

#### amplitude

```python
@property
def amplitude() -> float
```

(float):  [Read-Write] Amplitude of the perlin noise.

<a id="unreal.PerlinNoiseShaker.amplitude"></a>

#### amplitude

```python
@amplitude.setter
def amplitude(value: float) -> None
```

<a id="unreal.PerlinNoiseShaker.frequency"></a>

#### frequency

```python
@property
def frequency() -> float
```

(float):  [Read-Write] Frequency of the sinusoidal oscillation.

<a id="unreal.PerlinNoiseShaker.frequency"></a>

#### frequency

```python
@frequency.setter
def frequency(value: float) -> None
```

<a id="unreal.WaveOscillator"></a>