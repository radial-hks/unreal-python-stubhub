## PlatformUserId Objects

```python
class PlatformUserId(StructBase)
```

Handle that defines a local user on this platform.
This used to be just a typedef int32 that was used interchangeably as ControllerId and LocalUserIndex.
Moving forward these will be allocated by the platform application layer.

Opaque struct for the FPlatformUserId struct defined in CoreMiscDefines.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``internal_id`` (int32):  [Read-Only]

<a id="unreal.PlatformUserId.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.PlatformUserId.not_equal"></a>

#### not_equal

```python
def not_equal(b: PlatformUserId) -> bool
```

x.not_equal(b) -> bool
Returns true if PlatformUserId A is not equal to PlatformUserId B (A != B)

Args:
    b (PlatformUserId): 

Returns:
    bool:

<a id="unreal.PlatformUserId.equals"></a>

#### equals

```python
def equals(b: PlatformUserId) -> bool
```

x.equals(b) -> bool
Returns true if PlatformUserId A is equal to PlatformUserId B (A == B)

Args:
    b (PlatformUserId): 

Returns:
    bool:

<a id="unreal.PlatformUserId.__eq__"></a>

#### __eq__

```python
def __eq__(other: object) -> bool
```

**Overloads:**

- ``PlatformUserId`` Returns true if PlatformUserId A is equal to PlatformUserId B (A == B)

<a id="unreal.PlatformUserId.__ne__"></a>

#### __ne__

```python
def __ne__(other: object) -> bool
```

**Overloads:**

- ``PlatformUserId`` Returns true if PlatformUserId A is not equal to PlatformUserId B (A != B)

<a id="unreal.PlatformUserId.NONE"></a>

#### NONE

(PlatformUserId): Static invalid platform user

<a id="unreal.PolyglotTextData"></a>