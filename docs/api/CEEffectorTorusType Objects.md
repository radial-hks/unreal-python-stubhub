## CEEffectorTorusType Objects

```python
class CEEffectorTorusType(CEEffectorBoundType)
```

CEEffector Torus Type

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEEffectorTorusType.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``easing`` (CEClonerEasing):  [Read-Write] Weight easing function applied to lerp transforms
- ``invert_type`` (bool):  [Read-Write] Invert the type effect, instead of affecting the inside of a zone, will affect the outside
- ``torus_inner_radius`` (float):  [Read-Write] Minimum revolved radius for the torus effect, clones contained inside will be affected with a maximum weight
- ``torus_outer_radius`` (float):  [Read-Write] Maximum revolved radius for the torus effect, clones outside of it will not be affected
- ``torus_radius`` (float):  [Read-Write] Main torus radius from center to the edge where inner and outer tube will be revolved

<a id="unreal.CEEffectorTorusType.set_torus_radius"></a>

#### set_torus_radius

```python
def set_torus_radius(radius: float) -> None
```

x.set_torus_radius(radius) -> None
Set Torus Radius

Args:
    radius (float):

<a id="unreal.CEEffectorTorusType.set_torus_outer_radius"></a>

#### set_torus_outer_radius

```python
def set_torus_outer_radius(radius: float) -> None
```

x.set_torus_outer_radius(radius) -> None
Set Torus Outer Radius

Args:
    radius (float):

<a id="unreal.CEEffectorTorusType.set_torus_inner_radius"></a>

#### set_torus_inner_radius

```python
def set_torus_inner_radius(radius: float) -> None
```

x.set_torus_inner_radius(radius) -> None
Set Torus Inner Radius

Args:
    radius (float):

<a id="unreal.CEEffectorTorusType.get_torus_radius"></a>

#### get_torus_radius

```python
def get_torus_radius() -> float
```

x.get_torus_radius() -> float
Get Torus Radius

Returns:
    float:

<a id="unreal.CEEffectorTorusType.get_torus_outer_radius"></a>

#### get_torus_outer_radius

```python
def get_torus_outer_radius() -> float
```

x.get_torus_outer_radius() -> float
Get Torus Outer Radius

Returns:
    float:

<a id="unreal.CEEffectorTorusType.get_torus_inner_radius"></a>

#### get_torus_inner_radius

```python
def get_torus_inner_radius() -> float
```

x.get_torus_inner_radius() -> float
Get Torus Inner Radius

Returns:
    float:

<a id="unreal.CEEffectorUnboundType"></a>