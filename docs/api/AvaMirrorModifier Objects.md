## AvaMirrorModifier Objects

```python
class AvaMirrorModifier(AvaGeometryBaseModifier)
```

Ava Mirror Modifier

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaMirrorModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_plane_cut`` (bool):  [Read-Write]
- ``flip_cut_side`` (bool):  [Read-Write]
- ``mirror_frame_position`` (Vector):  [Read-Write]
- ``mirror_frame_rotation`` (Rotator):  [Read-Write]
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``show_mirror_frame`` (bool):  [Read-Write]
- ``weld_along_plane`` (bool):  [Read-Write]

<a id="unreal.AvaMirrorModifier.set_weld_along_plane"></a>

#### set_weld_along_plane

```python
def set_weld_along_plane(weld_along_plane: bool) -> None
```

x.set_weld_along_plane(weld_along_plane) -> None
Set Weld Along Plane

Args:
    weld_along_plane (bool):

<a id="unreal.AvaMirrorModifier.set_mirror_frame_rotation"></a>

#### set_mirror_frame_rotation

```python
def set_mirror_frame_rotation(mirror_frame_rotation: Rotator) -> None
```

x.set_mirror_frame_rotation(mirror_frame_rotation) -> None
Set Mirror Frame Rotation

Args:
    mirror_frame_rotation (Rotator):

<a id="unreal.AvaMirrorModifier.set_mirror_frame_position"></a>

#### set_mirror_frame_position

```python
def set_mirror_frame_position(mirror_frame_position: Vector) -> None
```

x.set_mirror_frame_position(mirror_frame_position) -> None
Set Mirror Frame Position

Args:
    mirror_frame_position (Vector):

<a id="unreal.AvaMirrorModifier.set_flip_cut_side"></a>

#### set_flip_cut_side

```python
def set_flip_cut_side(flip_cut_side: bool) -> None
```

x.set_flip_cut_side(flip_cut_side) -> None
Set Flip Cut Side

Args:
    flip_cut_side (bool):

<a id="unreal.AvaMirrorModifier.set_apply_plane_cut"></a>

#### set_apply_plane_cut

```python
def set_apply_plane_cut(apply_plane_cut: bool) -> None
```

x.set_apply_plane_cut(apply_plane_cut) -> None
Set Apply Plane Cut

Args:
    apply_plane_cut (bool):

<a id="unreal.AvaMirrorModifier.get_weld_along_plane"></a>

#### get_weld_along_plane

```python
def get_weld_along_plane() -> bool
```

x.get_weld_along_plane() -> bool
Get Weld Along Plane

Returns:
    bool:

<a id="unreal.AvaMirrorModifier.get_mirror_frame_rotation"></a>

#### get_mirror_frame_rotation

```python
def get_mirror_frame_rotation() -> Rotator
```

x.get_mirror_frame_rotation() -> Rotator
Get Mirror Frame Rotation

Returns:
    Rotator:

<a id="unreal.AvaMirrorModifier.get_mirror_frame_position"></a>

#### get_mirror_frame_position

```python
def get_mirror_frame_position() -> Vector
```

x.get_mirror_frame_position() -> Vector
Get Mirror Frame Position

Returns:
    Vector:

<a id="unreal.AvaMirrorModifier.get_flip_cut_side"></a>

#### get_flip_cut_side

```python
def get_flip_cut_side() -> bool
```

x.get_flip_cut_side() -> bool
Get Flip Cut Side

Returns:
    bool:

<a id="unreal.AvaMirrorModifier.get_apply_plane_cut"></a>

#### get_apply_plane_cut

```python
def get_apply_plane_cut() -> bool
```

x.get_apply_plane_cut() -> bool
Get Apply Plane Cut

Returns:
    bool:

<a id="unreal.AvaNormalModifier"></a>