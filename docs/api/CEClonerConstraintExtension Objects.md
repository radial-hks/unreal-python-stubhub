## CEClonerConstraintExtension Objects

```python
class CEClonerConstraintExtension(CEClonerExtensionBase)
```

Extension dealing with clone grid constraints

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEClonerConstraintExtension.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``constraint`` (CEClonerGridConstraint):  [Read-Write]
- ``cylinder_center`` (Vector):  [Read-Write]
- ``cylinder_height`` (float):  [Read-Write]
- ``cylinder_radius`` (float):  [Read-Write] Cylinder constraint
- ``invert_constraint`` (bool):  [Read-Write]
- ``sphere_center`` (Vector):  [Read-Write]
- ``sphere_radius`` (float):  [Read-Write] Sphere constraint
- ``texture_asset`` (Texture):  [Read-Write] Texture constraint
- ``texture_compare_mode`` (CEClonerCompareMode):  [Read-Write]
- ``texture_plane`` (CEClonerPlane):  [Read-Write]
- ``texture_sample_mode`` (CEClonerTextureSampleChannel):  [Read-Write]
- ``texture_threshold`` (float):  [Read-Write]

<a id="unreal.CEClonerConstraintExtension.set_texture_threshold"></a>

#### set_texture_threshold

```python
def set_texture_threshold(threshold: float) -> None
```

x.set_texture_threshold(threshold) -> None
Set Texture Threshold

Args:
    threshold (float):

<a id="unreal.CEClonerConstraintExtension.set_texture_sample_mode"></a>

#### set_texture_sample_mode

```python
def set_texture_sample_mode(sample_mode: CEClonerTextureSampleChannel) -> None
```

x.set_texture_sample_mode(sample_mode) -> None
Set Texture Sample Mode

Args:
    sample_mode (CEClonerTextureSampleChannel):

<a id="unreal.CEClonerConstraintExtension.set_texture_plane"></a>

#### set_texture_plane

```python
def set_texture_plane(plane: CEClonerPlane) -> None
```

x.set_texture_plane(plane) -> None
Set Texture Plane

Args:
    plane (CEClonerPlane):

<a id="unreal.CEClonerConstraintExtension.set_texture_compare_mode"></a>

#### set_texture_compare_mode

```python
def set_texture_compare_mode(mode: CEClonerCompareMode) -> None
```

x.set_texture_compare_mode(mode) -> None
Set Texture Compare Mode

Args:
    mode (CEClonerCompareMode):

<a id="unreal.CEClonerConstraintExtension.set_texture_asset"></a>

#### set_texture_asset

```python
def set_texture_asset(texture: Texture) -> None
```

x.set_texture_asset(texture) -> None
Set Texture Asset

Args:
    texture (Texture):

<a id="unreal.CEClonerConstraintExtension.set_sphere_radius"></a>

#### set_sphere_radius

```python
def set_sphere_radius(sphere_radius: float) -> None
```

x.set_sphere_radius(sphere_radius) -> None
Set Sphere Radius

Args:
    sphere_radius (float):

<a id="unreal.CEClonerConstraintExtension.set_sphere_center"></a>

#### set_sphere_center

```python
def set_sphere_center(sphere_center: Vector) -> None
```

x.set_sphere_center(sphere_center) -> None
Set Sphere Center

Args:
    sphere_center (Vector):

<a id="unreal.CEClonerConstraintExtension.set_invert_constraint"></a>

#### set_invert_constraint

```python
def set_invert_constraint(invert_constraint: bool) -> None
```

x.set_invert_constraint(invert_constraint) -> None
Set Invert Constraint

Args:
    invert_constraint (bool):

<a id="unreal.CEClonerConstraintExtension.set_cylinder_radius"></a>

#### set_cylinder_radius

```python
def set_cylinder_radius(cylinder_radius: float) -> None
```

x.set_cylinder_radius(cylinder_radius) -> None
Set Cylinder Radius

Args:
    cylinder_radius (float):

<a id="unreal.CEClonerConstraintExtension.set_cylinder_height"></a>

#### set_cylinder_height

```python
def set_cylinder_height(cylinder_height: float) -> None
```

x.set_cylinder_height(cylinder_height) -> None
Set Cylinder Height

Args:
    cylinder_height (float):

<a id="unreal.CEClonerConstraintExtension.set_cylinder_center"></a>

#### set_cylinder_center

```python
def set_cylinder_center(cylinder_center: Vector) -> None
```

x.set_cylinder_center(cylinder_center) -> None
Set Cylinder Center

Args:
    cylinder_center (Vector):

<a id="unreal.CEClonerConstraintExtension.set_constraint"></a>

#### set_constraint

```python
def set_constraint(constraint: CEClonerGridConstraint) -> None
```

x.set_constraint(constraint) -> None
Set Constraint

Args:
    constraint (CEClonerGridConstraint):

<a id="unreal.CEClonerConstraintExtension.get_texture_threshold"></a>

#### get_texture_threshold

```python
def get_texture_threshold() -> float
```

x.get_texture_threshold() -> float
Get Texture Threshold

Returns:
    float:

<a id="unreal.CEClonerConstraintExtension.get_texture_sample_mode"></a>

#### get_texture_sample_mode

```python
def get_texture_sample_mode() -> CEClonerTextureSampleChannel
```

x.get_texture_sample_mode() -> CEClonerTextureSampleChannel
Get Texture Sample Mode

Returns:
    CEClonerTextureSampleChannel:

<a id="unreal.CEClonerConstraintExtension.get_texture_plane"></a>

#### get_texture_plane

```python
def get_texture_plane() -> CEClonerPlane
```

x.get_texture_plane() -> CEClonerPlane
Get Texture Plane

Returns:
    CEClonerPlane:

<a id="unreal.CEClonerConstraintExtension.get_texture_compare_mode"></a>

#### get_texture_compare_mode

```python
def get_texture_compare_mode() -> CEClonerCompareMode
```

x.get_texture_compare_mode() -> CEClonerCompareMode
Get Texture Compare Mode

Returns:
    CEClonerCompareMode:

<a id="unreal.CEClonerConstraintExtension.get_texture_asset"></a>

#### get_texture_asset

```python
def get_texture_asset() -> Texture
```

x.get_texture_asset() -> Texture
Get Texture Asset

Returns:
    Texture:

<a id="unreal.CEClonerConstraintExtension.get_sphere_radius"></a>

#### get_sphere_radius

```python
def get_sphere_radius() -> float
```

x.get_sphere_radius() -> float
Get Sphere Radius

Returns:
    float:

<a id="unreal.CEClonerConstraintExtension.get_sphere_center"></a>

#### get_sphere_center

```python
def get_sphere_center() -> Vector
```

x.get_sphere_center() -> Vector
Get Sphere Center

Returns:
    Vector:

<a id="unreal.CEClonerConstraintExtension.get_invert_constraint"></a>

#### get_invert_constraint

```python
def get_invert_constraint() -> bool
```

x.get_invert_constraint() -> bool
Get Invert Constraint

Returns:
    bool:

<a id="unreal.CEClonerConstraintExtension.get_cylinder_radius"></a>

#### get_cylinder_radius

```python
def get_cylinder_radius() -> float
```

x.get_cylinder_radius() -> float
Get Cylinder Radius

Returns:
    float:

<a id="unreal.CEClonerConstraintExtension.get_cylinder_height"></a>

#### get_cylinder_height

```python
def get_cylinder_height() -> float
```

x.get_cylinder_height() -> float
Get Cylinder Height

Returns:
    float:

<a id="unreal.CEClonerConstraintExtension.get_cylinder_center"></a>

#### get_cylinder_center

```python
def get_cylinder_center() -> Vector
```

x.get_cylinder_center() -> Vector
Get Cylinder Center

Returns:
    Vector:

<a id="unreal.CEClonerConstraintExtension.get_constraint"></a>

#### get_constraint

```python
def get_constraint() -> CEClonerGridConstraint
```

x.get_constraint() -> CEClonerGridConstraint
Get Constraint

Returns:
    CEClonerGridConstraint:

<a id="unreal.CEClonerCylinderLayout"></a>