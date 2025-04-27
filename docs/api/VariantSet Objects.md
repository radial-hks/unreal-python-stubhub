## VariantSet Objects

```python
class VariantSet(Object)
```

Variant Set

**C++ Source:**

- **Plugin**: VariantManagerContent
- **Module**: VariantManagerContent
- **File**: VariantSet.h

<a id="unreal.VariantSet.set_thumbnail_from_texture"></a>

#### set_thumbnail_from_texture

```python
def set_thumbnail_from_texture(new_thumbnail: Texture2D) -> None
```

x.set_thumbnail_from_texture(new_thumbnail) -> None
Sets the thumbnail to use for this variant set. Can receive nullptr to clear it

Args:
    new_thumbnail (Texture2D):

<a id="unreal.VariantSet.set_thumbnail_from_file"></a>

#### set_thumbnail_from_file

```python
def set_thumbnail_from_file(file_path: str) -> None
```

x.set_thumbnail_from_file(file_path) -> None
Set Thumbnail from File

Args:
    file_path (str):

<a id="unreal.VariantSet.set_thumbnail_from_editor_viewport"></a>

#### set_thumbnail_from_editor_viewport

```python
def set_thumbnail_from_editor_viewport() -> None
```

x.set_thumbnail_from_editor_viewport() -> None
Sets the thumbnail from the active editor viewport. Doesn't do anything if the Editor is not available

<a id="unreal.VariantSet.set_thumbnail_from_camera"></a>

#### set_thumbnail_from_camera

```python
def set_thumbnail_from_camera(world_context_object: Object,
                              camera_transform: Transform,
                              fov_degrees: float = 50.000000,
                              min_z: float = 50.000000,
                              gamma: float = 2.200000) -> None
```

x.set_thumbnail_from_camera(world_context_object, camera_transform, fov_degrees=50.000000, min_z=50.000000, gamma=2.200000) -> None
Set Thumbnail from Camera

Args:
    world_context_object (Object): 
    camera_transform (Transform): 
    fov_degrees (float): 
    min_z (float): 
    gamma (float):

<a id="unreal.VariantSet.set_display_text"></a>

#### set_display_text

```python
def set_display_text(new_display_text: Text) -> None
```

x.set_display_text(new_display_text) -> None
Set Display Text

Args:
    new_display_text (Text):

<a id="unreal.VariantSet.get_variant_by_name"></a>

#### get_variant_by_name

```python
def get_variant_by_name(variant_name: str) -> Variant
```

x.get_variant_by_name(variant_name) -> Variant
Get Variant by Name

Args:
    variant_name (str): 

Returns:
    Variant:

<a id="unreal.VariantSet.get_variant"></a>

#### get_variant

```python
def get_variant(variant_index: int) -> Variant
```

x.get_variant(variant_index) -> Variant
Get Variant

Args:
    variant_index (int32): 

Returns:
    Variant:

<a id="unreal.VariantSet.get_thumbnail"></a>

#### get_thumbnail

```python
def get_thumbnail() -> Texture2D
```

x.get_thumbnail() -> Texture2D
Gets the thumbnail currently used for this variant set

Returns:
    Texture2D:

<a id="unreal.VariantSet.get_parent"></a>

#### get_parent

```python
def get_parent() -> LevelVariantSets
```

x.get_parent() -> LevelVariantSets
Get Parent

Returns:
    LevelVariantSets:

<a id="unreal.VariantSet.get_num_variants"></a>

#### get_num_variants

```python
def get_num_variants() -> int
```

x.get_num_variants() -> int32
Get Num Variants

Returns:
    int32:

<a id="unreal.VariantSet.get_display_text"></a>

#### get_display_text

```python
def get_display_text() -> Text
```

x.get_display_text() -> Text
Get Display Text

Returns:
    Text:

<a id="unreal.VariantSet.remove_variant_by_name"></a>

#### remove_variant_by_name

```python
def remove_variant_by_name(variant_name: str) -> None
```

x.remove_variant_by_name(variant_name) -> None
Looks for a variant with VariantName within VariantSet and removes it, if it exists

Args:
    variant_name (str):

<a id="unreal.VariantSet.remove_variant"></a>

#### remove_variant

```python
def remove_variant(variant: Variant) -> None
```

x.remove_variant(variant) -> None
Removes Variant from VariantSet, if that is its parent

Args:
    variant (Variant):

<a id="unreal.VariantSet.add_variant"></a>

#### add_variant

```python
def add_variant(variant: Variant) -> None
```

x.add_variant(variant) -> None
Adds Variant to the VariantSet's list of Variants

Args:
    variant (Variant):

<a id="unreal.DatasmithAreaLightActor"></a>