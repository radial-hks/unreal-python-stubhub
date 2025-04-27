## AnimSyncMarker Objects

```python
class AnimSyncMarker(StructBase)
```

Anim Sync Marker

**C++ Source:**

- **Module**: Engine
- **File**: AnimTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``marker_name`` (Name):  [Read-Write] The name of this marker
- ``time`` (float):  [Read-Write] Time in seconds of this marker

<a id="unreal.AnimSyncMarker.__init__"></a>

#### __init__

```python
def __init__(marker_name: Name = "None", time: float = 0.000000) -> None
```

<a id="unreal.AnimSyncMarker.marker_name"></a>

#### marker_name

```python
@property
def marker_name() -> Name
```

(Name):  [Read-Only] The name of this marker

<a id="unreal.AnimSyncMarker.time"></a>

#### time

```python
@property
def time() -> float
```

(float):  [Read-Only] Time in seconds of this marker

<a id="unreal.RawAnimSequenceTrack"></a>