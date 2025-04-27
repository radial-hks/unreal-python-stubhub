## SubtitleCue Objects

```python
class SubtitleCue(StructBase)
```

A line of subtitle text and the time at which it should be displayed.

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``text`` (Text):  [Read-Write] The text to appear in the subtitle.
- ``time`` (float):  [Read-Write] The time at which the subtitle is to be displayed, in seconds relative to the beginning of the line.

<a id="unreal.SubtitleCue.__init__"></a>

#### __init__

```python
def __init__(text: Text = "", time: float = 0.000000) -> None
```

<a id="unreal.SubtitleCue.text"></a>

#### text

```python
@property
def text() -> Text
```

(Text):  [Read-Only] The text to appear in the subtitle.

<a id="unreal.SubtitleCue.time"></a>

#### time

```python
@property
def time() -> float
```

(float):  [Read-Only] The time at which the subtitle is to be displayed, in seconds relative to the beginning of the line.

<a id="unreal.ChaosRemovalEvent"></a>