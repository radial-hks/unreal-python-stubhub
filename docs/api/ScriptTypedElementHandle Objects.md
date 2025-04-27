## ScriptTypedElementHandle Objects

```python
class ScriptTypedElementHandle(StructBase)
```

Script exposure for the typed element handle struct type
Act as a weak handle to simplify the scripting use of the typed element framework and making it safer to use by avoiding crash in case of a bad usage.
This type is the standard way that an element is passed through to interfaces for a script (Blueprint or Python), and also the type that is stored in the script element lists.
C++ code may choose to use TTypedElement instead, which is a combination of an element handle and its associated element interface.

Note: This type shouldn't be used in the engine code as it come with a performance and memory overhead that we want to avoid when compare to the native handles (FTypedElementHandle).

**C++ Source:**

- **Module**: TypedElementFramework
- **File**: TypedElementHandle.h

<a id="unreal.ScriptTypedElementHandle.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.ScriptTypedElementHandle.release"></a>

#### release

```python
def release() -> None
```

x.release() -> None
Release this handle and set it back to an empty state.

<a id="unreal.ScriptTypedElementHandle.not_equal"></a>

#### not_equal

```python
def not_equal(rhs: ScriptTypedElementHandle) -> bool
```

x.not_equal(rhs) -> bool
Are these two handles not equal?

Args:
    rhs (ScriptTypedElementHandle): 

Returns:
    bool:

<a id="unreal.ScriptTypedElementHandle.is_set"></a>

#### is_set

```python
def is_set() -> bool
```

x.is_set() -> bool
Has this handle been initialized to a valid element?

Returns:
    bool:

<a id="unreal.ScriptTypedElementHandle.equal"></a>

#### equal

```python
def equal(rhs: ScriptTypedElementHandle) -> bool
```

x.equal(rhs) -> bool
Are these two handles equal?

Args:
    rhs (ScriptTypedElementHandle): 

Returns:
    bool:

<a id="unreal.ScriptTypedElementHandle.__bool__"></a>

#### __bool__

```python
def __bool__() -> bool
```

Has this handle been initialized to a valid element?

<a id="unreal.ScriptTypedElementHandle.__eq__"></a>

#### __eq__

```python
def __eq__(other: object) -> bool
```

**Overloads:**

- ``ScriptTypedElementHandle`` Are these two handles equal?

<a id="unreal.ScriptTypedElementHandle.__ne__"></a>

#### __ne__

```python
def __ne__(other: object) -> bool
```

**Overloads:**

- ``ScriptTypedElementHandle`` Are these two handles not equal?

<a id="unreal.TypedElementSelectionOptions"></a>