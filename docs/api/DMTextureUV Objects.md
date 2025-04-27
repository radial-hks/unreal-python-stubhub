## DMTextureUV Objects

```python
class DMTextureUV(DMMaterialLinkedComponent)
```

* Represents a Texture UV material function with the following parameters: offset, tiling, pivot and rotation.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMTextureUV.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cached_parameter_names`` (Map[int32, Name]):  [Read-Only]
- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``exposed_parameters`` (Set[int32]):  [Read-Only]
- ``link_tiling`` (bool):  [Read-Write]
- ``material_parameters`` (Map[int32, DMMaterialParameter]):  [Read-Only]
- ``mirror_on_x`` (bool):  [Read-Write] Forces a material rebuild.
- ``mirror_on_y`` (bool):  [Read-Write] Forces a material rebuild.
- ``offset`` (Vector2D):  [Read-Write]
- ``pivot`` (Vector2D):  [Read-Write] Pivot for rotation and tiling.
- ``rotation`` (float):  [Read-Write]
- ``tiling`` (Vector2D):  [Read-Write]
- ``uv_source`` (DMUVSource):  [Read-Write] Forces a material rebuild.

<a id="unreal.DMTextureUV.link_tiling"></a>

#### link_tiling

```python
@property
def link_tiling() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DMTextureUV.link_tiling"></a>

#### link_tiling

```python
@link_tiling.setter
def link_tiling(value: bool) -> None
```

<a id="unreal.DMTextureUV.uv_source"></a>

#### uv_source

```python
@property
def uv_source() -> DMUVSource
```

(DMUVSource):  [Read-Write] Forces a material rebuild.

<a id="unreal.DMTextureUV.uv_source"></a>

#### uv_source

```python
@uv_source.setter
def uv_source(value: DMUVSource) -> None
```

<a id="unreal.DMTextureUV.offset"></a>

#### offset

```python
@property
def offset() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.DMTextureUV.offset"></a>

#### offset

```python
@offset.setter
def offset(value: Vector2D) -> None
```

<a id="unreal.DMTextureUV.pivot"></a>

#### pivot

```python
@property
def pivot() -> Vector2D
```

(Vector2D):  [Read-Write] Pivot for rotation and tiling.

<a id="unreal.DMTextureUV.pivot"></a>

#### pivot

```python
@pivot.setter
def pivot(value: Vector2D) -> None
```

<a id="unreal.DMTextureUV.rotation"></a>

#### rotation

```python
@property
def rotation() -> float
```

(float):  [Read-Write]

<a id="unreal.DMTextureUV.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: float) -> None
```

<a id="unreal.DMTextureUV.tiling"></a>

#### tiling

```python
@property
def tiling() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.DMTextureUV.tiling"></a>

#### tiling

```python
@tiling.setter
def tiling(value: Vector2D) -> None
```

<a id="unreal.DMTextureUV.mirror_on_x"></a>

#### mirror_on_x

```python
@property
def mirror_on_x() -> bool
```

(bool):  [Read-Write] Forces a material rebuild.

<a id="unreal.DMTextureUV.mirror_on_x"></a>

#### mirror_on_x

```python
@mirror_on_x.setter
def mirror_on_x(value: bool) -> None
```

<a id="unreal.DMTextureUV.mirror_on_y"></a>

#### mirror_on_y

```python
@property
def mirror_on_y() -> bool
```

(bool):  [Read-Write] Forces a material rebuild.

<a id="unreal.DMTextureUV.mirror_on_y"></a>

#### mirror_on_y

```python
@mirror_on_y.setter
def mirror_on_y(value: bool) -> None
```

<a id="unreal.DMTextureUV.material_parameters"></a>

#### material_parameters

```python
@property
def material_parameters() -> Map[int, DMMaterialParameter]
```

(Map[int32, DMMaterialParameter]):  [Read-Only]

<a id="unreal.DMTextureUV.cached_parameter_names"></a>

#### cached_parameter_names

```python
@property
def cached_parameter_names() -> Map[int, Name]
```

(Map[int32, Name]):  [Read-Only]

<a id="unreal.DMTextureUV.exposed_parameters"></a>

#### exposed_parameters

```python
@property
def exposed_parameters() -> Set[int]
```

(Set[int32]):  [Read-Only]

<a id="unreal.DMTextureUV.set_uv_source"></a>

#### set_uv_source

```python
def set_uv_source(uv_source: DMUVSource) -> None
```

x.set_uv_source(uv_source) -> None
Set UVSource

Args:
    uv_source (DMUVSource):

<a id="unreal.DMTextureUV.set_tiling"></a>

#### set_tiling

```python
def set_tiling(tiling: Vector2D) -> None
```

x.set_tiling(tiling) -> None
Set Tiling

Args:
    tiling (Vector2D):

<a id="unreal.DMTextureUV.set_should_expose_parameter"></a>

#### set_should_expose_parameter

```python
def set_should_expose_parameter(property_name: Name, component: int,
                                expose: bool) -> None
```

x.set_should_expose_parameter(property_name, component, expose) -> None
Set Should Expose Parameter

Args:
    property_name (Name): 
    component (int32): 
    expose (bool):

<a id="unreal.DMTextureUV.set_rotation"></a>

#### set_rotation

```python
def set_rotation(rotation: float) -> None
```

x.set_rotation(rotation) -> None
Set Rotation

Args:
    rotation (float):

<a id="unreal.DMTextureUV.set_pivot"></a>

#### set_pivot

```python
def set_pivot(pivot: Vector2D) -> None
```

x.set_pivot(pivot) -> None
Set Pivot

Args:
    pivot (Vector2D):

<a id="unreal.DMTextureUV.set_offset"></a>

#### set_offset

```python
def set_offset(offset: Vector2D) -> None
```

x.set_offset(offset) -> None
Set Offset

Args:
    offset (Vector2D):

<a id="unreal.DMTextureUV.set_mirror_on_y"></a>

#### set_mirror_on_y

```python
def set_mirror_on_y(mirror_on_y: bool) -> None
```

x.set_mirror_on_y(mirror_on_y) -> None
Set Mirror on Y

Args:
    mirror_on_y (bool):

<a id="unreal.DMTextureUV.set_mirror_on_x"></a>

#### set_mirror_on_x

```python
def set_mirror_on_x(mirror_on_x: bool) -> None
```

x.set_mirror_on_x(mirror_on_x) -> None
Set Mirror on X

Args:
    mirror_on_x (bool):

<a id="unreal.DMTextureUV.set_material_parameter_name"></a>

#### set_material_parameter_name

```python
def set_material_parameter_name(property_name: Name, component: int,
                                new_name: Name) -> bool
```

x.set_material_parameter_name(property_name, component, new_name) -> bool
Set Material Parameter Name

Args:
    property_name (Name): 
    component (int32): 
    new_name (Name): 

Returns:
    bool:

<a id="unreal.DMTextureUV.get_uv_source"></a>

#### get_uv_source

```python
def get_uv_source() -> DMUVSource
```

x.get_uv_source() -> DMUVSource
Get UVSource

Returns:
    DMUVSource:

<a id="unreal.DMTextureUV.get_tiling"></a>

#### get_tiling

```python
def get_tiling() -> Vector2D
```

x.get_tiling() -> Vector2D
Get Tiling

Returns:
    Vector2D:

<a id="unreal.DMTextureUV.get_should_expose_parameter"></a>

#### get_should_expose_parameter

```python
def get_should_expose_parameter(property_name: Name, component: int) -> bool
```

x.get_should_expose_parameter(property_name, component) -> bool
Get Should Expose Parameter

Args:
    property_name (Name): 
    component (int32): 

Returns:
    bool:

<a id="unreal.DMTextureUV.get_rotation"></a>

#### get_rotation

```python
def get_rotation() -> float
```

x.get_rotation() -> float
Get Rotation

Returns:
    float:

<a id="unreal.DMTextureUV.get_pivot"></a>

#### get_pivot

```python
def get_pivot() -> Vector2D
```

x.get_pivot() -> Vector2D
Get Pivot

Returns:
    Vector2D:

<a id="unreal.DMTextureUV.get_parameters"></a>

#### get_parameters

```python
def get_parameters() -> Array[DMMaterialParameter]
```

x.get_parameters() -> Array[DMMaterialParameter]
Get Parameters

Returns:
    Array[DMMaterialParameter]:

<a id="unreal.DMTextureUV.get_offset"></a>

#### get_offset

```python
def get_offset() -> Vector2D
```

x.get_offset() -> Vector2D
Get Offset

Returns:
    Vector2D:

<a id="unreal.DMTextureUV.get_mirror_on_y"></a>

#### get_mirror_on_y

```python
def get_mirror_on_y() -> bool
```

x.get_mirror_on_y() -> bool
Get Mirror on Y

Returns:
    bool:

<a id="unreal.DMTextureUV.get_mirror_on_x"></a>

#### get_mirror_on_x

```python
def get_mirror_on_x() -> bool
```

x.get_mirror_on_x() -> bool
Get Mirror on X

Returns:
    bool:

<a id="unreal.DMTextureUV.get_material_parameter_name"></a>

#### get_material_parameter_name

```python
def get_material_parameter_name(property_name: Name, component: int) -> Name
```

x.get_material_parameter_name(property_name, component) -> Name
Get Material Parameter Name

Args:
    property_name (Name): 
    component (int32): 

Returns:
    Name:

<a id="unreal.DMTextureUV.get_material_parameter"></a>

#### get_material_parameter

```python
def get_material_parameter(property_name: Name,
                           component: int) -> DMMaterialParameter
```

x.get_material_parameter(property_name, component) -> DMMaterialParameter
Get Material Parameter

Args:
    property_name (Name): 
    component (int32): 

Returns:
    DMMaterialParameter:

<a id="unreal.DMTextureUV.get_material_model"></a>

#### get_material_model

```python
def get_material_model() -> DynamicMaterialModel
```

x.get_material_model() -> DynamicMaterialModel
Get Material Model

Returns:
    DynamicMaterialModel:

<a id="unreal.DMTextureUV.create_texture_uv"></a>

#### create_texture_uv

```python
@classmethod
def create_texture_uv(cls, outer: Object) -> DMTextureUV
```

X.create_texture_uv(outer) -> DMTextureUV
Create Texture UV

Args:
    outer (Object): 

Returns:
    DMTextureUV:

<a id="unreal.DMTextureUVDynamic"></a>