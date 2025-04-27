## RigUnit_ChainHarmonics_Pendulum Objects

```python
class RigUnit_ChainHarmonics_Pendulum(StructBase)
```

Rig Unit Chain Harmonics Pendulum

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ChainHarmonics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write]
- ``pendulum_blend`` (float):  [Read-Write]
- ``pendulum_drag`` (float):  [Read-Write]
- ``pendulum_ease`` (RigVMAnimEasingType):  [Read-Write]
- ``pendulum_gravity`` (Vector):  [Read-Write]
- ``pendulum_maximum`` (float):  [Read-Write]
- ``pendulum_minimum`` (float):  [Read-Write]
- ``pendulum_stiffness`` (float):  [Read-Write]
- ``unwind_axis`` (Vector):  [Read-Write]
- ``unwind_maximum`` (float):  [Read-Write]
- ``unwind_minimum`` (float):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Pendulum.__init__"></a>

#### __init__

```python
def __init__(enabled: bool = False,
             pendulum_stiffness: float = 0.000000,
             pendulum_gravity: Vector = [0.000000, 0.000000, 0.000000],
             pendulum_blend: float = 0.000000,
             pendulum_drag: float = 0.000000,
             pendulum_minimum: float = 0.000000,
             pendulum_maximum: float = 0.000000,
             pendulum_ease: RigVMAnimEasingType = RigVMAnimEasingType.LINEAR,
             unwind_axis: Vector = [0.000000, 0.000000, 0.000000],
             unwind_minimum: float = 0.000000,
             unwind_maximum: float = 0.000000) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Pendulum.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Pendulum.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Pendulum.pendulum_stiffness"></a>

#### pendulum_stiffness

```python
@property
def pendulum_stiffness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Pendulum.pendulum_stiffness"></a>

#### pendulum_stiffness

```python
@pendulum_stiffness.setter
def pendulum_stiffness(value: float) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Pendulum.pendulum_gravity"></a>

#### pendulum_gravity

```python
@property
def pendulum_gravity() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Pendulum.pendulum_gravity"></a>

#### pendulum_gravity

```python
@pendulum_gravity.setter
def pendulum_gravity(value: Vector) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Pendulum.pendulum_blend"></a>

#### pendulum_blend

```python
@property
def pendulum_blend() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Pendulum.pendulum_blend"></a>

#### pendulum_blend

```python
@pendulum_blend.setter
def pendulum_blend(value: float) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Pendulum.pendulum_drag"></a>

#### pendulum_drag

```python
@property
def pendulum_drag() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Pendulum.pendulum_drag"></a>

#### pendulum_drag

```python
@pendulum_drag.setter
def pendulum_drag(value: float) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Pendulum.pendulum_minimum"></a>

#### pendulum_minimum

```python
@property
def pendulum_minimum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Pendulum.pendulum_minimum"></a>

#### pendulum_minimum

```python
@pendulum_minimum.setter
def pendulum_minimum(value: float) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Pendulum.pendulum_maximum"></a>

#### pendulum_maximum

```python
@property
def pendulum_maximum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Pendulum.pendulum_maximum"></a>

#### pendulum_maximum

```python
@pendulum_maximum.setter
def pendulum_maximum(value: float) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Pendulum.pendulum_ease"></a>

#### pendulum_ease

```python
@property
def pendulum_ease() -> RigVMAnimEasingType
```

(RigVMAnimEasingType):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Pendulum.pendulum_ease"></a>

#### pendulum_ease

```python
@pendulum_ease.setter
def pendulum_ease(value: RigVMAnimEasingType) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Pendulum.unwind_axis"></a>

#### unwind_axis

```python
@property
def unwind_axis() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Pendulum.unwind_axis"></a>

#### unwind_axis

```python
@unwind_axis.setter
def unwind_axis(value: Vector) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Pendulum.unwind_minimum"></a>

#### unwind_minimum

```python
@property
def unwind_minimum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Pendulum.unwind_minimum"></a>

#### unwind_minimum

```python
@unwind_minimum.setter
def unwind_minimum(value: float) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Pendulum.unwind_maximum"></a>

#### unwind_maximum

```python
@property
def unwind_maximum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Pendulum.unwind_maximum"></a>

#### unwind_maximum

```python
@unwind_maximum.setter
def unwind_maximum(value: float) -> None
```

<a id="unreal.RigUnit_ChainHarmonics"></a>