## AnimDataModel Objects

```python
class AnimDataModel(Object)
```

The Model represents the source data for animations. It contains both bone animation data as well as animated curves.
They are currently only a sub-object of a AnimSequenceBase instance. The instance derives all runtime data from the source data.

**C++ Source:**

- **Module**: Engine
- **File**: AnimDataModel.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``animated_bone_attributes`` (Array[AnimatedBoneAttribute]):  [Read-Only] Container with all animated (bone) attribute data
- ``bone_animation_tracks`` (Array[BoneAnimationTrack]):  [Read-Only] All individual bone animation tracks
- ``curve_data`` (AnimationCurveData):  [Read-Only] Container with all animated curve data
- ``frame_rate`` (FrameRate):  [Read-Only] Rate at which the animated data is sampled
- ``modified_event`` (AnimDataModelModifiedDynamicEvent):  [Read-Write] Dynamic delegate event allows scripting to register to any broadcasted notify.
- ``number_of_frames`` (int32):  [Read-Only] Total number of sampled animated frames
- ``number_of_keys`` (int32):  [Read-Only] Total number of sampled animated keys
- ``play_length`` (float):  [Read-Only]

<a id="unreal.AnimDataModel.modified_event"></a>

#### modified_event

```python
@property
def modified_event() -> AnimDataModelModifiedDynamicEvent
```

(AnimDataModelModifiedDynamicEvent):  [Read-Write] Dynamic delegate event allows scripting to register to any broadcasted notify.

<a id="unreal.AnimDataModel.modified_event"></a>

#### modified_event

```python
@modified_event.setter
def modified_event(value: AnimDataModelModifiedDynamicEvent) -> None
```

<a id="unreal.AnimDataModel.bone_animation_tracks"></a>

#### bone_animation_tracks

```python
@property
def bone_animation_tracks() -> Array[BoneAnimationTrack]
```

(Array[BoneAnimationTrack]):  [Read-Only] All individual bone animation tracks

<a id="unreal.AnimDataModel.play_length"></a>

#### play_length

```python
@property
def play_length() -> float
```

(float):  [Read-Only]

<a id="unreal.AnimDataModel.frame_rate"></a>

#### frame_rate

```python
@property
def frame_rate() -> FrameRate
```

(FrameRate):  [Read-Only] Rate at which the animated data is sampled

<a id="unreal.AnimDataModel.number_of_frames"></a>

#### number_of_frames

```python
@property
def number_of_frames() -> int
```

(int32):  [Read-Only] Total number of sampled animated frames

<a id="unreal.AnimDataModel.number_of_keys"></a>

#### number_of_keys

```python
@property
def number_of_keys() -> int
```

(int32):  [Read-Only] Total number of sampled animated keys

<a id="unreal.AnimDataModel.curve_data"></a>

#### curve_data

```python
@property
def curve_data() -> AnimationCurveData
```

(AnimationCurveData):  [Read-Only] Container with all animated curve data

<a id="unreal.AnimDataModel.animated_bone_attributes"></a>

#### animated_bone_attributes

```python
@property
def animated_bone_attributes() -> Array[AnimatedBoneAttribute]
```

(Array[AnimatedBoneAttribute]):  [Read-Only] Container with all animated (bone) attribute data

<a id="unreal.AnimDataModel.is_valid_bone_track_name"></a>

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

<a id="unreal.AnimDataModel.is_valid_bone_track_index"></a>

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

<a id="unreal.AnimDataModel.get_play_length"></a>

#### get_play_length

```python
def get_play_length() -> float
```

x.get_play_length() -> double


Returns:
    double: Total length of play-able animation data

<a id="unreal.AnimDataModel.get_num_bone_tracks"></a>

#### get_num_bone_tracks

```python
def get_num_bone_tracks() -> int
```

x.get_num_bone_tracks() -> int32


Returns:
    int32: Total number of bone animation tracks

<a id="unreal.AnimDataModel.get_number_of_transform_curves"></a>

#### get_number_of_transform_curves

```python
def get_number_of_transform_curves() -> int
```

x.get_number_of_transform_curves() -> int32


Returns:
    int32: Total number of stored FTransform curves

<a id="unreal.AnimDataModel.get_number_of_keys"></a>

#### get_number_of_keys

```python
def get_number_of_keys() -> int
```

x.get_number_of_keys() -> int32


Returns:
    int32: Total number of animation data keys stored

<a id="unreal.AnimDataModel.get_number_of_frames"></a>

#### get_number_of_frames

```python
def get_number_of_frames() -> int
```

x.get_number_of_frames() -> int32


Returns:
    int32: Total number of frames of animation data stored

<a id="unreal.AnimDataModel.get_number_of_float_curves"></a>

#### get_number_of_float_curves

```python
def get_number_of_float_curves() -> int
```

x.get_number_of_float_curves() -> int32


Returns:
    int32: Total number of stored float curves

<a id="unreal.AnimDataModel.get_frame_rate"></a>

#### get_frame_rate

```python
def get_frame_rate() -> FrameRate
```

x.get_frame_rate() -> FrameRate


Returns:
    FrameRate: Frame rate at which the animation data is key-ed

<a id="unreal.AnimDataModel.get_bone_track_names"></a>

#### get_bone_track_names

```python
def get_bone_track_names() -> Array[Name]
```

x.get_bone_track_names() -> Array[Name]
Populates the provided array with all contained (bone) track names

Returns:
    Array[Name]: 

    out_names (Array[Name]): [out] Array containing all bone track names

<a id="unreal.AnimDataModel.get_bone_track_index_by_name"></a>

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

<a id="unreal.AnimDataModel.get_bone_track_index"></a>

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

<a id="unreal.AnimDataModel.get_bone_track_by_name"></a>

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

<a id="unreal.AnimDataModel.get_bone_track_by_index"></a>

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

<a id="unreal.AnimDataModel.get_bone_animation_tracks"></a>

#### get_bone_animation_tracks

```python
def get_bone_animation_tracks() -> Array[BoneAnimationTrack]
```

x.get_bone_animation_tracks() -> Array[BoneAnimationTrack]
Get Bone Animation Tracks

Returns:
    Array[BoneAnimationTrack]:

<a id="unreal.AnimDataModel.get_animation_sequence"></a>

#### get_animation_sequence

```python
def get_animation_sequence() -> AnimSequence
```

x.get_animation_sequence() -> AnimSequence


Returns:
    AnimSequence: The outer UAnimSequence object if found, otherwise returns a nullptr

<a id="unreal.AnimMetaData"></a>