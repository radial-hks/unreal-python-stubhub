## KeyBind Objects

```python
class KeyBind(StructBase)
```

Struct containing mappings for legacy method of binding keys to exec commands.

**C++ Source:**

- **Module**: Engine
- **File**: PlayerInput.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alt`` (bool):  [Read-Write] Whether the alt key needs to be held when the key event occurs
- ``cmd`` (bool):  [Read-Write] Whether the command key needs to be held when the key event occurs
- ``command`` (str):  [Read-Write] The command to execute when the key is pressed/released
- ``control`` (bool):  [Read-Write] Whether the control key needs to be held when the key event occurs
- ``ignore_alt`` (bool):  [Read-Write] Whether the alt key must not be held when the key event occurs
- ``ignore_cmd`` (bool):  [Read-Write] Whether the command key must not be held when the key event occurs
- ``ignore_ctrl`` (bool):  [Read-Write] Whether the control key must not be held when the key event occurs
- ``ignore_shift`` (bool):  [Read-Write] Whether the shift key must not be held when the key event occurs
- ``key`` (Key):  [Read-Write] The key to be bound to the command
- ``shift`` (bool):  [Read-Write] Whether the shift key needs to be held when the key event occurs

<a id="unreal.KeyBind.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.NiagaraSystemScalabilityOverrides"></a>