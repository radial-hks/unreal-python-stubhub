## UniversalObjectLocatorScriptingExtensions Objects

```python
class UniversalObjectLocatorScriptingExtensions(BlueprintFunctionLibrary)
```

Function library containing methods that should be hoisted onto FUniversalObjectLocators for scripting

**C++ Source:**

- **Module**: Engine
- **File**: UniversalObjectLocatorScriptingExtensions.h

<a id="unreal.UniversalObjectLocatorScriptingExtensions.universal_object_locator_from_string"></a>

#### universal_object_locator_from_string

```python
@classmethod
def universal_object_locator_from_string(
        cls, string: str) -> UniversalObjectLocator
```

X.universal_object_locator_from_string(string) -> UniversalObjectLocator
Construct a new universal object locator from a string

Args:
    string (str): 

Returns:
    UniversalObjectLocator:

<a id="unreal.UniversalObjectLocatorScriptingExtensions.to_string"></a>

#### to_string

```python
@classmethod
def to_string(cls, locator: UniversalObjectLocator) -> str
```

X.to_string(locator) -> str
Convert the specified locator to its string representation

Args:
    locator (UniversalObjectLocator): 

Returns:
    str:

<a id="unreal.UniversalObjectLocatorScriptingExtensions.sync_unload"></a>

#### sync_unload

```python
@classmethod
def sync_unload(cls,
                locator: UniversalObjectLocator,
                context: Object = None) -> None
```

X.sync_unload(locator, context=None) -> None
Attempt to resolve the object locator by unloading the object if possible.

Args:
    locator (UniversalObjectLocator): 
    context (Object): (Optional) Context object to use for resolving the object. This should usually be the object that owns or created the locator.

<a id="unreal.UniversalObjectLocatorScriptingExtensions.sync_load"></a>

#### sync_load

```python
@classmethod
def sync_load(cls,
              locator: UniversalObjectLocator,
              context: Object = None) -> Object
```

X.sync_load(locator, context=None) -> Object
Attempt to resolve the object locator by finding or loading the object.

Args:
    locator (UniversalObjectLocator): 
    context (Object): (Optional) Context object to use for resolving the object. This should usually be the object that owns or created the locator.

Returns:
    Object: The resolve object pointer, or null if it was not found.

<a id="unreal.UniversalObjectLocatorScriptingExtensions.sync_find"></a>

#### sync_find

```python
@classmethod
def sync_find(cls,
              locator: UniversalObjectLocator,
              context: Object = None) -> Object
```

X.sync_find(locator, context=None) -> Object
Attempt to resolve the object locator by finding the object. If it is not currently loaded or created,

Args:
    locator (UniversalObjectLocator): 
    context (Object): (Optional) Context object to use for resolving the object. This should usually be the object that owns or created the locator.

Returns:
    Object: The resolve object pointer, or null if it was not found.

<a id="unreal.UniversalObjectLocatorScriptingExtensions.make_universal_object_locator"></a>

#### make_universal_object_locator

```python
@classmethod
def make_universal_object_locator(cls, object: Object,
                                  context: Object) -> UniversalObjectLocator
```

X.make_universal_object_locator(object, context) -> UniversalObjectLocator
Construct a new universal object locator

Args:
    object (Object): 
    context (Object): 

Returns:
    UniversalObjectLocator:

<a id="unreal.UniversalObjectLocatorScriptingExtensions.is_empty"></a>

#### is_empty

```python
@classmethod
def is_empty(cls, locator: UniversalObjectLocator) -> bool
```

X.is_empty(locator) -> bool
Check whether the specified locator is empty; not equivalent to Resolve() != None.
An empty locator will never resolve to a valid object.

Args:
    locator (UniversalObjectLocator): 

Returns:
    bool:

<a id="unreal.VectorFieldComponent"></a>