## CEEffectorRadialType Objects

```python
class CEEffectorRadialType(CEEffectorBoundType)
```

CEEffector Radial Type

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEEffectorRadialType.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``easing`` (CEClonerEasing):  [Read-Write] Weight easing function applied to lerp transforms
- ``invert_type`` (bool):  [Read-Write] Invert the type effect, instead of affecting the inside of a zone, will affect the outside
- ``radial_angle`` (float):  [Read-Write] Radial angle in degree, everything within the angle will be affected
- ``radial_max_radius`` (float):  [Read-Write] Maximum radius for the radial effect to be applied on clones, above clones will not be affected
- ``radial_min_radius`` (float):  [Read-Write] Minimum radius for the radial effect to be applied on clones, below clones will not be affected

<a id="unreal.CEEffectorRadialType.set_radial_min_radius"></a>

#### set_radial_min_radius

```python
def set_radial_min_radius(radius: float) -> None
```

x.set_radial_min_radius(radius) -> None
Set Radial Min Radius

Args:
    radius (float):

<a id="unreal.CEEffectorRadialType.set_radial_max_radius"></a>

#### set_radial_max_radius

```python
def set_radial_max_radius(radius: float) -> None
```

x.set_radial_max_radius(radius) -> None
Set Radial Max Radius

Args:
    radius (float):

<a id="unreal.CEEffectorRadialType.set_radial_angle"></a>

#### set_radial_angle

```python
def set_radial_angle(angle: float) -> None
```

x.set_radial_angle(angle) -> None
Set Radial Angle

Args:
    angle (float):

<a id="unreal.CEEffectorRadialType.get_radial_min_radius"></a>

#### get_radial_min_radius

```python
def get_radial_min_radius() -> float
```

x.get_radial_min_radius() -> float
Get Radial Min Radius

Returns:
    float:

<a id="unreal.CEEffectorRadialType.get_radial_max_radius"></a>

#### get_radial_max_radius

```python
def get_radial_max_radius() -> float
```

x.get_radial_max_radius() -> float
Get Radial Max Radius

Returns:
    float:

<a id="unreal.CEEffectorRadialType.get_radial_angle"></a>

#### get_radial_angle

```python
def get_radial_angle() -> float
```

x.get_radial_angle() -> float
Get Radial Angle

Returns:
    float:

<a id="unreal.CEEffectorSphereType"></a>