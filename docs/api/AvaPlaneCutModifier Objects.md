## AvaPlaneCutModifier Objects

```python
class AvaPlaneCutModifier(AvaGeometryBaseModifier)
```

This modifier cuts a shape based on a 2D plane

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaPlaneCutModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``fill_holes`` (bool):  [Read-Write]
- ``invert_cut`` (bool):  [Read-Write]
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``plane_origin`` (float):  [Read-Write]
- ``plane_rotation`` (Rotator):  [Read-Write]
- ``use_preview`` (bool):  [Read-Write]

<a id="unreal.AvaPlaneCutModifier.set_plane_rotation"></a>

#### set_plane_rotation

```python
def set_plane_rotation(rotation: Rotator) -> None
```

x.set_plane_rotation(rotation) -> None
Set Plane Rotation

Args:
    rotation (Rotator):

<a id="unreal.AvaPlaneCutModifier.set_plane_origin"></a>

#### set_plane_origin

```python
def set_plane_origin(origin: float) -> None
```

x.set_plane_origin(origin) -> None
Set Plane Origin

Args:
    origin (float):

<a id="unreal.AvaPlaneCutModifier.set_invert_cut"></a>

#### set_invert_cut

```python
def set_invert_cut(invert_cut: bool) -> None
```

x.set_invert_cut(invert_cut) -> None
Set Invert Cut

Args:
    invert_cut (bool):

<a id="unreal.AvaPlaneCutModifier.set_fill_holes"></a>

#### set_fill_holes

```python
def set_fill_holes(fill_holes: bool) -> None
```

x.set_fill_holes(fill_holes) -> None
Set Fill Holes

Args:
    fill_holes (bool):

<a id="unreal.AvaPlaneCutModifier.get_plane_rotation"></a>

#### get_plane_rotation

```python
def get_plane_rotation() -> Rotator
```

x.get_plane_rotation() -> Rotator
Get Plane Rotation

Returns:
    Rotator:

<a id="unreal.AvaPlaneCutModifier.get_plane_origin"></a>

#### get_plane_origin

```python
def get_plane_origin() -> float
```

x.get_plane_origin() -> float
Get Plane Origin

Returns:
    float:

<a id="unreal.AvaPlaneCutModifier.get_invert_cut"></a>

#### get_invert_cut

```python
def get_invert_cut() -> bool
```

x.get_invert_cut() -> bool
Get Invert Cut

Returns:
    bool:

<a id="unreal.AvaPlaneCutModifier.get_fill_holes"></a>

#### get_fill_holes

```python
def get_fill_holes() -> bool
```

x.get_fill_holes() -> bool
Get Fill Holes

Returns:
    bool:

<a id="unreal.AvaRadialArrangeModifier"></a>