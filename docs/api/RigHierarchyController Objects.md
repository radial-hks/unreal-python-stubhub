## RigHierarchyController Objects

```python
class RigHierarchyController(Object)
```

Rig Hierarchy Controller

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigHierarchyController.h

<a id="unreal.RigHierarchyController.set_selection"></a>

#### set_selection

```python
def set_selection(keys: Array[RigElementKey],
                  print_python_command: bool = False) -> bool
```

x.set_selection(keys, print_python_command=False) -> bool
Sets the selection based on a list of keys

Args:
    keys (Array[RigElementKey]): The array of keys of the elements to select
    print_python_command (bool): 

Returns:
    bool: Returns true if the selection was applied

<a id="unreal.RigHierarchyController.set_parent"></a>

#### set_parent

```python
def set_parent(child: RigElementKey,
               parent: RigElementKey,
               maintain_global_transform: bool = True,
               setup_undo: bool = False,
               print_python_command: bool = False) -> bool
```

x.set_parent(child, parent, maintain_global_transform=True, setup_undo=False, print_python_command=False) -> bool
Sets a new parent to an element. For elements that allow more than one parent the parent list will be replaced.

Args:
    child (RigElementKey): The key of the element to set the parent for
    parent (RigElementKey): The key of the new parent to set
    maintain_global_transform (bool): If set to true the child will stay in the same place spatially, otherwise it will maintain it's local transform (and potential move).
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_command (bool): If set to true a python command equivalent to this call will be printed out

Returns:
    bool: Returns true if successful.

<a id="unreal.RigHierarchyController.set_hierarchy"></a>

#### set_hierarchy

```python
def set_hierarchy(hierarchy: RigHierarchy) -> None
```

x.set_hierarchy(hierarchy) -> None
Sets the hierarchy currently linked to this controller

Args:
    hierarchy (RigHierarchy):

<a id="unreal.RigHierarchyController.set_display_name"></a>

#### set_display_name

```python
def set_display_name(control: RigElementKey,
                     display_name: Name,
                     rename_element: bool = False,
                     setup_undo: bool = False,
                     print_python_command: bool = False) -> Name
```

x.set_display_name(control, display_name, rename_element=False, setup_undo=False, print_python_command=False) -> Name
Sets the display name on a control

Args:
    control (RigElementKey): The key of the control to change the display name for
    display_name (Name): The new display name to set for the control
    rename_element (bool): True if the control should also be renamed
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_command (bool): If set to true a python command equivalent to this call will be printed out

Returns:
    Name: Returns the new display name used for the control

<a id="unreal.RigHierarchyController.set_control_settings"></a>

#### set_control_settings

```python
def set_control_settings(key: RigElementKey,
                         settings: RigControlSettings,
                         setup_undo: bool = False) -> bool
```

x.set_control_settings(key, settings, setup_undo=False) -> bool
Sets a control's settings given a control key

Args:
    key (RigElementKey): The key of the control to set the settings for
    settings (RigControlSettings): 
    setup_undo (bool): 

Returns:
    bool: Returns true if the settings have been set correctly

<a id="unreal.RigHierarchyController.set_available_space_index"></a>

#### set_available_space_index

```python
def set_available_space_index(control: RigElementKey,
                              space: RigElementKey,
                              index: int,
                              setup_undo: bool = False,
                              print_python_command: bool = False) -> bool
```

x.set_available_space_index(control, space, index, setup_undo=False, print_python_command=False) -> bool
Reorders an available space for the given control

Args:
    control (RigElementKey): The control to reorder the host for
    space (RigElementKey): The space to set the new index for
    index (int32): The new index of the available space
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_command (bool): If set to true a python command equivalent to this call will be printed out

Returns:
    bool: Returns true if successful.

<a id="unreal.RigHierarchyController.select_element"></a>

#### select_element

```python
def select_element(key: RigElementKey,
                   select: bool = True,
                   clear_selection: bool = False) -> bool
```

x.select_element(key, select=True, clear_selection=False) -> bool
Selects or deselects an element in the hierarchy

Args:
    key (RigElementKey): The key of the element to select
    select (bool): If set to false the element will be deselected
    clear_selection (bool): 

Returns:
    bool: Returns true if the selection was applied

<a id="unreal.RigHierarchyController.reorder_element"></a>

#### reorder_element

```python
def reorder_element(element: RigElementKey,
                    index: int,
                    setup_undo: bool = False,
                    print_python_command: bool = False) -> bool
```

x.reorder_element(element, index, setup_undo=False, print_python_command=False) -> bool
Changes the element's index within its default parent (or the top level)

Args:
    element (RigElementKey): The key of the element to rename
    index (int32): The new index of the element to take within its default parent (or the top level)
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_command (bool): If set to true a python command equivalent to this call will be printed out

Returns:
    bool: Returns true if the element has been reordered accordingly

<a id="unreal.RigHierarchyController.rename_element"></a>

#### rename_element

```python
def rename_element(element: RigElementKey,
                   name: Name,
                   setup_undo: bool = False,
                   print_python_command: bool = False,
                   clear_selection: bool = True) -> RigElementKey
```

x.rename_element(element, name, setup_undo=False, print_python_command=False, clear_selection=True) -> RigElementKey
Renames an existing element in the hierarchy

Args:
    element (RigElementKey): The key of the element to rename
    name (Name): The new name to set for the element
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_command (bool): If set to true a python command equivalent to this call will be printed out
    clear_selection (bool): True if the selection should be cleared after a rename

Returns:
    RigElementKey: Returns the new element key used for the element

<a id="unreal.RigHierarchyController.remove_parent"></a>

#### remove_parent

```python
def remove_parent(child: RigElementKey,
                  parent: RigElementKey,
                  maintain_global_transform: bool = True,
                  setup_undo: bool = False,
                  print_python_command: bool = False) -> bool
```

x.remove_parent(child, parent, maintain_global_transform=True, setup_undo=False, print_python_command=False) -> bool
Removes an existing parent from an element in the hierarchy. For elements that allow only one parent the element will be unparented (same as ::RemoveAllParents)

Args:
    child (RigElementKey): The key of the element to remove the parent for
    parent (RigElementKey): The key of the parent to remove
    maintain_global_transform (bool): If set to true the child will stay in the same place spatially, otherwise it will maintain it's local transform (and potential move).
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_command (bool): If set to true a python command equivalent to this call will be printed out

Returns:
    bool: Returns true if successful.

<a id="unreal.RigHierarchyController.remove_element"></a>

#### remove_element

```python
def remove_element(element: RigElementKey,
                   setup_undo: bool = False,
                   print_python_command: bool = False) -> bool
```

x.remove_element(element, setup_undo=False, print_python_command=False) -> bool
Removes an existing element from the hierarchy

Args:
    element (RigElementKey): The key of the element to remove
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_command (bool): If set to true a python command equivalent to this call will be printed out

Returns:
    bool: Returns true if successful.

<a id="unreal.RigHierarchyController.remove_channel_host"></a>

#### remove_channel_host

```python
def remove_channel_host(channel: RigElementKey,
                        host: RigElementKey,
                        setup_undo: bool = False,
                        print_python_command: bool = False) -> bool
```

x.remove_channel_host(channel, host, setup_undo=False, print_python_command=False) -> bool
Removes an channel host from the animation channel
note: This is just an overload of RemoveAvailableSpace for readability

Args:
    channel (RigElementKey): The animation channel to remove the channel host from
    host (RigElementKey): The host to remove from the channel from
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_command (bool): If set to true a python command equivalent to this call will be printed out

Returns:
    bool: Returns true if successful.

<a id="unreal.RigHierarchyController.remove_available_space"></a>

#### remove_available_space

```python
def remove_available_space(control: RigElementKey,
                           space: RigElementKey,
                           setup_undo: bool = False,
                           print_python_command: bool = False) -> bool
```

x.remove_available_space(control, space, setup_undo=False, print_python_command=False) -> bool
Removes an available space from the given control

Args:
    control (RigElementKey): The control to remove the available space from
    space (RigElementKey): The space to remove from the available spaces list
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_command (bool): If set to true a python command equivalent to this call will be printed out

Returns:
    bool: Returns true if successful.

<a id="unreal.RigHierarchyController.remove_all_parents"></a>

#### remove_all_parents

```python
def remove_all_parents(child: RigElementKey,
                       maintain_global_transform: bool = True,
                       setup_undo: bool = False,
                       print_python_command: bool = False) -> bool
```

x.remove_all_parents(child, maintain_global_transform=True, setup_undo=False, print_python_command=False) -> bool
Removes all parents from an element in the hierarchy.

Args:
    child (RigElementKey): The key of the element to remove all parents for
    maintain_global_transform (bool): If set to true the child will stay in the same place spatially, otherwise it will maintain it's local transform (and potential move).
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_command (bool): If set to true a python command equivalent to this call will be printed out

Returns:
    bool: Returns true if successful.

<a id="unreal.RigHierarchyController.mirror_elements"></a>

#### mirror_elements

```python
def mirror_elements(
        keys: Array[RigElementKey],
        settings: RigVMMirrorSettings,
        select_new_elements: bool = True,
        setup_undo: bool = False,
        print_python_commands: bool = False) -> Array[RigElementKey]
```

x.mirror_elements(keys, settings, select_new_elements=True, setup_undo=False, print_python_commands=False) -> Array[RigElementKey]
Mirrors the given elements

Args:
    keys (Array[RigElementKey]): The keys of the elements to mirror
    settings (RigVMMirrorSettings): The settings to use for the mirror operation
    select_new_elements (bool): If set to true the new elements will be selected
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_commands (bool): 

Returns:
    Array[RigElementKey]: The keys of the mirrored items

<a id="unreal.RigHierarchyController.import_from_text"></a>

#### import_from_text

```python
def import_from_text(
        content: str,
        replace_existing_elements: bool = False,
        select_new_elements: bool = True,
        setup_undo: bool = False,
        print_python_commands: bool = False) -> Array[RigElementKey]
```

x.import_from_text(content, replace_existing_elements=False, select_new_elements=True, setup_undo=False, print_python_commands=False) -> Array[RigElementKey]
Imports the content of a text buffer to the hierarchy

Args:
    content (str): The string buffer representing the content to import
    replace_existing_elements (bool): If set to true existing items will be replaced / updated with the content in the buffer
    select_new_elements (bool): If set to true the new elements will be selected
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_commands (bool): 

Returns:
    Array[RigElementKey]:

<a id="unreal.RigHierarchyController.import_curves_from_skeletal_mesh"></a>

#### import_curves_from_skeletal_mesh

```python
def import_curves_from_skeletal_mesh(
        skeletal_mesh: SkeletalMesh,
        name_space: Name = "None",
        select_curves: bool = False,
        setup_undo: bool = False,
        print_python_command: bool = False) -> Array[RigElementKey]
```

x.import_curves_from_skeletal_mesh(skeletal_mesh, name_space="None", select_curves=False, setup_undo=False, print_python_command=False) -> Array[RigElementKey]
Imports all curves from a skeletalmesh to the hierarchy

Args:
    skeletal_mesh (SkeletalMesh): The skeletalmesh to import the curves from
    name_space (Name): The namespace to prefix the bone names with
    select_curves (bool): If true the curves will be selected upon import
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_command (bool): 

Returns:
    Array[RigElementKey]: The keys of the imported elements

<a id="unreal.RigHierarchyController.import_curves_from_asset"></a>

#### import_curves_from_asset

```python
def import_curves_from_asset(asset_path: str,
                             name_space: Name = "None",
                             select_curves: bool = False,
                             setup_undo: bool = False) -> Array[RigElementKey]
```

x.import_curves_from_asset(asset_path, name_space="None", select_curves=False, setup_undo=False) -> Array[RigElementKey]
Imports all curves from a skeleton to the hierarchy

Args:
    asset_path (str): The path to the uasset to import from
    name_space (Name): The namespace to prefix the bone names with
    select_curves (bool): If true the curves will be selected upon import
    setup_undo (bool): If set to true the stack will record the change for undo / redo

Returns:
    Array[RigElementKey]: The keys of the imported elements

<a id="unreal.RigHierarchyController.import_curves"></a>

#### import_curves

```python
def import_curves(skeleton: Skeleton,
                  name_space: Name = "None",
                  select_curves: bool = False,
                  setup_undo: bool = False,
                  print_python_command: bool = False) -> Array[RigElementKey]
```

x.import_curves(skeleton, name_space="None", select_curves=False, setup_undo=False, print_python_command=False) -> Array[RigElementKey]
Imports all curves from a skeleton to the hierarchy

Args:
    skeleton (Skeleton): The skeleton to import the curves from
    name_space (Name): The namespace to prefix the bone names with
    select_curves (bool): If true the curves will be selected upon import
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_command (bool): 

Returns:
    Array[RigElementKey]: The keys of the imported elements

<a id="unreal.RigHierarchyController.import_bones_from_asset"></a>

#### import_bones_from_asset

```python
def import_bones_from_asset(asset_path: str,
                            name_space: Name = "None",
                            replace_existing_bones: bool = True,
                            remove_obsolete_bones: bool = True,
                            select_bones: bool = False,
                            setup_undo: bool = False) -> Array[RigElementKey]
```

x.import_bones_from_asset(asset_path, name_space="None", replace_existing_bones=True, remove_obsolete_bones=True, select_bones=False, setup_undo=False) -> Array[RigElementKey]
Imports an existing skeleton to the hierarchy

Args:
    asset_path (str): The path to the uasset to import from
    name_space (Name): The namespace to prefix the bone names with
    replace_existing_bones (bool): If true existing bones will be removed
    remove_obsolete_bones (bool): If true bones non-existent in the skeleton will be removed from the hierarchy
    select_bones (bool): If true the bones will be selected upon import
    setup_undo (bool): If set to true the stack will record the change for undo / redo

Returns:
    Array[RigElementKey]: The keys of the imported elements

<a id="unreal.RigHierarchyController.import_bones"></a>

#### import_bones

```python
def import_bones(skeleton: Skeleton,
                 name_space: Name = "None",
                 replace_existing_bones: bool = True,
                 remove_obsolete_bones: bool = True,
                 select_bones: bool = False,
                 setup_undo: bool = False,
                 print_python_command: bool = False) -> Array[RigElementKey]
```

x.import_bones(skeleton, name_space="None", replace_existing_bones=True, remove_obsolete_bones=True, select_bones=False, setup_undo=False, print_python_command=False) -> Array[RigElementKey]
Imports an existing skeleton to the hierarchy

Args:
    skeleton (Skeleton): The skeleton to import
    name_space (Name): The namespace to prefix the bone names with
    replace_existing_bones (bool): If true existing bones will be removed
    remove_obsolete_bones (bool): If true bones non-existent in the skeleton will be removed from the hierarchy
    select_bones (bool): If true the bones will be selected upon import
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_command (bool): If set to true a python command equivalent to this call will be printed out

Returns:
    Array[RigElementKey]: The keys of the imported elements

<a id="unreal.RigHierarchyController.get_hierarchy"></a>

#### get_hierarchy

```python
def get_hierarchy() -> RigHierarchy
```

x.get_hierarchy() -> RigHierarchy
Returns the hierarchy currently linked to this controller

Returns:
    RigHierarchy:

<a id="unreal.RigHierarchyController.get_control_settings"></a>

#### get_control_settings

```python
def get_control_settings(key: RigElementKey) -> RigControlSettings
```

x.get_control_settings(key) -> RigControlSettings
Returns the control settings of a given control

Args:
    key (RigElementKey): The key of the control to receive the settings for

Returns:
    RigControlSettings: The settings of the given control

<a id="unreal.RigHierarchyController.generate_python_commands"></a>

#### generate_python_commands

```python
def generate_python_commands() -> Array[str]
```

x.generate_python_commands() -> Array[str]
Generate Python Commands

Returns:
    Array[str]:

<a id="unreal.RigHierarchyController.export_to_text"></a>

#### export_to_text

```python
def export_to_text(keys: Array[RigElementKey]) -> str
```

x.export_to_text(keys) -> str
Exports a list of items to text

Args:
    keys (Array[RigElementKey]): The keys to export to text

Returns:
    str: The text representation of the requested elements

<a id="unreal.RigHierarchyController.export_selection_to_text"></a>

#### export_selection_to_text

```python
def export_selection_to_text() -> str
```

x.export_selection_to_text() -> str
Exports the selected items to text

Returns:
    str: The text representation of the selected items

<a id="unreal.RigHierarchyController.duplicate_elements"></a>

#### duplicate_elements

```python
def duplicate_elements(
        keys: Array[RigElementKey],
        select_new_elements: bool = True,
        setup_undo: bool = False,
        print_python_commands: bool = False) -> Array[RigElementKey]
```

x.duplicate_elements(keys, select_new_elements=True, setup_undo=False, print_python_commands=False) -> Array[RigElementKey]
Duplicate the given elements

Args:
    keys (Array[RigElementKey]): The keys of the elements to duplicate
    select_new_elements (bool): If set to true the new elements will be selected
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_commands (bool): 

Returns:
    Array[RigElementKey]: The keys of the 4d items

<a id="unreal.RigHierarchyController.deselect_element"></a>

#### deselect_element

```python
def deselect_element(key: RigElementKey) -> bool
```

x.deselect_element(key) -> bool
Deselects or deselects an element in the hierarchy

Args:
    key (RigElementKey): The key of the element to deselect

Returns:
    bool: Returns true if the selection was applied

<a id="unreal.RigHierarchyController.clear_selection"></a>

#### clear_selection

```python
def clear_selection() -> bool
```

x.clear_selection() -> bool
Clears the selection

Returns:
    bool: Returns true if the selection was applied

<a id="unreal.RigHierarchyController.add_socket"></a>

#### add_socket

```python
def add_socket(name: Name,
               parent: RigElementKey,
               transform: Transform,
               transform_in_global: bool = True,
               color: LinearColor = [1.000000, 1.000000, 1.000000, 1.000000],
               description: str = "",
               setup_undo: bool = False,
               print_python_command: bool = False) -> RigElementKey
```

x.add_socket(name, parent, transform, transform_in_global=True, color=[1.000000, 1.000000, 1.000000, 1.000000], description="", setup_undo=False, print_python_command=False) -> RigElementKey
Adds a socket to the hierarchy

Args:
    name (Name): The suggested name of the new socket - will eventually be corrected by the namespace
    parent (RigElementKey): The (optional) parent of the new null. If you don't need a parent, pass FRigElementKey()
    transform (Transform): The transform for the new socket - either in local or global space, based on bTransformInGlobal
    transform_in_global (bool): Set this to true if the Transform passed is expressed in global space, false for local space.
    color (LinearColor): The color of the socket
    description (str): The description of the socket
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_command (bool): If set to true a python command equivalent to this call will be printed out

Returns:
    RigElementKey: The key for the newly created bone.

<a id="unreal.RigHierarchyController.add_physics_element"></a>

#### add_physics_element

```python
def add_physics_element(name: Name,
                        parent: RigElementKey,
                        solver: RigPhysicsSolverID,
                        settings: RigPhysicsSettings,
                        local_transform: Transform,
                        setup_undo: bool = False,
                        print_python_command: bool = False) -> RigElementKey
```

x.add_physics_element(name, parent, solver, settings, local_transform, setup_undo=False, print_python_command=False) -> RigElementKey
Adds a physics element to the hierarchy

Args:
    name (Name): The suggested name of the new physics element - will eventually be corrected by the namespace
    parent (RigElementKey): The (optional) parent of the new physics element. If you don't need a parent, pass FRigElementKey()
    solver (RigPhysicsSolverID): The guid identifying the solver to use
    settings (RigPhysicsSettings): All of the physics element's settings
    local_transform (Transform): The transform for the new physics element - in the space of the provided parent
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_command (bool): If set to true a python command equivalent to this call will be printed out

Returns:
    RigElementKey: The key for the newly created physics element.

<a id="unreal.RigHierarchyController.add_parent"></a>

#### add_parent

```python
def add_parent(child: RigElementKey,
               parent: RigElementKey,
               weight: float = 0.000000,
               maintain_global_transform: bool = True,
               setup_undo: bool = False) -> bool
```

x.add_parent(child, parent, weight=0.000000, maintain_global_transform=True, setup_undo=False) -> bool
Adds a new parent to an element. For elements that allow only one parent the parent will be replaced (Same as ::SetParent).

Args:
    child (RigElementKey): The key of the element to add the parent for
    parent (RigElementKey): The key of the new parent to add
    weight (float): The initial weight to give to the parent
    maintain_global_transform (bool): If set to true the child will stay in the same place spatially, otherwise it will maintain it's local transform (and potential move).
    setup_undo (bool): If set to true the stack will record the change for undo / redo

Returns:
    bool: Returns true if successful.

<a id="unreal.RigHierarchyController.add_null"></a>

#### add_null

```python
def add_null(name: Name,
             parent: RigElementKey,
             transform: Transform,
             transform_in_global: bool = True,
             setup_undo: bool = False,
             print_python_command: bool = False) -> RigElementKey
```

x.add_null(name, parent, transform, transform_in_global=True, setup_undo=False, print_python_command=False) -> RigElementKey
Adds a null to the hierarchy

Args:
    name (Name): The suggested name of the new null - will eventually be corrected by the namespace
    parent (RigElementKey): The (optional) parent of the new null. If you don't need a parent, pass FRigElementKey()
    transform (Transform): The transform for the new null - either in local or global null, based on bTransformInGlobal
    transform_in_global (bool): Set this to true if the Transform passed is expressed in global null, false for local null.
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_command (bool): If set to true a python command equivalent to this call will be printed out

Returns:
    RigElementKey: The key for the newly created null.

<a id="unreal.RigHierarchyController.add_curve"></a>

#### add_curve

```python
def add_curve(name: Name,
              value: float = 0.000000,
              setup_undo: bool = True,
              print_python_command: bool = False) -> RigElementKey
```

x.add_curve(name, value=0.000000, setup_undo=True, print_python_command=False) -> RigElementKey
Adds a curve to the hierarchy

Args:
    name (Name): The suggested name of the new curve - will eventually be corrected by the namespace
    value (float): The value to use for the curve
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_command (bool): If set to true a python command equivalent to this call will be printed out

Returns:
    RigElementKey: The key for the newly created curve.

<a id="unreal.RigHierarchyController.add_control"></a>

#### add_control

```python
def add_control(name: Name,
                parent: RigElementKey,
                settings: RigControlSettings,
                value: RigControlValue,
                setup_undo: bool = True,
                print_python_command: bool = False) -> RigElementKey
```

x.add_control(name, parent, settings, value, setup_undo=True, print_python_command=False) -> RigElementKey
Adds a control to the hierarchy

Args:
    name (Name): The suggested name of the new control - will eventually be corrected by the namespace
    parent (RigElementKey): The (optional) parent of the new control. If you don't need a parent, pass FRigElementKey()
    settings (RigControlSettings): All of the control's settings
    value (RigControlValue): The value to use for the control
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_command (bool): 

Returns:
    RigElementKey: The key for the newly created control.

<a id="unreal.RigHierarchyController.add_connector"></a>

#### add_connector

```python
def add_connector(name: Name,
                  settings: RigConnectorSettings = [
                      "", ConnectorType.PRIMARY, False, []
                  ],
                  setup_undo: bool = False,
                  print_python_command: bool = False) -> RigElementKey
```

x.add_connector(name, settings=["", ConnectorType.PRIMARY, False, []], setup_undo=False, print_python_command=False) -> RigElementKey
Adds a connector to the hierarchy

Args:
    name (Name): The suggested name of the new connector - will eventually be corrected by the namespace
    settings (RigConnectorSettings): All of the connector's settings
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_command (bool): If set to true a python command equivalent to this call will be printed out

Returns:
    RigElementKey: The key for the newly created bone.

<a id="unreal.RigHierarchyController.add_channel_host"></a>

#### add_channel_host

```python
def add_channel_host(channel: RigElementKey,
                     host: RigElementKey,
                     setup_undo: bool = False,
                     print_python_command: bool = False) -> bool
```

x.add_channel_host(channel, host, setup_undo=False, print_python_command=False) -> bool
Adds a new channel host to the animation channel
note: This is just an overload of AddAvailableSpace for readability

Args:
    channel (RigElementKey): The animation channel to add the channel host for
    host (RigElementKey): The host to add to the channel to
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_command (bool): If set to true a python command equivalent to this call will be printed out

Returns:
    bool: Returns true if successful.

<a id="unreal.RigHierarchyController.add_bone"></a>

#### add_bone

```python
def add_bone(name: Name,
             parent: RigElementKey,
             transform: Transform,
             transform_in_global: bool = True,
             bone_type: RigBoneType = RigBoneType.USER,
             setup_undo: bool = False,
             print_python_command: bool = False) -> RigElementKey
```

x.add_bone(name, parent, transform, transform_in_global=True, bone_type=RigBoneType.USER, setup_undo=False, print_python_command=False) -> RigElementKey
Adds a bone to the hierarchy

Args:
    name (Name): The suggested name of the new bone - will eventually be corrected by the namespace
    parent (RigElementKey): The (optional) parent of the new bone. If you don't need a parent, pass FRigElementKey()
    transform (Transform): The transform for the new bone - either in local or global space, based on bTransformInGlobal
    transform_in_global (bool): Set this to true if the Transform passed is expressed in global space, false for local space.
    bone_type (RigBoneType): The type of bone to add. This can be used to differentiate between imported bones and user defined bones.
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_command (bool): If set to true a python command equivalent to this call will be printed out

Returns:
    RigElementKey: The key for the newly created bone.

<a id="unreal.RigHierarchyController.add_available_space"></a>

#### add_available_space

```python
def add_available_space(control: RigElementKey,
                        space: RigElementKey,
                        setup_undo: bool = False,
                        print_python_command: bool = False) -> bool
```

x.add_available_space(control, space, setup_undo=False, print_python_command=False) -> bool
Adds a new available space to the given control

Args:
    control (RigElementKey): The control to add the available space for
    space (RigElementKey): The space to add to the available spaces list
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_command (bool): If set to true a python command equivalent to this call will be printed out

Returns:
    bool: Returns true if successful.

<a id="unreal.RigHierarchyController.add_animation_channel"></a>

#### add_animation_channel

```python
def add_animation_channel(name: Name,
                          parent_control: RigElementKey,
                          settings: RigControlSettings,
                          setup_undo: bool = True,
                          print_python_command: bool = False) -> RigElementKey
```

x.add_animation_channel(name, parent_control, settings, setup_undo=True, print_python_command=False) -> RigElementKey
Adds a control to the hierarchy

Args:
    name (Name): The suggested name of the new animation channel - will eventually be corrected by the namespace
    parent_control (RigElementKey): The parent of the new animation channel.
    settings (RigControlSettings): All of the animation channel's settings
    setup_undo (bool): If set to true the stack will record the change for undo / redo
    print_python_command (bool): 

Returns:
    RigElementKey: The key for the newly created animation channel.

<a id="unreal.ControlRigLayerInstance"></a>