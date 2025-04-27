## InputDeviceId Objects

```python
class InputDeviceId(StructBase)
```

Represents a single input device such as a gamepad, keyboard, or mouse.

Has a globally unique identifier.

Opaque struct for the FInputDeviceId struct defined in CoreMiscDefines.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``internal_id`` (int32):  [Read-Only]

<a id="unreal.InputDeviceId.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.InputDeviceId.not_equal"></a>

#### not_equal

```python
def not_equal(b: InputDeviceId) -> bool
```

x.not_equal(b) -> bool
Returns true if InputDeviceId A is not equal to InputDeviceId B (A != B)

Args:
    b (InputDeviceId): 

Returns:
    bool:

<a id="unreal.InputDeviceId.equals"></a>

#### equals

```python
def equals(b: InputDeviceId) -> bool
```

x.equals(b) -> bool
Returns true if InputDeviceId A is equal to InputDeviceId B (A == B)

Args:
    b (InputDeviceId): 

Returns:
    bool:

<a id="unreal.InputDeviceId.__eq__"></a>

#### __eq__

```python
def __eq__(other: object) -> bool
```

**Overloads:**

- ``InputDeviceId`` Returns true if InputDeviceId A is equal to InputDeviceId B (A == B)

<a id="unreal.InputDeviceId.__ne__"></a>

#### __ne__

```python
def __ne__(other: object) -> bool
```

**Overloads:**

- ``InputDeviceId`` Returns true if InputDeviceId A is not equal to InputDeviceId B (A != B)

<a id="unreal.InputDeviceId.NONE"></a>

#### NONE

(InputDeviceId): Static invalid input device

<a id="unreal.Int32Interval"></a>