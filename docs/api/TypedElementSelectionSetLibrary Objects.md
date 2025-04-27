## TypedElementSelectionSetLibrary Objects

```python
class TypedElementSelectionSetLibrary(Object)
```

Library of functions for the scripting of Typed Elements that use both a selection set and a element list

Note: These functions should only be used for scripting purposes only as they come at higher performance cost then their non script implementation

**C++ Source:**

- **Module**: TypedElementRuntime
- **File**: TypedElementSelectionSetLibrary.h

<a id="unreal.TypedElementSelectionSetLibrary.set_selection_from_list"></a>

#### set_selection_from_list

```python
@classmethod
def set_selection_from_list(
        cls, selection_set: TypedElementSelectionSet,
        element_list: TypedElementList,
        selection_options: TypedElementSelectionOptions) -> bool
```

X.set_selection_from_list(selection_set, element_list, selection_options) -> bool
Attempt to make the selection the given elements.
note: Equivalent to calling ClearSelection then SelectElements, but happens in a single batch.

Args:
    selection_set (TypedElementSelectionSet): 
    element_list (TypedElementList): 
    selection_options (TypedElementSelectionOptions): 

Returns:
    bool: True if the selection was changed, false otherwise.

<a id="unreal.TypedElementSelectionSetLibrary.select_elements_from_list"></a>

#### select_elements_from_list

```python
@classmethod
def select_elements_from_list(
        cls, selection_set: TypedElementSelectionSet,
        element_list: TypedElementList,
        selection_options: TypedElementSelectionOptions) -> bool
```

X.select_elements_from_list(selection_set, element_list, selection_options) -> bool
Attempt to select the given elements.

Args:
    selection_set (TypedElementSelectionSet): 
    element_list (TypedElementList): 
    selection_options (TypedElementSelectionOptions): 

Returns:
    bool: True if the selection was changed, false otherwise.

<a id="unreal.TypedElementSelectionSetLibrary.get_normalized_selection"></a>

#### get_normalized_selection

```python
@classmethod
def get_normalized_selection(
    cls, selection_set: TypedElementSelectionSet,
    normalization_options: TypedElementSelectionNormalizationOptions
) -> TypedElementList
```

X.get_normalized_selection(selection_set, normalization_options) -> TypedElementList
Get a normalized version of this selection set that can be used to perform operations like gizmo manipulation, deletion, copying, etc.
This will do things like expand out groups, and resolve any parent<->child elements so that duplication operations aren't performed on both the parent and the child.

Args:
    selection_set (TypedElementSelectionSet): 
    normalization_options (TypedElementSelectionNormalizationOptions): 

Returns:
    TypedElementList:

<a id="unreal.TypedElementSelectionSetLibrary.get_normalized_element_list"></a>

#### get_normalized_element_list

```python
@classmethod
def get_normalized_element_list(
    cls, selection_set: TypedElementSelectionSet,
    element_list: TypedElementList,
    normalization_options: TypedElementSelectionNormalizationOptions
) -> TypedElementList
```

X.get_normalized_element_list(selection_set, element_list, normalization_options) -> TypedElementList
Get a normalized version of the given element list that can be used to perform operations like gizmo manipulation, deletion, copying, etc.
This will do things like expand out groups, and resolve any parent<->child elements so that duplication operations aren't performed on both the parent and the child.

Args:
    selection_set (TypedElementSelectionSet): 
    element_list (TypedElementList): 
    normalization_options (TypedElementSelectionNormalizationOptions): 

Returns:
    TypedElementList:

<a id="unreal.TypedElementSelectionSetLibrary.deselect_elements_from_list"></a>

#### deselect_elements_from_list

```python
@classmethod
def deselect_elements_from_list(
        cls, selection_set: TypedElementSelectionSet,
        element_list: TypedElementList,
        selection_options: TypedElementSelectionOptions) -> bool
```

X.deselect_elements_from_list(selection_set, element_list, selection_options) -> bool
Attempt to deselect the given elements.

Args:
    selection_set (TypedElementSelectionSet): 
    element_list (TypedElementList): 
    selection_options (TypedElementSelectionOptions): 

Returns:
    bool: True if the selection was changed, false otherwise.

<a id="unreal.TypedElementAssetDataInterface"></a>