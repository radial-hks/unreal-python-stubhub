## ControlRigBlueprintLibrary Objects

```python
class ControlRigBlueprintLibrary(RigVMBlueprintLibrary)
```

Control Rig Blueprint Editor Library

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRigEditor
- **File**: ControlRigBlueprintEditorLibrary.h

<a id="unreal.ControlRigBlueprintLibrary.setup_all_editor_menus"></a>

#### setup_all_editor_menus

```python
@classmethod
def setup_all_editor_menus(cls) -> None
```

X.setup_all_editor_menus() -> None
Setup All Editor Menus

<a id="unreal.ControlRigBlueprintLibrary.set_preview_mesh"></a>

#### set_preview_mesh

```python
@classmethod
def set_preview_mesh(cls,
                     rig_blueprint: ControlRigBlueprint,
                     preview_mesh: SkeletalMesh,
                     mark_as_dirty: bool = True) -> None
```

X.set_preview_mesh(rig_blueprint, preview_mesh, mark_as_dirty=True) -> None
Set Preview Mesh

Args:
    rig_blueprint (ControlRigBlueprint): 
    preview_mesh (SkeletalMesh): 
    mark_as_dirty (bool):

<a id="unreal.ControlRigBlueprintLibrary.request_control_rig_init"></a>

#### request_control_rig_init

```python
@classmethod
def request_control_rig_init(cls, rig_blueprint: ControlRigBlueprint) -> None
```

X.request_control_rig_init(rig_blueprint) -> None
Request Control Rig Init

Args:
    rig_blueprint (ControlRigBlueprint):

<a id="unreal.ControlRigBlueprintLibrary.get_preview_mesh"></a>

#### get_preview_mesh

```python
@classmethod
def get_preview_mesh(cls, rig_blueprint: ControlRigBlueprint) -> SkeletalMesh
```

X.get_preview_mesh(rig_blueprint) -> SkeletalMesh
Get Preview Mesh

Args:
    rig_blueprint (ControlRigBlueprint): 

Returns:
    SkeletalMesh:

<a id="unreal.ControlRigBlueprintLibrary.get_hierarchy_controller"></a>

#### get_hierarchy_controller

```python
@classmethod
def get_hierarchy_controller(
        cls, rig_blueprint: ControlRigBlueprint) -> RigHierarchyController
```

X.get_hierarchy_controller(rig_blueprint) -> RigHierarchyController
Get Hierarchy Controller

Args:
    rig_blueprint (ControlRigBlueprint): 

Returns:
    RigHierarchyController:

<a id="unreal.ControlRigBlueprintLibrary.get_hierarchy"></a>

#### get_hierarchy

```python
@classmethod
def get_hierarchy(cls, rig_blueprint: ControlRigBlueprint) -> RigHierarchy
```

X.get_hierarchy(rig_blueprint) -> RigHierarchy
Get Hierarchy

Args:
    rig_blueprint (ControlRigBlueprint): 

Returns:
    RigHierarchy:

<a id="unreal.ControlRigBlueprintLibrary.get_currently_open_rig_blueprints"></a>

#### get_currently_open_rig_blueprints

```python
@classmethod
def get_currently_open_rig_blueprints(cls) -> Array[ControlRigBlueprint]
```

X.get_currently_open_rig_blueprints() -> Array[ControlRigBlueprint]
Get Currently Open Rig Blueprints

Returns:
    Array[ControlRigBlueprint]:

<a id="unreal.ControlRigBlueprintLibrary.get_available_rig_units"></a>

#### get_available_rig_units

```python
@classmethod
def get_available_rig_units(cls) -> Array[Struct]
```

X.get_available_rig_units() -> Array[Struct]
Get Available Rig Units

Returns:
    Array[Struct]:

<a id="unreal.ControlRigBlueprintLibrary.get_available_rig_modules"></a>

#### get_available_rig_modules

```python
@classmethod
def get_available_rig_modules(cls) -> Array[RigModuleDescription]
```

X.get_available_rig_modules() -> Array[RigModuleDescription]
Get Available Rig Modules

Returns:
    Array[RigModuleDescription]:

<a id="unreal.ControlRigBlueprintLibrary.cast_to_control_rig_blueprint"></a>

#### cast_to_control_rig_blueprint

```python
@classmethod
def cast_to_control_rig_blueprint(
    cls, object: Object
) -> Tuple[CastToControlRigBlueprintCases, ControlRigBlueprint]
```

X.cast_to_control_rig_blueprint(object) -> (branches=CastToControlRigBlueprintCases, as_control_rig_blueprint=ControlRigBlueprint)
Cast to Control Rig Blueprint

Args:
    object (Object): 

Returns:
    tuple: 

    branches (CastToControlRigBlueprintCases): 

    as_control_rig_blueprint (ControlRigBlueprint):

<a id="unreal.ControlRigBlueprintFactory"></a>