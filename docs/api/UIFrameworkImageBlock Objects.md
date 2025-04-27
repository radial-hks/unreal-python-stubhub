## UIFrameworkImageBlock Objects

```python
class UIFrameworkImageBlock(UIFrameworkWidget)
```

UIFramework Image Block

**C++ Source:**

- **Plugin**: UIFramework
- **Module**: UIFramework
- **File**: UIFImageBlock.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_enabled`` (bool):  [Read-Write]
- ``visibility`` (SlateVisibility):  [Read-Write]
- ``widget_class`` (Class):  [Read-Write]

<a id="unreal.UIFrameworkImageBlock.set_tint"></a>

#### set_tint

```python
def set_tint(tint: LinearColor) -> None
```

x.set_tint(tint) -> None
Set Tint

Args:
    tint (LinearColor):

<a id="unreal.UIFrameworkImageBlock.set_tiling"></a>

#### set_tiling

```python
def set_tiling(overflow_policy: SlateBrushTileType) -> None
```

x.set_tiling(overflow_policy) -> None
Set Tiling

Args:
    overflow_policy (SlateBrushTileType):

<a id="unreal.UIFrameworkImageBlock.set_texture"></a>

#### set_texture

```python
def set_texture(texture: Texture2D, use_texture_size: bool) -> None
```

x.set_texture(texture, use_texture_size) -> None
Set Texture

Args:
    texture (Texture2D): 
    use_texture_size (bool):

<a id="unreal.UIFrameworkImageBlock.set_material"></a>

#### set_material

```python
def set_material(material: MaterialInterface) -> None
```

x.set_material(material) -> None
Set Material

Args:
    material (MaterialInterface):

<a id="unreal.UIFrameworkImageBlock.set_desired_size"></a>

#### set_desired_size

```python
def set_desired_size(desired_size: Vector2f) -> None
```

x.set_desired_size(desired_size) -> None
Set Desired Size

Args:
    desired_size (Vector2f):

<a id="unreal.UIFrameworkImageBlock.get_tint"></a>

#### get_tint

```python
def get_tint() -> LinearColor
```

x.get_tint() -> LinearColor
Get Tint

Returns:
    LinearColor:

<a id="unreal.UIFrameworkImageBlock.get_tiling"></a>

#### get_tiling

```python
def get_tiling() -> SlateBrushTileType
```

x.get_tiling() -> SlateBrushTileType
Get Tiling

Returns:
    SlateBrushTileType:

<a id="unreal.UIFrameworkImageBlock.get_desired_size"></a>

#### get_desired_size

```python
def get_desired_size() -> Vector2f
```

x.get_desired_size() -> Vector2f
Get Desired Size

Returns:
    Vector2f:

<a id="unreal.UIFrameworkImageBlock.ge_resource_object"></a>

#### ge_resource_object

```python
def ge_resource_object() -> Object
```

x.ge_resource_object() -> Object
Ge Resource Object

Returns:
    Object:

<a id="unreal.UIFrameworkOverlay"></a>