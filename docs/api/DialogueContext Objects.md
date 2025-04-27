## DialogueContext Objects

```python
class DialogueContext(StructBase)
```

Dialogue Context

**C++ Source:**

- **Module**: Engine
- **File**: DialogueTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``speaker`` (DialogueVoice):  [Read-Write] The person speaking the dialogue.
- ``targets`` (Array[DialogueVoice]):  [Read-Write] The people being spoken to.

<a id="unreal.DialogueContext.__init__"></a>

#### __init__

```python
def __init__(speaker: DialogueVoice = None,
             targets: Array[DialogueVoice] = []) -> None
```

<a id="unreal.DialogueContext.speaker"></a>

#### speaker

```python
@property
def speaker() -> DialogueVoice
```

(DialogueVoice):  [Read-Write] The person speaking the dialogue.

<a id="unreal.DialogueContext.speaker"></a>

#### speaker

```python
@speaker.setter
def speaker(value: DialogueVoice) -> None
```

<a id="unreal.DialogueContext.targets"></a>

#### targets

```python
@property
def targets() -> Array[DialogueVoice]
```

(Array[DialogueVoice]):  [Read-Write] The people being spoken to.

<a id="unreal.DialogueContext.targets"></a>

#### targets

```python
@targets.setter
def targets(value: Array[DialogueVoice]) -> None
```

<a id="unreal.TypedElementPasteOptions"></a>