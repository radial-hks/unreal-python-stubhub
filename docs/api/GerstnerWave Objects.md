## GerstnerWave Objects

```python
class GerstnerWave(StructBase)
```

Raw wave parameters for one gerstner wave

**C++ Source:**

- **Plugin**: Water
- **Module**: Water
- **File**: GerstnerWaterWaves.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``amplitude`` (float):  [Read-Write]
- ``direction`` (Vector):  [Read-Write]
- ``steepness`` (float):  [Read-Write]
- ``wave_length`` (float):  [Read-Write]

<a id="unreal.GerstnerWave.__init__"></a>

#### __init__

```python
def __init__(wave_length: float = 0.000000,
             amplitude: float = 0.000000,
             steepness: float = 0.000000,
             direction: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.GerstnerWave.wave_length"></a>

#### wave_length

```python
@property
def wave_length() -> float
```

(float):  [Read-Write]

<a id="unreal.GerstnerWave.wave_length"></a>

#### wave_length

```python
@wave_length.setter
def wave_length(value: float) -> None
```

<a id="unreal.GerstnerWave.amplitude"></a>

#### amplitude

```python
@property
def amplitude() -> float
```

(float):  [Read-Write]

<a id="unreal.GerstnerWave.amplitude"></a>

#### amplitude

```python
@amplitude.setter
def amplitude(value: float) -> None
```

<a id="unreal.GerstnerWave.steepness"></a>

#### steepness

```python
@property
def steepness() -> float
```

(float):  [Read-Write]

<a id="unreal.GerstnerWave.steepness"></a>

#### steepness

```python
@steepness.setter
def steepness(value: float) -> None
```

<a id="unreal.GerstnerWave.direction"></a>

#### direction

```python
@property
def direction() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.GerstnerWave.direction"></a>

#### direction

```python
@direction.setter
def direction(value: Vector) -> None
```

<a id="unreal.GerstnerWaveOctave"></a>