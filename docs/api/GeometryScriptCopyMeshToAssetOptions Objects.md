## GeometryScriptCopyMeshToAssetOptions Objects

```python
class GeometryScriptCopyMeshToAssetOptions(StructBase)
```

Geometry Script Copy Mesh to Asset Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshAssetFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_nanite_settings`` (bool):  [Read-Write] If enabled, NaniteSettings will be applied to the target Asset if possible
- ``defer_mesh_post_edit_change`` (bool):  [Read-Write]
- ``emit_transaction`` (bool):  [Read-Write]
- ``enable_recompute_normals`` (bool):  [Read-Write]
- ``enable_recompute_tangents`` (bool):  [Read-Write]
- ``enable_remove_degenerates`` (bool):  [Read-Write]
- ``nanite_settings`` (GeometryScriptNaniteOptions):  [Read-Write] Replaced FGeometryScriptNaniteOptions with usage of Engine FMeshNaniteSettings
- ``new_material_slot_names`` (Array[Name]):  [Read-Write] Optional slot names for the New Materials. Ignored if not the same length as the New Materials array.
- ``new_materials`` (Array[MaterialInterface]):  [Read-Write] New materials to set if Replace Materials is enabled. Ignored otherwise.
- ``new_nanite_settings`` (MeshNaniteSettings):  [Read-Write] Nanite Settings applied to the target Asset, if bApplyNaniteSettings = true
- ``remap_bone_indices_to_match_asset`` (bool):  [Read-Write] Remap the bone indices to match the asset. This requires the source mesh to have bone information present. If no bone information is present
  then all bone weights are mapped to the root.
- ``replace_materials`` (bool):  [Read-Write] Whether to replace the materials on the asset with those in the New Materials array
- ``use_build_scale`` (bool):  [Read-Write] Whether to use the build scale on the target asset. If enabled, the inverse scale will be applied when saving to the asset, and the BuildScale will be preserved. Otherwise, BuildScale will be set to 1.0 on the asset BuildSettings.
- ``use_original_vertex_order`` (bool):  [Read-Write] Use the original vertex order found in the source data. This is useful if the inbound mesh was originally non-manifold, and needs to keep
  the non-manifold structure when re-created.

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.__init__"></a>

#### __init__

```python
def __init__(enable_recompute_normals: bool = False,
             enable_recompute_tangents: bool = False,
             enable_remove_degenerates: bool = False,
             remap_bone_indices_to_match_asset: bool = False,
             use_original_vertex_order: bool = False,
             use_build_scale: bool = False,
             replace_materials: bool = False,
             new_materials: Array[MaterialInterface] = [],
             new_material_slot_names: Array[Name] = [],
             apply_nanite_settings: bool = False,
             nanite_settings: GeometryScriptNaniteOptions = [
                 True, 100.000000, 0.000000
             ],
             new_nanite_settings: MeshNaniteSettings = [
                 False, False, False, True, -2147483648, -1, -1, 1.000000,
                 0.000000, NaniteFallbackTarget.AUTO, 1.000000, 1.000000,
                 0.000000, 0
             ],
             emit_transaction: bool = False,
             defer_mesh_post_edit_change: bool = False) -> None
```

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.enable_recompute_normals"></a>

#### enable_recompute_normals

```python
@property
def enable_recompute_normals() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.enable_recompute_normals"></a>

#### enable_recompute_normals

```python
@enable_recompute_normals.setter
def enable_recompute_normals(value: bool) -> None
```

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.enable_recompute_tangents"></a>

#### enable_recompute_tangents

```python
@property
def enable_recompute_tangents() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.enable_recompute_tangents"></a>

#### enable_recompute_tangents

```python
@enable_recompute_tangents.setter
def enable_recompute_tangents(value: bool) -> None
```

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.enable_remove_degenerates"></a>

#### enable_remove_degenerates

```python
@property
def enable_remove_degenerates() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.enable_remove_degenerates"></a>

#### enable_remove_degenerates

```python
@enable_remove_degenerates.setter
def enable_remove_degenerates(value: bool) -> None
```

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.remap_bone_indices_to_match_asset"></a>

#### remap_bone_indices_to_match_asset

```python
@property
def remap_bone_indices_to_match_asset() -> bool
```

(bool):  [Read-Write] Remap the bone indices to match the asset. This requires the source mesh to have bone information present. If no bone information is present
then all bone weights are mapped to the root.

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.remap_bone_indices_to_match_asset"></a>

#### remap_bone_indices_to_match_asset

```python
@remap_bone_indices_to_match_asset.setter
def remap_bone_indices_to_match_asset(value: bool) -> None
```

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.use_original_vertex_order"></a>

#### use_original_vertex_order

```python
@property
def use_original_vertex_order() -> bool
```

(bool):  [Read-Write] Use the original vertex order found in the source data. This is useful if the inbound mesh was originally non-manifold, and needs to keep
the non-manifold structure when re-created.

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.use_original_vertex_order"></a>

#### use_original_vertex_order

```python
@use_original_vertex_order.setter
def use_original_vertex_order(value: bool) -> None
```

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.use_build_scale"></a>

#### use_build_scale

```python
@property
def use_build_scale() -> bool
```

(bool):  [Read-Write] Whether to use the build scale on the target asset. If enabled, the inverse scale will be applied when saving to the asset, and the BuildScale will be preserved. Otherwise, BuildScale will be set to 1.0 on the asset BuildSettings.

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.use_build_scale"></a>

#### use_build_scale

```python
@use_build_scale.setter
def use_build_scale(value: bool) -> None
```

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.replace_materials"></a>

#### replace_materials

```python
@property
def replace_materials() -> bool
```

(bool):  [Read-Write] Whether to replace the materials on the asset with those in the New Materials array

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.replace_materials"></a>

#### replace_materials

```python
@replace_materials.setter
def replace_materials(value: bool) -> None
```

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.new_materials"></a>

#### new_materials

```python
@property
def new_materials() -> Array[MaterialInterface]
```

(Array[MaterialInterface]):  [Read-Write] New materials to set if Replace Materials is enabled. Ignored otherwise.

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.new_materials"></a>

#### new_materials

```python
@new_materials.setter
def new_materials(value: Array[MaterialInterface]) -> None
```

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.new_material_slot_names"></a>

#### new_material_slot_names

```python
@property
def new_material_slot_names() -> Array[Name]
```

(Array[Name]):  [Read-Write] Optional slot names for the New Materials. Ignored if not the same length as the New Materials array.

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.new_material_slot_names"></a>

#### new_material_slot_names

```python
@new_material_slot_names.setter
def new_material_slot_names(value: Array[Name]) -> None
```

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.apply_nanite_settings"></a>

#### apply_nanite_settings

```python
@property
def apply_nanite_settings() -> bool
```

(bool):  [Read-Write] If enabled, NaniteSettings will be applied to the target Asset if possible

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.apply_nanite_settings"></a>

#### apply_nanite_settings

```python
@apply_nanite_settings.setter
def apply_nanite_settings(value: bool) -> None
```

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.nanite_settings"></a>

#### nanite_settings

```python
@property
def nanite_settings() -> GeometryScriptNaniteOptions
```

(GeometryScriptNaniteOptions):  [Read-Write] Replaced FGeometryScriptNaniteOptions with usage of Engine FMeshNaniteSettings

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.nanite_settings"></a>

#### nanite_settings

```python
@nanite_settings.setter
def nanite_settings(value: GeometryScriptNaniteOptions) -> None
```

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.new_nanite_settings"></a>

#### new_nanite_settings

```python
@property
def new_nanite_settings() -> MeshNaniteSettings
```

(MeshNaniteSettings):  [Read-Write] Nanite Settings applied to the target Asset, if bApplyNaniteSettings = true

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.new_nanite_settings"></a>

#### new_nanite_settings

```python
@new_nanite_settings.setter
def new_nanite_settings(value: MeshNaniteSettings) -> None
```

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.emit_transaction"></a>

#### emit_transaction

```python
@property
def emit_transaction() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.emit_transaction"></a>

#### emit_transaction

```python
@emit_transaction.setter
def emit_transaction(value: bool) -> None
```

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.defer_mesh_post_edit_change"></a>

#### defer_mesh_post_edit_change

```python
@property
def defer_mesh_post_edit_change() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCopyMeshToAssetOptions.defer_mesh_post_edit_change"></a>

#### defer_mesh_post_edit_change

```python
@defer_mesh_post_edit_change.setter
def defer_mesh_post_edit_change(value: bool) -> None
```

<a id="unreal.GeometryScriptCopyMorphTargetToAssetOptions"></a>