## DialogueWave Objects

```python
class DialogueWave(Object)
```

Dialogue Wave

**C++ Source:**

- **Module**: Engine
- **File**: DialogueWave.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``context_mappings`` (Array[DialogueContextMapping]):  [Read-Write] Mappings between dialogue contexts and associated soundwaves.
- ``mature`` (bool):  [Read-Write] true if this dialogue is considered to contain mature/adult content.
- ``override_subtitle_override`` (bool):  [Read-Write]
- ``spoken_text`` (str):  [Read-Write] A localized version of the text that is actually spoken phonetically in the audio.
- ``subtitle_override`` (str):  [Read-Write] A localized version of the subtitle text that should be displayed for this audio. By default this will be the same as the Spoken Text.
- ``voice_actor_direction`` (str):  [Read-Write] Provides general notes to the voice actor intended to direct their performance, as well as contextual information to the translator.

<a id="unreal.DialogueWave.mature"></a>

#### mature

```python
@property
def mature() -> bool
```

(bool):  [Read-Only] true if this dialogue is considered to contain mature/adult content.

<a id="unreal.DialogueWave.override_subtitle_override"></a>

#### override_subtitle_override

```python
@property
def override_subtitle_override() -> bool
```

(bool):  [Read-Only]

<a id="unreal.DialogueWave.spoken_text"></a>

#### spoken_text

```python
@property
def spoken_text() -> str
```

(str):  [Read-Only] A localized version of the text that is actually spoken phonetically in the audio.

<a id="unreal.DialogueWave.subtitle_override"></a>

#### subtitle_override

```python
@property
def subtitle_override() -> str
```

(str):  [Read-Only] A localized version of the subtitle text that should be displayed for this audio. By default this will be the same as the Spoken Text.

<a id="unreal.DocumentationActor"></a>