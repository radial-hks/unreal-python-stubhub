## TypedElementSelectionSet Objects

```python
class TypedElementSelectionSet(Object)
```

A wrapper around an element list that ensures mutation goes via the selection
interfaces, as well as providing some utilities for batching operations.

**C++ Source:**

- **Module**: TypedElementRuntime
- **File**: TypedElementSelectionSet.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_pre_selection_change`` (OnPreChangeDynamic):  [Read-Write] Delegate that is invoked whenever the underlying element list is potentially about to change.
- ``on_selection_change`` (OnChangeDynamic):  [Read-Write] Delegate that is invoked whenever the underlying element list has been changed.

<a id="unreal.TypedElementSelectionSet.on_pre_selection_change"></a>

#### on_pre_selection_change

```python
@property
def on_pre_selection_change() -> OnPreChangeDynamic
```

(OnPreChangeDynamic):  [Read-Write] Delegate that is invoked whenever the underlying element list is potentially about to change.

<a id="unreal.TypedElementSelectionSet.on_pre_selection_change"></a>

#### on_pre_selection_change

```python
@on_pre_selection_change.setter
def on_pre_selection_change(value: OnPreChangeDynamic) -> None
```

<a id="unreal.TypedElementSelectionSet.on_selection_change"></a>

#### on_selection_change

```python
@property
def on_selection_change() -> OnChangeDynamic
```

(OnChangeDynamic):  [Read-Write] Delegate that is invoked whenever the underlying element list has been changed.

<a id="unreal.TypedElementSelectionSet.on_selection_change"></a>

#### on_selection_change

```python
@on_selection_change.setter
def on_selection_change(value: OnChangeDynamic) -> None
```

<a id="unreal.TypedElementSelectionSet.set_selection"></a>

#### set_selection

```python
def set_selection(element_handles: Array[ScriptTypedElementHandle],
                  selection_options: TypedElementSelectionOptions) -> bool
```

x.set_selection(element_handles, selection_options) -> bool
Attempt to make the selection the given elements.
note: Equivalent to calling ClearSelection then SelectElements, but happens in a single batch.

Args:
    element_handles (Array[ScriptTypedElementHandle]): 
    selection_options (TypedElementSelectionOptions): 

Returns:
    bool: True if the selection was changed, false otherwise.

<a id="unreal.TypedElementSelectionSet.select_elements"></a>

#### select_elements

```python
def select_elements(element_handles: Array[ScriptTypedElementHandle],
                    selection_options: TypedElementSelectionOptions) -> bool
```

x.select_elements(element_handles, selection_options) -> bool
Attempt to select the given elements.

Args:
    element_handles (Array[ScriptTypedElementHandle]): 
    selection_options (TypedElementSelectionOptions): 

Returns:
    bool: True if the selection was changed, false otherwise.

<a id="unreal.TypedElementSelectionSet.select_element"></a>

#### select_element

```python
def select_element(element_handle: ScriptTypedElementHandle,
                   selection_options: TypedElementSelectionOptions) -> bool
```

x.select_element(element_handle, selection_options) -> bool
Attempt to select the given element.

Args:
    element_handle (ScriptTypedElementHandle): 
    selection_options (TypedElementSelectionOptions): 

Returns:
    bool: True if the selection was changed, false otherwise.

<a id="unreal.TypedElementSelectionSet.restore_selection_state"></a>

#### restore_selection_state

```python
def restore_selection_state(
        selection_state: TypedElementSelectionSetState) -> None
```

x.restore_selection_state(selection_state) -> None
Restores the selection set from the given state.
The calling code is responsible for managing any undo state.

Args:
    selection_state (TypedElementSelectionSetState):

<a id="unreal.TypedElementSelectionSet.get_selected_element_handles"></a>

#### get_selected_element_handles

```python
def get_selected_element_handles(
        base_interface_type: Class = None) -> Array[ScriptTypedElementHandle]
```

x.get_selected_element_handles(base_interface_type=None) -> Array[ScriptTypedElementHandle]
Get the handle of every selected element, optionally filtering to elements that implement the given interface.

Args:
    base_interface_type (type(Class)): 

Returns:
    Array[ScriptTypedElementHandle]:

<a id="unreal.TypedElementSelectionSet.is_element_selected"></a>

#### is_element_selected

```python
def is_element_selected(
        element_handle: ScriptTypedElementHandle,
        selection_options: TypedElementIsSelectedOptions) -> bool
```

x.is_element_selected(element_handle, selection_options) -> bool
Test to see whether the given element is currently considered selected.

Args:
    element_handle (ScriptTypedElementHandle): 
    selection_options (TypedElementIsSelectedOptions): 

Returns:
    bool:

<a id="unreal.TypedElementSelectionSet.has_selected_objects"></a>

#### has_selected_objects

```python
def has_selected_objects(required_class: Class = None) -> bool
```

x.has_selected_objects(required_class=None) -> bool
Test whether there are any selected objects.

Args:
    required_class (type(Class)): 

Returns:
    bool:

<a id="unreal.TypedElementSelectionSet.has_selected_elements"></a>

#### has_selected_elements

```python
def has_selected_elements(base_interface_type: Class = None) -> bool
```

x.has_selected_elements(base_interface_type=None) -> bool
Test whether there selected elements, optionally filtering to elements that implement the given interface.

Args:
    base_interface_type (type(Class)): 

Returns:
    bool:

<a id="unreal.TypedElementSelectionSet.get_top_selected_object"></a>

#### get_top_selected_object

```python
def get_top_selected_object(required_class: Class = None) -> Object
```

x.get_top_selected_object(required_class=None) -> Object
Get the first selected object of the given type.

Args:
    required_class (type(Class)): 

Returns:
    Object:

<a id="unreal.TypedElementSelectionSet.get_selection_element"></a>

#### get_selection_element

```python
def get_selection_element(
        element_handle: ScriptTypedElementHandle,
        selection_method: TypedElementSelectionMethod
) -> ScriptTypedElementHandle
```

x.get_selection_element(element_handle, selection_method) -> ScriptTypedElementHandle
Given an element, return the element that should actually perform a selection operation.

Args:
    element_handle (ScriptTypedElementHandle): 
    selection_method (TypedElementSelectionMethod): 

Returns:
    ScriptTypedElementHandle:

<a id="unreal.TypedElementSelectionSet.get_selected_objects"></a>

#### get_selected_objects

```python
def get_selected_objects(required_class: Class = None) -> Array[Object]
```

x.get_selected_objects(required_class=None) -> Array[Object]
Get the array of selected objects from the currently selected elements.

Args:
    required_class (type(Class)): 

Returns:
    Array[Object]:

<a id="unreal.TypedElementSelectionSet.get_num_selected_elements"></a>

#### get_num_selected_elements

```python
def get_num_selected_elements() -> int
```

x.get_num_selected_elements() -> int32
Get the number of selected elements.

Returns:
    int32:

<a id="unreal.TypedElementSelectionSet.get_current_selection_state"></a>

#### get_current_selection_state

```python
def get_current_selection_state() -> TypedElementSelectionSetState
```

x.get_current_selection_state() -> TypedElementSelectionSetState
Serializes the current selection set.
The calling code is responsible for storing any state information. The selection set can be returned to a prior state using RestoreSelectionState.

Returns:
    TypedElementSelectionSetState: the current state of the selection set.

<a id="unreal.TypedElementSelectionSet.get_bottom_selected_object"></a>

#### get_bottom_selected_object

```python
def get_bottom_selected_object(required_class: Class = None) -> Object
```

x.get_bottom_selected_object(required_class=None) -> Object
Get the last selected object of the given type.

Args:
    required_class (type(Class)): 

Returns:
    Object:

<a id="unreal.TypedElementSelectionSet.deselect_elements"></a>

#### deselect_elements

```python
def deselect_elements(element_handles: Array[ScriptTypedElementHandle],
                      selection_options: TypedElementSelectionOptions) -> bool
```

x.deselect_elements(element_handles, selection_options) -> bool
Attempt to deselect the given elements.

Args:
    element_handles (Array[ScriptTypedElementHandle]): 
    selection_options (TypedElementSelectionOptions): 

Returns:
    bool: True if the selection was changed, false otherwise.

<a id="unreal.TypedElementSelectionSet.deselect_element"></a>

#### deselect_element

```python
def deselect_element(element_handle: ScriptTypedElementHandle,
                     selection_options: TypedElementSelectionOptions) -> bool
```

x.deselect_element(element_handle, selection_options) -> bool
Attempt to deselect the given element.

Args:
    element_handle (ScriptTypedElementHandle): 
    selection_options (TypedElementSelectionOptions): 

Returns:
    bool: True if the selection was changed, false otherwise.

<a id="unreal.TypedElementSelectionSet.count_selected_objects"></a>

#### count_selected_objects

```python
def count_selected_objects(required_class: Class = None) -> int
```

x.count_selected_objects(required_class=None) -> int32
Count the number of selected objects.

Args:
    required_class (type(Class)): 

Returns:
    int32:

<a id="unreal.TypedElementSelectionSet.count_selected_elements"></a>

#### count_selected_elements

```python
def count_selected_elements(base_interface_type: Class = None) -> int
```

x.count_selected_elements(base_interface_type=None) -> int32
Count the number of selected elements, optionally filtering to elements that implement the given interface.

Args:
    base_interface_type (type(Class)): 

Returns:
    int32:

<a id="unreal.TypedElementSelectionSet.clear_selection"></a>

#### clear_selection

```python
def clear_selection(selection_options: TypedElementSelectionOptions) -> bool
```

x.clear_selection(selection_options) -> bool
Clear the current selection.

Args:
    selection_options (TypedElementSelectionOptions): 

Returns:
    bool: True if the selection was changed, false otherwise.

<a id="unreal.TypedElementSelectionSet.can_select_element"></a>

#### can_select_element

```python
def can_select_element(
        element_handle: ScriptTypedElementHandle,
        selection_options: TypedElementSelectionOptions) -> bool
```

x.can_select_element(element_handle, selection_options) -> bool
Test to see whether the given element can be selected.

Args:
    element_handle (ScriptTypedElementHandle): 
    selection_options (TypedElementSelectionOptions): 

Returns:
    bool:

<a id="unreal.TypedElementSelectionSet.can_deselect_element"></a>

#### can_deselect_element

```python
def can_deselect_element(
        element_handle: ScriptTypedElementHandle,
        selection_options: TypedElementSelectionOptions) -> bool
```

x.can_deselect_element(element_handle, selection_options) -> bool
Test to see whether the given element can be deselected.

Args:
    element_handle (ScriptTypedElementHandle): 
    selection_options (TypedElementSelectionOptions): 

Returns:
    bool:

<a id="unreal.TypedElementSelectionSet.allow_selection_modifiers"></a>

#### allow_selection_modifiers

```python
def allow_selection_modifiers(
        element_handle: ScriptTypedElementHandle) -> bool
```

x.allow_selection_modifiers(element_handle) -> bool
Test to see whether selection modifiers (Ctrl or Shift) are allowed while selecting this element.

Args:
    element_handle (ScriptTypedElementHandle): 

Returns:
    bool:

<a id="unreal.TypedElementSelectionSet.set_selection_from_list"></a>

#### set_selection_from_list

```python
def set_selection_from_list(
        element_list: TypedElementList,
        selection_options: TypedElementSelectionOptions) -> bool
```

x.set_selection_from_list(element_list, selection_options) -> bool
Attempt to make the selection the given elements.
note: Equivalent to calling ClearSelection then SelectElements, but happens in a single batch.

Args:
    element_list (TypedElementList): 
    selection_options (TypedElementSelectionOptions): 

Returns:
    bool: True if the selection was changed, false otherwise.

<a id="unreal.TypedElementSelectionSet.select_elements_from_list"></a>

#### select_elements_from_list

```python
def select_elements_from_list(
        element_list: TypedElementList,
        selection_options: TypedElementSelectionOptions) -> bool
```

x.select_elements_from_list(element_list, selection_options) -> bool
Attempt to select the given elements.

Args:
    element_list (TypedElementList): 
    selection_options (TypedElementSelectionOptions): 

Returns:
    bool: True if the selection was changed, false otherwise.

<a id="unreal.TypedElementSelectionSet.get_normalized_selection"></a>

#### get_normalized_selection

```python
def get_normalized_selection(
    normalization_options: TypedElementSelectionNormalizationOptions
) -> TypedElementList
```

x.get_normalized_selection(normalization_options) -> TypedElementList
Get a normalized version of this selection set that can be used to perform operations like gizmo manipulation, deletion, copying, etc.
This will do things like expand out groups, and resolve any parent<->child elements so that duplication operations aren't performed on both the parent and the child.

Args:
    normalization_options (TypedElementSelectionNormalizationOptions): 

Returns:
    TypedElementList:

<a id="unreal.TypedElementSelectionSet.get_normalized_element_list"></a>

#### get_normalized_element_list

```python
def get_normalized_element_list(
    element_list: TypedElementList,
    normalization_options: TypedElementSelectionNormalizationOptions
) -> TypedElementList
```

x.get_normalized_element_list(element_list, normalization_options) -> TypedElementList
Get a normalized version of the given element list that can be used to perform operations like gizmo manipulation, deletion, copying, etc.
This will do things like expand out groups, and resolve any parent<->child elements so that duplication operations aren't performed on both the parent and the child.

Args:
    element_list (TypedElementList): 
    normalization_options (TypedElementSelectionNormalizationOptions): 

Returns:
    TypedElementList:

<a id="unreal.TypedElementSelectionSet.deselect_elements_from_list"></a>

#### deselect_elements_from_list

```python
def deselect_elements_from_list(
        element_list: TypedElementList,
        selection_options: TypedElementSelectionOptions) -> bool
```

x.deselect_elements_from_list(element_list, selection_options) -> bool
Attempt to deselect the given elements.

Args:
    element_list (TypedElementList): 
    selection_options (TypedElementSelectionOptions): 

Returns:
    bool: True if the selection was changed, false otherwise.

<a id="unreal.TypedElementSelectionSetLibrary"></a>