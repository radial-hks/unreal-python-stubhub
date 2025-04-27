## TypedElementObjectInterface Objects

```python
class TypedElementObjectInterface(Interface)
```

Typed Element Object Interface

**C++ Source:**

- **Module**: TypedElementRuntime
- **File**: TypedElementObjectInterface.h

<a id="unreal.TypedElementObjectInterface.get_object_class"></a>

#### get_object_class

```python
def get_object_class(element_handle: ScriptTypedElementHandle) -> Class
```

x.get_object_class(element_handle) -> type(Class)
Gets the object instance's class that the handle represents, if any.

Args:
    element_handle (ScriptTypedElementHandle): 

Returns:
    type(Class):

<a id="unreal.TypedElementObjectInterface.get_object"></a>

#### get_object

```python
def get_object(element_handle: ScriptTypedElementHandle) -> Object
```

x.get_object(element_handle) -> Object
Get the object instance that this handle represents, if any.

Args:
    element_handle (ScriptTypedElementHandle): 

Returns:
    Object:

<a id="unreal.TypedElementPrimitiveCustomDataInterface"></a>