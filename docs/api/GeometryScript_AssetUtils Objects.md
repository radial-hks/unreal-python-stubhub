## GeometryScript_AssetUtils Objects

```python
class GeometryScript_AssetUtils(BlueprintFunctionLibrary)
```

Although the class name indicates StaticMeshFunctions, that was a naming mistake that is difficult
to correct. This class is intended to serve as a generic asset utils function library. The naming
issue is only visible at the C++ level. It is not visible in Python or BP.

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshAssetFunctions.h

<a id="unreal.GeometryScript_AssetUtils.get_section_material_list_from_static_mesh"></a>

#### get_section_material_list_from_static_mesh

```python
@classmethod
def get_section_material_list_from_static_mesh(
    cls,
    from_static_mesh_asset: StaticMesh,
    requested_lod: GeometryScriptMeshReadLOD,
    debug: GeometryScriptDebug = None
) -> Tuple[Array[MaterialInterface], Array[int], Array[Name],
           GeometryScriptOutcomePins]
```

X.get_section_material_list_from_static_mesh(from_static_mesh_asset, requested_lod, debug=None) -> (material_list=Array[MaterialInterface], material_index=Array[int32], material_slot_names=Array[Name], outcome=GeometryScriptOutcomePins)
Extracts the Material List and corresponding Material Indices from the specified LOD of the Static Mesh Asset.
The MaterialList is sorted by Section, so if CopyMeshToStaticMesh was used to create a DynamicMesh with bUseSectionMaterials=true, then the
returned MaterialList here will correspond to the MaterialIDs in that DynamicMesh (as each Static Mesh Section becomes a MaterialID, in-order).
So, the returned MaterialList can be passed directly to (eg) a DynamicMeshComponent.

Args:
    from_static_mesh_asset (StaticMesh): 
    requested_lod (GeometryScriptMeshReadLOD): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    material_list (Array[MaterialInterface]): 

    material_index (Array[int32]): this returned array is the same size as MaterialList, with each value the index of that Material in the StaticMesh Material List

    material_slot_names (Array[Name]): 

    outcome (GeometryScriptOutcomePins):

<a id="unreal.GeometryScript_AssetUtils.get_num_static_mesh_lo_ds_of_type"></a>

#### get_num_static_mesh_lo_ds_of_type

```python
@classmethod
def get_num_static_mesh_lo_ds_of_type(
    cls,
    static_mesh_asset: StaticMesh,
    lod_type: GeometryScriptLODType = GeometryScriptLODType.SOURCE_MODEL
) -> int
```

X.get_num_static_mesh_lo_ds_of_type(static_mesh_asset, lod_type=GeometryScriptLODType.SOURCE_MODEL) -> int32
Determine the number of available LODs of the requested LODType in a Static Mesh Asset

Args:
    static_mesh_asset (StaticMesh): 
    lod_type (GeometryScriptLODType): 

Returns:
    int32:

<a id="unreal.GeometryScript_AssetUtils.get_material_list_from_static_mesh"></a>

#### get_material_list_from_static_mesh

```python
@classmethod
def get_material_list_from_static_mesh(
    cls,
    from_static_mesh_asset: StaticMesh,
    debug: GeometryScriptDebug = None
) -> Tuple[Array[MaterialInterface], Array[Name]]
```

X.get_material_list_from_static_mesh(from_static_mesh_asset, debug=None) -> (material_list=Array[MaterialInterface], material_slot_names=Array[Name])
Get the asset materials from the static mesh asset. These will match the DynamicMesh material if CopyMeshFromStaticMesh
was used to create a DynamicMesh with bUseSectionMaterials=false

Args:
    from_static_mesh_asset (StaticMesh): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    material_list (Array[MaterialInterface]): 

    material_slot_names (Array[Name]):

<a id="unreal.GeometryScript_AssetUtils.get_material_list_from_skeletal_mesh"></a>

#### get_material_list_from_skeletal_mesh

```python
@classmethod
def get_material_list_from_skeletal_mesh(
    cls,
    from_skeletal_mesh_asset: SkeletalMesh,
    debug: GeometryScriptDebug = None
) -> Tuple[Array[MaterialInterface], Array[Name]]
```

X.get_material_list_from_skeletal_mesh(from_skeletal_mesh_asset, debug=None) -> (material_list=Array[MaterialInterface], material_slot_names=Array[Name])
Get the asset materials from the skeletal mesh asset.
Note: For LOD-specific materials, use GetLODMaterialListFromSkeletalMesh instead.

Args:
    from_skeletal_mesh_asset (SkeletalMesh): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    material_list (Array[MaterialInterface]): 

    material_slot_names (Array[Name]):

<a id="unreal.GeometryScript_AssetUtils.get_lod_material_list_from_skeletal_mesh"></a>

#### get_lod_material_list_from_skeletal_mesh

```python
@classmethod
def get_lod_material_list_from_skeletal_mesh(
    cls,
    from_skeletal_mesh_asset: SkeletalMesh,
    requested_lod: GeometryScriptMeshReadLOD,
    debug: GeometryScriptDebug = None
) -> Tuple[Array[MaterialInterface], Array[int], Array[Name],
           GeometryScriptOutcomePins]
```

X.get_lod_material_list_from_skeletal_mesh(from_skeletal_mesh_asset, requested_lod, debug=None) -> (material_list=Array[MaterialInterface], material_index=Array[int32], material_slot_names=Array[Name], outcome=GeometryScriptOutcomePins)
Extracts the Material List and corresponding Material Indices from the specified LOD of the Skeletal Mesh Asset.
If Copy Mesh To Skeletal Mesh was used to create a Dynamic Mesh, then the returned Material List can be passed directly to a Dynamic Mesh Component.

Args:
    from_skeletal_mesh_asset (SkeletalMesh): 
    requested_lod (GeometryScriptMeshReadLOD): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    material_list (Array[MaterialInterface]): 

    material_index (Array[int32]): this returned array is the same size as MaterialList, with each value the index of that Material in the Skeletal Mesh's Material List

    material_slot_names (Array[Name]): 

    outcome (GeometryScriptOutcomePins):

<a id="unreal.GeometryScript_AssetUtils.copy_skin_weight_profile_to_skeletal_mesh"></a>

#### copy_skin_weight_profile_to_skeletal_mesh

```python
@classmethod
def copy_skin_weight_profile_to_skeletal_mesh(
    cls,
    from_dynamic_mesh: DynamicMesh,
    to_skeletal_mesh_asset: SkeletalMesh,
    target_profile_name: Name,
    source_profile_name: Name,
    options: GeometryScriptCopySkinWeightProfileToAssetOptions,
    target_lod: GeometryScriptMeshWriteLOD,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptOutcomePins]
```

X.copy_skin_weight_profile_to_skeletal_mesh(from_dynamic_mesh, to_skeletal_mesh_asset, target_profile_name, source_profile_name, options, target_lod, debug=None) -> (DynamicMesh, outcome=GeometryScriptOutcomePins)
Add a Dynamic Mesh skin weight profile to a Skeletal Mesh Asset.

Args:
    from_dynamic_mesh (DynamicMesh): the dynamic mesh representing the geometry of the morph target
    to_skeletal_mesh_asset (SkeletalMesh): the asset we are writing the morph target into
    target_profile_name (Name): the name of the skin weight profile as it will appear in the UI. Leave blank for the default profile.
    source_profile_name (Name): The name of the skin weight profile to copy from the dynamic mesh. Leave blank for the default profile.
    options (GeometryScriptCopySkinWeightProfileToAssetOptions): 
    target_lod (GeometryScriptMeshWriteLOD): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptOutcomePins: 

    outcome (GeometryScriptOutcomePins):

<a id="unreal.GeometryScript_AssetUtils.copy_morph_target_to_skeletal_mesh"></a>

#### copy_morph_target_to_skeletal_mesh

```python
@classmethod
def copy_morph_target_to_skeletal_mesh(
    cls,
    from_morph_target: DynamicMesh,
    to_skeletal_mesh_asset: SkeletalMesh,
    morph_target_name: Name,
    options: GeometryScriptCopyMorphTargetToAssetOptions,
    target_lod: GeometryScriptMeshWriteLOD,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptOutcomePins]
```

X.copy_morph_target_to_skeletal_mesh(from_morph_target, to_skeletal_mesh_asset, morph_target_name, options, target_lod, debug=None) -> (DynamicMesh, outcome=GeometryScriptOutcomePins)
Add a Dynamic Mesh morph target to a Skeletal Mesh Asset.

Args:
    from_morph_target (DynamicMesh): the dynamic mesh representing the geometry of the morph target
    to_skeletal_mesh_asset (SkeletalMesh): the asset we are writing the morph target into
    morph_target_name (Name): the name of the morph target as it will appear in the UI
    options (GeometryScriptCopyMorphTargetToAssetOptions): 
    target_lod (GeometryScriptMeshWriteLOD): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptOutcomePins: 

    outcome (GeometryScriptOutcomePins):

<a id="unreal.GeometryScript_AssetUtils.copy_mesh_to_static_mesh"></a>

#### copy_mesh_to_static_mesh

```python
@classmethod
def copy_mesh_to_static_mesh(
    cls,
    from_dynamic_mesh: DynamicMesh,
    to_static_mesh_asset: StaticMesh,
    options: GeometryScriptCopyMeshToAssetOptions,
    target_lod: GeometryScriptMeshWriteLOD,
    use_section_materials: bool = True,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptOutcomePins]
```

X.copy_mesh_to_static_mesh(from_dynamic_mesh, to_static_mesh_asset, options, target_lod, use_section_materials=True, debug=None) -> (DynamicMesh, outcome=GeometryScriptOutcomePins)
Updates a Static Mesh Asset with new geometry converted from a Dynamic Mesh

Args:
    from_dynamic_mesh (DynamicMesh): 
    to_static_mesh_asset (StaticMesh): 
    options (GeometryScriptCopyMeshToAssetOptions): 
    target_lod (GeometryScriptMeshWriteLOD): 
    use_section_materials (bool): Whether to assume Dynamic Mesh material IDs are section indices in the target Static Mesh. Should match the value passed to CopyMeshFromStaticMesh. Has no effect if replacing the asset materials.
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptOutcomePins: 

    outcome (GeometryScriptOutcomePins):

<a id="unreal.GeometryScript_AssetUtils.copy_mesh_to_skeletal_mesh"></a>

#### copy_mesh_to_skeletal_mesh

```python
@classmethod
def copy_mesh_to_skeletal_mesh(
    cls,
    from_dynamic_mesh: DynamicMesh,
    to_skeletal_mesh_asset: SkeletalMesh,
    options: GeometryScriptCopyMeshToAssetOptions,
    target_lod: GeometryScriptMeshWriteLOD,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptOutcomePins]
```

X.copy_mesh_to_skeletal_mesh(from_dynamic_mesh, to_skeletal_mesh_asset, options, target_lod, debug=None) -> (DynamicMesh, outcome=GeometryScriptOutcomePins)
Updates a Skeletal Mesh Asset with new geometry and bone weights data from a Dynamic Mesh.

Args:
    from_dynamic_mesh (DynamicMesh): 
    to_skeletal_mesh_asset (SkeletalMesh): 
    options (GeometryScriptCopyMeshToAssetOptions): 
    target_lod (GeometryScriptMeshWriteLOD): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptOutcomePins: 

    outcome (GeometryScriptOutcomePins):

<a id="unreal.GeometryScript_AssetUtils.copy_mesh_from_static_mesh_v2"></a>

#### copy_mesh_from_static_mesh_v2

```python
@classmethod
def copy_mesh_from_static_mesh_v2(
    cls,
    from_static_mesh_asset: StaticMesh,
    to_dynamic_mesh: DynamicMesh,
    asset_options: GeometryScriptCopyMeshFromAssetOptions,
    requested_lod: GeometryScriptMeshReadLOD,
    use_section_materials: bool = True,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptOutcomePins]
```

X.copy_mesh_from_static_mesh_v2(from_static_mesh_asset, to_dynamic_mesh, asset_options, requested_lod, use_section_materials=True, debug=None) -> (DynamicMesh, outcome=GeometryScriptOutcomePins)
Extracts a Dynamic Mesh from a Static Mesh Asset.

Note that the LOD Index in RequestedLOD will be silently clamped to the available number of LODs (SourceModel or RenderData)

Args:
    from_static_mesh_asset (StaticMesh): 
    to_dynamic_mesh (DynamicMesh): 
    asset_options (GeometryScriptCopyMeshFromAssetOptions): 
    requested_lod (GeometryScriptMeshReadLOD): 
    use_section_materials (bool): Whether to use the mesh section indices as material IDs. If true, use GetSectionMaterialListFromStaticMesh to get the corresponding materials. If false, use GetMaterialListFromStaticMesh to get the materials instead.
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptOutcomePins: 

    outcome (GeometryScriptOutcomePins):

<a id="unreal.GeometryScript_AssetUtils.copy_mesh_from_static_mesh"></a>

#### copy_mesh_from_static_mesh

```python
@classmethod
def copy_mesh_from_static_mesh(
    cls,
    from_static_mesh_asset: StaticMesh,
    to_dynamic_mesh: DynamicMesh,
    asset_options: GeometryScriptCopyMeshFromAssetOptions,
    requested_lod: GeometryScriptMeshReadLOD,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptOutcomePins]
```

X.copy_mesh_from_static_mesh(from_static_mesh_asset, to_dynamic_mesh, asset_options, requested_lod, debug=None) -> (DynamicMesh, outcome=GeometryScriptOutcomePins)
Extracts a Dynamic Mesh from a Static Mesh Asset, using section indices for the material IDs -- use GetSectionMaterialListFromStaticMesh to get the corresponding materials.

Note that the LOD Index in RequestedLOD will be silently clamped to the available number of LODs (SourceModel or RenderData)

Args:
    from_static_mesh_asset (StaticMesh): 
    to_dynamic_mesh (DynamicMesh): 
    asset_options (GeometryScriptCopyMeshFromAssetOptions): 
    requested_lod (GeometryScriptMeshReadLOD): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptOutcomePins: 

    outcome (GeometryScriptOutcomePins):

<a id="unreal.GeometryScript_AssetUtils.copy_mesh_from_skeletal_mesh"></a>

#### copy_mesh_from_skeletal_mesh

```python
@classmethod
def copy_mesh_from_skeletal_mesh(
    cls,
    from_skeletal_mesh_asset: SkeletalMesh,
    to_dynamic_mesh: DynamicMesh,
    asset_options: GeometryScriptCopyMeshFromAssetOptions,
    requested_lod: GeometryScriptMeshReadLOD,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptOutcomePins]
```

X.copy_mesh_from_skeletal_mesh(from_skeletal_mesh_asset, to_dynamic_mesh, asset_options, requested_lod, debug=None) -> (DynamicMesh, outcome=GeometryScriptOutcomePins)
Extracts a Dynamic Mesh from a Skeletal Mesh Asset.

Args:
    from_skeletal_mesh_asset (SkeletalMesh): 
    to_dynamic_mesh (DynamicMesh): 
    asset_options (GeometryScriptCopyMeshFromAssetOptions): 
    requested_lod (GeometryScriptMeshReadLOD): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptOutcomePins: 

    outcome (GeometryScriptOutcomePins):

<a id="unreal.GeometryScript_AssetUtils.convert_material_map_to_material_list"></a>

#### convert_material_map_to_material_list

```python
@classmethod
def convert_material_map_to_material_list(
    cls, material_map: Map[Name, MaterialInterface]
) -> Tuple[Array[MaterialInterface], Array[Name]]
```

X.convert_material_map_to_material_list(material_map) -> (material_list=Array[MaterialInterface], material_slot_names=Array[Name])
Converts material map to a material list and a slot names list. Null materials will be kept in the list, and the list will have the same number of elements as the map.

Args:
    material_map (Map[Name, MaterialInterface]): 

Returns:
    tuple: 

    material_list (Array[MaterialInterface]): 

    material_slot_names (Array[Name]):

<a id="unreal.GeometryScript_AssetUtils.convert_material_list_to_material_map"></a>

#### convert_material_list_to_material_map

```python
@classmethod
def convert_material_list_to_material_map(
        cls, material_list: Array[MaterialInterface],
        material_slot_names: Array[Name]) -> Map[Name, MaterialInterface]
```

X.convert_material_list_to_material_map(material_list, material_slot_names) -> Map[Name, MaterialInterface]
Converts material list and slot names list to material map, which is the format expected by CreateNewSkeletalMeshAssetFromMesh.
Material List and Material Slot Names should have the same length. However, if there are fewer slot names than materials,
slot names will be auto-generated (as '[Name of material]_[Index]', or 'Material_[Index]' for null materials)

Args:
    material_list (Array[MaterialInterface]): 
    material_slot_names (Array[Name]): 

Returns:
    Map[Name, MaterialInterface]:

<a id="unreal.GeometryScript_AssetUtils.check_static_mesh_has_available_lod"></a>

#### check_static_mesh_has_available_lod

```python
@classmethod
def check_static_mesh_has_available_lod(
    cls,
    static_mesh_asset: StaticMesh,
    requested_lod: GeometryScriptMeshReadLOD,
    debug: GeometryScriptDebug = None
) -> Optional[GeometryScriptSearchOutcomePins]
```

X.check_static_mesh_has_available_lod(static_mesh_asset, requested_lod, debug=None) -> GeometryScriptSearchOutcomePins or None
Check if a Static Mesh Asset has the RequestedLOD available, ie if CopyMeshFromStaticMesh will be able to
succeed for the given LODType and LODIndex.

Args:
    static_mesh_asset (StaticMesh): 
    requested_lod (GeometryScriptMeshReadLOD): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptSearchOutcomePins or None: 

    outcome (GeometryScriptSearchOutcomePins):

<a id="unreal.GeometryScript_Bake"></a>