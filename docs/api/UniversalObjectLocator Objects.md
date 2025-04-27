## UniversalObjectLocator Objects

```python
class UniversalObjectLocator(StructBase)
```

Universal Object Locators (UOLs) define an address to an object.

The address is implemented as a chain of FUniversalObjectLocatorFragments, allowing addressing of objects
  that may be nested deeply within levels of externally defined spawn or ownership logic.

For example, a Universal Object Locator may reference an Anim Instance within a Skeletal Mesh Actor
  is spawned by a Child Actor Component that is spawned by Sequencer. This is impossible with a
  regular soft object path, but is perfectly feasible for a UOL.

This type is 16 bytes.

**C++ Source:**

- **Module**: UniversalObjectLocator
- **File**: UniversalObjectLocator.h

<a id="unreal.UniversalObjectLocator.__init__"></a>

#### __init__

```python
def __init__(object: Object = None, context: Object = None) -> None
```

<a id="unreal.UniversalObjectLocator.to_string"></a>

#### to_string

```python
def to_string() -> str
```

x.to_string() -> str
Convert the specified locator to its string representation

Returns:
    str:

<a id="unreal.UniversalObjectLocator.sync_unload"></a>

#### sync_unload

```python
def sync_unload(context: Object = None) -> None
```

x.sync_unload(context=None) -> None
Attempt to resolve the object locator by unloading the object if possible.

Args:
    context (Object): (Optional) Context object to use for resolving the object. This should usually be the object that owns or created the locator.

<a id="unreal.UniversalObjectLocator.sync_load"></a>

#### sync_load

```python
def sync_load(context: Object = None) -> Object
```

x.sync_load(context=None) -> Object
Attempt to resolve the object locator by finding or loading the object.

Args:
    context (Object): (Optional) Context object to use for resolving the object. This should usually be the object that owns or created the locator.

Returns:
    Object: The resolve object pointer, or null if it was not found.

<a id="unreal.UniversalObjectLocator.sync_find"></a>

#### sync_find

```python
def sync_find(context: Object = None) -> Object
```

x.sync_find(context=None) -> Object
Attempt to resolve the object locator by finding the object. If it is not currently loaded or created,

Args:
    context (Object): (Optional) Context object to use for resolving the object. This should usually be the object that owns or created the locator.

Returns:
    Object: The resolve object pointer, or null if it was not found.

<a id="unreal.UniversalObjectLocator.is_empty"></a>

#### is_empty

```python
def is_empty() -> bool
```

x.is_empty() -> bool
Check whether the specified locator is empty; not equivalent to Resolve() != None.
An empty locator will never resolve to a valid object.

Returns:
    bool:

<a id="unreal.UniversalObjectLocatorFragment"></a>