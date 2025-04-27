## RigUnit_DebugLineStripItemSpace Objects

```python
class RigUnit_DebugLineStripItemSpace(RigUnit_DebugBaseMutable)
```

Draws a line strip in the viewport given any number of points

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DebugLineStrip.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write]
- ``enabled`` (bool):  [Read-Write]
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``points`` (Array[Vector]):  [Read-Write]
- ``space`` (RigElementKey):  [Read-Write]
- ``thickness`` (float):  [Read-Write]
- ``world_offset`` (Transform):  [Read-Write]

<a id="unreal.RigUnit_DebugLineStripItemSpace.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             points: Array[Vector] = [],
             color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             thickness: float = 0.000000,
             space: RigElementKey = [RigElementType.NONE, "None"],
             world_offset: Transform = [[0.000000, 0.000000, 0.000000],
                                        [-0.000000, 0.000000, 0.000000],
                                        [1.000000, 1.000000, 1.000000]],
             enabled: bool = False) -> None
```

<a id="unreal.RigUnit_DebugLineStripItemSpace.points"></a>

#### points

```python
@property
def points() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.RigUnit_DebugLineStripItemSpace.points"></a>

#### points

```python
@points.setter
def points(value: Array[Vector]) -> None
```

<a id="unreal.RigUnit_DebugLineStripItemSpace.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigUnit_DebugLineStripItemSpace.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigUnit_DebugLineStripItemSpace.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_DebugLineStripItemSpace.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.RigUnit_DebugLineStripItemSpace.space"></a>

#### space

```python
@property
def space() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_DebugLineStripItemSpace.space"></a>

#### space

```python
@space.setter
def space(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_DebugLineStripItemSpace.world_offset"></a>

#### world_offset

```python
@property
def world_offset() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigUnit_DebugLineStripItemSpace.world_offset"></a>

#### world_offset

```python
@world_offset.setter
def world_offset(value: Transform) -> None
```

<a id="unreal.RigUnit_DebugLineStripItemSpace.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_DebugLineStripItemSpace.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.RigUnit_DebugRectangle"></a>