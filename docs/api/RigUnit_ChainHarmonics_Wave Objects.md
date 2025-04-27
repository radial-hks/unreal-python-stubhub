## RigUnit_ChainHarmonics_Wave Objects

```python
class RigUnit_ChainHarmonics_Wave(StructBase)
```

Rig Unit Chain Harmonics Wave

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ChainHarmonics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write]
- ``wave_amplitude`` (Vector):  [Read-Write]
- ``wave_ease`` (RigVMAnimEasingType):  [Read-Write]
- ``wave_frequency`` (Vector):  [Read-Write]
- ``wave_maximum`` (float):  [Read-Write]
- ``wave_minimum`` (float):  [Read-Write]
- ``wave_noise`` (Vector):  [Read-Write]
- ``wave_offset`` (Vector):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Wave.__init__"></a>

#### __init__

```python
def __init__(
        enabled: bool = False,
        wave_frequency: Vector = [0.000000, 0.000000, 0.000000],
        wave_amplitude: Vector = [0.000000, 0.000000, 0.000000],
        wave_offset: Vector = [0.000000, 0.000000, 0.000000],
        wave_noise: Vector = [0.000000, 0.000000, 0.000000],
        wave_minimum: float = 0.000000,
        wave_maximum: float = 0.000000,
        wave_ease: RigVMAnimEasingType = RigVMAnimEasingType.LINEAR) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Wave.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Wave.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Wave.wave_frequency"></a>

#### wave_frequency

```python
@property
def wave_frequency() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Wave.wave_frequency"></a>

#### wave_frequency

```python
@wave_frequency.setter
def wave_frequency(value: Vector) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Wave.wave_amplitude"></a>

#### wave_amplitude

```python
@property
def wave_amplitude() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Wave.wave_amplitude"></a>

#### wave_amplitude

```python
@wave_amplitude.setter
def wave_amplitude(value: Vector) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Wave.wave_offset"></a>

#### wave_offset

```python
@property
def wave_offset() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Wave.wave_offset"></a>

#### wave_offset

```python
@wave_offset.setter
def wave_offset(value: Vector) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Wave.wave_noise"></a>

#### wave_noise

```python
@property
def wave_noise() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Wave.wave_noise"></a>

#### wave_noise

```python
@wave_noise.setter
def wave_noise(value: Vector) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Wave.wave_minimum"></a>

#### wave_minimum

```python
@property
def wave_minimum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Wave.wave_minimum"></a>

#### wave_minimum

```python
@wave_minimum.setter
def wave_minimum(value: float) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Wave.wave_maximum"></a>

#### wave_maximum

```python
@property
def wave_maximum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Wave.wave_maximum"></a>

#### wave_maximum

```python
@wave_maximum.setter
def wave_maximum(value: float) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Wave.wave_ease"></a>

#### wave_ease

```python
@property
def wave_ease() -> RigVMAnimEasingType
```

(RigVMAnimEasingType):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Wave.wave_ease"></a>

#### wave_ease

```python
@wave_ease.setter
def wave_ease(value: RigVMAnimEasingType) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Pendulum"></a>