## AvaExtrudeModifier Objects

```python
class AvaExtrudeModifier(AvaGeometryBaseModifier)
```

This modifier extrude triangles from a 2D shape with a specific depth and optionally closes the back

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaExtrudeModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``close_back`` (bool):  [Read-Write] Closes the back of the extrude for a 2D shape for example
- ``depth`` (float):  [Read-Write] Handles mesh depth to extrude primary section
- ``extrude_mode`` (AvaExtrudeMode):  [Read-Write] Specifies the Extrude direction
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``move_mesh_opposite_direction`` (bool):  [Read-Write] Moves the mesh in the opposite extrude direction by the depth distance
  deprecated: Use ExtrudeMode instead

<a id="unreal.AvaExtrudeModifier.move_mesh_opposite_direction"></a>

#### move_mesh_opposite_direction

```python
@property
def move_mesh_opposite_direction() -> bool
```

(bool):  [Read-Write] Moves the mesh in the opposite extrude direction by the depth distance
deprecated: Use ExtrudeMode instead

<a id="unreal.AvaExtrudeModifier.move_mesh_opposite_direction"></a>

#### move_mesh_opposite_direction

```python
@move_mesh_opposite_direction.setter
def move_mesh_opposite_direction(value: bool) -> None
```

<a id="unreal.AvaExtrudeModifier.set_extrude_mode"></a>

#### set_extrude_mode

```python
def set_extrude_mode(extrude_mode: AvaExtrudeMode) -> None
```

x.set_extrude_mode(extrude_mode) -> None
Set Extrude Mode

Args:
    extrude_mode (AvaExtrudeMode):

<a id="unreal.AvaExtrudeModifier.set_depth"></a>

#### set_depth

```python
def set_depth(depth: float) -> None
```

x.set_depth(depth) -> None
Set Depth

Args:
    depth (float):

<a id="unreal.AvaExtrudeModifier.set_close_back"></a>

#### set_close_back

```python
def set_close_back(close_back: bool) -> None
```

x.set_close_back(close_back) -> None
Set Close Back

Args:
    close_back (bool):

<a id="unreal.AvaExtrudeModifier.get_extrude_mode"></a>

#### get_extrude_mode

```python
def get_extrude_mode() -> AvaExtrudeMode
```

x.get_extrude_mode() -> AvaExtrudeMode
Get Extrude Mode

Returns:
    AvaExtrudeMode:

<a id="unreal.AvaExtrudeModifier.get_depth"></a>

#### get_depth

```python
def get_depth() -> float
```

x.get_depth() -> float
Get Depth

Returns:
    float:

<a id="unreal.AvaExtrudeModifier.get_close_back"></a>

#### get_close_back

```python
def get_close_back() -> bool
```

x.get_close_back() -> bool
Get Close Back

Returns:
    bool:

<a id="unreal.AvaArrangeBaseModifier"></a>