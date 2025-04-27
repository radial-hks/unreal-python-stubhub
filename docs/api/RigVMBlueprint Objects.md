## RigVMBlueprint Objects

```python
class RigVMBlueprint(Blueprint)
```

Rig VMBlueprint

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMBlueprint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_variant`` (RigVMVariant):  [Read-Write] Variant information about this asset
- ``blueprint_category`` (str):  [Read-Write] The category of the Blueprint, used to organize this Blueprint class when displayed in palette windows
- ``blueprint_description`` (str):  [Read-Write] Shows up in the content browser tooltip when the blueprint is hovered
- ``blueprint_display_name`` (str):  [Read-Write] Overrides the BP's display name in the editor UI
- ``blueprint_namespace`` (str):  [Read-Write] The namespace of this blueprint (if set, the Blueprint will be treated differently for the context menu)
- ``compile_mode`` (BlueprintCompileMode):  [Read-Write] The mode that will be used when compiling this class.
- ``deprecate`` (bool):  [Read-Write] Deprecates the Blueprint, marking the generated class with the CLASS_Deprecated flag
- ``generate_abstract_class`` (bool):  [Read-Write] Whether or not this blueprint's class is a abstract class or not.  Should set CLASS_Abstract in the KismetCompiler.
- ``generate_const_class`` (bool):  [Read-Write] Whether or not this blueprint's class is a const class or not.  Should set CLASS_Const in the KismetCompiler.
- ``hide_categories`` (Array[str]):  [Read-Write] Additional HideCategories. These are added to HideCategories from parent.
- ``python_log_settings`` (RigVMPythonSettings):  [Read-Write]
- ``rig_graph_display_settings`` (RigVMEdGraphDisplaySettings):  [Read-Write]
- ``run_construction_script_in_sequencer`` (bool):  [Read-Write] whether or not you want to continuously rerun the construction script for an actor in sequencer
- ``run_construction_script_on_drag`` (bool):  [Read-Write] whether or not you want to continuously rerun the construction script for an actor as you drag it in the editor, or only when the drag operation is complete
- ``should_cook_property_guids_value`` (ShouldCookBlueprintPropertyGuids):  [Read-Write] Whether to include the property GUIDs for the generated class in a cooked build.
  note: This option may slightly increase memory usage in a cooked build, but can avoid needing to add CoreRedirect data for Blueprint classes stored within SaveGame archives.
- ``thumbnail_info`` (ThumbnailInfo):  [Read-Only] Information for thumbnail rendering
- ``vm_compile_settings`` (RigVMCompileSettings):  [Read-Write]
- ``vm_runtime_settings`` (RigVMRuntimeSettings):  [Read-Write]

<a id="unreal.RigVMBlueprint.vm_compile_settings"></a>

#### vm_compile_settings

```python
@property
def vm_compile_settings() -> RigVMCompileSettings
```

(RigVMCompileSettings):  [Read-Write]

<a id="unreal.RigVMBlueprint.vm_compile_settings"></a>

#### vm_compile_settings

```python
@vm_compile_settings.setter
def vm_compile_settings(value: RigVMCompileSettings) -> None
```

<a id="unreal.RigVMBlueprint.suspend_notifications"></a>

#### suspend_notifications

```python
def suspend_notifications(suspend_notifs: bool) -> None
```

x.suspend_notifications(suspend_notifs) -> None
Suspend Notifications

Args:
    suspend_notifs (bool):

<a id="unreal.RigVMBlueprint.split_asset_variant"></a>

#### split_asset_variant

```python
def split_asset_variant() -> bool
```

x.split_asset_variant() -> bool
Resets the asset's guid to a new one and splits it from the former variant set

Returns:
    bool:

<a id="unreal.RigVMBlueprint.set_auto_vm_recompile"></a>

#### set_auto_vm_recompile

```python
def set_auto_vm_recompile(auto_recompile: bool) -> None
```

x.set_auto_vm_recompile(auto_recompile) -> None
Set Auto VMRecompile

Args:
    auto_recompile (bool):

<a id="unreal.RigVMBlueprint.request_rig_vm_init"></a>

#### request_rig_vm_init

```python
def request_rig_vm_init() -> None
```

x.request_rig_vm_init() -> None
Request Rig VMInit

<a id="unreal.RigVMBlueprint.request_auto_vm_recompilation"></a>

#### request_auto_vm_recompilation

```python
def request_auto_vm_recompilation() -> None
```

x.request_auto_vm_recompilation() -> None
Request Auto VMRecompilation

<a id="unreal.RigVMBlueprint.rename_member_variable"></a>

#### rename_member_variable

```python
def rename_member_variable(old_name: Name, new_name: Name) -> bool
```

x.rename_member_variable(old_name, new_name) -> bool
Rename Member Variable

Args:
    old_name (Name): 
    new_name (Name): 

Returns:
    bool:

<a id="unreal.RigVMBlueprint.remove_model"></a>

#### remove_model

```python
def remove_model(name: str = "Rig Graph",
                 setup_undo_redo: bool = True,
                 print_python_command: bool = True) -> bool
```

x.remove_model(name="Rig Graph", setup_undo_redo=True, print_python_command=True) -> bool
Remove Model

Args:
    name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMBlueprint.remove_member_variable"></a>

#### remove_member_variable

```python
def remove_member_variable(name: Name) -> bool
```

x.remove_member_variable(name) -> bool
Remove Member Variable

Args:
    name (Name): 

Returns:
    bool:

<a id="unreal.RigVMBlueprint.recompile_vm_if_required"></a>

#### recompile_vm_if_required

```python
def recompile_vm_if_required() -> None
```

x.recompile_vm_if_required() -> None
Recompile VMIf Required

<a id="unreal.RigVMBlueprint.recompile_vm"></a>

#### recompile_vm

```python
def recompile_vm() -> None
```

x.recompile_vm() -> None
Recompile VM

<a id="unreal.RigVMBlueprint.join_asset_variant"></a>

#### join_asset_variant

```python
def join_asset_variant(guid: Guid) -> bool
```

x.join_asset_variant(guid) -> bool
Merges the asset's guid with a provided one to join the variant set

Args:
    guid (Guid): 

Returns:
    bool:

<a id="unreal.RigVMBlueprint.get_rig_vm_host_class"></a>

#### get_rig_vm_host_class

```python
def get_rig_vm_host_class() -> Class
```

x.get_rig_vm_host_class() -> type(Class)
Get Rig VMHost Class

Returns:
    type(Class):

<a id="unreal.RigVMBlueprint.get_or_create_local_function_library"></a>

#### get_or_create_local_function_library

```python
def get_or_create_local_function_library(
        setup_undo_redo: bool = True) -> RigVMFunctionLibrary
```

x.get_or_create_local_function_library(setup_undo_redo=True) -> RigVMFunctionLibrary
Get or Create Local Function Library

Args:
    setup_undo_redo (bool): 

Returns:
    RigVMFunctionLibrary:

<a id="unreal.RigVMBlueprint.get_or_create_controller"></a>

#### get_or_create_controller

```python
def get_or_create_controller(graph: RigVMGraph = None) -> RigVMController
```

x.get_or_create_controller(graph=None) -> RigVMController
Get or Create Controller

Args:
    graph (RigVMGraph): 

Returns:
    RigVMController:

<a id="unreal.RigVMBlueprint.get_model"></a>

#### get_model

```python
def get_model(ed_graph: EdGraph = None) -> RigVMGraph
```

x.get_model(ed_graph=None) -> RigVMGraph
Get Model

Args:
    ed_graph (EdGraph): 

Returns:
    RigVMGraph:

<a id="unreal.RigVMBlueprint.get_member_variables"></a>

#### get_member_variables

```python
def get_member_variables() -> Array[RigVMGraphVariableDescription]
```

x.get_member_variables() -> Array[RigVMGraphVariableDescription]
Get Member Variables

Returns:
    Array[RigVMGraphVariableDescription]:

<a id="unreal.RigVMBlueprint.get_matching_variants"></a>

#### get_matching_variants

```python
def get_matching_variants() -> Array[RigVMVariantRef]
```

x.get_matching_variants() -> Array[RigVMVariantRef]
Get Matching Variants

Returns:
    Array[RigVMVariantRef]:

<a id="unreal.RigVMBlueprint.get_local_function_library"></a>

#### get_local_function_library

```python
def get_local_function_library() -> RigVMFunctionLibrary
```

x.get_local_function_library() -> RigVMFunctionLibrary
Get Local Function Library

Returns:
    RigVMFunctionLibrary:

<a id="unreal.RigVMBlueprint.get_focused_model"></a>

#### get_focused_model

```python
def get_focused_model() -> RigVMGraph
```

x.get_focused_model() -> RigVMGraph
Get Focused Model

Returns:
    RigVMGraph:

<a id="unreal.RigVMBlueprint.get_default_model"></a>

#### get_default_model

```python
def get_default_model() -> RigVMGraph
```

x.get_default_model() -> RigVMGraph
Get Default Model

Returns:
    RigVMGraph:

<a id="unreal.RigVMBlueprint.get_debugged_rig_vm_host"></a>

#### get_debugged_rig_vm_host

```python
def get_debugged_rig_vm_host() -> RigVMHost
```

x.get_debugged_rig_vm_host() -> RigVMHost
Get Debugged Rig VMHost

Returns:
    RigVMHost:

<a id="unreal.RigVMBlueprint.get_controller_by_name"></a>

#### get_controller_by_name

```python
def get_controller_by_name(graph_name: str = "") -> RigVMController
```

x.get_controller_by_name(graph_name="") -> RigVMController
Get Controller by Name

Args:
    graph_name (str): 

Returns:
    RigVMController:

<a id="unreal.RigVMBlueprint.get_controller"></a>

#### get_controller

```python
def get_controller(graph: RigVMGraph = None) -> RigVMController
```

x.get_controller(graph=None) -> RigVMController
Get Controller

Args:
    graph (RigVMGraph): 

Returns:
    RigVMController:

<a id="unreal.RigVMBlueprint.get_available_rig_vm_structs"></a>

#### get_available_rig_vm_structs

```python
def get_available_rig_vm_structs() -> Array[Struct]
```

x.get_available_rig_vm_structs() -> Array[Struct]
Get Available Rig VMStructs

Returns:
    Array[Struct]:

<a id="unreal.RigVMBlueprint.get_auto_vm_recompile"></a>

#### get_auto_vm_recompile

```python
def get_auto_vm_recompile() -> bool
```

x.get_auto_vm_recompile() -> bool
Get Auto VMRecompile

Returns:
    bool:

<a id="unreal.RigVMBlueprint.get_asset_variant"></a>

#### get_asset_variant

```python
def get_asset_variant() -> RigVMVariant
```

x.get_asset_variant() -> RigVMVariant
Get Asset Variant BP

Returns:
    RigVMVariant:

<a id="unreal.RigVMBlueprint.get_all_models"></a>

#### get_all_models

```python
def get_all_models() -> Array[RigVMGraph]
```

x.get_all_models() -> Array[RigVMGraph]
Get All Models

Returns:
    Array[RigVMGraph]:

<a id="unreal.RigVMBlueprint.generate_python_commands"></a>

#### generate_python_commands

```python
def generate_python_commands(new_blueprint_name: str) -> Array[str]
```

x.generate_python_commands(new_blueprint_name) -> Array[str]
Generate Python Commands

Args:
    new_blueprint_name (str): 

Returns:
    Array[str]:

<a id="unreal.RigVMBlueprint.create_rig_vm_host"></a>

#### create_rig_vm_host

```python
def create_rig_vm_host() -> RigVMHost
```

x.create_rig_vm_host() -> RigVMHost
Create Rig VMHost

Returns:
    RigVMHost:

<a id="unreal.RigVMBlueprint.change_member_variable_type"></a>

#### change_member_variable_type

```python
def change_member_variable_type(name: Name,
                                cpp_type: str,
                                is_public: bool = False,
                                is_read_only: bool = False,
                                default_value: str = "") -> bool
```

x.change_member_variable_type(name, cpp_type, is_public=False, is_read_only=False, default_value="") -> bool
Change Member Variable Type

Args:
    name (Name): 
    cpp_type (str): 
    is_public (bool): 
    is_read_only (bool): 
    default_value (str): 

Returns:
    bool:

<a id="unreal.RigVMBlueprint.add_model"></a>

#### add_model

```python
def add_model(name: str = "Rig Graph",
              setup_undo_redo: bool = True,
              print_python_command: bool = True) -> RigVMGraph
```

x.add_model(name="Rig Graph", setup_undo_redo=True, print_python_command=True) -> RigVMGraph
Add Model

Args:
    name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMGraph:

<a id="unreal.RigVMBlueprint.add_member_variable"></a>

#### add_member_variable

```python
def add_member_variable(name: Name,
                        cpp_type: str,
                        is_public: bool = False,
                        is_read_only: bool = False,
                        default_value: str = "") -> Name
```

x.add_member_variable(name, cpp_type, is_public=False, is_read_only=False, default_value="") -> Name
Add Member Variable

Args:
    name (Name): 
    cpp_type (str): 
    is_public (bool): 
    is_read_only (bool): 
    default_value (str): 

Returns:
    Name:

<a id="unreal.RigVMCompiler"></a>