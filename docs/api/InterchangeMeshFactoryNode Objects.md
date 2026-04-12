## InterchangeMeshFactoryNode Objects

```python
class InterchangeMeshFactoryNode(InterchangeFactoryBaseNode)
```

namespace Interchange

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeFactoryNodes
- **File**: InterchangeMeshFactoryNode.h

<a id="unreal.InterchangeMeshFactoryNode.set_slot_material_dependency_uid"></a>

#### set\_slot\_material\_dependency\_uid

```python
def set_slot_material_dependency_uid(slot_name: str,
                                     material_dependency_uid: str) -> bool
```

x.set_slot_material_dependency_uid(slot_name, material_dependency_uid) -> bool
Add a Material dependency to the specified slot of this object.

Args:
    slot_name (str): 
    material_dependency_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeMeshFactoryNode.set_custom_vertex_color_replace"></a>

#### set\_custom\_vertex\_color\_replace

```python
def set_custom_vertex_color_replace(attribute_value: bool) -> bool
```

x.set_custom_vertex_color_replace(attribute_value) -> bool
Set whether the static mesh factory should replace the vertex color. Return false if the attribute could not be set.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMeshFactoryNode.set_custom_vertex_color_override"></a>

#### set\_custom\_vertex\_color\_override

```python
def set_custom_vertex_color_override(attribute_value: Color) -> bool
```

x.set_custom_vertex_color_override(attribute_value) -> bool
Set whether the static mesh factory should override the vertex color. Return false if the attribute could not be set.

Args:
    attribute_value (Color): 

Returns:
    bool:

<a id="unreal.InterchangeMeshFactoryNode.set_custom_vertex_color_ignore"></a>

#### set\_custom\_vertex\_color\_ignore

```python
def set_custom_vertex_color_ignore(attribute_value: bool) -> bool
```

x.set_custom_vertex_color_ignore(attribute_value) -> bool
Set whether the static mesh factory should ignore the vertex color. Return false if the attribute could not be set.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMeshFactoryNode.set_custom_use_mikk_t_space"></a>

#### set\_custom\_use\_mikk\_t\_space

```python
def set_custom_use_mikk_t_space(attribute_value: bool,
                                add_apply_delegate: bool = True) -> bool
```

x.set_custom_use_mikk_t_space(attribute_value, add_apply_delegate=True) -> bool
Set whether tangents are recomputed using MikkTSpace when they need to be recomputed.

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMeshFactoryNode.set_custom_use_high_precision_tangent_basis"></a>

#### set\_custom\_use\_high\_precision\_tangent\_basis

```python
def set_custom_use_high_precision_tangent_basis(attribute_value: bool,
                                                add_apply_delegate: bool = True
                                                ) -> bool
```

x.set_custom_use_high_precision_tangent_basis(attribute_value, add_apply_delegate=True) -> bool
Set whether tangents are stored at 16-bit precision instead of the default 8-bit precision.

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMeshFactoryNode.set_custom_use_full_precision_u_vs"></a>

#### set\_custom\_use\_full\_precision\_u\_vs

```python
def set_custom_use_full_precision_u_vs(attribute_value: bool,
                                       add_apply_delegate: bool = True
                                       ) -> bool
```

x.set_custom_use_full_precision_u_vs(attribute_value, add_apply_delegate=True) -> bool
Set whether UVs are stored at full floating point precision.

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMeshFactoryNode.set_custom_use_backwards_compatible_f16_trunc_u_vs"></a>

#### set\_custom\_use\_backwards\_compatible\_f16\_trunc\_u\_vs

```python
def set_custom_use_backwards_compatible_f16_trunc_u_vs(
        attribute_value: bool, add_apply_delegate: bool = True) -> bool
```

x.set_custom_use_backwards_compatible_f16_trunc_u_vs(attribute_value, add_apply_delegate=True) -> bool
Set whether UVs are converted to 16-bit by a legacy truncation process instead of the default rounding process. This may avoid differences when reimporting older content.

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMeshFactoryNode.set_custom_remove_degenerates"></a>

#### set\_custom\_remove\_degenerates

```python
def set_custom_remove_degenerates(attribute_value: bool,
                                  add_apply_delegate: bool = True) -> bool
```

x.set_custom_remove_degenerates(attribute_value, add_apply_delegate=True) -> bool
Set whether degenerate triangles are removed.

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMeshFactoryNode.set_custom_recompute_tangents"></a>

#### set\_custom\_recompute\_tangents

```python
def set_custom_recompute_tangents(attribute_value: bool,
                                  add_apply_delegate: bool = True) -> bool
```

x.set_custom_recompute_tangents(attribute_value, add_apply_delegate=True) -> bool
Set whether tangents in the imported mesh are ignored and recomputed.

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMeshFactoryNode.set_custom_recompute_normals"></a>

#### set\_custom\_recompute\_normals

```python
def set_custom_recompute_normals(attribute_value: bool,
                                 add_apply_delegate: bool = True) -> bool
```

x.set_custom_recompute_normals(attribute_value, add_apply_delegate=True) -> bool
Set whether normals in the imported mesh are ignored and recomputed. When normals are recomputed, the tangents are also recomputed.

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMeshFactoryNode.set_custom_lod_group"></a>

#### set\_custom\_lod\_group

```python
def set_custom_lod_group(attribute_value: Name,
                         add_apply_delegate: bool = True) -> bool
```

x.set_custom_lod_group(attribute_value, add_apply_delegate=True) -> bool
Set a custom LOD group for the mesh.

Args:
    attribute_value (Name): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMeshFactoryNode.set_custom_keep_sections_separate"></a>

#### set\_custom\_keep\_sections\_separate

```python
def set_custom_keep_sections_separate(attribute_value: bool) -> bool
```

x.set_custom_keep_sections_separate(attribute_value) -> bool
Set whether sections with matching materials are kept separate and will not get combined.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMeshFactoryNode.set_custom_compute_weighted_normals"></a>

#### set\_custom\_compute\_weighted\_normals

```python
def set_custom_compute_weighted_normals(attribute_value: bool,
                                        add_apply_delegate: bool = True
                                        ) -> bool
```

x.set_custom_compute_weighted_normals(attribute_value, add_apply_delegate=True) -> bool
Set whether normals are recomputed by weighting the surface area and the corner angle of the triangle as a ratio.

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMeshFactoryNode.reset_slot_material_dependencies"></a>

#### reset\_slot\_material\_dependencies

```python
def reset_slot_material_dependencies() -> bool
```

x.reset_slot_material_dependencies() -> bool
Reset all the material dependencies.

Returns:
    bool:

<a id="unreal.InterchangeMeshFactoryNode.remove_slot_material_dependency_uid"></a>

#### remove\_slot\_material\_dependency\_uid

```python
def remove_slot_material_dependency_uid(slot_name: str) -> bool
```

x.remove_slot_material_dependency_uid(slot_name) -> bool
Remove the Material dependency associated with the specfied slot name of this object.

Args:
    slot_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeMeshFactoryNode.remove_lod_data_unique_id"></a>

#### remove\_lod\_data\_unique\_id

```python
def remove_lod_data_unique_id(lod_data_unique_id: str) -> bool
```

x.remove_lod_data_unique_id(lod_data_unique_id) -> bool
Remove Lod Data Unique Id

Args:
    lod_data_unique_id (str): 

Returns:
    bool:

<a id="unreal.InterchangeMeshFactoryNode.get_slot_material_dependency_uid"></a>

#### get\_slot\_material\_dependency\_uid

```python
def get_slot_material_dependency_uid(slot_name: str) -> Optional[str]
```

x.get_slot_material_dependency_uid(slot_name) -> str or None
Retrieve the Material dependency for the specified slot of this object.

Args:
    slot_name (str): 

Returns:
    str or None: 

    out_material_dependency (str):

<a id="unreal.InterchangeMeshFactoryNode.get_slot_material_dependencies"></a>

#### get\_slot\_material\_dependencies

```python
def get_slot_material_dependencies() -> Map[str, str]
```

x.get_slot_material_dependencies() -> Map[str, str]
Retrieve the correspondence table between slot names and assigned materials for this object.

Returns:
    Map[str, str]: 

    out_material_dependencies (Map[str, str]):

<a id="unreal.InterchangeMeshFactoryNode.get_lod_data_unique_ids"></a>

#### get\_lod\_data\_unique\_ids

```python
def get_lod_data_unique_ids() -> Array[str]
```

x.get_lod_data_unique_ids() -> Array[str]
Get Lod Data Unique Ids

Returns:
    Array[str]: 

    out_lod_data_unique_ids (Array[str]):

<a id="unreal.InterchangeMeshFactoryNode.get_lod_data_count"></a>

#### get\_lod\_data\_count

```python
def get_lod_data_count() -> int
```

x.get_lod_data_count() -> int32
Return the number of LODs this static mesh has.

Returns:
    int32:

<a id="unreal.InterchangeMeshFactoryNode.get_custom_vertex_color_replace"></a>

#### get\_custom\_vertex\_color\_replace

```python
def get_custom_vertex_color_replace() -> Optional[bool]
```

x.get_custom_vertex_color_replace() -> bool or None
Query whether the static mesh factory should replace the vertex color. Return false if the attribute was not set.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeMeshFactoryNode.get_custom_vertex_color_override"></a>

#### get\_custom\_vertex\_color\_override

```python
def get_custom_vertex_color_override() -> Optional[Color]
```

x.get_custom_vertex_color_override() -> Color or None
Query whether the static mesh factory should override the vertex color. Return false if the attribute was not set.

Returns:
    Color or None: 

    attribute_value (Color):

<a id="unreal.InterchangeMeshFactoryNode.get_custom_vertex_color_ignore"></a>

#### get\_custom\_vertex\_color\_ignore

```python
def get_custom_vertex_color_ignore() -> Optional[bool]
```

x.get_custom_vertex_color_ignore() -> bool or None
Query whether the static mesh factory should ignore the vertex color. Return false if the attribute was not set.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeMeshFactoryNode.get_custom_use_mikk_t_space"></a>

#### get\_custom\_use\_mikk\_t\_space

```python
def get_custom_use_mikk_t_space() -> Optional[bool]
```

x.get_custom_use_mikk_t_space() -> bool or None
Query whether tangents are recomputed using MikkTSpace when they need to be recomputed.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeMeshFactoryNode.get_custom_use_high_precision_tangent_basis"></a>

#### get\_custom\_use\_high\_precision\_tangent\_basis

```python
def get_custom_use_high_precision_tangent_basis() -> Optional[bool]
```

x.get_custom_use_high_precision_tangent_basis() -> bool or None
Query whether tangents are stored at 16-bit precision instead of the default 8-bit precision.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeMeshFactoryNode.get_custom_use_full_precision_u_vs"></a>

#### get\_custom\_use\_full\_precision\_u\_vs

```python
def get_custom_use_full_precision_u_vs() -> Optional[bool]
```

x.get_custom_use_full_precision_u_vs() -> bool or None
Query whether UVs are stored at full floating point precision.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeMeshFactoryNode.get_custom_use_backwards_compatible_f16_trunc_u_vs"></a>

#### get\_custom\_use\_backwards\_compatible\_f16\_trunc\_u\_vs

```python
def get_custom_use_backwards_compatible_f16_trunc_u_vs() -> Optional[bool]
```

x.get_custom_use_backwards_compatible_f16_trunc_u_vs() -> bool or None
Query whether UVs are converted to 16-bit by a legacy truncation process instead of the default rounding process. This may avoid differences when reimporting older content.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeMeshFactoryNode.get_custom_remove_degenerates"></a>

#### get\_custom\_remove\_degenerates

```python
def get_custom_remove_degenerates() -> Optional[bool]
```

x.get_custom_remove_degenerates() -> bool or None
Query whether degenerate triangles are removed.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeMeshFactoryNode.get_custom_recompute_tangents"></a>

#### get\_custom\_recompute\_tangents

```python
def get_custom_recompute_tangents() -> Optional[bool]
```

x.get_custom_recompute_tangents() -> bool or None
Query whether tangents in the imported mesh are ignored and recomputed.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeMeshFactoryNode.get_custom_recompute_normals"></a>

#### get\_custom\_recompute\_normals

```python
def get_custom_recompute_normals() -> Optional[bool]
```

x.get_custom_recompute_normals() -> bool or None
Query whether normals in the imported mesh are ignored and recomputed. When normals are recomputed, the tangents are also recomputed.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeMeshFactoryNode.get_custom_lod_group"></a>

#### get\_custom\_lod\_group

```python
def get_custom_lod_group() -> Optional[Name]
```

x.get_custom_lod_group() -> Name or None
Query whether a custom LOD group is set for the mesh.

Returns:
    Name or None: 

    attribute_value (Name):

<a id="unreal.InterchangeMeshFactoryNode.get_custom_keep_sections_separate"></a>

#### get\_custom\_keep\_sections\_separate

```python
def get_custom_keep_sections_separate() -> Optional[bool]
```

x.get_custom_keep_sections_separate() -> bool or None
Query whether sections with matching materials are kept separate and will not get combined.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeMeshFactoryNode.get_custom_compute_weighted_normals"></a>

#### get\_custom\_compute\_weighted\_normals

```python
def get_custom_compute_weighted_normals() -> Optional[bool]
```

x.get_custom_compute_weighted_normals() -> bool or None
Query whether normals are recomputed by weighting the surface area and the corner angle of the triangle as a ratio.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeMeshFactoryNode.add_lod_data_unique_id"></a>

#### add\_lod\_data\_unique\_id

```python
def add_lod_data_unique_id(lod_data_unique_id: str) -> bool
```

x.add_lod_data_unique_id(lod_data_unique_id) -> bool
Add Lod Data Unique Id

Args:
    lod_data_unique_id (str): 

Returns:
    bool:

<a id="unreal.InterchangeSceneImportAssetFactoryNode"></a>