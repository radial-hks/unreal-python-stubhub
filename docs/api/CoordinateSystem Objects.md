## CoordinateSystem Objects

```python
class CoordinateSystem(StructBase)
```

Coordinate System

**C++ Source:**

- **Plugin**: RigLogic
- **Module**: RigLogicModule
- **File**: DNACommon.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``x_axis`` (Direction):  [Read-Write]
- ``y_axis`` (Direction):  [Read-Write]
- ``z_axis`` (Direction):  [Read-Write]

<a id="unreal.CoordinateSystem.__init__"></a>

#### __init__

```python
def __init__(x_axis: Direction = Direction.LEFT,
             y_axis: Direction = Direction.LEFT,
             z_axis: Direction = Direction.LEFT) -> None
```

<a id="unreal.CoordinateSystem.x_axis"></a>

#### x_axis

```python
@property
def x_axis() -> Direction
```

(Direction):  [Read-Only]

<a id="unreal.CoordinateSystem.y_axis"></a>

#### y_axis

```python
@property
def y_axis() -> Direction
```

(Direction):  [Read-Only]

<a id="unreal.CoordinateSystem.z_axis"></a>

#### z_axis

```python
@property
def z_axis() -> Direction
```

(Direction):  [Read-Only]

<a id="unreal.MeshBlendShapeChannelMapping"></a>