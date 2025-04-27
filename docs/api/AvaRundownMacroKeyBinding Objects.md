## AvaRundownMacroKeyBinding Objects

```python
class AvaRundownMacroKeyBinding(StructBase)
```

Defines a macro (list of commands) that is assigned to a shortcut key.

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheMedia
- **File**: AvaRundownMacroCollection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``commands`` (Array[AvaRundownMacroCommand]):  [Read-Write] List of commands this macro will run.
- ``description`` (str):  [Read-Write] Macro description
- ``input_chord`` (InputChord):  [Read-Write] Input Key this Macro is bound to.

<a id="unreal.AvaRundownMacroKeyBinding.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.NiagaraPlatformSetRedirect"></a>