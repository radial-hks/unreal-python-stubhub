## RigUnit\_ChainHarmonics\_Reach Objects

```python
class RigUnit_ChainHarmonics_Reach(StructBase)
```

Rig Unit Chain Harmonics Reach

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ChainHarmonics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write]
- ``reach_axis`` (Vector):  [Read-Only]
- ``reach_ease`` (RigVMAnimEasingType):  [Read-Write]
- ``reach_maximum`` (float):  [Read-Write]
- ``reach_minimum`` (float):  [Read-Write]
- ``reach_target`` (Vector):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Reach.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        enabled: bool = False,
        reach_target: Vector = [0.000000, 0.000000, 0.000000],
        reach_axis: Vector = [0.000000, 0.000000, 0.000000],
        reach_minimum: float = 0.000000,
        reach_maximum: float = 0.000000,
        reach_ease: RigVMAnimEasingType = RigVMAnimEasingType.LINEAR) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Reach.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Reach.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Reach.reach_target"></a>

#### reach\_target

```python
@property
def reach_target() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Reach.reach_target"></a>

#### reach\_target

```python
@reach_target.setter
def reach_target(value: Vector) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Reach.reach_axis"></a>

#### reach\_axis

```python
@property
def reach_axis() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_ChainHarmonics_Reach.reach_minimum"></a>

#### reach\_minimum

```python
@property
def reach_minimum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Reach.reach_minimum"></a>

#### reach\_minimum

```python
@reach_minimum.setter
def reach_minimum(value: float) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Reach.reach_maximum"></a>

#### reach\_maximum

```python
@property
def reach_maximum() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Reach.reach_maximum"></a>

#### reach\_maximum

```python
@reach_maximum.setter
def reach_maximum(value: float) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Reach.reach_ease"></a>

#### reach\_ease

```python
@property
def reach_ease() -> RigVMAnimEasingType
```

(RigVMAnimEasingType):  [Read-Write]

<a id="unreal.RigUnit_ChainHarmonics_Reach.reach_ease"></a>

#### reach\_ease

```python
@reach_ease.setter
def reach_ease(value: RigVMAnimEasingType) -> None
```

<a id="unreal.RigUnit_ChainHarmonics_Wave"></a>