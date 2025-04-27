## SubobjectDataSubsystem Objects

```python
class SubobjectDataSubsystem(EngineSubsystem)
```

The Subobject Data Subsystem will produce the reflected subobject data
based on a given root object. A root object can be anything, an actor
instance clicked on via the level editor, a UBlueprint* by opening an asset,
or something piped in from python or other scripting languages.

**C++ Source:**

- **Module**: SubobjectDataInterface
- **File**: SubobjectDataSubsystem.h

<a id="unreal.SubobjectDataSubsystem.reparent_subobjects"></a>

#### reparent_subobjects

```python
def reparent_subobjects(params: ReparentSubobjectParams,
                        handles_to_move: Array[SubobjectDataHandle]) -> bool
```

x.reparent_subobjects(params, handles_to_move) -> bool
Attempts to reparent all subobjects in the HandlesToMove array to the new parent handle.

Args:
    params (ReparentSubobjectParams): 
    handles_to_move (Array[SubobjectDataHandle]): 

Returns:
    bool:

<a id="unreal.SubobjectDataSubsystem.reparent_subobject"></a>

#### reparent_subobject

```python
def reparent_subobject(params: ReparentSubobjectParams,
                       to_reparent_handle: SubobjectDataHandle) -> bool
```

x.reparent_subobject(params, to_reparent_handle) -> bool
Attempts to reparent the given subobject to the new parent

Args:
    params (ReparentSubobjectParams): 
    to_reparent_handle (SubobjectDataHandle): The handle of the subobject that will get moved

Returns:
    bool: True if the reparent was successful, false otherwise.

<a id="unreal.SubobjectDataSubsystem.rename_subobject_member_variable"></a>

#### rename_subobject_member_variable

```python
@classmethod
def rename_subobject_member_variable(cls, bp_context: Blueprint,
                                     handle: SubobjectDataHandle,
                                     new_name: Name) -> None
```

X.rename_subobject_member_variable(bp_context, handle, new_name) -> None
Rename Subobject Member Variable

Args:
    bp_context (Blueprint): 
    handle (SubobjectDataHandle): 
    new_name (Name):

<a id="unreal.SubobjectDataSubsystem.rename_subobject"></a>

#### rename_subobject

```python
def rename_subobject(handle: SubobjectDataHandle, new_name: Text) -> bool
```

x.rename_subobject(handle, new_name) -> bool
Attempts to rename the given subobject to the new name.

Args:
    handle (SubobjectDataHandle): Handle to the subobject to rename
    new_name (Text): The new name that is desired for the given subobject

Returns:
    bool: True if the rename was successful, false otherwise.

<a id="unreal.SubobjectDataSubsystem.paste_subobjects"></a>

#### paste_subobjects

```python
def paste_subobjects(paste_to_context: SubobjectDataHandle,
                     new_parent_handles: Array[SubobjectDataHandle],
                     bp_context: Blueprint) -> Array[SubobjectDataHandle]
```

x.paste_subobjects(paste_to_context, new_parent_handles, bp_context) -> Array[SubobjectDataHandle]
Pastes the given subobjects to the PasteToContext.

Args:
    paste_to_context (SubobjectDataHandle): The subobject to paste things onto
    new_parent_handles (Array[SubobjectDataHandle]): Array of Subobject Handles that you would like to paste
    bp_context (Blueprint): Blueprint to use, if you are pasting to a blueprint. Null if pasting to an instanced object

Returns:
    Array[SubobjectDataHandle]: 

    out_pasted_handles (Array[SubobjectDataHandle]): Array populated with the handles to the newly pasted subobjects

<a id="unreal.SubobjectDataSubsystem.make_new_scene_root"></a>

#### make_new_scene_root

```python
def make_new_scene_root(context: SubobjectDataHandle,
                        new_scene_root: SubobjectDataHandle,
                        bp_context: Blueprint) -> bool
```

x.make_new_scene_root(context, new_scene_root, bp_context) -> bool
Make New Scene Root

Args:
    context (SubobjectDataHandle): 
    new_scene_root (SubobjectDataHandle): 
    bp_context (Blueprint): 

Returns:
    bool:

<a id="unreal.SubobjectDataSubsystem.k2_gather_subobject_data_for_instance"></a>

#### k2_gather_subobject_data_for_instance

```python
def k2_gather_subobject_data_for_instance(
        context: Actor) -> Array[SubobjectDataHandle]
```

x.k2_gather_subobject_data_for_instance(context) -> Array[SubobjectDataHandle]
Gather all subobjects that the given actor instance has. Populates an array of
handles that will have the given context and all it's subobjects.

Args:
    context (Actor): Object to gather subobjects for

Returns:
    Array[SubobjectDataHandle]: 

    out_array (Array[SubobjectDataHandle]): Array to populate (will be emptied first)

<a id="unreal.SubobjectDataSubsystem.k2_gather_subobject_data_for_blueprint"></a>

#### k2_gather_subobject_data_for_blueprint

```python
def k2_gather_subobject_data_for_blueprint(
        context: Blueprint) -> Array[SubobjectDataHandle]
```

x.k2_gather_subobject_data_for_blueprint(context) -> Array[SubobjectDataHandle]
Gather all subobjects that the given Blueprint context has. Populates an array of
handles that will have the given context and all it's subobjects.

Args:
    context (Blueprint): Object to gather subobjects for

Returns:
    Array[SubobjectDataHandle]: 

    out_array (Array[SubobjectDataHandle]): Array to populate (will be emptied first)

<a id="unreal.SubobjectDataSubsystem.k2_find_subobject_data_from_handle"></a>

#### k2_find_subobject_data_from_handle

```python
def k2_find_subobject_data_from_handle(
        handle: SubobjectDataHandle) -> Optional[SubobjectData]
```

x.k2_find_subobject_data_from_handle(handle) -> SubobjectData or None
Attempt to find the subobject data for a given handle. OutData will only
be valid if the function returns true.

Args:
    handle (SubobjectDataHandle): Handle of the subobject data you want to acquire

Returns:
    SubobjectData or None: bool          true if the data was found

    out_data (SubobjectData): Reference to the subobject data to populate

<a id="unreal.SubobjectDataSubsystem.k2_delete_subobjects_from_instance"></a>

#### k2_delete_subobjects_from_instance

```python
def k2_delete_subobjects_from_instance(
        context_handle: SubobjectDataHandle,
        subobjects_to_delete: Array[SubobjectDataHandle]) -> int
```

x.k2_delete_subobjects_from_instance(context_handle, subobjects_to_delete) -> int32
Attempts to delete the given array of subobjects from their context

Args:
    context_handle (SubobjectDataHandle): The owning context of the subobjects that should be removed
    subobjects_to_delete (Array[SubobjectDataHandle]): Array of subobject handles that should be deleted

Returns:
    int32: The number of subobjects successfully deleted

<a id="unreal.SubobjectDataSubsystem.k2_delete_subobject_from_instance"></a>

#### k2_delete_subobject_from_instance

```python
def k2_delete_subobject_from_instance(
        context_handle: SubobjectDataHandle,
        subobject_to_delete: SubobjectDataHandle) -> int
```

x.k2_delete_subobject_from_instance(context_handle, subobject_to_delete) -> int32
Attempts to delete the given subobject from its context

Args:
    context_handle (SubobjectDataHandle): The owning context of the subobjects that should be removed
    subobject_to_delete (SubobjectDataHandle): The subobject handles that should be deleted

Returns:
    int32: The number of subobjects successfully deleted

<a id="unreal.SubobjectDataSubsystem.is_valid_rename"></a>

#### is_valid_rename

```python
def is_valid_rename(handle: SubobjectDataHandle,
                    new_text: Text) -> Optional[Text]
```

x.is_valid_rename(handle, new_text) -> Text or None
Returns true if the given new text is a valid option to rename the
subobject with the given handle. Populates the OutErrorMessage if
it is not valid.

Args:
    handle (SubobjectDataHandle): Handle to the subobject that is being checked
    new_text (Text): The new name that is desired

Returns:
    Text or None: True if the rename is valid

    out_error_message (Text): The reasoning for an invalid name

<a id="unreal.SubobjectDataSubsystem.find_handle_for_object"></a>

#### find_handle_for_object

```python
def find_handle_for_object(
        context: SubobjectDataHandle,
        object_to_find: Object,
        bp_context: Blueprint = None) -> SubobjectDataHandle
```

x.find_handle_for_object(context, object_to_find, bp_context=None) -> SubobjectDataHandle
Attempt to find an existing handle for the given object.

Args:
    context (SubobjectDataHandle): The context that the object to find is within
    object_to_find (Object): The object that you want to find the handle for within the context
    bp_context (Blueprint): 

Returns:
    SubobjectDataHandle: FSubobjectDataHandle  The subobject handle for the object, Invalid handle if not found.

<a id="unreal.SubobjectDataSubsystem.duplicate_subobjects"></a>

#### duplicate_subobjects

```python
def duplicate_subobjects(context: SubobjectDataHandle,
                         subobjects_to_dup: Array[SubobjectDataHandle],
                         bp_context: Blueprint) -> Array[SubobjectDataHandle]
```

x.duplicate_subobjects(context, subobjects_to_dup, bp_context) -> Array[SubobjectDataHandle]
Duplicate the given array of subobjects on the context.

Args:
    context (SubobjectDataHandle): The owning context that the subobjects to dup come from
    subobjects_to_dup (Array[SubobjectDataHandle]): Array of handles of existing subobjects you would like to have duplicated
    bp_context (Blueprint): Pointer to the current blueprint context if necessary. Use nullptr if dealing with instances

Returns:
    Array[SubobjectDataHandle]: 

    out_new_subobjects (Array[SubobjectDataHandle]): Array that will be populated with any newly created subobjects

<a id="unreal.SubobjectDataSubsystem.detach_subobject"></a>

#### detach_subobject

```python
def detach_subobject(owner_handle: SubobjectDataHandle,
                     child_to_remove: SubobjectDataHandle) -> bool
```

x.detach_subobject(owner_handle, child_to_remove) -> bool
Remove the child subobject from the owner

Args:
    owner_handle (SubobjectDataHandle): 
    child_to_remove (SubobjectDataHandle): 

Returns:
    bool: True if the child was successfully removed.

<a id="unreal.SubobjectDataSubsystem.delete_subobjects"></a>

#### delete_subobjects

```python
def delete_subobjects(context_handle: SubobjectDataHandle,
                      subobjects_to_delete: Array[SubobjectDataHandle],
                      bp_context: Blueprint = None) -> int
```

x.delete_subobjects(context_handle, subobjects_to_delete, bp_context=None) -> int32
Attempts to delete the given array of subobjects from their context

Args:
    context_handle (SubobjectDataHandle): The owning context of the subobjects that should be removed
    subobjects_to_delete (Array[SubobjectDataHandle]): Array of subobject handles that should be deleted
    bp_context (Blueprint): The blueprint context for the given

Returns:
    int32: The number of subobjects successfully deleted

<a id="unreal.SubobjectDataSubsystem.delete_subobject"></a>

#### delete_subobject

```python
def delete_subobject(context_handle: SubobjectDataHandle,
                     subobject_to_delete: SubobjectDataHandle,
                     bp_context: Blueprint = None) -> int
```

x.delete_subobject(context_handle, subobject_to_delete, bp_context=None) -> int32
Attempts to delete the given subobject from its blueprint context

Args:
    context_handle (SubobjectDataHandle): The owning context of the subobjects that should be removed
    subobject_to_delete (SubobjectDataHandle): The subobject handles that should be deleted
    bp_context (Blueprint): The blueprint context for the given

Returns:
    int32: The number of subobjects successfully deleted

<a id="unreal.SubobjectDataSubsystem.create_new_cpp_component"></a>

#### create_new_cpp_component

```python
@classmethod
def create_new_cpp_component(cls, component_class: Class, new_class_path: str,
                             new_class_name: str) -> Class
```

X.create_new_cpp_component(component_class, new_class_path, new_class_name) -> type(Class)
Creates a new C++ component from the specified class type
The user will be prompted to pick a new subclass name and code will be recompiled

Args:
    component_class (type(Class)): 
    new_class_path (str): 
    new_class_name (str): 

Returns:
    type(Class): The new class that was created

<a id="unreal.SubobjectDataSubsystem.create_new_bp_component"></a>

#### create_new_bp_component

```python
@classmethod
def create_new_bp_component(cls, component_class: Class, new_class_path: str,
                            new_class_name: str) -> Class
```

X.create_new_bp_component(component_class, new_class_path, new_class_name) -> type(Class)
Creates a new Blueprint component from the specified class type
The user will be prompted to pick a new subclass name and a blueprint asset will be created

Args:
    component_class (type(Class)): 
    new_class_path (str): 
    new_class_name (str): 

Returns:
    type(Class): The new class that was created

<a id="unreal.SubobjectDataSubsystem.copy_subobjects"></a>

#### copy_subobjects

```python
def copy_subobjects(handles: Array[SubobjectDataHandle],
                    bp_context: Blueprint) -> None
```

x.copy_subobjects(handles, bp_context) -> None
Copy Subobjects

Args:
    handles (Array[SubobjectDataHandle]): 
    bp_context (Blueprint):

<a id="unreal.SubobjectDataSubsystem.change_subobject_class"></a>

#### change_subobject_class

```python
def change_subobject_class(handle: SubobjectDataHandle,
                           new_class: Class) -> bool
```

x.change_subobject_class(handle, new_class) -> bool
Attempts to change the subclass of a native component

Args:
    handle (SubobjectDataHandle): Handle to the subobject to change class of
    new_class (type(Class)): The new class that is desired for the given subobject

Returns:
    bool: True if the class change was successful, false otherwise.

<a id="unreal.SubobjectDataSubsystem.can_paste_subobjects"></a>

#### can_paste_subobjects

```python
def can_paste_subobjects(root_handle: SubobjectDataHandle,
                         bp_context: Blueprint = None) -> bool
```

x.can_paste_subobjects(root_handle, bp_context=None) -> bool
Can Paste Subobjects

Args:
    root_handle (SubobjectDataHandle): 
    bp_context (Blueprint): 

Returns:
    bool:

<a id="unreal.SubobjectDataSubsystem.can_copy_subobjects"></a>

#### can_copy_subobjects

```python
def can_copy_subobjects(handles: Array[SubobjectDataHandle]) -> bool
```

x.can_copy_subobjects(handles) -> bool
Returns true if the given array of handles represents subobjects that
can be copied.

Args:
    handles (Array[SubobjectDataHandle]): 

Returns:
    bool:

<a id="unreal.SubobjectDataSubsystem.attach_subobject"></a>

#### attach_subobject

```python
def attach_subobject(owner_handle: SubobjectDataHandle,
                     child_to_add_handle: SubobjectDataHandle) -> bool
```

x.attach_subobject(owner_handle, child_to_add_handle) -> bool
Add the given subobject to a new owner. This will remove the subobject from its previous
owner if necessary.

Args:
    owner_handle (SubobjectDataHandle): The new owner to attach to
    child_to_add_handle (SubobjectDataHandle): Handle to the subobject that will become a child of the owner

Returns:
    bool: true if the child was added successfully

<a id="unreal.SubobjectDataSubsystem.add_new_subobject"></a>

#### add_new_subobject

```python
def add_new_subobject(
        params: AddNewSubobjectParams) -> Tuple[SubobjectDataHandle, Text]
```

x.add_new_subobject(params) -> (SubobjectDataHandle, fail_reason=Text)
Add a new subobject as a child to the given parent object

Args:
    params (AddNewSubobjectParams): Options to consider when adding this subobject

Returns:
    Text: FSubobjectDataHandle          Handle to the newly created subobject, Invalid handle if creation failed

    fail_reason (Text):

<a id="unreal.SubobjectEditorMenuContext"></a>