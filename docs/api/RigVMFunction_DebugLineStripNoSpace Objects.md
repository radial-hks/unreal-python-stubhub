## RigVMFunction_DebugLineStripNoSpace Objects

```python
class RigVMFunction_DebugLineStripNoSpace(RigVMFunction_DebugBaseMutable)
```

Draws a line strip in the viewport given any number of points

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_DebugLineStrip.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write]
- ``enabled`` (bool):  [Read-Write]
- ``execute_context`` (RigVMExecuteContext):  [Read-Write] * This property is used to chain multiple mutable nodes together
- ``points`` (Array[Vector]):  [Read-Write]
- ``thickness`` (float):  [Read-Write]
- ``world_offset`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_DebugLineStripNoSpace.__init__"></a>

#### __init__

```python
def __init__(execute_context: RigVMExecuteContext = [],
             points: Array[Vector] = [],
             color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             thickness: float = 0.000000,
             world_offset: Transform = [[0.000000, 0.000000, 0.000000],
                                        [-0.000000, 0.000000, 0.000000],
                                        [1.000000, 1.000000, 1.000000]],
             enabled: bool = False) -> None
```

<a id="unreal.RigVMFunction_DebugLineStripNoSpace.points"></a>

#### points

```python
@property
def points() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.RigVMFunction_DebugLineStripNoSpace.points"></a>

#### points

```python
@points.setter
def points(value: Array[Vector]) -> None
```

<a id="unreal.RigVMFunction_DebugLineStripNoSpace.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigVMFunction_DebugLineStripNoSpace.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigVMFunction_DebugLineStripNoSpace.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_DebugLineStripNoSpace.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.RigVMFunction_DebugLineStripNoSpace.world_offset"></a>

#### world_offset

```python
@property
def world_offset() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_DebugLineStripNoSpace.world_offset"></a>

#### world_offset

```python
@world_offset.setter
def world_offset(value: Transform) -> None
```

<a id="unreal.RigVMFunction_DebugLineStripNoSpace.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_DebugLineStripNoSpace.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.RigVMFunction_DebugBase"></a>