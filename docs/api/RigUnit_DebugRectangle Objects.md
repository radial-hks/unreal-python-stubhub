## RigUnit_DebugRectangle Objects

```python
class RigUnit_DebugRectangle(RigUnit_DebugBaseMutable)
```

Rig Unit Debug Rectangle

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DebugPrimitives.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write]
- ``enabled`` (bool):  [Read-Only]
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``scale`` (float):  [Read-Write]
- ``space`` (Name):  [Read-Write]
- ``thickness`` (float):  [Read-Write]
- ``transform`` (Transform):  [Read-Write]
- ``world_offset`` (Transform):  [Read-Write]

<a id="unreal.RigUnit_DebugRectangle.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
             color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             scale: float = 0.000000,
             thickness: float = 0.000000,
             space: Name = "None",
             world_offset: Transform = [[0.000000, 0.000000, 0.000000],
                                        [-0.000000, 0.000000, 0.000000],
                                        [1.000000, 1.000000, 1.000000]],
             enabled: bool = False) -> None
```

<a id="unreal.RigUnit_DebugRectangle.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigUnit_DebugRectangle.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigUnit_DebugRectangle.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigUnit_DebugRectangle.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigUnit_DebugRectangle.scale"></a>

#### scale

```python
@property
def scale() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_DebugRectangle.scale"></a>

#### scale

```python
@scale.setter
def scale(value: float) -> None
```

<a id="unreal.RigUnit_DebugRectangle.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_DebugRectangle.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.RigUnit_DebugRectangle.space"></a>

#### space

```python
@property
def space() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigUnit_DebugRectangle.space"></a>

#### space

```python
@space.setter
def space(value: Name) -> None
```

<a id="unreal.RigUnit_DebugRectangle.world_offset"></a>

#### world_offset

```python
@property
def world_offset() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigUnit_DebugRectangle.world_offset"></a>

#### world_offset

```python
@world_offset.setter
def world_offset(value: Transform) -> None
```

<a id="unreal.RigUnit_DebugRectangle.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_DebugRectangleItemSpace"></a>