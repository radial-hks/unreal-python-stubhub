## RigUnit\_BoneHarmonics Objects

```python
class RigUnit_BoneHarmonics(RigUnit_HighlevelBaseMutable)
```

Performs point based simulation

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_BoneHarmonics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bones`` (Array[RigUnit_BoneHarmonics_BoneTarget]):  [Read-Only] The bones to drive.
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``propagate_to_children`` (bool):  [Read-Only] If set to true all of the global transforms of the children
  of this bone will be recalculated based on their local transforms.
  Note: This is computationally more expensive than turning it off.
- ``rotation_order`` (EulerRotationOrder):  [Read-Write]
- ``wave_amplitude`` (Vector):  [Read-Write] The amplitude in degrees per axis
- ``wave_ease`` (RigVMAnimEasingType):  [Read-Write]
- ``wave_frequency`` (Vector):  [Read-Write]
- ``wave_maximum`` (float):  [Read-Write]
- ``wave_minimum`` (float):  [Read-Write]
- ``wave_noise`` (Vector):  [Read-Write]
- ``wave_offset`` (Vector):  [Read-Write]
- ``wave_speed`` (Vector):  [Read-Write]

<a id="unreal.RigUnit_BoneHarmonics.__init__"></a>

#### \_\_init\_\_

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             bones: Array[RigUnit_BoneHarmonics_BoneTarget] = [],
             wave_speed: Vector = [0.000000, 0.000000, 0.000000],
             wave_frequency: Vector = [0.000000, 0.000000, 0.000000],
             wave_amplitude: Vector = [0.000000, 0.000000, 0.000000],
             wave_offset: Vector = [0.000000, 0.000000, 0.000000],
             wave_noise: Vector = [0.000000, 0.000000, 0.000000],
             wave_ease: RigVMAnimEasingType = RigVMAnimEasingType.LINEAR,
             wave_minimum: float = 0.000000,
             wave_maximum: float = 0.000000,
             rotation_order: EulerRotationOrder = EulerRotationOrder.XYZ,
             propagate_to_children: bool = False) -> None
```

<a id="unreal.RigUnit_BoneHarmonics.bones"></a>

#### bones

```python
@property
def bones() -> Array[RigUnit_BoneHarmonics_BoneTarget]
```

(Array[RigUnit_BoneHarmonics_BoneTarget]):  [Read-Only] The bones to drive.

<a id="unreal.RigUnit_BoneHarmonics.wave_speed"></a>

#### wave\_speed

```python
@property
def wave_speed() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_BoneHarmonics.wave_speed"></a>

#### wave\_speed

```python
@wave_speed.setter
def wave_speed(value: Vector) -> None
```

<a id="unreal.RigUnit_BoneHarmonics.wave_frequency"></a>

#### wave\_frequency

```python
@property
def wave_frequency() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_BoneHarmonics.wave_frequency"></a>

#### wave\_frequency

```python
@wave_frequency.setter
def wave_frequency(value: Vector) -> None
```

<a id="unreal.RigUnit_BoneHarmonics.wave_amplitude"></a>

#### wave\_amplitude

```python
@property
def wave_amplitude() -> Vector
```

(Vector):  [Read-Write] The amplitude in degrees per axis

<a id="unreal.RigUnit_BoneHarmonics.wave_amplitude"></a>

#### wave\_amplitude

```python
@wave_amplitude.setter
def wave_amplitude(value: Vector) -> None
```

<a id="unreal.RigUnit_BoneHarmonics.wave_offset"></a>

#### wave\_offset

```python
@property
def wave_offset() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_BoneHarmonics.wave_offset"></a>

#### wave\_offset

```python
@wave_offset.setter
def wave_offset(value: Vector) -> None
```

<a id="unreal.RigUnit_BoneHarmonics.wave_noise"></a>

#### wave\_noise

```python
@property
def wave_noise() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_BoneHarmonics.wave_noise"></a>

#### wave\_noise

```python
@wave_noise.setter
def wave_noise(value: Vector) -> None
```

<a id="unreal.RigUnit_BoneHarmonics.wave_ease"></a>

#### wave\_ease

```python
@property
def wave_ease() -> RigVMAnimEasingType
```

(RigVMAnimEasingType):  [Read-Write]

<a id="unreal.RigUnit_BoneHarmonics.wave_ease"></a>

#### wave\_ease

```python
@wave_ease.setter
def wave_ease(value: RigVMAnimEasingType) -> None
```

<a id="unreal.RigUnit_BoneHarmonics.wave_minimum"></a>

#### wave\_minimum

```python
@property
def wave_minimum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_BoneHarmonics.wave_minimum"></a>

#### wave\_minimum

```python
@wave_minimum.setter
def wave_minimum(value: float) -> None
```

<a id="unreal.RigUnit_BoneHarmonics.wave_maximum"></a>

#### wave\_maximum

```python
@property
def wave_maximum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_BoneHarmonics.wave_maximum"></a>

#### wave\_maximum

```python
@wave_maximum.setter
def wave_maximum(value: float) -> None
```

<a id="unreal.RigUnit_BoneHarmonics.rotation_order"></a>

#### rotation\_order

```python
@property
def rotation_order() -> EulerRotationOrder
```

(EulerRotationOrder):  [Read-Write]

<a id="unreal.RigUnit_BoneHarmonics.rotation_order"></a>

#### rotation\_order

```python
@rotation_order.setter
def rotation_order(value: EulerRotationOrder) -> None
```

<a id="unreal.RigUnit_BoneHarmonics.propagate_to_children"></a>

#### propagate\_to\_children

```python
@property
def propagate_to_children() -> bool
```

(bool):  [Read-Only] If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

<a id="unreal.RigUnit_ItemHarmonics"></a>