## CEEffectorPlaneType Objects

```python
class CEEffectorPlaneType(CEEffectorBoundType)
```

CEEffector Plane Type

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEEffectorPlaneType.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``easing`` (CEClonerEasing):  [Read-Write] Weight easing function applied to lerp transforms
- ``invert_type`` (bool):  [Read-Write] Invert the type effect, instead of affecting the inside of a zone, will affect the outside
- ``plane_spacing`` (float):  [Read-Write] Plane spacing, everything inside this zone will be affected

<a id="unreal.CEEffectorPlaneType.set_plane_spacing"></a>

#### set_plane_spacing

```python
def set_plane_spacing(spacing: float) -> None
```

x.set_plane_spacing(spacing) -> None
Set Plane Spacing

Args:
    spacing (float):

<a id="unreal.CEEffectorPlaneType.get_plane_spacing"></a>

#### get_plane_spacing

```python
def get_plane_spacing() -> float
```

x.get_plane_spacing() -> float
Get Plane Spacing

Returns:
    float:

<a id="unreal.CEEffectorPushMode"></a>