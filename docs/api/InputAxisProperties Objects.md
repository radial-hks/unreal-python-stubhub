## InputAxisProperties Objects

```python
class InputAxisProperties(StructBase)
```

Configurable properties for control axes, used to transform raw input into game ready values.

**C++ Source:**

- **Module**: Engine
- **File**: PlayerInput.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dead_zone`` (float):  [Read-Write] What the dead zone of the axis is.  For control axes such as analog sticks.
- ``exponent`` (float):  [Read-Write] For applying curves to [0..1] axes, e.g. analog sticks
- ``invert`` (bool):  [Read-Write] Inverts reported values for this axis
- ``sensitivity`` (float):  [Read-Write] Scaling factor to multiply raw value by.

<a id="unreal.InputAxisProperties.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.NiagaraSystemScalabilitySettings"></a>