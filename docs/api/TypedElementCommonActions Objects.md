## TypedElementCommonActions Objects

```python
class TypedElementCommonActions(Object)
```

A utility to handle higher-level common actions, but default via UTypedElementWorldInterface,
but asset editors can customize this behavior via FTypedElementCommonActionsCustomization.

**C++ Source:**

- **Module**: Engine
- **File**: TypedElementCommonActions.h

<a id="unreal.TypedElementCommonActions.paste_normalized_elements_from_string"></a>

#### paste_normalized_elements_from_string

```python
def paste_normalized_elements_from_string(
        element_list: TypedElementList, world: World,
        paste_option: TypedElementPasteOptions,
        input_string: str) -> Array[ScriptTypedElementHandle]
```

x.paste_normalized_elements_from_string(element_list, world, paste_option, input_string) -> Array[ScriptTypedElementHandle]
Paste any elements from the given string
note: This list should have been pre-normalized via UTypedElementSelectionSet::GetNormalizedSelection or UTypedElementSelectionSet::GetNormalizedElementList.

Args:
    element_list (TypedElementList): 
    world (World): 
    paste_option (TypedElementPasteOptions): 
    input_string (str): 

Returns:
    Array[ScriptTypedElementHandle]:

<a id="unreal.TypedElementCommonActions.paste_elements_from_string"></a>

#### paste_elements_from_string

```python
def paste_elements_from_string(
        selection_set: TypedElementSelectionSet, world: World,
        paste_option: TypedElementPasteOptions,
        input_string: str) -> Array[ScriptTypedElementHandle]
```

x.paste_elements_from_string(selection_set, world, paste_option, input_string) -> Array[ScriptTypedElementHandle]
Paste any elements from the given string
note: Internally this just calls PasteNormalizedElements on the result of UTypedElementSelectionSet::GetNormalizedSelection.

Args:
    selection_set (TypedElementSelectionSet): 
    world (World): 
    paste_option (TypedElementPasteOptions): 
    input_string (str): 

Returns:
    Array[ScriptTypedElementHandle]:

<a id="unreal.TypedElementCommonActions.paste_normalized_elements"></a>

#### paste_normalized_elements

```python
def paste_normalized_elements(
        element_list: TypedElementList, world: World,
        paste_option: TypedElementPasteOptions
) -> Array[ScriptTypedElementHandle]
```

x.paste_normalized_elements(element_list, world, paste_option) -> Array[ScriptTypedElementHandle]
Paste any elements from the clipboard
note: This list should have been pre-normalized via UTypedElementSelectionSet::GetNormalizedSelection or UTypedElementSelectionSet::GetNormalizedElementList.

Args:
    element_list (TypedElementList): 
    world (World): 
    paste_option (TypedElementPasteOptions): 

Returns:
    Array[ScriptTypedElementHandle]:

<a id="unreal.TypedElementCommonActions.paste_elements"></a>

#### paste_elements

```python
def paste_elements(
        selection_set: TypedElementSelectionSet, world: World,
        paste_option: TypedElementPasteOptions
) -> Array[ScriptTypedElementHandle]
```

x.paste_elements(selection_set, world, paste_option) -> Array[ScriptTypedElementHandle]
Paste any elements from the clipboard
note: Internally this just calls PasteNormalizedElements on the result of UTypedElementSelectionSet::GetNormalizedSelection.

Args:
    selection_set (TypedElementSelectionSet): 
    world (World): 
    paste_option (TypedElementPasteOptions): 

Returns:
    Array[ScriptTypedElementHandle]:

<a id="unreal.TypedElementCommonActions.duplicate_selected_elements"></a>

#### duplicate_selected_elements

```python
def duplicate_selected_elements(
        selection_set: TypedElementSelectionSet, world: World,
        location_offset: Vector) -> Array[ScriptTypedElementHandle]
```

x.duplicate_selected_elements(selection_set, world, location_offset) -> Array[ScriptTypedElementHandle]
Duplicate any elements from the given selection set that can be duplicated.
note: Internally this just calls DuplicateNormalizedElements on the result of UTypedElementSelectionSet::GetNormalizedSelection.

Args:
    selection_set (TypedElementSelectionSet): 
    world (World): 
    location_offset (Vector): 

Returns:
    Array[ScriptTypedElementHandle]:

<a id="unreal.TypedElementCommonActions.duplicate_normalized_elements"></a>

#### duplicate_normalized_elements

```python
def duplicate_normalized_elements(
        element_list: TypedElementList, world: World,
        location_offset: Vector) -> Array[ScriptTypedElementHandle]
```

x.duplicate_normalized_elements(element_list, world, location_offset) -> Array[ScriptTypedElementHandle]
Duplicate any elements from the given list that can be duplicated.
note: This list should have been pre-normalized via UTypedElementSelectionSet::GetNormalizedSelection or UTypedElementSelectionSet::GetNormalizedElementList.

Args:
    element_list (TypedElementList): 
    world (World): 
    location_offset (Vector): 

Returns:
    Array[ScriptTypedElementHandle]:

<a id="unreal.TypedElementCommonActions.delete_selected_elements"></a>

#### delete_selected_elements

```python
def delete_selected_elements(
        selection_set: TypedElementSelectionSet, world: World,
        deletion_options: TypedElementDeletionOptions) -> bool
```

x.delete_selected_elements(selection_set, world, deletion_options) -> bool
Delete any elements from the given selection set that can be deleted.
note: Internally this just calls DeleteNormalizedElements on the result of UTypedElementSelectionSet::GetNormalizedSelection.

Args:
    selection_set (TypedElementSelectionSet): 
    world (World): 
    deletion_options (TypedElementDeletionOptions): 

Returns:
    bool:

<a id="unreal.TypedElementCommonActions.delete_normalized_elements"></a>

#### delete_normalized_elements

```python
def delete_normalized_elements(
        element_list: TypedElementList, world: World,
        selection_set: TypedElementSelectionSet,
        deletion_options: TypedElementDeletionOptions) -> bool
```

x.delete_normalized_elements(element_list, world, selection_set, deletion_options) -> bool
Delete any elements from the given list that can be deleted.
note: This list should have been pre-normalized via UTypedElementSelectionSet::GetNormalizedSelection or UTypedElementSelectionSet::GetNormalizedElementList.

Args:
    element_list (TypedElementList): 
    world (World): 
    selection_set (TypedElementSelectionSet): 
    deletion_options (TypedElementDeletionOptions): 

Returns:
    bool:

<a id="unreal.TypedElementCommonActions.copy_selected_elements_to_string"></a>

#### copy_selected_elements_to_string

```python
def copy_selected_elements_to_string(
        selection_set: TypedElementSelectionSet) -> Optional[str]
```

x.copy_selected_elements_to_string(selection_set) -> str or None
Copy any elements from the given selection set that can be copied into the string
note: Internally this just calls CopyNormalizedElements on the result of UTypedElementSelectionSet::GetNormalizedSelection.

Args:
    selection_set (TypedElementSelectionSet): 

Returns:
    str or None: 

    output_string (str):

<a id="unreal.TypedElementCommonActions.copy_selected_elements"></a>

#### copy_selected_elements

```python
def copy_selected_elements(selection_set: TypedElementSelectionSet) -> bool
```

x.copy_selected_elements(selection_set) -> bool
Copy any elements from the given selection set that can be copied into the clipboard
note: Internally this just calls CopyNormalizedElements on the result of UTypedElementSelectionSet::GetNormalizedSelection.

Args:
    selection_set (TypedElementSelectionSet): 

Returns:
    bool:

<a id="unreal.TypedElementCommonActions.copy_normalized_elements_to_string"></a>

#### copy_normalized_elements_to_string

```python
def copy_normalized_elements_to_string(
        element_list: TypedElementList) -> Optional[str]
```

x.copy_normalized_elements_to_string(element_list) -> str or None
* Copy any elements from the given selection set that can be copied into the clipboard.
*
note: This list should have been pre-normalized via UTypedElementSelectionSet::GetNormalizedSelection or UTypedElementSelectionSet::GetNormalizedElementList.

Args:
    element_list (TypedElementList): 

Returns:
    str or None: 

    output_string (str):

<a id="unreal.TypedElementCommonActions.copy_normalized_elements"></a>

#### copy_normalized_elements

```python
def copy_normalized_elements(element_list: TypedElementList) -> bool
```

x.copy_normalized_elements(element_list) -> bool
* Copy any elements from the given selection set that can be copied into the clipboard.
*
note: This list should have been pre-normalized via UTypedElementSelectionSet::GetNormalizedSelection or UTypedElementSelectionSet::GetNormalizedElementList.

Args:
    element_list (TypedElementList): 

Returns:
    bool:

<a id="unreal.TypedElementWorldInterface"></a>