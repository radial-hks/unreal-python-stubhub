## AvaBendModifier Objects

```python
class AvaBendModifier(AvaGeometryBaseModifier)
```

Ava Bend Modifier

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaBendModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angle`` (float):  [Read-Write]
- ``bend_position`` (Vector):  [Read-Write]
- ``bend_rotation`` (Rotator):  [Read-Write]
- ``bidirectional`` (bool):  [Read-Write]
- ``extent`` (float):  [Read-Write]
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``symmetric_extents`` (bool):  [Read-Write]

<a id="unreal.AvaBendModifier.set_symmetric_extents"></a>

#### set_symmetric_extents

```python
def set_symmetric_extents(symmetric_extents: bool) -> None
```

x.set_symmetric_extents(symmetric_extents) -> None
Set Symmetric Extents

Args:
    symmetric_extents (bool):

<a id="unreal.AvaBendModifier.set_extent"></a>

#### set_extent

```python
def set_extent(extent: float) -> None
```

x.set_extent(extent) -> None
Set Extent

Args:
    extent (float):

<a id="unreal.AvaBendModifier.set_bidirectional"></a>

#### set_bidirectional

```python
def set_bidirectional(bidirectional: bool) -> None
```

x.set_bidirectional(bidirectional) -> None
Set Bidirectional

Args:
    bidirectional (bool):

<a id="unreal.AvaBendModifier.set_bend_rotation"></a>

#### set_bend_rotation

```python
def set_bend_rotation(bend_rotation: Rotator) -> None
```

x.set_bend_rotation(bend_rotation) -> None
Set Bend Rotation

Args:
    bend_rotation (Rotator):

<a id="unreal.AvaBendModifier.set_bend_position"></a>

#### set_bend_position

```python
def set_bend_position(bend_position: Vector) -> None
```

x.set_bend_position(bend_position) -> None
Set Bend Position

Args:
    bend_position (Vector):

<a id="unreal.AvaBendModifier.set_angle"></a>

#### set_angle

```python
def set_angle(angle: float) -> None
```

x.set_angle(angle) -> None
Set Angle

Args:
    angle (float):

<a id="unreal.AvaBendModifier.get_symmetric_extents"></a>

#### get_symmetric_extents

```python
def get_symmetric_extents() -> bool
```

x.get_symmetric_extents() -> bool
Get Symmetric Extents

Returns:
    bool:

<a id="unreal.AvaBendModifier.get_extent"></a>

#### get_extent

```python
def get_extent() -> float
```

x.get_extent() -> float
Get Extent

Returns:
    float:

<a id="unreal.AvaBendModifier.get_bidirectional"></a>

#### get_bidirectional

```python
def get_bidirectional() -> bool
```

x.get_bidirectional() -> bool
Get Bidirectional

Returns:
    bool:

<a id="unreal.AvaBendModifier.get_bend_rotation"></a>

#### get_bend_rotation

```python
def get_bend_rotation() -> Rotator
```

x.get_bend_rotation() -> Rotator
Get Bend Rotation

Returns:
    Rotator:

<a id="unreal.AvaBendModifier.get_bend_position"></a>

#### get_bend_position

```python
def get_bend_position() -> Vector
```

x.get_bend_position() -> Vector
Get Bend Position

Returns:
    Vector:

<a id="unreal.AvaBendModifier.get_angle"></a>

#### get_angle

```python
def get_angle() -> float
```

x.get_angle() -> float
Get Angle

Returns:
    float:

<a id="unreal.AvaBevelModifier"></a>