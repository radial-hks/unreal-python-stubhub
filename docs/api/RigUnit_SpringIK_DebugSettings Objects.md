## RigUnit_SpringIK_DebugSettings Objects

```python
class RigUnit_SpringIK_DebugSettings(StructBase)
```

Rig Unit Spring IK Debug Settings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SpringIK.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write] The color to use for debug drawing
- ``enabled`` (bool):  [Read-Write] If enabled debug information will be drawn
- ``scale`` (float):  [Read-Write] The size of the debug drawing information
- ``world_offset`` (Transform):  [Read-Write] The offset at which to draw the debug information in the world

<a id="unreal.RigUnit_SpringIK_DebugSettings.__init__"></a>

#### __init__

```python
def __init__(
    enabled: bool = False,
    scale: float = 0.000000,
    color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    world_offset: Transform = [[0.000000, 0.000000, 0.000000],
                               [-0.000000, 0.000000, 0.000000],
                               [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_SpringIK_DebugSettings.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write] If enabled debug information will be drawn

<a id="unreal.RigUnit_SpringIK_DebugSettings.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.RigUnit_SpringIK_DebugSettings.scale"></a>

#### scale

```python
@property
def scale() -> float
```

(float):  [Read-Write] The size of the debug drawing information

<a id="unreal.RigUnit_SpringIK_DebugSettings.scale"></a>

#### scale

```python
@scale.setter
def scale(value: float) -> None
```

<a id="unreal.RigUnit_SpringIK_DebugSettings.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write] The color to use for debug drawing

<a id="unreal.RigUnit_SpringIK_DebugSettings.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigUnit_SpringIK_DebugSettings.world_offset"></a>

#### world_offset

```python
@property
def world_offset() -> Transform
```

(Transform):  [Read-Write] The offset at which to draw the debug information in the world

<a id="unreal.RigUnit_SpringIK_DebugSettings.world_offset"></a>

#### world_offset

```python
@world_offset.setter
def world_offset(value: Transform) -> None
```

<a id="unreal.RigUnit_SpringIK"></a>