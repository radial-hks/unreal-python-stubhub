## RigVMFunction_DebugArc Objects

```python
class RigVMFunction_DebugArc(RigVMFunction_DebugBaseMutable)
```

Rig VMFunction Debug Arc

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_DebugPrimitives.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write]
- ``detail`` (int32):  [Read-Write]
- ``enabled`` (bool):  [Read-Only]
- ``execute_context`` (RigVMExecuteContext):  [Read-Write] * This property is used to chain multiple mutable nodes together
- ``maximum_degrees`` (float):  [Read-Write]
- ``minimum_degrees`` (float):  [Read-Write]
- ``radius`` (float):  [Read-Write]
- ``space`` (Name):  [Read-Write]
- ``thickness`` (float):  [Read-Write]
- ``transform`` (Transform):  [Read-Write]
- ``world_offset`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_DebugArc.__init__"></a>

#### __init__

```python
def __init__(execute_context: RigVMExecuteContext = [],
             transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
             color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             radius: float = 0.000000,
             minimum_degrees: float = 0.000000,
             maximum_degrees: float = 0.000000,
             thickness: float = 0.000000,
             detail: int = 0,
             space: Name = "None",
             world_offset: Transform = [[0.000000, 0.000000, 0.000000],
                                        [-0.000000, 0.000000, 0.000000],
                                        [1.000000, 1.000000, 1.000000]],
             enabled: bool = False) -> None
```

<a id="unreal.RigVMFunction_DebugArc.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_DebugArc.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigVMFunction_DebugArc.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigVMFunction_DebugArc.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigVMFunction_DebugArc.radius"></a>

#### radius

```python
@property
def radius() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_DebugArc.radius"></a>

#### radius

```python
@radius.setter
def radius(value: float) -> None
```

<a id="unreal.RigVMFunction_DebugArc.minimum_degrees"></a>

#### minimum_degrees

```python
@property
def minimum_degrees() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_DebugArc.minimum_degrees"></a>

#### minimum_degrees

```python
@minimum_degrees.setter
def minimum_degrees(value: float) -> None
```

<a id="unreal.RigVMFunction_DebugArc.maximum_degrees"></a>

#### maximum_degrees

```python
@property
def maximum_degrees() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_DebugArc.maximum_degrees"></a>

#### maximum_degrees

```python
@maximum_degrees.setter
def maximum_degrees(value: float) -> None
```

<a id="unreal.RigVMFunction_DebugArc.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_DebugArc.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.RigVMFunction_DebugArc.detail"></a>

#### detail

```python
@property
def detail() -> int
```

(int32):  [Read-Write]

<a id="unreal.RigVMFunction_DebugArc.detail"></a>

#### detail

```python
@detail.setter
def detail(value: int) -> None
```

<a id="unreal.RigVMFunction_DebugArc.space"></a>

#### space

```python
@property
def space() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigVMFunction_DebugArc.space"></a>

#### space

```python
@space.setter
def space(value: Name) -> None
```

<a id="unreal.RigVMFunction_DebugArc.world_offset"></a>

#### world_offset

```python
@property
def world_offset() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_DebugArc.world_offset"></a>

#### world_offset

```python
@world_offset.setter
def world_offset(value: Transform) -> None
```

<a id="unreal.RigVMFunction_DebugArc.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigVMFunction_DebugArcNoSpace"></a>