## RigVMFunction_DebugArcNoSpace Objects

```python
class RigVMFunction_DebugArcNoSpace(RigVMFunction_DebugBaseMutable)
```

Draws an arc in the viewport, can take in different min and max degrees

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_DebugPrimitives.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write]
- ``detail`` (int32):  [Read-Write]
- ``enabled`` (bool):  [Read-Write]
- ``execute_context`` (RigVMExecuteContext):  [Read-Write] * This property is used to chain multiple mutable nodes together
- ``maximum_degrees`` (float):  [Read-Write]
- ``minimum_degrees`` (float):  [Read-Write]
- ``radius`` (float):  [Read-Write]
- ``thickness`` (float):  [Read-Write]
- ``transform`` (Transform):  [Read-Write]
- ``world_offset`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_DebugArcNoSpace.__init__"></a>

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
             world_offset: Transform = [[0.000000, 0.000000, 0.000000],
                                        [-0.000000, 0.000000, 0.000000],
                                        [1.000000, 1.000000, 1.000000]],
             enabled: bool = False) -> None
```

<a id="unreal.RigVMFunction_DebugArcNoSpace.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_DebugArcNoSpace.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigVMFunction_DebugArcNoSpace.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigVMFunction_DebugArcNoSpace.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigVMFunction_DebugArcNoSpace.radius"></a>

#### radius

```python
@property
def radius() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_DebugArcNoSpace.radius"></a>

#### radius

```python
@radius.setter
def radius(value: float) -> None
```

<a id="unreal.RigVMFunction_DebugArcNoSpace.minimum_degrees"></a>

#### minimum_degrees

```python
@property
def minimum_degrees() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_DebugArcNoSpace.minimum_degrees"></a>

#### minimum_degrees

```python
@minimum_degrees.setter
def minimum_degrees(value: float) -> None
```

<a id="unreal.RigVMFunction_DebugArcNoSpace.maximum_degrees"></a>

#### maximum_degrees

```python
@property
def maximum_degrees() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_DebugArcNoSpace.maximum_degrees"></a>

#### maximum_degrees

```python
@maximum_degrees.setter
def maximum_degrees(value: float) -> None
```

<a id="unreal.RigVMFunction_DebugArcNoSpace.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_DebugArcNoSpace.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.RigVMFunction_DebugArcNoSpace.detail"></a>

#### detail

```python
@property
def detail() -> int
```

(int32):  [Read-Write]

<a id="unreal.RigVMFunction_DebugArcNoSpace.detail"></a>

#### detail

```python
@detail.setter
def detail(value: int) -> None
```

<a id="unreal.RigVMFunction_DebugArcNoSpace.world_offset"></a>

#### world_offset

```python
@property
def world_offset() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_DebugArcNoSpace.world_offset"></a>

#### world_offset

```python
@world_offset.setter
def world_offset(value: Transform) -> None
```

<a id="unreal.RigVMFunction_DebugArcNoSpace.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_DebugArcNoSpace.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.RigVMFunction_DebugBoxNoSpace"></a>