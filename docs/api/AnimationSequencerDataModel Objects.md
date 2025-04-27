## AnimationSequencerDataModel Objects

```python
class AnimationSequencerDataModel(MovieSceneSequence)
```

Animation Sequencer Data Model

**C++ Source:**

- **Plugin**: AnimationData
- **Module**: AnimationData
- **File**: AnimSequencerDataModel.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``animated_bone_attributes`` (Array[AnimatedBoneAttribute]):  [Read-Only]
- ``cached_raw_data_guid`` (Guid):  [Read-Only] Raw data GUID taken from UAnimSequence when initially populating - this allows for retaining compressed data state initially
- ``curve_identifier_to_meta_data`` (Map[AnimationCurveIdentifier, AnimationCurveMetaData]):  [Read-Only] Per-curve information holding flags/color, due to be deprecated in the future
- ``legacy_curve_data`` (AnimationCurveData):  [Read-Only]
- ``modified_event`` (AnimDataModelModifiedDynamicEvent):  [Read-Write] Dynamic delegate event allows scripting to register to any broadcast-ed notify.
- ``movie_scene`` (MovieScene):  [Read-Only] Movie scene instance containing FK Control rig and section representing the animation data
- ``populated`` (bool):  [Read-Only]

<a id="unreal.AnimationSequencerDataModel.modified_event"></a>

#### modified_event

```python
@property
def modified_event() -> AnimDataModelModifiedDynamicEvent
```

(AnimDataModelModifiedDynamicEvent):  [Read-Write] Dynamic delegate event allows scripting to register to any broadcast-ed notify.

<a id="unreal.AnimationSequencerDataModel.modified_event"></a>

#### modified_event

```python
@modified_event.setter
def modified_event(value: AnimDataModelModifiedDynamicEvent) -> None
```

<a id="unreal.AnimationSequencerDataModel.is_valid_bone_track_name"></a>

#### is_valid_bone_track_name

```python
def is_valid_bone_track_name(track_name: Name) -> bool
```

x.is_valid_bone_track_name(track_name) -> bool
Is Valid Bone Track Name

Args:
    track_name (Name): 

Returns:
    bool:

<a id="unreal.AnimationSequencerDataModel.is_valid_bone_track_index"></a>

#### is_valid_bone_track_index

```python
def is_valid_bone_track_index(track_index: int) -> bool
```

x.is_valid_bone_track_index(track_index) -> bool
Is Valid Bone Track Index

Args:
    track_index (int32): 

Returns:
    bool:

<a id="unreal.AnimationSequencerDataModel.get_play_length"></a>

#### get_play_length

```python
def get_play_length() -> float
```

x.get_play_length() -> double


Returns:
    double: Total length of play-able animation data

<a id="unreal.AnimationSequencerDataModel.get_num_bone_tracks"></a>

#### get_num_bone_tracks

```python
def get_num_bone_tracks() -> int
```

x.get_num_bone_tracks() -> int32


Returns:
    int32: Total number of bone animation tracks

<a id="unreal.AnimationSequencerDataModel.get_number_of_transform_curves"></a>

#### get_number_of_transform_curves

```python
def get_number_of_transform_curves() -> int
```

x.get_number_of_transform_curves() -> int32


Returns:
    int32: Total number of stored FTransform curves

<a id="unreal.AnimationSequencerDataModel.get_number_of_keys"></a>

#### get_number_of_keys

```python
def get_number_of_keys() -> int
```

x.get_number_of_keys() -> int32


Returns:
    int32: Total number of animation data keys stored

<a id="unreal.AnimationSequencerDataModel.get_number_of_frames"></a>

#### get_number_of_frames

```python
def get_number_of_frames() -> int
```

x.get_number_of_frames() -> int32


Returns:
    int32: Total number of frames of animation data stored

<a id="unreal.AnimationSequencerDataModel.get_number_of_float_curves"></a>

#### get_number_of_float_curves

```python
def get_number_of_float_curves() -> int
```

x.get_number_of_float_curves() -> int32


Returns:
    int32: Total number of stored float curves

<a id="unreal.AnimationSequencerDataModel.get_frame_rate"></a>

#### get_frame_rate

```python
def get_frame_rate() -> FrameRate
```

x.get_frame_rate() -> FrameRate


Returns:
    FrameRate: Frame rate at which the animation data is key-ed

<a id="unreal.AnimationSequencerDataModel.get_bone_track_names"></a>

#### get_bone_track_names

```python
def get_bone_track_names() -> Array[Name]
```

x.get_bone_track_names() -> Array[Name]
Populates the provided array with all contained (bone) track names

Returns:
    Array[Name]: 

    out_names (Array[Name]): [out] Array containing all bone track names

<a id="unreal.AnimationSequencerDataModel.get_bone_track_index_by_name"></a>

#### get_bone_track_index_by_name

```python
def get_bone_track_index_by_name(track_name: Name) -> int
```

x.get_bone_track_index_by_name(track_name) -> int32
Get Bone Track Index by Name

Args:
    track_name (Name): 

Returns:
    int32:

<a id="unreal.AnimationSequencerDataModel.get_bone_track_index"></a>

#### get_bone_track_index

```python
def get_bone_track_index(track: BoneAnimationTrack) -> int
```

x.get_bone_track_index(track) -> int32
Get Bone Track Index

Args:
    track (BoneAnimationTrack): 

Returns:
    int32:

<a id="unreal.AnimationSequencerDataModel.get_bone_track_by_name"></a>

#### get_bone_track_by_name

```python
def get_bone_track_by_name(track_name: Name) -> BoneAnimationTrack
```

x.get_bone_track_by_name(track_name) -> BoneAnimationTrack
Get Bone Track by Name

Args:
    track_name (Name): 

Returns:
    BoneAnimationTrack:

<a id="unreal.AnimationSequencerDataModel.get_bone_track_by_index"></a>

#### get_bone_track_by_index

```python
def get_bone_track_by_index(track_index: int) -> BoneAnimationTrack
```

x.get_bone_track_by_index(track_index) -> BoneAnimationTrack
Get Bone Track by Index

Args:
    track_index (int32): 

Returns:
    BoneAnimationTrack:

<a id="unreal.AnimationSequencerDataModel.get_bone_animation_tracks"></a>

#### get_bone_animation_tracks

```python
def get_bone_animation_tracks() -> Array[BoneAnimationTrack]
```

x.get_bone_animation_tracks() -> Array[BoneAnimationTrack]
Get Bone Animation Tracks

Returns:
    Array[BoneAnimationTrack]:

<a id="unreal.AnimationSequencerDataModel.get_animation_sequence"></a>

#### get_animation_sequence

```python
def get_animation_sequence() -> AnimSequence
```

x.get_animation_sequence() -> AnimSequence


Returns:
    AnimSequence: The outer UAnimSequence object if found, otherwise returns a nullptr

<a id="unreal.BlendStackAnimNodeLibrary"></a>