## TypedElementHandleLibrary Objects

```python
class TypedElementHandleLibrary(Object)
```

Script exposure for FScriptTypedElementHandle.

**C++ Source:**

- **Module**: TypedElementFramework
- **File**: TypedElementHandle.h

<a id="unreal.TypedElementHandleLibrary.release"></a>

#### release

```python
@classmethod
def release(
        cls,
        element_handle: ScriptTypedElementHandle) -> ScriptTypedElementHandle
```

X.release(element_handle) -> ScriptTypedElementHandle
Release this handle and set it back to an empty state.

Args:
    element_handle (ScriptTypedElementHandle): 

Returns:
    ScriptTypedElementHandle: 

    element_handle (ScriptTypedElementHandle):

<a id="unreal.TypedElementHandleLibrary.not_equal"></a>

#### not_equal

```python
@classmethod
def not_equal(cls, lhs: ScriptTypedElementHandle,
              rhs: ScriptTypedElementHandle) -> bool
```

X.not_equal(lhs, rhs) -> bool
Are these two handles not equal?

Args:
    lhs (ScriptTypedElementHandle): 
    rhs (ScriptTypedElementHandle): 

Returns:
    bool:

<a id="unreal.TypedElementHandleLibrary.is_set"></a>

#### is_set

```python
@classmethod
def is_set(cls, element_handle: ScriptTypedElementHandle) -> bool
```

X.is_set(element_handle) -> bool
Has this handle been initialized to a valid element?

Args:
    element_handle (ScriptTypedElementHandle): 

Returns:
    bool:

<a id="unreal.TypedElementHandleLibrary.equal"></a>

#### equal

```python
@classmethod
def equal(cls, lhs: ScriptTypedElementHandle,
          rhs: ScriptTypedElementHandle) -> bool
```

X.equal(lhs, rhs) -> bool
Are these two handles equal?

Args:
    lhs (ScriptTypedElementHandle): 
    rhs (ScriptTypedElementHandle): 

Returns:
    bool:

<a id="unreal.TypedElementRegistry"></a>