## TypedElementList Objects

```python
class TypedElementList(StructBase)
```

A list of script element handles (proxy to a FScriptTypedElementList instance).
Provides high-level access to groups of elements, including accessing elements that implement specific interfaces.

Note: the script list proxy use should be avoided when not using it for the script exposure apis.
The weak model for the handles come with an additional cost to the runtime performance and the memory usage.

**C++ Source:**

- **Module**: TypedElementFramework
- **File**: TypedElementListProxy.h

<a id="unreal.TypedElementList.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.TypedElementList.shrink"></a>

#### shrink

```python
def shrink() -> None
```

x.shrink() -> None
Shrink this element list storage to avoid slack.

<a id="unreal.TypedElementList.reset"></a>

#### reset

```python
def reset() -> None
```

x.reset() -> None
Remove all entries from this element list, preserving existing allocations.

<a id="unreal.TypedElementList.reserve"></a>

#### reserve

```python
def reserve(size: int) -> None
```

x.reserve(size) -> None
Pre-allocate enough memory in this element list to store the given number of entries.

Args:
    size (int32):

<a id="unreal.TypedElementList.remove"></a>

#### remove

```python
def remove(element_handle: ScriptTypedElementHandle) -> bool
```

x.remove(element_handle) -> bool
Remove the given element handle from this element list, if it is in the list.

Args:
    element_handle (ScriptTypedElementHandle): 

Returns:
    bool: True if the element handle was removed, false if it isn't in the list.

<a id="unreal.TypedElementList.num"></a>

#### num

```python
def num() -> int
```

x.num() -> int32
Get the number of entries within this element list.

Returns:
    int32:

<a id="unreal.TypedElementList.is_valid_index"></a>

#### is_valid_index

```python
def is_valid_index(index: int) -> bool
```

x.is_valid_index(index) -> bool
Is the given index a valid entry within this element list?

Args:
    index (int32): 

Returns:
    bool:

<a id="unreal.TypedElementList.has_elements_of_type"></a>

#### has_elements_of_type

```python
def has_elements_of_type(element_type_name: Name) -> bool
```

x.has_elements_of_type(element_type_name) -> bool
Test whether there are elements in this list of the given type.

Args:
    element_type_name (Name): 

Returns:
    bool:

<a id="unreal.TypedElementList.has_elements"></a>

#### has_elements

```python
def has_elements(base_interface_type: Class = None) -> bool
```

x.has_elements(base_interface_type=None) -> bool
Test whether there are elements in this list, optionally filtering to elements that implement the given interface.

Args:
    base_interface_type (type(Class)): 

Returns:
    bool:

<a id="unreal.TypedElementList.get_element_interface"></a>

#### get_element_interface

```python
def get_element_interface(element_handle: ScriptTypedElementHandle,
                          base_interface_type: Class) -> Object
```

x.get_element_interface(element_handle, base_interface_type) -> Object
Get the element interface from the given handle.

Args:
    element_handle (ScriptTypedElementHandle): 
    base_interface_type (type(Class)): 

Returns:
    Object:

<a id="unreal.TypedElementList.get_element_handles"></a>

#### get_element_handles

```python
def get_element_handles(
        base_interface_type: Class) -> Array[ScriptTypedElementHandle]
```

x.get_element_handles(base_interface_type) -> Array[ScriptTypedElementHandle]
Get the handle of every element in this list, optionally filtering to elements that implement the given interface.

Args:
    base_interface_type (type(Class)): 

Returns:
    Array[ScriptTypedElementHandle]:

<a id="unreal.TypedElementList.get_element_handle_at"></a>

#### get_element_handle_at

```python
def get_element_handle_at(index: int) -> ScriptTypedElementHandle
```

x.get_element_handle_at(index) -> ScriptTypedElementHandle
Get the element handle at the given index.
note: Use IsValidIndex to test for validity.

Args:
    index (int32): 

Returns:
    ScriptTypedElementHandle:

<a id="unreal.TypedElementList.empty"></a>

#### empty

```python
def empty(slack: int = 0) -> None
```

x.empty(slack=0) -> None
Remove all entries from this element list, potentially leaving space allocated for the given number of entries.

Args:
    slack (int32):

<a id="unreal.TypedElementList.count_elements_of_type"></a>

#### count_elements_of_type

```python
def count_elements_of_type(element_type_name: Name) -> int
```

x.count_elements_of_type(element_type_name) -> int32
Count the number of elements in this list of the given type.

Args:
    element_type_name (Name): 

Returns:
    int32:

<a id="unreal.TypedElementList.count_elements"></a>

#### count_elements

```python
def count_elements(base_interface_type: Class = None) -> int
```

x.count_elements(base_interface_type=None) -> int32
Count the number of elements in this list, optionally filtering to elements that implement the given interface.

Args:
    base_interface_type (type(Class)): 

Returns:
    int32:

<a id="unreal.TypedElementList.contains"></a>

#### contains

```python
def contains(element_handle: ScriptTypedElementHandle) -> bool
```

x.contains(element_handle) -> bool
Does this element list contain an entry for the given element handle?

Args:
    element_handle (ScriptTypedElementHandle): 

Returns:
    bool:

<a id="unreal.TypedElementList.clone"></a>

#### clone

```python
def clone() -> TypedElementList
```

x.clone() -> TypedElementList
Clone this list instance.
note: Only copies elements; does not copy any bindings!

Returns:
    TypedElementList:

<a id="unreal.TypedElementList.append_list"></a>

#### append_list

```python
def append_list(other_element_list: TypedElementList) -> None
```

x.append_list(other_element_list) -> None
Append the another element list to this element list.

Args:
    other_element_list (TypedElementList):

<a id="unreal.TypedElementList.append"></a>

#### append

```python
def append(element_handles: Array[ScriptTypedElementHandle]) -> None
```

x.append(element_handles) -> None
Append the given element handles to this element list.

Args:
    element_handles (Array[ScriptTypedElementHandle]):

<a id="unreal.TypedElementList.add"></a>

#### add

```python
def add(element_handle: ScriptTypedElementHandle) -> bool
```

x.add(element_handle) -> bool
Add the given element handle to this element list, if it isn't already in the list.

Args:
    element_handle (ScriptTypedElementHandle): 

Returns:
    bool: True if the element handle was added, false if it is already in the list.

<a id="unreal.TypedElementSelectionNormalizationOptions"></a>