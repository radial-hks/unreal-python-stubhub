## TypedElementListLibrary Objects

```python
class TypedElementListLibrary(Object)
```

Typed Element List Library

**C++ Source:**

- **Module**: TypedElementFramework
- **File**: TypedElementListLibrary.h

<a id="unreal.TypedElementListLibrary.shrink"></a>

#### shrink

```python
@classmethod
def shrink(cls, element_list: TypedElementList) -> None
```

X.shrink(element_list) -> None
Shrink this element list storage to avoid slack.

Args:
    element_list (TypedElementList):

<a id="unreal.TypedElementListLibrary.reset"></a>

#### reset

```python
@classmethod
def reset(cls, element_list: TypedElementList) -> None
```

X.reset(element_list) -> None
Remove all entries from this element list, preserving existing allocations.

Args:
    element_list (TypedElementList):

<a id="unreal.TypedElementListLibrary.reserve"></a>

#### reserve

```python
@classmethod
def reserve(cls, element_list: TypedElementList, size: int) -> None
```

X.reserve(element_list, size) -> None
Pre-allocate enough memory in this element list to store the given number of entries.

Args:
    element_list (TypedElementList): 
    size (int32):

<a id="unreal.TypedElementListLibrary.remove"></a>

#### remove

```python
@classmethod
def remove(cls, element_list: TypedElementList,
           element_handle: ScriptTypedElementHandle) -> bool
```

X.remove(element_list, element_handle) -> bool
Remove the given element handle from this element list, if it is in the list.

Args:
    element_list (TypedElementList): 
    element_handle (ScriptTypedElementHandle): 

Returns:
    bool: True if the element handle was removed, false if it isn't in the list.

<a id="unreal.TypedElementListLibrary.num"></a>

#### num

```python
@classmethod
def num(cls, element_list: TypedElementList) -> int
```

X.num(element_list) -> int32
Get the number of entries within this element list.

Args:
    element_list (TypedElementList): 

Returns:
    int32:

<a id="unreal.TypedElementListLibrary.is_valid_index"></a>

#### is_valid_index

```python
@classmethod
def is_valid_index(cls, element_list: TypedElementList, index: int) -> bool
```

X.is_valid_index(element_list, index) -> bool
Is the given index a valid entry within this element list?

Args:
    element_list (TypedElementList): 
    index (int32): 

Returns:
    bool:

<a id="unreal.TypedElementListLibrary.has_elements_of_type"></a>

#### has_elements_of_type

```python
@classmethod
def has_elements_of_type(cls, element_list: TypedElementList,
                         element_type_name: Name) -> bool
```

X.has_elements_of_type(element_list, element_type_name) -> bool
Test whether there are elements in this list of the given type.

Args:
    element_list (TypedElementList): 
    element_type_name (Name): 

Returns:
    bool:

<a id="unreal.TypedElementListLibrary.has_elements"></a>

#### has_elements

```python
@classmethod
def has_elements(cls,
                 element_list: TypedElementList,
                 base_interface_type: Class = None) -> bool
```

X.has_elements(element_list, base_interface_type=None) -> bool
Test whether there are elements in this list, optionally filtering to elements that implement the given interface.

Args:
    element_list (TypedElementList): 
    base_interface_type (type(Class)): 

Returns:
    bool:

<a id="unreal.TypedElementListLibrary.get_element_interface"></a>

#### get_element_interface

```python
@classmethod
def get_element_interface(cls, element_list: TypedElementList,
                          element_handle: ScriptTypedElementHandle,
                          base_interface_type: Class) -> Object
```

X.get_element_interface(element_list, element_handle, base_interface_type) -> Object
Get the element interface from the given handle.

Args:
    element_list (TypedElementList): 
    element_handle (ScriptTypedElementHandle): 
    base_interface_type (type(Class)): 

Returns:
    Object:

<a id="unreal.TypedElementListLibrary.get_element_handles"></a>

#### get_element_handles

```python
@classmethod
def get_element_handles(
        cls, element_list: TypedElementList,
        base_interface_type: Class) -> Array[ScriptTypedElementHandle]
```

X.get_element_handles(element_list, base_interface_type) -> Array[ScriptTypedElementHandle]
Get the handle of every element in this list, optionally filtering to elements that implement the given interface.

Args:
    element_list (TypedElementList): 
    base_interface_type (type(Class)): 

Returns:
    Array[ScriptTypedElementHandle]:

<a id="unreal.TypedElementListLibrary.get_element_handle_at"></a>

#### get_element_handle_at

```python
@classmethod
def get_element_handle_at(cls, element_list: TypedElementList,
                          index: int) -> ScriptTypedElementHandle
```

X.get_element_handle_at(element_list, index) -> ScriptTypedElementHandle
Get the element handle at the given index.
note: Use IsValidIndex to test for validity.

Args:
    element_list (TypedElementList): 
    index (int32): 

Returns:
    ScriptTypedElementHandle:

<a id="unreal.TypedElementListLibrary.empty"></a>

#### empty

```python
@classmethod
def empty(cls, element_list: TypedElementList, slack: int = 0) -> None
```

X.empty(element_list, slack=0) -> None
Remove all entries from this element list, potentially leaving space allocated for the given number of entries.

Args:
    element_list (TypedElementList): 
    slack (int32):

<a id="unreal.TypedElementListLibrary.create_element_list"></a>

#### create_element_list

```python
@classmethod
def create_element_list(cls,
                        registry: TypedElementRegistry) -> TypedElementList
```

X.create_element_list(registry) -> TypedElementList
Create an empty list of elements associated with the given registry.

Args:
    registry (TypedElementRegistry): 

Returns:
    TypedElementList:

<a id="unreal.TypedElementListLibrary.count_elements_of_type"></a>

#### count_elements_of_type

```python
@classmethod
def count_elements_of_type(cls, element_list: TypedElementList,
                           element_type_name: Name) -> int
```

X.count_elements_of_type(element_list, element_type_name) -> int32
Count the number of elements in this list of the given type.

Args:
    element_list (TypedElementList): 
    element_type_name (Name): 

Returns:
    int32:

<a id="unreal.TypedElementListLibrary.count_elements"></a>

#### count_elements

```python
@classmethod
def count_elements(cls,
                   element_list: TypedElementList,
                   base_interface_type: Class = None) -> int
```

X.count_elements(element_list, base_interface_type=None) -> int32
Count the number of elements in this list, optionally filtering to elements that implement the given interface.

Args:
    element_list (TypedElementList): 
    base_interface_type (type(Class)): 

Returns:
    int32:

<a id="unreal.TypedElementListLibrary.contains"></a>

#### contains

```python
@classmethod
def contains(cls, element_list: TypedElementList,
             element_handle: ScriptTypedElementHandle) -> bool
```

X.contains(element_list, element_handle) -> bool
Does this element list contain an entry for the given element handle?

Args:
    element_list (TypedElementList): 
    element_handle (ScriptTypedElementHandle): 

Returns:
    bool:

<a id="unreal.TypedElementListLibrary.clone"></a>

#### clone

```python
@classmethod
def clone(cls, element_list: TypedElementList) -> TypedElementList
```

X.clone(element_list) -> TypedElementList
Clone this list instance.
note: Only copies elements; does not copy any bindings!

Args:
    element_list (TypedElementList): 

Returns:
    TypedElementList:

<a id="unreal.TypedElementListLibrary.append_list"></a>

#### append_list

```python
@classmethod
def append_list(cls, element_list: TypedElementList,
                other_element_list: TypedElementList) -> None
```

X.append_list(element_list, other_element_list) -> None
Append the another element list to this element list.

Args:
    element_list (TypedElementList): 
    other_element_list (TypedElementList):

<a id="unreal.TypedElementListLibrary.append"></a>

#### append

```python
@classmethod
def append(cls, element_list: TypedElementList,
           element_handles: Array[ScriptTypedElementHandle]) -> None
```

X.append(element_list, element_handles) -> None
Append the given element handles to this element list.

Args:
    element_list (TypedElementList): 
    element_handles (Array[ScriptTypedElementHandle]):

<a id="unreal.TypedElementListLibrary.add"></a>

#### add

```python
@classmethod
def add(cls, element_list: TypedElementList,
        element_handle: ScriptTypedElementHandle) -> bool
```

X.add(element_list, element_handle) -> bool
Add the given element handle to this element list, if it isn't already in the list.

Args:
    element_list (TypedElementList): 
    element_handle (ScriptTypedElementHandle): 

Returns:
    bool: True if the element handle was added, false if it is already in the list.

<a id="unreal.TestTypedElementInterfaceA"></a>