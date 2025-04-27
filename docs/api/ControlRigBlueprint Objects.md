## ControlRigBlueprint Objects

```python
class ControlRigBlueprint(RigVMBlueprint)
```

Control Rig Blueprint

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRigDeveloper
- **File**: ControlRigBlueprint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_multiple_instances`` (bool):  [Read-Write] If set to true, multiple control rig tracks can be created for the same rig in sequencer
- ``asset_variant`` (RigVMVariant):  [Read-Write] Variant information about this asset
- ``blueprint_category`` (str):  [Read-Write] The category of the Blueprint, used to organize this Blueprint class when displayed in palette windows
- ``blueprint_description`` (str):  [Read-Write] Shows up in the content browser tooltip when the blueprint is hovered
- ``blueprint_display_name`` (str):  [Read-Write] Overrides the BP's display name in the editor UI
- ``blueprint_namespace`` (str):  [Read-Write] The namespace of this blueprint (if set, the Blueprint will be treated differently for the context menu)
- ``compile_mode`` (BlueprintCompileMode):  [Read-Write] The mode that will be used when compiling this class.
- ``custom_thumbnail`` (str):  [Read-Write] This relates to FAssetThumbnailPool::CustomThumbnailTagName and allows
  the thumbnail pool to show the thumbnail of the icon rather than the
  rig itself to avoid deploying the 3D renderer.
- ``deprecate`` (bool):  [Read-Write] Deprecates the Blueprint, marking the generated class with the CLASS_Deprecated flag
- ``draw_container`` (RigVMDrawContainer):  [Read-Write]
- ``generate_abstract_class`` (bool):  [Read-Write] Whether or not this blueprint's class is a abstract class or not.  Should set CLASS_Abstract in the KismetCompiler.
- ``generate_const_class`` (bool):  [Read-Write] Whether or not this blueprint's class is a const class or not.  Should set CLASS_Const in the KismetCompiler.
- ``hide_categories`` (Array[str]):  [Read-Write] Additional HideCategories. These are added to HideCategories from parent.
- ``hierarchy`` (RigHierarchy):  [Read-Write]
- ``hierarchy_settings`` (RigHierarchySettings):  [Read-Write]
- ``influences`` (RigInfluenceMapPerEvent):  [Read-Write]
- ``modular_rig_model`` (ModularRigModel):  [Read-Write]
- ``modular_rig_settings`` (ModularRigSettings):  [Read-Write]
- ``python_log_settings`` (RigVMPythonSettings):  [Read-Write]
- ``rig_graph_display_settings`` (RigVMEdGraphDisplaySettings):  [Read-Write]
- ``rig_module_settings`` (RigModuleSettings):  [Read-Write]
- ``run_construction_script_in_sequencer`` (bool):  [Read-Write] whether or not you want to continuously rerun the construction script for an actor in sequencer
- ``run_construction_script_on_drag`` (bool):  [Read-Write] whether or not you want to continuously rerun the construction script for an actor as you drag it in the editor, or only when the drag operation is complete
- ``shape_libraries`` (Array[ControlRigShapeLibrary]):  [Read-Write]
- ``should_cook_property_guids_value`` (ShouldCookBlueprintPropertyGuids):  [Read-Write] Whether to include the property GUIDs for the generated class in a cooked build.
  note: This option may slightly increase memory usage in a cooked build, but can avoid needing to add CoreRedirect data for Blueprint classes stored within SaveGame archives.
- ``source_curve_import`` (Object):  [Read-Write] The skeleton from import into a curve
- ``source_hierarchy_import`` (Object):  [Read-Write] The skeleton from import into a hierarchy
- ``thumbnail_info`` (ThumbnailInfo):  [Read-Only] Information for thumbnail rendering
- ``vm_compile_settings`` (RigVMCompileSettings):  [Read-Write]
- ``vm_runtime_settings`` (RigVMRuntimeSettings):  [Read-Write]

<a id="unreal.ControlRigBlueprint.hierarchy"></a>

#### hierarchy

```python
@property
def hierarchy() -> RigHierarchy
```

(RigHierarchy):  [Read-Only]

<a id="unreal.ControlRigBlueprint.modular_rig_model"></a>

#### modular_rig_model

```python
@property
def modular_rig_model() -> ModularRigModel
```

(ModularRigModel):  [Read-Only]

<a id="unreal.ControlRigBlueprint.turn_into_standalone_rig"></a>

#### turn_into_standalone_rig

```python
def turn_into_standalone_rig() -> bool
```

x.turn_into_standalone_rig() -> bool
Turn Into Standalone Rig Blueprint

Returns:
    bool:

<a id="unreal.ControlRigBlueprint.turn_into_control_rig_module"></a>

#### turn_into_control_rig_module

```python
def turn_into_control_rig_module() -> bool
```

x.turn_into_control_rig_module() -> bool
Turn Into Control Rig Module Blueprint

Returns:
    bool:

<a id="unreal.ControlRigBlueprint.set_preview_mesh"></a>

#### set_preview_mesh

```python
def set_preview_mesh(preview_mesh: SkeletalMesh,
                     mark_as_dirty: bool = True) -> None
```

x.set_preview_mesh(preview_mesh, mark_as_dirty=True) -> None
IInterface_PreviewMeshProvider interface

Args:
    preview_mesh (SkeletalMesh): 
    mark_as_dirty (bool):

<a id="unreal.ControlRigBlueprint.recompile_modular_rig"></a>

#### recompile_modular_rig

```python
def recompile_modular_rig() -> None
```

x.recompile_modular_rig() -> None
Recompile Modular Rig

<a id="unreal.ControlRigBlueprint.is_control_rig_module"></a>

#### is_control_rig_module

```python
def is_control_rig_module() -> bool
```

x.is_control_rig_module() -> bool
Is Control Rig Module

Returns:
    bool:

<a id="unreal.ControlRigBlueprint.get_rig_module_icon"></a>

#### get_rig_module_icon

```python
def get_rig_module_icon() -> Texture2D
```

x.get_rig_module_icon() -> Texture2D
Get Rig Module Icon

Returns:
    Texture2D:

<a id="unreal.ControlRigBlueprint.get_preview_mesh"></a>

#### get_preview_mesh

```python
def get_preview_mesh() -> SkeletalMesh
```

x.get_preview_mesh() -> SkeletalMesh
Get Preview Mesh

Returns:
    SkeletalMesh:

<a id="unreal.ControlRigBlueprint.get_modular_rig_controller"></a>

#### get_modular_rig_controller

```python
def get_modular_rig_controller() -> ModularRigController
```

x.get_modular_rig_controller() -> ModularRigController
Get Modular Rig Controller

Returns:
    ModularRigController:

<a id="unreal.ControlRigBlueprint.get_hierarchy_controller"></a>

#### get_hierarchy_controller

```python
def get_hierarchy_controller() -> RigHierarchyController
```

x.get_hierarchy_controller() -> RigHierarchyController
Get Hierarchy Controller

Returns:
    RigHierarchyController:

<a id="unreal.ControlRigBlueprint.get_debugged_control_rig"></a>

#### get_debugged_control_rig

```python
def get_debugged_control_rig() -> ControlRig
```

x.get_debugged_control_rig() -> ControlRig
Get Debugged Control Rig

Returns:
    ControlRig:

<a id="unreal.ControlRigBlueprint.get_currently_open_rig_blueprints"></a>

#### get_currently_open_rig_blueprints

```python
@classmethod
def get_currently_open_rig_blueprints(cls) -> Array[ControlRigBlueprint]
```

X.get_currently_open_rig_blueprints() -> Array[ControlRigBlueprint]
Get Currently Open Rig Blueprints

Returns:
    Array[ControlRigBlueprint]:

<a id="unreal.ControlRigBlueprint.get_control_rig_class"></a>

#### get_control_rig_class

```python
def get_control_rig_class() -> Class
```

x.get_control_rig_class() -> type(Class)
Get Control Rig Class

Returns:
    type(Class):

<a id="unreal.ControlRigBlueprint.find_references_to_module"></a>

#### find_references_to_module

```python
def find_references_to_module() -> Array[ModuleReferenceData]
```

x.find_references_to_module() -> Array[ModuleReferenceData]
Find References to Module

Returns:
    Array[ModuleReferenceData]:

<a id="unreal.ControlRigBlueprint.create_control_rig"></a>

#### create_control_rig

```python
def create_control_rig() -> ControlRig
```

x.create_control_rig() -> ControlRig
Create Control Rig

Returns:
    ControlRig:

<a id="unreal.ControlRigBlueprint.convert_hierarchy_elements_to_spawner_nodes"></a>

#### convert_hierarchy_elements_to_spawner_nodes

```python
def convert_hierarchy_elements_to_spawner_nodes(
        hierarchy: RigHierarchy,
        keys: Array[RigElementKey],
        remove_elements: bool = True) -> Array[RigVMNode]
```

x.convert_hierarchy_elements_to_spawner_nodes(hierarchy, keys, remove_elements=True) -> Array[RigVMNode]
Convert Hierarchy Elements to Spawner Nodes

Args:
    hierarchy (RigHierarchy): 
    keys (Array[RigElementKey]): 
    remove_elements (bool): 

Returns:
    Array[RigVMNode]:

<a id="unreal.ControlRigBlueprint.can_turn_into_standalone_rig"></a>

#### can_turn_into_standalone_rig

```python
def can_turn_into_standalone_rig() -> bool
```

x.can_turn_into_standalone_rig() -> bool
Can Turn Into Standalone Rig Blueprint

Returns:
    bool:

<a id="unreal.ComputeDataProvider"></a>