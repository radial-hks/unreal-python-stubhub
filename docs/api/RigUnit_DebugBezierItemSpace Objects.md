## RigUnit_DebugBezierItemSpace Objects

```python
class RigUnit_DebugBezierItemSpace(RigVMFunction_DebugBaseMutable)
```

Rig Unit Debug Bezier Item Space

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DebugBezier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bezier`` (RigVMFourPointBezier):  [Read-Write]
- ``color`` (LinearColor):  [Read-Write]
- ``detail`` (int32):  [Read-Write]
- ``enabled`` (bool):  [Read-Only]
- ``execute_context`` (RigVMExecuteContext):  [Read-Write] * This property is used to chain multiple mutable nodes together
- ``maximum_u`` (float):  [Read-Write]
- ``minimum_u`` (float):  [Read-Write]
- ``space`` (RigElementKey):  [Read-Write]
- ``thickness`` (float):  [Read-Write]
- ``world_offset`` (Transform):  [Read-Write]

<a id="unreal.RigUnit_DebugBezierItemSpace.__init__"></a>

#### __init__

```python
def __init__(execute_context: RigVMExecuteContext = [],
             bezier: RigVMFourPointBezier = [],
             minimum_u: float = 0.000000,
             maximum_u: float = 0.000000,
             color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             thickness: float = 0.000000,
             detail: int = 0,
             space: RigElementKey = [RigElementType.NONE, "None"],
             world_offset: Transform = [[0.000000, 0.000000, 0.000000],
                                        [-0.000000, 0.000000, 0.000000],
                                        [1.000000, 1.000000, 1.000000]],
             enabled: bool = False) -> None
```

<a id="unreal.RigUnit_DebugBezierItemSpace.bezier"></a>

#### bezier

```python
@property
def bezier() -> RigVMFourPointBezier
```

(RigVMFourPointBezier):  [Read-Write]

<a id="unreal.RigUnit_DebugBezierItemSpace.bezier"></a>

#### bezier

```python
@bezier.setter
def bezier(value: RigVMFourPointBezier) -> None
```

<a id="unreal.RigUnit_DebugBezierItemSpace.minimum_u"></a>

#### minimum_u

```python
@property
def minimum_u() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_DebugBezierItemSpace.minimum_u"></a>

#### minimum_u

```python
@minimum_u.setter
def minimum_u(value: float) -> None
```

<a id="unreal.RigUnit_DebugBezierItemSpace.maximum_u"></a>

#### maximum_u

```python
@property
def maximum_u() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_DebugBezierItemSpace.maximum_u"></a>

#### maximum_u

```python
@maximum_u.setter
def maximum_u(value: float) -> None
```

<a id="unreal.RigUnit_DebugBezierItemSpace.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigUnit_DebugBezierItemSpace.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigUnit_DebugBezierItemSpace.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_DebugBezierItemSpace.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.RigUnit_DebugBezierItemSpace.detail"></a>

#### detail

```python
@property
def detail() -> int
```

(int32):  [Read-Write]

<a id="unreal.RigUnit_DebugBezierItemSpace.detail"></a>

#### detail

```python
@detail.setter
def detail(value: int) -> None
```

<a id="unreal.RigUnit_DebugBezierItemSpace.space"></a>

#### space

```python
@property
def space() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_DebugBezierItemSpace.space"></a>

#### space

```python
@space.setter
def space(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_DebugBezierItemSpace.world_offset"></a>

#### world_offset

```python
@property
def world_offset() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigUnit_DebugBezierItemSpace.world_offset"></a>

#### world_offset

```python
@world_offset.setter
def world_offset(value: Transform) -> None
```

<a id="unreal.RigUnit_DebugBezierItemSpace.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_DebugHierarchy"></a>