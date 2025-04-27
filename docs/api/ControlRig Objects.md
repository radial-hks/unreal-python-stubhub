## ControlRig Objects

```python
class ControlRig(RigVMHost)
```

Runs logic for mapping input data to transforms (the "Rig")

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: ControlRig.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``on_control_selected_bp`` (OnControlSelectedBP):  [Read-Write]

<a id="unreal.ControlRig.on_control_selected_bp"></a>

#### on_control_selected_bp

```python
@property
def on_control_selected_bp() -> OnControlSelectedBP
```

(OnControlSelectedBP):  [Read-Write]

<a id="unreal.ControlRig.on_control_selected_bp"></a>

#### on_control_selected_bp

```python
@on_control_selected_bp.setter
def on_control_selected_bp(value: OnControlSelectedBP) -> None
```

<a id="unreal.ControlRig.supports_backwards_solve"></a>

#### supports_backwards_solve

```python
def supports_backwards_solve() -> bool
```

x.supports_backwards_solve() -> bool
Contains a backwards solve event

Returns:
    bool:

<a id="unreal.ControlRig.select_control"></a>

#### select_control

```python
def select_control(control_name: Name, select: bool = True) -> None
```

x.select_control(control_name, select=True) -> None
Select Control

Args:
    control_name (Name): 
    select (bool):

<a id="unreal.ControlRig.request_construction"></a>

#### request_construction

```python
def request_construction() -> None
```

x.request_construction() -> None
Requests to perform construction during the next execution

<a id="unreal.ControlRig.is_control_selected"></a>

#### is_control_selected

```python
def is_control_selected(control_name: Name) -> bool
```

x.is_control_selected(control_name) -> bool
Is Control Selected

Args:
    control_name (Name): 

Returns:
    bool:

<a id="unreal.ControlRig.get_hosting_actor"></a>

#### get_hosting_actor

```python
def get_hosting_actor() -> Actor
```

x.get_hosting_actor() -> Actor
Find the actor the rig is bound to, if any

Returns:
    Actor:

<a id="unreal.ControlRig.get_hierarchy"></a>

#### get_hierarchy

```python
def get_hierarchy() -> RigHierarchy
```

x.get_hierarchy() -> RigHierarchy
Get Hierarchy

Returns:
    RigHierarchy:

<a id="unreal.ControlRig.find_control_rigs"></a>

#### find_control_rigs

```python
@classmethod
def find_control_rigs(cls, outer: Object,
                      optional_class: Class) -> Array[ControlRig]
```

X.find_control_rigs(outer, optional_class) -> Array[ControlRig]
Find Control Rigs

Args:
    outer (Object): 
    optional_class (type(Class)): 

Returns:
    Array[ControlRig]:

<a id="unreal.ControlRig.current_control_selection"></a>

#### current_control_selection

```python
def current_control_selection() -> Array[Name]
```

x.current_control_selection() -> Array[Name]
Current Control Selection

Returns:
    Array[Name]:

<a id="unreal.ControlRig.create_transformable_control_handle"></a>

#### create_transformable_control_handle

```python
def create_transformable_control_handle(
        control_name: Name) -> TransformableControlHandle
```

x.create_transformable_control_handle(control_name) -> TransformableControlHandle
Creates a transformable control handle for the specified control to be used by the constraints system. Should use the UObject from
      ConstraintsScriptingLibrary::GetManager(UWorld* InWorld)

Args:
    control_name (Name): 

Returns:
    TransformableControlHandle:

<a id="unreal.ControlRig.clear_control_selection"></a>

#### clear_control_selection

```python
def clear_control_selection() -> bool
```

x.clear_control_selection() -> bool
Clear Control Selection

Returns:
    bool:

<a id="unreal.ControlRig.add_physics_solver"></a>

#### add_physics_solver

```python
def add_physics_solver(
        name: Name,
        setup_undo: bool = False,
        print_python_command: bool = False) -> RigPhysicsSolverID
```

x.add_physics_solver(name, setup_undo=False, print_python_command=False) -> RigPhysicsSolverID
Adds a physics solver to the hierarchy

Args:
    name (Name): The suggested name of the new physics solver - will eventually be corrected by the namespace
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_command (bool): If set to true a python command equivalent to this call will be printed out

Returns:
    RigPhysicsSolverID: The ID for the newly created physics solver.

<a id="unreal.ModularRig"></a>