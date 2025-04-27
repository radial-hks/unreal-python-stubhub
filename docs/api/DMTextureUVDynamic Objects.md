## DMTextureUVDynamic Objects

```python
class DMTextureUVDynamic(DMMaterialComponentDynamic)
```

A texture uv used inside a instanced material instance. Links to the original texture uv in the parent material.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMTextureUVDynamic.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``offset`` (Vector2D):  [Read-Write]
- ``parent_component_name`` (Name):  [Read-Only]
- ``pivot`` (Vector2D):  [Read-Write] Pivot for rotation and tiling.
- ``rotation`` (float):  [Read-Write]
- ``tiling`` (Vector2D):  [Read-Write]

<a id="unreal.DMTextureUVDynamic.offset"></a>

#### offset

```python
@property
def offset() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.DMTextureUVDynamic.offset"></a>

#### offset

```python
@offset.setter
def offset(value: Vector2D) -> None
```

<a id="unreal.DMTextureUVDynamic.pivot"></a>

#### pivot

```python
@property
def pivot() -> Vector2D
```

(Vector2D):  [Read-Write] Pivot for rotation and tiling.

<a id="unreal.DMTextureUVDynamic.pivot"></a>

#### pivot

```python
@pivot.setter
def pivot(value: Vector2D) -> None
```

<a id="unreal.DMTextureUVDynamic.rotation"></a>

#### rotation

```python
@property
def rotation() -> float
```

(float):  [Read-Write]

<a id="unreal.DMTextureUVDynamic.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: float) -> None
```

<a id="unreal.DMTextureUVDynamic.tiling"></a>

#### tiling

```python
@property
def tiling() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.DMTextureUVDynamic.tiling"></a>

#### tiling

```python
@tiling.setter
def tiling(value: Vector2D) -> None
```

<a id="unreal.DMTextureUVDynamic.set_tiling"></a>

#### set_tiling

```python
def set_tiling(tiling: Vector2D) -> None
```

x.set_tiling(tiling) -> None
Sets the dynamic value for this property.

Args:
    tiling (Vector2D):

<a id="unreal.DMTextureUVDynamic.set_rotation"></a>

#### set_rotation

```python
def set_rotation(rotation: float) -> None
```

x.set_rotation(rotation) -> None
Sets the dynamic value for this property.

Args:
    rotation (float):

<a id="unreal.DMTextureUVDynamic.set_pivot"></a>

#### set_pivot

```python
def set_pivot(pivot: Vector2D) -> None
```

x.set_pivot(pivot) -> None
Sets the dynamic value for this property.

Args:
    pivot (Vector2D):

<a id="unreal.DMTextureUVDynamic.set_offset"></a>

#### set_offset

```python
def set_offset(offset: Vector2D) -> None
```

x.set_offset(offset) -> None
Sets the dynamic value for this property.

Args:
    offset (Vector2D):

<a id="unreal.DMTextureUVDynamic.get_tiling"></a>

#### get_tiling

```python
def get_tiling() -> Vector2D
```

x.get_tiling() -> Vector2D
Returns the dynamic value for this property.

Returns:
    Vector2D:

<a id="unreal.DMTextureUVDynamic.get_rotation"></a>

#### get_rotation

```python
def get_rotation() -> float
```

x.get_rotation() -> float
Returns the dynamic value for this property.

Returns:
    float:

<a id="unreal.DMTextureUVDynamic.get_pivot"></a>

#### get_pivot

```python
def get_pivot() -> Vector2D
```

x.get_pivot() -> Vector2D
Returns the dynamic value for this property.

Returns:
    Vector2D:

<a id="unreal.DMTextureUVDynamic.get_parent_texture_uv"></a>

#### get_parent_texture_uv

```python
def get_parent_texture_uv() -> DMTextureUV
```

x.get_parent_texture_uv() -> DMTextureUV
Resolves and returns the parent texture uv from the parent model.

Returns:
    DMTextureUV:

<a id="unreal.DMTextureUVDynamic.get_offset"></a>

#### get_offset

```python
def get_offset() -> Vector2D
```

x.get_offset() -> Vector2D
Returns the dynamic value for this property.

Returns:
    Vector2D:

<a id="unreal.DMValueDefinitionLibrary"></a>