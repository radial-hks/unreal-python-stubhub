## AnimationTrackAddedPayload Objects

```python
class AnimationTrackAddedPayload(AnimationTrackPayload)
```

Animation Track Added Payload

**C++ Source:**

- **Module**: Engine
- **File**: AnimDataNotifications.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (Name):  [Read-Write] Name of the track (bone)
- ``track_index`` (int32):  [Read-Write]

<a id="unreal.AnimationTrackAddedPayload.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None", track_index: int = 0) -> None
```

<a id="unreal.AnimationTrackAddedPayload.track_index"></a>

#### track_index

```python
@property
def track_index() -> int
```

(int32):  [Read-Only]

<a id="unreal.SequenceLengthChangedPayload"></a>