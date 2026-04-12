## AnimationDataModel Objects

```python
class AnimationDataModel(Interface)
```

Animation Data Model

**C++ Source:**

- **Module**: Engine
- **File**: IAnimationDataModel.h

<a id="unreal.AnimationDataModel.is_valid_bone_track_name"></a>

#### is\_valid\_bone\_track\_name

```python
def is_valid_bone_track_name(track_name: Name) -> bool
```

x.is_valid_bone_track_name(track_name) -> bool
Is Valid Bone Track Name

Args:
    track_name (Name): 

Returns:
    bool:

<a id="unreal.AnimationDataModel.is_valid_bone_track_index"></a>

#### is\_valid\_bone\_track\_index

```python
def is_valid_bone_track_index(track_index: int) -> bool
```

x.is_valid_bone_track_index(track_index) -> bool
Is Valid Bone Track Index

Args:
    track_index (int32): 

Returns:
    bool:

<a id="unreal.AnimationDataModel.get_play_length"></a>

#### get\_play\_length

```python
def get_play_length() -> float
```

x.get_play_length() -> double


Returns:
    double: Total length of play-able animation data

<a id="unreal.AnimationDataModel.get_num_bone_tracks"></a>

#### get\_num\_bone\_tracks

```python
def get_num_bone_tracks() -> int
```

x.get_num_bone_tracks() -> int32


Returns:
    int32: Total number of bone animation tracks

<a id="unreal.AnimationDataModel.get_number_of_transform_curves"></a>

#### get\_number\_of\_transform\_curves

```python
def get_number_of_transform_curves() -> int
```

x.get_number_of_transform_curves() -> int32


Returns:
    int32: Total number of stored FTransform curves

<a id="unreal.AnimationDataModel.get_number_of_keys"></a>

#### get\_number\_of\_keys

```python
def get_number_of_keys() -> int
```

x.get_number_of_keys() -> int32


Returns:
    int32: Total number of animation data keys stored

<a id="unreal.AnimationDataModel.get_number_of_frames"></a>

#### get\_number\_of\_frames

```python
def get_number_of_frames() -> int
```

x.get_number_of_frames() -> int32


Returns:
    int32: Total number of frames of animation data stored

<a id="unreal.AnimationDataModel.get_number_of_float_curves"></a>

#### get\_number\_of\_float\_curves

```python
def get_number_of_float_curves() -> int
```

x.get_number_of_float_curves() -> int32


Returns:
    int32: Total number of stored float curves

<a id="unreal.AnimationDataModel.get_frame_rate"></a>

#### get\_frame\_rate

```python
def get_frame_rate() -> FrameRate
```

x.get_frame_rate() -> FrameRate


Returns:
    FrameRate: Frame rate at which the animation data is key-ed

<a id="unreal.AnimationDataModel.get_bone_track_names"></a>

#### get\_bone\_track\_names

```python
def get_bone_track_names() -> Array[Name]
```

x.get_bone_track_names() -> Array[Name]
Populates the provided array with all contained (bone) track names

Returns:
    Array[Name]: 

    out_names (Array[Name]): [out] Array containing all bone track names

<a id="unreal.AnimationDataModel.get_bone_track_index_by_name"></a>

#### get\_bone\_track\_index\_by\_name

```python
def get_bone_track_index_by_name(track_name: Name) -> int
```

x.get_bone_track_index_by_name(track_name) -> int32
Get Bone Track Index by Name

Args:
    track_name (Name): 

Returns:
    int32:

<a id="unreal.AnimationDataModel.get_bone_track_index"></a>

#### get\_bone\_track\_index

```python
def get_bone_track_index(track: BoneAnimationTrack) -> int
```

x.get_bone_track_index(track) -> int32
Get Bone Track Index

Args:
    track (BoneAnimationTrack): 

Returns:
    int32:

<a id="unreal.AnimationDataModel.get_bone_track_by_name"></a>

#### get\_bone\_track\_by\_name

```python
def get_bone_track_by_name(track_name: Name) -> BoneAnimationTrack
```

x.get_bone_track_by_name(track_name) -> BoneAnimationTrack
Get Bone Track by Name

Args:
    track_name (Name): 

Returns:
    BoneAnimationTrack:

<a id="unreal.AnimationDataModel.get_bone_track_by_index"></a>

#### get\_bone\_track\_by\_index

```python
def get_bone_track_by_index(track_index: int) -> BoneAnimationTrack
```

x.get_bone_track_by_index(track_index) -> BoneAnimationTrack
Get Bone Track by Index

Args:
    track_index (int32): 

Returns:
    BoneAnimationTrack:

<a id="unreal.AnimationDataModel.get_bone_animation_tracks"></a>

#### get\_bone\_animation\_tracks

```python
def get_bone_animation_tracks() -> Array[BoneAnimationTrack]
```

x.get_bone_animation_tracks() -> Array[BoneAnimationTrack]
Get Bone Animation Tracks

Returns:
    Array[BoneAnimationTrack]:

<a id="unreal.AnimationDataModel.get_animation_sequence"></a>

#### get\_animation\_sequence

```python
def get_animation_sequence() -> AnimSequence
```

x.get_animation_sequence() -> AnimSequence


Returns:
    AnimSequence: The outer UAnimSequence object if found, otherwise returns a nullptr

<a id="unreal.Interface_AssetUserData"></a>