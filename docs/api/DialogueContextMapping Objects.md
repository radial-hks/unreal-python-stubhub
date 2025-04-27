## DialogueContextMapping Objects

```python
class DialogueContextMapping(StructBase)
```

Dialogue Context Mapping

**C++ Source:**

- **Module**: Engine
- **File**: DialogueWave.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``context`` (DialogueContext):  [Read-Write] The context of the dialogue.
- ``localization_key_format`` (str):  [Read-Write] The format string to use when generating the localization key for this context. This must be unique within the owner dialogue wave.
  Available format markers:
    * {ContextHash} - A hash generated from the speaker and target voices.
- ``sound_wave`` (SoundWave):  [Read-Write] The soundwave to play for this dialogue.

<a id="unreal.DialogueContextMapping.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.FontCharacter"></a>