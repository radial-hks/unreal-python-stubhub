## FbxImportUI Objects

```python
class FbxImportUI(Object)
```

Fbx Import UI

**C++ Source:**

- **Module**: UnrealEd
- **File**: FbxImportUI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``anim_end_frame`` (str):  [Read-Only] The fbx animation end frame
- ``anim_sequence_import_data`` (FbxAnimSequenceImportData):  [Read-Write] Import data used when importing animations
- ``anim_start_frame`` (str):  [Read-Only] The fbx animation start frame
- ``auto_compute_lod_distances`` (bool):  [Read-Write] If checked, the editor will automatically compute screen size values for the static mesh's LODs. If unchecked, the user can enter custom screen size values for each LOD.
- ``automated_import_should_detect_type`` (bool):  [Read-Write] If true the automated import path should detect the import type.  If false the import type was specified by the user
- ``create_physics_asset`` (bool):  [Read-Write] If checked, create new PhysicsAsset if it doesn't have it
- ``file_axis_direction`` (str):  [Read-Only] The file axis direction, up vector and hand
- ``file_creator`` (str):  [Read-Only] The file creator information
- ``file_creator_application`` (str):  [Read-Only] The file vendor information, software name and version that was use to create the file
- ``file_sample_rate`` (str):  [Read-Only] The fbx animation frame rate
- ``file_units`` (str):  [Read-Only] The file units
- ``file_version`` (str):  [Read-Only] The fbx file version
- ``import_animations`` (bool):  [Read-Write] True to import animations from the FBX File
- ``import_as_skeletal`` (bool):  [Read-Write] Whether to import the incoming FBX as a skeletal object
- ``import_materials`` (bool):  [Read-Write] If no existing materials are found, whether to automatically create Unreal materials for materials found in the FBX scene
- ``import_mesh`` (bool):  [Read-Write] Whether to import the mesh. Allows animation only import when importing a skeletal mesh.
- ``import_rigid_mesh`` (bool):  [Read-Write] Enables importing of 'rigid skeletalmesh' (unskinned, hierarchy-based animation) from this FBX file, no longer shown, used behind the scenes
- ``import_textures`` (bool):  [Read-Write] Whether or not we should import textures. This option is disabled when we are importing materials because textures are always imported in that case.
- ``is_obj_import`` (bool):  [Read-Write] Whether or not the imported file is in OBJ format
- ``lod_distance0`` (float):  [Read-Write] Set a screen size value for LOD 0
- ``lod_distance1`` (float):  [Read-Write] Set a screen size value for LOD 1
- ``lod_distance2`` (float):  [Read-Write] Set a screen size value for LOD 2
- ``lod_distance3`` (float):  [Read-Write] Set a screen size value for LOD 3
- ``lod_distance4`` (float):  [Read-Write] Set a screen size value for LOD 4
- ``lod_distance5`` (float):  [Read-Write] Set a screen size value for LOD 5
- ``lod_distance6`` (float):  [Read-Write] Set a screen size value for LOD 6
- ``lod_distance7`` (float):  [Read-Write] Set a screen size value for LOD 7
- ``lod_number`` (int32):  [Read-Write] Set the number of LODs for the editor to import. Setting the value to 0 imports the number of LODs found in the file (up to the maximum).
- ``mesh_type_to_import`` (FBXImportType):  [Read-Write] Type of asset to import from the FBX file
- ``minimum_lod_number`` (int32):  [Read-Write] Set the minimum LOD used for rendering. Setting the value to 0 will use the default value of LOD0.
- ``original_import_type`` (FBXImportType):  [Read-Write] The original detected type of this import
- ``override_animation_name`` (str):  [Read-Write] Override for the name of the animation to import. By default, it will be the name of FBX *
- ``override_full_name`` (bool):  [Read-Write] Use the string in "Name" field as full name of mesh. The option only works when the scene contains one mesh.
- ``physics_asset`` (PhysicsAsset):  [Read-Write] If this is set, use this PhysicsAsset. It is possible bCreatePhysicsAsset == false, and PhysicsAsset == NULL. It is possible they do not like to create anything.
- ``reset_to_fbx_on_material_conflict`` (bool):  [Read-Write] If true, the imported material sections will automatically be reset to the imported data in case of a reimport conflict.
- ``skeletal_mesh_import_data`` (FbxSkeletalMeshImportData):  [Read-Write] Import data used when importing skeletal meshes
- ``skeleton`` (Skeleton):  [Read-Write] Skeleton to use for imported asset. When importing a mesh, leaving this as "None" will create a new skeleton. When importing an animation this MUST be specified to import the asset.
- ``static_mesh_import_data`` (FbxStaticMeshImportData):  [Read-Write] Import data used when importing static meshes
- ``texture_import_data`` (FbxTextureImportData):  [Read-Write] Import data used when importing textures

<a id="unreal.FbxImportUI.is_obj_import"></a>

#### is_obj_import

```python
@property
def is_obj_import() -> bool
```

(bool):  [Read-Write] Whether or not the imported file is in OBJ format

<a id="unreal.FbxImportUI.is_obj_import"></a>

#### is_obj_import

```python
@is_obj_import.setter
def is_obj_import(value: bool) -> None
```

<a id="unreal.FbxImportUI.original_import_type"></a>

#### original_import_type

```python
@property
def original_import_type() -> FBXImportType
```

(FBXImportType):  [Read-Write] The original detected type of this import

<a id="unreal.FbxImportUI.original_import_type"></a>

#### original_import_type

```python
@original_import_type.setter
def original_import_type(value: FBXImportType) -> None
```

<a id="unreal.FbxImportUI.mesh_type_to_import"></a>

#### mesh_type_to_import

```python
@property
def mesh_type_to_import() -> FBXImportType
```

(FBXImportType):  [Read-Write] Type of asset to import from the FBX file

<a id="unreal.FbxImportUI.mesh_type_to_import"></a>

#### mesh_type_to_import

```python
@mesh_type_to_import.setter
def mesh_type_to_import(value: FBXImportType) -> None
```

<a id="unreal.FbxImportUI.override_full_name"></a>

#### override_full_name

```python
@property
def override_full_name() -> bool
```

(bool):  [Read-Write] Use the string in "Name" field as full name of mesh. The option only works when the scene contains one mesh.

<a id="unreal.FbxImportUI.override_full_name"></a>

#### override_full_name

```python
@override_full_name.setter
def override_full_name(value: bool) -> None
```

<a id="unreal.FbxImportUI.import_as_skeletal"></a>

#### import_as_skeletal

```python
@property
def import_as_skeletal() -> bool
```

(bool):  [Read-Write] Whether to import the incoming FBX as a skeletal object

<a id="unreal.FbxImportUI.import_as_skeletal"></a>

#### import_as_skeletal

```python
@import_as_skeletal.setter
def import_as_skeletal(value: bool) -> None
```

<a id="unreal.FbxImportUI.import_mesh"></a>

#### import_mesh

```python
@property
def import_mesh() -> bool
```

(bool):  [Read-Write] Whether to import the mesh. Allows animation only import when importing a skeletal mesh.

<a id="unreal.FbxImportUI.import_mesh"></a>

#### import_mesh

```python
@import_mesh.setter
def import_mesh(value: bool) -> None
```

<a id="unreal.FbxImportUI.skeleton"></a>

#### skeleton

```python
@property
def skeleton() -> Skeleton
```

(Skeleton):  [Read-Write] Skeleton to use for imported asset. When importing a mesh, leaving this as "None" will create a new skeleton. When importing an animation this MUST be specified to import the asset.

<a id="unreal.FbxImportUI.skeleton"></a>

#### skeleton

```python
@skeleton.setter
def skeleton(value: Skeleton) -> None
```

<a id="unreal.FbxImportUI.create_physics_asset"></a>

#### create_physics_asset

```python
@property
def create_physics_asset() -> bool
```

(bool):  [Read-Write] If checked, create new PhysicsAsset if it doesn't have it

<a id="unreal.FbxImportUI.create_physics_asset"></a>

#### create_physics_asset

```python
@create_physics_asset.setter
def create_physics_asset(value: bool) -> None
```

<a id="unreal.FbxImportUI.physics_asset"></a>

#### physics_asset

```python
@property
def physics_asset() -> PhysicsAsset
```

(PhysicsAsset):  [Read-Write] If this is set, use this PhysicsAsset. It is possible bCreatePhysicsAsset == false, and PhysicsAsset == NULL. It is possible they do not like to create anything.

<a id="unreal.FbxImportUI.physics_asset"></a>

#### physics_asset

```python
@physics_asset.setter
def physics_asset(value: PhysicsAsset) -> None
```

<a id="unreal.FbxImportUI.auto_compute_lod_distances"></a>

#### auto_compute_lod_distances

```python
@property
def auto_compute_lod_distances() -> bool
```

(bool):  [Read-Write] If checked, the editor will automatically compute screen size values for the static mesh's LODs. If unchecked, the user can enter custom screen size values for each LOD.

<a id="unreal.FbxImportUI.auto_compute_lod_distances"></a>

#### auto_compute_lod_distances

```python
@auto_compute_lod_distances.setter
def auto_compute_lod_distances(value: bool) -> None
```

<a id="unreal.FbxImportUI.lod_distance0"></a>

#### lod_distance0

```python
@property
def lod_distance0() -> float
```

(float):  [Read-Write] Set a screen size value for LOD 0

<a id="unreal.FbxImportUI.lod_distance0"></a>

#### lod_distance0

```python
@lod_distance0.setter
def lod_distance0(value: float) -> None
```

<a id="unreal.FbxImportUI.lod_distance1"></a>

#### lod_distance1

```python
@property
def lod_distance1() -> float
```

(float):  [Read-Write] Set a screen size value for LOD 1

<a id="unreal.FbxImportUI.lod_distance1"></a>

#### lod_distance1

```python
@lod_distance1.setter
def lod_distance1(value: float) -> None
```

<a id="unreal.FbxImportUI.lod_distance2"></a>

#### lod_distance2

```python
@property
def lod_distance2() -> float
```

(float):  [Read-Write] Set a screen size value for LOD 2

<a id="unreal.FbxImportUI.lod_distance2"></a>

#### lod_distance2

```python
@lod_distance2.setter
def lod_distance2(value: float) -> None
```

<a id="unreal.FbxImportUI.lod_distance3"></a>

#### lod_distance3

```python
@property
def lod_distance3() -> float
```

(float):  [Read-Write] Set a screen size value for LOD 3

<a id="unreal.FbxImportUI.lod_distance3"></a>

#### lod_distance3

```python
@lod_distance3.setter
def lod_distance3(value: float) -> None
```

<a id="unreal.FbxImportUI.lod_distance4"></a>

#### lod_distance4

```python
@property
def lod_distance4() -> float
```

(float):  [Read-Write] Set a screen size value for LOD 4

<a id="unreal.FbxImportUI.lod_distance4"></a>

#### lod_distance4

```python
@lod_distance4.setter
def lod_distance4(value: float) -> None
```

<a id="unreal.FbxImportUI.lod_distance5"></a>

#### lod_distance5

```python
@property
def lod_distance5() -> float
```

(float):  [Read-Write] Set a screen size value for LOD 5

<a id="unreal.FbxImportUI.lod_distance5"></a>

#### lod_distance5

```python
@lod_distance5.setter
def lod_distance5(value: float) -> None
```

<a id="unreal.FbxImportUI.lod_distance6"></a>

#### lod_distance6

```python
@property
def lod_distance6() -> float
```

(float):  [Read-Write] Set a screen size value for LOD 6

<a id="unreal.FbxImportUI.lod_distance6"></a>

#### lod_distance6

```python
@lod_distance6.setter
def lod_distance6(value: float) -> None
```

<a id="unreal.FbxImportUI.lod_distance7"></a>

#### lod_distance7

```python
@property
def lod_distance7() -> float
```

(float):  [Read-Write] Set a screen size value for LOD 7

<a id="unreal.FbxImportUI.lod_distance7"></a>

#### lod_distance7

```python
@lod_distance7.setter
def lod_distance7(value: float) -> None
```

<a id="unreal.FbxImportUI.minimum_lod_number"></a>

#### minimum_lod_number

```python
@property
def minimum_lod_number() -> int
```

(int32):  [Read-Write] Set the minimum LOD used for rendering. Setting the value to 0 will use the default value of LOD0.

<a id="unreal.FbxImportUI.minimum_lod_number"></a>

#### minimum_lod_number

```python
@minimum_lod_number.setter
def minimum_lod_number(value: int) -> None
```

<a id="unreal.FbxImportUI.lod_number"></a>

#### lod_number

```python
@property
def lod_number() -> int
```

(int32):  [Read-Write] Set the number of LODs for the editor to import. Setting the value to 0 imports the number of LODs found in the file (up to the maximum).

<a id="unreal.FbxImportUI.lod_number"></a>

#### lod_number

```python
@lod_number.setter
def lod_number(value: int) -> None
```

<a id="unreal.FbxImportUI.import_animations"></a>

#### import_animations

```python
@property
def import_animations() -> bool
```

(bool):  [Read-Write] True to import animations from the FBX File

<a id="unreal.FbxImportUI.import_animations"></a>

#### import_animations

```python
@import_animations.setter
def import_animations(value: bool) -> None
```

<a id="unreal.FbxImportUI.override_animation_name"></a>

#### override_animation_name

```python
@property
def override_animation_name() -> str
```

(str):  [Read-Write] Override for the name of the animation to import. By default, it will be the name of FBX *

<a id="unreal.FbxImportUI.override_animation_name"></a>

#### override_animation_name

```python
@override_animation_name.setter
def override_animation_name(value: str) -> None
```

<a id="unreal.FbxImportUI.import_rigid_mesh"></a>

#### import_rigid_mesh

```python
@property
def import_rigid_mesh() -> bool
```

(bool):  [Read-Write] Enables importing of 'rigid skeletalmesh' (unskinned, hierarchy-based animation) from this FBX file, no longer shown, used behind the scenes

<a id="unreal.FbxImportUI.import_rigid_mesh"></a>

#### import_rigid_mesh

```python
@import_rigid_mesh.setter
def import_rigid_mesh(value: bool) -> None
```

<a id="unreal.FbxImportUI.import_materials"></a>

#### import_materials

```python
@property
def import_materials() -> bool
```

(bool):  [Read-Write] If no existing materials are found, whether to automatically create Unreal materials for materials found in the FBX scene

<a id="unreal.FbxImportUI.import_materials"></a>

#### import_materials

```python
@import_materials.setter
def import_materials(value: bool) -> None
```

<a id="unreal.FbxImportUI.import_textures"></a>

#### import_textures

```python
@property
def import_textures() -> bool
```

(bool):  [Read-Write] Whether or not we should import textures. This option is disabled when we are importing materials because textures are always imported in that case.

<a id="unreal.FbxImportUI.import_textures"></a>

#### import_textures

```python
@import_textures.setter
def import_textures(value: bool) -> None
```

<a id="unreal.FbxImportUI.reset_to_fbx_on_material_conflict"></a>

#### reset_to_fbx_on_material_conflict

```python
@property
def reset_to_fbx_on_material_conflict() -> bool
```

(bool):  [Read-Write] If true, the imported material sections will automatically be reset to the imported data in case of a reimport conflict.

<a id="unreal.FbxImportUI.reset_to_fbx_on_material_conflict"></a>

#### reset_to_fbx_on_material_conflict

```python
@reset_to_fbx_on_material_conflict.setter
def reset_to_fbx_on_material_conflict(value: bool) -> None
```

<a id="unreal.FbxImportUI.static_mesh_import_data"></a>

#### static_mesh_import_data

```python
@property
def static_mesh_import_data() -> FbxStaticMeshImportData
```

(FbxStaticMeshImportData):  [Read-Write] Import data used when importing static meshes

<a id="unreal.FbxImportUI.static_mesh_import_data"></a>

#### static_mesh_import_data

```python
@static_mesh_import_data.setter
def static_mesh_import_data(value: FbxStaticMeshImportData) -> None
```

<a id="unreal.FbxImportUI.skeletal_mesh_import_data"></a>

#### skeletal_mesh_import_data

```python
@property
def skeletal_mesh_import_data() -> FbxSkeletalMeshImportData
```

(FbxSkeletalMeshImportData):  [Read-Write] Import data used when importing skeletal meshes

<a id="unreal.FbxImportUI.skeletal_mesh_import_data"></a>

#### skeletal_mesh_import_data

```python
@skeletal_mesh_import_data.setter
def skeletal_mesh_import_data(value: FbxSkeletalMeshImportData) -> None
```

<a id="unreal.FbxImportUI.anim_sequence_import_data"></a>

#### anim_sequence_import_data

```python
@property
def anim_sequence_import_data() -> FbxAnimSequenceImportData
```

(FbxAnimSequenceImportData):  [Read-Write] Import data used when importing animations

<a id="unreal.FbxImportUI.anim_sequence_import_data"></a>

#### anim_sequence_import_data

```python
@anim_sequence_import_data.setter
def anim_sequence_import_data(value: FbxAnimSequenceImportData) -> None
```

<a id="unreal.FbxImportUI.texture_import_data"></a>

#### texture_import_data

```python
@property
def texture_import_data() -> FbxTextureImportData
```

(FbxTextureImportData):  [Read-Write] Import data used when importing textures

<a id="unreal.FbxImportUI.texture_import_data"></a>

#### texture_import_data

```python
@texture_import_data.setter
def texture_import_data(value: FbxTextureImportData) -> None
```

<a id="unreal.FbxImportUI.automated_import_should_detect_type"></a>

#### automated_import_should_detect_type

```python
@property
def automated_import_should_detect_type() -> bool
```

(bool):  [Read-Write] If true the automated import path should detect the import type.  If false the import type was specified by the user

<a id="unreal.FbxImportUI.automated_import_should_detect_type"></a>

#### automated_import_should_detect_type

```python
@automated_import_should_detect_type.setter
def automated_import_should_detect_type(value: bool) -> None
```

<a id="unreal.FbxImportUI.reset_to_default"></a>

#### reset_to_default

```python
def reset_to_default() -> None
```

x.reset_to_default() -> None
Reset to Default

<a id="unreal.FbxMeshImportData"></a>