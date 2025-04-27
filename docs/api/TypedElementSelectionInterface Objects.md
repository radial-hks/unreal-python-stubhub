## TypedElementSelectionInterface Objects

```python
class TypedElementSelectionInterface(Interface)
```

Typed Element Selection Interface

**C++ Source:**

- **Module**: TypedElementRuntime
- **File**: TypedElementSelectionInterface.h

<a id="unreal.TypedElementSelectionInterface.select_element"></a>

#### select_element

```python
def select_element(element_handle: ScriptTypedElementHandle,
                   selection_set: TypedElementList,
                   selection_options: TypedElementSelectionOptions) -> bool
```

x.select_element(element_handle, selection_set, selection_options) -> bool
Attempt to select the given element.

Args:
    element_handle (ScriptTypedElementHandle): 
    selection_set (TypedElementList): 
    selection_options (TypedElementSelectionOptions): 

Returns:
    bool: True if the selection was changed, false otherwise.

<a id="unreal.TypedElementSelectionInterface.is_element_selected"></a>

#### is_element_selected

```python
def is_element_selected(
        element_handle: ScriptTypedElementHandle,
        selection_set: TypedElementList,
        selection_options: TypedElementIsSelectedOptions) -> bool
```

x.is_element_selected(element_handle, selection_set, selection_options) -> bool
Test to see whether the given element is currently considered selected.

Args:
    element_handle (ScriptTypedElementHandle): 
    selection_set (TypedElementList): 
    selection_options (TypedElementIsSelectedOptions): 

Returns:
    bool:

<a id="unreal.TypedElementSelectionInterface.get_selection_element"></a>

#### get_selection_element

```python
def get_selection_element(
        element_handle: ScriptTypedElementHandle,
        current_selection: TypedElementList,
        selection_method: TypedElementSelectionMethod
) -> ScriptTypedElementHandle
```

x.get_selection_element(element_handle, current_selection, selection_method) -> ScriptTypedElementHandle
Given an element, return the element that should actually perform a selection operation.

Args:
    element_handle (ScriptTypedElementHandle): 
    current_selection (TypedElementList): 
    selection_method (TypedElementSelectionMethod): 

Returns:
    ScriptTypedElementHandle:

<a id="unreal.TypedElementSelectionInterface.deselect_element"></a>

#### deselect_element

```python
def deselect_element(element_handle: ScriptTypedElementHandle,
                     selection_set: TypedElementList,
                     selection_options: TypedElementSelectionOptions) -> bool
```

x.deselect_element(element_handle, selection_set, selection_options) -> bool
Attempt to deselect the given element.

Args:
    element_handle (ScriptTypedElementHandle): 
    selection_set (TypedElementList): 
    selection_options (TypedElementSelectionOptions): 

Returns:
    bool: True if the selection was changed, false otherwise.

<a id="unreal.TypedElementSelectionInterface.can_select_element"></a>

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

<a id="unreal.TypedElementSelectionInterface.can_deselect_element"></a>

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

<a id="unreal.TypedElementSelectionInterface.allow_selection_modifiers"></a>

#### allow_selection_modifiers

```python
def allow_selection_modifiers(element_handle: ScriptTypedElementHandle,
                              selection_set: TypedElementList) -> bool
```

x.allow_selection_modifiers(element_handle, selection_set) -> bool
Test to see whether selection modifiers (Ctrl or Shift) are allowed while selecting this element.

Args:
    element_handle (ScriptTypedElementHandle): 
    selection_set (TypedElementList): 

Returns:
    bool:

<a id="unreal.SharedImageConstRefBlueprintFns"></a>