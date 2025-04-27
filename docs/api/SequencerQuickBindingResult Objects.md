## SequencerQuickBindingResult Objects

```python
class SequencerQuickBindingResult(StructBase)
```

Wrapper around result of quick binding for event track in sequencer.

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScriptingEditor
- **File**: SequencerTools.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``payload_names`` (Array[str]):  [Read-Write] Names of the payload variables of the event.

<a id="unreal.SequencerQuickBindingResult.__init__"></a>

#### __init__

```python
def __init__(payload_names: Array[str] = []) -> None
```

<a id="unreal.SequencerQuickBindingResult.payload_names"></a>

#### payload_names

```python
@property
def payload_names() -> Array[str]
```

(Array[str]):  [Read-Only] Names of the payload variables of the event.

<a id="unreal.SequencerExportFBXParams"></a>