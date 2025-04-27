## GerstnerWaveOctave Objects

```python
class GerstnerWaveOctave(StructBase)
```

Gerstner Wave Octave

**C++ Source:**

- **Plugin**: Water
- **Module**: Water
- **File**: GerstnerWaterWaves.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``amplitude_scale`` (float):  [Read-Write]
- ``main_direction`` (float):  [Read-Write]
- ``num_waves`` (int32):  [Read-Write]
- ``spread_angle`` (float):  [Read-Write]
- ``uniform_spread`` (bool):  [Read-Write]

<a id="unreal.GerstnerWaveOctave.__init__"></a>

#### __init__

```python
def __init__(num_waves: int = 0,
             amplitude_scale: float = 0.000000,
             main_direction: float = 0.000000,
             spread_angle: float = 0.000000,
             uniform_spread: bool = False) -> None
```

<a id="unreal.GerstnerWaveOctave.num_waves"></a>

#### num_waves

```python
@property
def num_waves() -> int
```

(int32):  [Read-Write]

<a id="unreal.GerstnerWaveOctave.num_waves"></a>

#### num_waves

```python
@num_waves.setter
def num_waves(value: int) -> None
```

<a id="unreal.GerstnerWaveOctave.amplitude_scale"></a>

#### amplitude_scale

```python
@property
def amplitude_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.GerstnerWaveOctave.amplitude_scale"></a>

#### amplitude_scale

```python
@amplitude_scale.setter
def amplitude_scale(value: float) -> None
```

<a id="unreal.GerstnerWaveOctave.main_direction"></a>

#### main_direction

```python
@property
def main_direction() -> float
```

(float):  [Read-Write]

<a id="unreal.GerstnerWaveOctave.main_direction"></a>

#### main_direction

```python
@main_direction.setter
def main_direction(value: float) -> None
```

<a id="unreal.GerstnerWaveOctave.spread_angle"></a>

#### spread_angle

```python
@property
def spread_angle() -> float
```

(float):  [Read-Write]

<a id="unreal.GerstnerWaveOctave.spread_angle"></a>

#### spread_angle

```python
@spread_angle.setter
def spread_angle(value: float) -> None
```

<a id="unreal.GerstnerWaveOctave.uniform_spread"></a>

#### uniform_spread

```python
@property
def uniform_spread() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GerstnerWaveOctave.uniform_spread"></a>

#### uniform_spread

```python
@uniform_spread.setter
def uniform_spread(value: bool) -> None
```

<a id="unreal.UnderwaterPostProcessSettings"></a>