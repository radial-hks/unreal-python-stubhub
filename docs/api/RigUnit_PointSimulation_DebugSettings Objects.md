## RigUnit_PointSimulation_DebugSettings Objects

```python
class RigUnit_PointSimulation_DebugSettings(StructBase)
```

Rig Unit Point Simulation Debug Settings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_PointSimulation.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collision_scale`` (float):  [Read-Write] The size of the debug drawing information
- ``color`` (LinearColor):  [Read-Write] The color to use for debug drawing
- ``draw_points_as_spheres`` (bool):  [Read-Write] If set to true points will be drawn as spheres with their sizes reflected
- ``enabled`` (bool):  [Read-Write] If enabled debug information will be drawn
- ``scale`` (float):  [Read-Write] The size of the debug drawing information
- ``world_offset`` (Transform):  [Read-Write] The offset at which to draw the debug information in the world

<a id="unreal.RigUnit_PointSimulation_DebugSettings.__init__"></a>

#### __init__

```python
def __init__(
    enabled: bool = False,
    scale: float = 0.000000,
    collision_scale: float = 0.000000,
    draw_points_as_spheres: bool = False,
    color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    world_offset: Transform = [[0.000000, 0.000000, 0.000000],
                               [-0.000000, 0.000000, 0.000000],
                               [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_PointSimulation_DebugSettings.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write] If enabled debug information will be drawn

<a id="unreal.RigUnit_PointSimulation_DebugSettings.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.RigUnit_PointSimulation_DebugSettings.scale"></a>

#### scale

```python
@property
def scale() -> float
```

(float):  [Read-Write] The size of the debug drawing information

<a id="unreal.RigUnit_PointSimulation_DebugSettings.scale"></a>

#### scale

```python
@scale.setter
def scale(value: float) -> None
```

<a id="unreal.RigUnit_PointSimulation_DebugSettings.collision_scale"></a>

#### collision_scale

```python
@property
def collision_scale() -> float
```

(float):  [Read-Write] The size of the debug drawing information

<a id="unreal.RigUnit_PointSimulation_DebugSettings.collision_scale"></a>

#### collision_scale

```python
@collision_scale.setter
def collision_scale(value: float) -> None
```

<a id="unreal.RigUnit_PointSimulation_DebugSettings.draw_points_as_spheres"></a>

#### draw_points_as_spheres

```python
@property
def draw_points_as_spheres() -> bool
```

(bool):  [Read-Write] If set to true points will be drawn as spheres with their sizes reflected

<a id="unreal.RigUnit_PointSimulation_DebugSettings.draw_points_as_spheres"></a>

#### draw_points_as_spheres

```python
@draw_points_as_spheres.setter
def draw_points_as_spheres(value: bool) -> None
```

<a id="unreal.RigUnit_PointSimulation_DebugSettings.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write] The color to use for debug drawing

<a id="unreal.RigUnit_PointSimulation_DebugSettings.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigUnit_PointSimulation_DebugSettings.world_offset"></a>

#### world_offset

```python
@property
def world_offset() -> Transform
```

(Transform):  [Read-Write] The offset at which to draw the debug information in the world

<a id="unreal.RigUnit_PointSimulation_DebugSettings.world_offset"></a>

#### world_offset

```python
@world_offset.setter
def world_offset(value: Transform) -> None
```

<a id="unreal.RigUnit_PointSimulation_BoneTarget"></a>