## TypedElementHierarchyInterface Objects

```python
class TypedElementHierarchyInterface(Interface)
```

Typed Element Hierarchy Interface

**C++ Source:**

- **Module**: TypedElementRuntime
- **File**: TypedElementHierarchyInterface.h

<a id="unreal.TypedElementHierarchyInterface.get_parent_element"></a>

#### get_parent_element

```python
def get_parent_element(element_handle: ScriptTypedElementHandle,
                       allow_create: bool = True) -> ScriptTypedElementHandle
```

x.get_parent_element(element_handle, allow_create=True) -> ScriptTypedElementHandle
Get the logical parent of this element, if any.
eg) A component might return its actor, or a static mesh instance might return its ISM component.

Args:
    element_handle (ScriptTypedElementHandle): 
    allow_create (bool): 

Returns:
    ScriptTypedElementHandle:

<a id="unreal.TypedElementHierarchyInterface.get_child_elements"></a>

#### get_child_elements

```python
def get_child_elements(
        element_handle: ScriptTypedElementHandle,
        allow_create: bool = True) -> Array[ScriptTypedElementHandle]
```

x.get_child_elements(element_handle, allow_create=True) -> Array[ScriptTypedElementHandle]
Get the logical children of this element, if any.
eg) An actor might return its component, or an ISM component might return its static mesh instances.
note: Appends to OutElementHandles.

Args:
    element_handle (ScriptTypedElementHandle): 
    allow_create (bool): 

Returns:
    Array[ScriptTypedElementHandle]: 

    out_element_handles (Array[ScriptTypedElementHandle]):

<a id="unreal.TypedElementObjectInterface"></a>