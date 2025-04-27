## RigUnit_DebugLineItemSpace Objects

```python
class RigUnit_DebugLineItemSpace(RigUnit_DebugBaseMutable)
```

Draws a line in the viewport given a start and end vector

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DebugLine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (Vector):  [Read-Write]
- ``b`` (Vector):  [Read-Write]
- ``color`` (LinearColor):  [Read-Write]
- ``enabled`` (bool):  [Read-Write]
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``space`` (RigElementKey):  [Read-Write]
- ``thickness`` (float):  [Read-Write]
- ``world_offset`` (Transform):  [Read-Write]

<a id="unreal.RigUnit_DebugLineItemSpace.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             a: Vector = [0.000000, 0.000000, 0.000000],
             b: Vector = [0.000000, 0.000000, 0.000000],
             color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             thickness: float = 0.000000,
             space: RigElementKey = [RigElementType.NONE, "None"],
             world_offset: Transform = [[0.000000, 0.000000, 0.000000],
                                        [-0.000000, 0.000000, 0.000000],
                                        [1.000000, 1.000000, 1.000000]],
             enabled: bool = False) -> None
```

<a id="unreal.RigUnit_DebugLineItemSpace.a"></a>

#### a

```python
@property
def a() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_DebugLineItemSpace.a"></a>

#### a

```python
@a.setter
def a(value: Vector) -> None
```

<a id="unreal.RigUnit_DebugLineItemSpace.b"></a>

#### b

```python
@property
def b() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_DebugLineItemSpace.b"></a>

#### b

```python
@b.setter
def b(value: Vector) -> None
```

<a id="unreal.RigUnit_DebugLineItemSpace.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigUnit_DebugLineItemSpace.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigUnit_DebugLineItemSpace.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_DebugLineItemSpace.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.RigUnit_DebugLineItemSpace.space"></a>

#### space

```python
@property
def space() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_DebugLineItemSpace.space"></a>

#### space

```python
@space.setter
def space(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_DebugLineItemSpace.world_offset"></a>

#### world_offset

```python
@property
def world_offset() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigUnit_DebugLineItemSpace.world_offset"></a>

#### world_offset

```python
@world_offset.setter
def world_offset(value: Transform) -> None
```

<a id="unreal.RigUnit_DebugLineItemSpace.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_DebugLineItemSpace.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.RigUnit_DebugLineStrip"></a>