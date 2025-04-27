## TypedElementRegistry Objects

```python
class TypedElementRegistry(Object)
```

Registry of element types and their associated interfaces, along with the elements that represent their instances.

**C++ Source:**

- **Module**: TypedElementFramework
- **File**: TypedElementRegistry.h

<a id="unreal.TypedElementRegistry.get_default_typed_element_registry"></a>

#### get_default_typed_element_registry

```python
@classmethod
def get_default_typed_element_registry(cls) -> TypedElementRegistry
```

X.get_default_typed_element_registry() -> TypedElementRegistry
Get the singleton instance of the registry used in most cases.

Returns:
    TypedElementRegistry:

<a id="unreal.TypedElementRegistry.get_element_interface"></a>

#### get_element_interface

```python
def get_element_interface(element_handle: ScriptTypedElementHandle,
                          base_interface_type: Class) -> Object
```

x.get_element_interface(element_handle, base_interface_type) -> Object
Get the element interface supported by the given handle, or null if there is no support for this interface or if the handle is invalid.

Args:
    element_handle (ScriptTypedElementHandle): 
    base_interface_type (type(Class)): 

Returns:
    Object:

<a id="unreal.TypedElementRegistry.create_element_list"></a>

#### create_element_list

```python
def create_element_list() -> TypedElementList
```

x.create_element_list() -> TypedElementList
Create an empty list of elements associated with the given registry.

Returns:
    TypedElementList:

<a id="unreal.TypedElementListLibrary"></a>