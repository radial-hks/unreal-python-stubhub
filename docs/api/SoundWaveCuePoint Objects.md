## SoundWaveCuePoint Objects

```python
class SoundWaveCuePoint(StructBase)
```

Struct defining a cue point in a sound wave asset

**C++ Source:**

- **Module**: Engine
- **File**: SoundWave.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cue_point_id`` (int32):  [Read-Only] Unique identifier for the wave cue point
- ``frame_length`` (int32):  [Read-Only] The frame length of the cue point (non-zero if it's a region)
- ``frame_position`` (int32):  [Read-Only] The frame position of the cue point
- ``is_loop_region`` (bool):  [Read-Only] intentionally kept private.
  only USoundFactory should modify this value on import
- ``label`` (str):  [Read-Only] The label for the cue point

<a id="unreal.SoundWaveCuePoint.__init__"></a>

#### __init__

```python
def __init__(cue_point_id: int = 0,
             label: str = "",
             frame_position: int = 0,
             frame_length: int = 0) -> None
```

<a id="unreal.SoundWaveCuePoint.cue_point_id"></a>

#### cue_point_id

```python
@property
def cue_point_id() -> int
```

(int32):  [Read-Only] Unique identifier for the wave cue point

<a id="unreal.SoundWaveCuePoint.label"></a>

#### label

```python
@property
def label() -> str
```

(str):  [Read-Only] The label for the cue point

<a id="unreal.SoundWaveCuePoint.frame_position"></a>

#### frame_position

```python
@property
def frame_position() -> int
```

(int32):  [Read-Only] The frame position of the cue point

<a id="unreal.SoundWaveCuePoint.frame_length"></a>

#### frame_length

```python
@property
def frame_length() -> int
```

(int32):  [Read-Only] The frame length of the cue point (non-zero if it's a region)

<a id="unreal.EquirectProps"></a>