## RigUnit_ItemHarmonics Objects

```python
class RigUnit_ItemHarmonics(RigUnit_HighlevelBaseMutable)
```

Drives an array of items through a harmonics spectrum

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_BoneHarmonics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``rotation_order`` (EulerRotationOrder):  [Read-Write]
- ``targets`` (Array[RigUnit_Harmonics_TargetItem]):  [Read-Only] The items to drive.
- ``wave_amplitude`` (Vector):  [Read-Write] The amplitude in degrees per axis
- ``wave_ease`` (RigVMAnimEasingType):  [Read-Write]
- ``wave_frequency`` (Vector):  [Read-Write]
- ``wave_maximum`` (float):  [Read-Write]
- ``wave_minimum`` (float):  [Read-Write]
- ``wave_noise`` (Vector):  [Read-Write]
- ``wave_offset`` (Vector):  [Read-Write]
- ``wave_speed`` (Vector):  [Read-Write]

<a id="unreal.RigUnit_ItemHarmonics.__init__"></a>

#### __init__

```python
def __init__(
        execute_context: ControlRigExecuteContext = [],
        targets: Array[RigUnit_Harmonics_TargetItem] = [],
        wave_speed: Vector = [0.000000, 0.000000, 0.000000],
        wave_frequency: Vector = [0.000000, 0.000000, 0.000000],
        wave_amplitude: Vector = [0.000000, 0.000000, 0.000000],
        wave_offset: Vector = [0.000000, 0.000000, 0.000000],
        wave_noise: Vector = [0.000000, 0.000000, 0.000000],
        wave_ease: RigVMAnimEasingType = RigVMAnimEasingType.LINEAR,
        wave_minimum: float = 0.000000,
        wave_maximum: float = 0.000000,
        rotation_order: EulerRotationOrder = EulerRotationOrder.XYZ) -> None
```

<a id="unreal.RigUnit_ItemHarmonics.targets"></a>

#### targets

```python
@property
def targets() -> Array[RigUnit_Harmonics_TargetItem]
```

(Array[RigUnit_Harmonics_TargetItem]):  [Read-Only] The items to drive.

<a id="unreal.RigUnit_ItemHarmonics.wave_speed"></a>

#### wave_speed

```python
@property
def wave_speed() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_ItemHarmonics.wave_speed"></a>

#### wave_speed

```python
@wave_speed.setter
def wave_speed(value: Vector) -> None
```

<a id="unreal.RigUnit_ItemHarmonics.wave_frequency"></a>

#### wave_frequency

```python
@property
def wave_frequency() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_ItemHarmonics.wave_frequency"></a>

#### wave_frequency

```python
@wave_frequency.setter
def wave_frequency(value: Vector) -> None
```

<a id="unreal.RigUnit_ItemHarmonics.wave_amplitude"></a>

#### wave_amplitude

```python
@property
def wave_amplitude() -> Vector
```

(Vector):  [Read-Write] The amplitude in degrees per axis

<a id="unreal.RigUnit_ItemHarmonics.wave_amplitude"></a>

#### wave_amplitude

```python
@wave_amplitude.setter
def wave_amplitude(value: Vector) -> None
```

<a id="unreal.RigUnit_ItemHarmonics.wave_offset"></a>

#### wave_offset

```python
@property
def wave_offset() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_ItemHarmonics.wave_offset"></a>

#### wave_offset

```python
@wave_offset.setter
def wave_offset(value: Vector) -> None
```

<a id="unreal.RigUnit_ItemHarmonics.wave_noise"></a>

#### wave_noise

```python
@property
def wave_noise() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_ItemHarmonics.wave_noise"></a>

#### wave_noise

```python
@wave_noise.setter
def wave_noise(value: Vector) -> None
```

<a id="unreal.RigUnit_ItemHarmonics.wave_ease"></a>

#### wave_ease

```python
@property
def wave_ease() -> RigVMAnimEasingType
```

(RigVMAnimEasingType):  [Read-Write]

<a id="unreal.RigUnit_ItemHarmonics.wave_ease"></a>

#### wave_ease

```python
@wave_ease.setter
def wave_ease(value: RigVMAnimEasingType) -> None
```

<a id="unreal.RigUnit_ItemHarmonics.wave_minimum"></a>

#### wave_minimum

```python
@property
def wave_minimum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_ItemHarmonics.wave_minimum"></a>

#### wave_minimum

```python
@wave_minimum.setter
def wave_minimum(value: float) -> None
```

<a id="unreal.RigUnit_ItemHarmonics.wave_maximum"></a>

#### wave_maximum

```python
@property
def wave_maximum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_ItemHarmonics.wave_maximum"></a>

#### wave_maximum

```python
@wave_maximum.setter
def wave_maximum(value: float) -> None
```

<a id="unreal.RigUnit_ItemHarmonics.rotation_order"></a>

#### rotation_order

```python
@property
def rotation_order() -> EulerRotationOrder
```

(EulerRotationOrder):  [Read-Write]

<a id="unreal.RigUnit_ItemHarmonics.rotation_order"></a>

#### rotation_order

```python
@rotation_order.setter
def rotation_order(value: EulerRotationOrder) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Reach"></a>