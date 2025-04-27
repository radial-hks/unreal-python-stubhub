## AnimationLibrary Objects

```python
class AnimationLibrary(BlueprintFunctionLibrary)
```

Blueprint library for altering and analyzing animation / skeletal data

**C++ Source:**

- **Module**: AnimationBlueprintLibrary
- **File**: AnimationBlueprintLibrary.h

<a id="unreal.AnimationLibrary.set_variable_frame_stripping_settings"></a>

#### set_variable_frame_stripping_settings

```python
@classmethod
def set_variable_frame_stripping_settings(
        cls, animation_sequence: AnimSequence,
        variable_frame_stripping_settings: VariableFrameStrippingSettings
) -> None
```

X.set_variable_frame_stripping_settings(animation_sequence, variable_frame_stripping_settings) -> None
Sets the Variable Frame Stripping Settings for the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 
    variable_frame_stripping_settings (VariableFrameStrippingSettings):

<a id="unreal.AnimationLibrary.set_root_motion_lock_type"></a>

#### set_root_motion_lock_type

```python
@classmethod
def set_root_motion_lock_type(
        cls, animation_sequence: AnimSequence,
        root_motion_lock_type: RootMotionRootLock) -> None
```

X.set_root_motion_lock_type(animation_sequence, root_motion_lock_type) -> None
Sets the Root Motion Lock Type for the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 
    root_motion_lock_type (RootMotionRootLock):

<a id="unreal.AnimationLibrary.set_root_motion_enabled"></a>

#### set_root_motion_enabled

```python
@classmethod
def set_root_motion_enabled(cls, animation_sequence: AnimSequence,
                            enabled: bool) -> None
```

X.set_root_motion_enabled(animation_sequence, enabled) -> None
Sets whether or not Root Motion is Enabled for the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 
    enabled (bool):

<a id="unreal.AnimationLibrary.set_rate_scale"></a>

#### set_rate_scale

```python
@classmethod
def set_rate_scale(cls, animation_sequence_base: AnimSequenceBase,
                   rate_scale: float) -> None
```

X.set_rate_scale(animation_sequence_base, rate_scale) -> None
Sets the (Play) Rate Scale for the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 
    rate_scale (float):

<a id="unreal.AnimationLibrary.set_is_root_motion_lock_forced"></a>

#### set_is_root_motion_lock_forced

```python
@classmethod
def set_is_root_motion_lock_forced(cls, animation_sequence: AnimSequence,
                                   forced: bool) -> None
```

X.set_is_root_motion_lock_forced(animation_sequence, forced) -> None
Sets whether or not Root Motion locking is Forced for the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 
    forced (bool):

<a id="unreal.AnimationLibrary.set_curve_compression_settings"></a>

#### set_curve_compression_settings

```python
@classmethod
def set_curve_compression_settings(
        cls, animation_sequence: AnimSequence,
        compression_settings: AnimCurveCompressionSettings) -> None
```

X.set_curve_compression_settings(animation_sequence, compression_settings) -> None
Sets the Curve Compression Settings for the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 
    compression_settings (AnimCurveCompressionSettings):

<a id="unreal.AnimationLibrary.set_bone_compression_settings"></a>

#### set_bone_compression_settings

```python
@classmethod
def set_bone_compression_settings(
        cls, animation_sequence: AnimSequence,
        compression_settings: AnimBoneCompressionSettings) -> None
```

X.set_bone_compression_settings(animation_sequence, compression_settings) -> None
Sets the Bone Compression Settings for the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 
    compression_settings (AnimBoneCompressionSettings):

<a id="unreal.AnimationLibrary.set_animation_interpolation_type"></a>

#### set_animation_interpolation_type

```python
@classmethod
def set_animation_interpolation_type(
        cls, animation_sequence: AnimSequence,
        interpolation_type: AnimInterpolationType) -> None
```

X.set_animation_interpolation_type(animation_sequence, interpolation_type) -> None
Sets the Animation Interpolation type for the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 
    interpolation_type (AnimInterpolationType):

<a id="unreal.AnimationLibrary.set_additive_base_pose_type"></a>

#### set_additive_base_pose_type

```python
@classmethod
def set_additive_base_pose_type(
        cls, animation_sequence: AnimSequence,
        additive_base_pose_type: AdditiveBasePoseType) -> None
```

X.set_additive_base_pose_type(animation_sequence, additive_base_pose_type) -> None
Sets the Additive Base Pose type for the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 
    additive_base_pose_type (AdditiveBasePoseType):

<a id="unreal.AnimationLibrary.set_additive_animation_type"></a>

#### set_additive_animation_type

```python
@classmethod
def set_additive_animation_type(
        cls, animation_sequence: AnimSequence,
        additive_animation_type: AdditiveAnimationType) -> None
```

X.set_additive_animation_type(animation_sequence, additive_animation_type) -> None
Sets the Additive Animation type for the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 
    additive_animation_type (AdditiveAnimationType):

<a id="unreal.AnimationLibrary.replace_anim_notify_states"></a>

#### replace_anim_notify_states

```python
@classmethod
def replace_anim_notify_states(
        cls, animation_sequence_base: AnimSequenceBase,
        old_notify_class: Class, new_notify_class: Class,
        on_notify_state_replaced: OnNotifyStateReplaced) -> None
```

X.replace_anim_notify_states(animation_sequence_base, old_notify_class, new_notify_class, on_notify_state_replaced) -> None
Replaces animation notifies in the specified Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 
    old_notify_class (type(Class)): 
    new_notify_class (type(Class)): 
    on_notify_state_replaced (OnNotifyStateReplaced):

<a id="unreal.AnimationLibrary.replace_anim_notifies"></a>

#### replace_anim_notifies

```python
@classmethod
def replace_anim_notifies(cls, animation_sequence_base: AnimSequenceBase,
                          old_notify_class: Class, new_notify_class: Class,
                          on_notify_replaced: OnNotifyReplaced) -> None
```

X.replace_anim_notifies(animation_sequence_base, old_notify_class, new_notify_class, on_notify_replaced) -> None
Replaces animation notifies in the specified Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 
    old_notify_class (type(Class)): 
    new_notify_class (type(Class)): 
    on_notify_replaced (OnNotifyReplaced):

<a id="unreal.AnimationLibrary.remove_virtual_bones"></a>

#### remove_virtual_bones

```python
@classmethod
def remove_virtual_bones(cls, animation_sequence: AnimSequence,
                         virtual_bone_names: Array[Name]) -> None
```

X.remove_virtual_bones(animation_sequence, virtual_bone_names) -> None
Removes Virtual Bones with the specified Bone Names from the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 
    virtual_bone_names (Array[Name]):

<a id="unreal.AnimationLibrary.remove_virtual_bone"></a>

#### remove_virtual_bone

```python
@classmethod
def remove_virtual_bone(cls, animation_sequence: AnimSequence,
                        virtual_bone_name: Name) -> None
```

X.remove_virtual_bone(animation_sequence, virtual_bone_name) -> None
Removes a Virtual Bone with the specified Bone Name from the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 
    virtual_bone_name (Name):

<a id="unreal.AnimationLibrary.remove_meta_data_of_class"></a>

#### remove_meta_data_of_class

```python
@classmethod
def remove_meta_data_of_class(cls, animation_asset: AnimationAsset,
                              meta_data_class: Class) -> None
```

X.remove_meta_data_of_class(animation_asset, meta_data_class) -> None
Removes all Meta Data Instance of the specified Class from the given Animation Asset

Args:
    animation_asset (AnimationAsset): 
    meta_data_class (type(Class)):

<a id="unreal.AnimationLibrary.remove_meta_data"></a>

#### remove_meta_data

```python
@classmethod
def remove_meta_data(cls, animation_asset: AnimationAsset,
                     meta_data_object: AnimMetaData) -> None
```

X.remove_meta_data(animation_asset, meta_data_object) -> None
Removes the specified Meta Data Instance from the given Animation Asset

Args:
    animation_asset (AnimationAsset): 
    meta_data_object (AnimMetaData):

<a id="unreal.AnimationLibrary.remove_curve"></a>

#### remove_curve

```python
@classmethod
def remove_curve(cls,
                 animation_sequence_base: AnimSequenceBase,
                 curve_name: Name,
                 remove_name_from_skeleton: bool = False) -> None
```

X.remove_curve(animation_sequence_base, curve_name, remove_name_from_skeleton=False) -> None
Removes an Animation Curve by Name from the given Animation Sequence (Raw Animation Curves [Names] may not be removed from the Skeleton)

Args:
    animation_sequence_base (AnimSequenceBase): 
    curve_name (Name): 
    remove_name_from_skeleton (bool):

<a id="unreal.AnimationLibrary.remove_bone_animation"></a>

#### remove_bone_animation

```python
@classmethod
def remove_bone_animation(cls,
                          animation_sequence: AnimSequence,
                          bone_name: Name,
                          include_children: bool = True,
                          finalize: bool = True) -> None
```

X.remove_bone_animation(animation_sequence, bone_name, include_children=True, finalize=True) -> None
Removes an Animation Curve by Name from the given Animation Sequence (Raw Animation Curves [Names] may not be removed from the Skeleton)

Args:
    animation_sequence (AnimSequence): : AnimSequence
    bone_name (Name): : Name of bone track user wants to remove
    include_children (bool): : true if user wants to include all children of BoneName
    finalize (bool): : If you set this to true, it will trigger compression. If you set bFinalize to be false, you'll have to manually trigger Finalize.

<a id="unreal.AnimationLibrary.remove_animation_sync_markers_by_track"></a>

#### remove_animation_sync_markers_by_track

```python
@classmethod
def remove_animation_sync_markers_by_track(cls,
                                           animation_sequence: AnimSequence,
                                           notify_track_name: Name) -> int
```

X.remove_animation_sync_markers_by_track(animation_sequence, notify_track_name) -> int32
Removes All Animation Sync Marker found within the Animation Sequence that belong to the specific Notify Track, and returns the number of removed instances

Args:
    animation_sequence (AnimSequence): 
    notify_track_name (Name): 

Returns:
    int32:

<a id="unreal.AnimationLibrary.remove_animation_sync_markers_by_name"></a>

#### remove_animation_sync_markers_by_name

```python
@classmethod
def remove_animation_sync_markers_by_name(cls,
                                          animation_sequence: AnimSequence,
                                          marker_name: Name) -> int
```

X.remove_animation_sync_markers_by_name(animation_sequence, marker_name) -> int32
Removes All Animation Sync Marker found within the Animation Sequence whose name matches MarkerName, and returns the number of removed instances

Args:
    animation_sequence (AnimSequence): 
    marker_name (Name): 

Returns:
    int32:

<a id="unreal.AnimationLibrary.remove_animation_notify_track"></a>

#### remove_animation_notify_track

```python
@classmethod
def remove_animation_notify_track(cls,
                                  animation_sequence_base: AnimSequenceBase,
                                  notify_track_name: Name) -> None
```

X.remove_animation_notify_track(animation_sequence_base, notify_track_name) -> None
Removes an Animation Notify Track from Animation Sequence by Name

Args:
    animation_sequence_base (AnimSequenceBase): 
    notify_track_name (Name):

<a id="unreal.AnimationLibrary.remove_animation_notify_events_by_track"></a>

#### remove_animation_notify_events_by_track

```python
@classmethod
def remove_animation_notify_events_by_track(
        cls, animation_sequence_base: AnimSequenceBase,
        notify_track_name: Name) -> int
```

X.remove_animation_notify_events_by_track(animation_sequence_base, notify_track_name) -> int32
Removes Animation Notify Events found by Track within the Animation Sequence, and returns the number of removed name instances

Args:
    animation_sequence_base (AnimSequenceBase): 
    notify_track_name (Name): 

Returns:
    int32:

<a id="unreal.AnimationLibrary.remove_animation_notify_events_by_name"></a>

#### remove_animation_notify_events_by_name

```python
@classmethod
def remove_animation_notify_events_by_name(
        cls, animation_sequence_base: AnimSequenceBase,
        notify_name: Name) -> int
```

X.remove_animation_notify_events_by_name(animation_sequence_base, notify_name) -> int32
Removes Animation Notify Events found by Name within the Animation Sequence, and returns the number of removed name instances

Args:
    animation_sequence_base (AnimSequenceBase): 
    notify_name (Name): 

Returns:
    int32:

<a id="unreal.AnimationLibrary.remove_all_virtual_bones"></a>

#### remove_all_virtual_bones

```python
@classmethod
def remove_all_virtual_bones(cls, animation_sequence: AnimSequence) -> None
```

X.remove_all_virtual_bones(animation_sequence) -> None
Removes all Virtual Bones from the given Animation Sequence

Args:
    animation_sequence (AnimSequence):

<a id="unreal.AnimationLibrary.remove_all_meta_data"></a>

#### remove_all_meta_data

```python
@classmethod
def remove_all_meta_data(cls, animation_asset: AnimationAsset) -> None
```

X.remove_all_meta_data(animation_asset) -> None
Removes all Meta Data from the given Animation Asset

Args:
    animation_asset (AnimationAsset):

<a id="unreal.AnimationLibrary.remove_all_curve_data"></a>

#### remove_all_curve_data

```python
@classmethod
def remove_all_curve_data(cls,
                          animation_sequence_base: AnimSequenceBase) -> None
```

X.remove_all_curve_data(animation_sequence_base) -> None
Removes all Animation Curve Data from the given Animation Sequence (Raw Animation Curves [Names] may not be removed from the Skeleton)

Args:
    animation_sequence_base (AnimSequenceBase):

<a id="unreal.AnimationLibrary.remove_all_bone_animation"></a>

#### remove_all_bone_animation

```python
@classmethod
def remove_all_bone_animation(cls, animation_sequence: AnimSequence) -> None
```

X.remove_all_bone_animation(animation_sequence) -> None
Removes all Animation Bone Track Data from the given Animation Sequence

Args:
    animation_sequence (AnimSequence):

<a id="unreal.AnimationLibrary.remove_all_animation_sync_markers"></a>

#### remove_all_animation_sync_markers

```python
@classmethod
def remove_all_animation_sync_markers(
        cls, animation_sequence: AnimSequence) -> None
```

X.remove_all_animation_sync_markers(animation_sequence) -> None
Removes All Animation Sync Markers found within the Animation Sequence, and returns the number of removed instances

Args:
    animation_sequence (AnimSequence):

<a id="unreal.AnimationLibrary.remove_all_animation_notify_tracks"></a>

#### remove_all_animation_notify_tracks

```python
@classmethod
def remove_all_animation_notify_tracks(
        cls, animation_sequence_base: AnimSequenceBase) -> None
```

X.remove_all_animation_notify_tracks(animation_sequence_base) -> None
Removes All Animation Notify Tracks from Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase):

<a id="unreal.AnimationLibrary.is_valid_time"></a>

#### is_valid_time

```python
@classmethod
def is_valid_time(cls, animation_sequence_base: AnimSequenceBase,
                  time: float) -> bool
```

X.is_valid_time(animation_sequence_base, time) -> bool
Checks whether or not the given Time Value lies within the given Animation Sequence's Length

Args:
    animation_sequence_base (AnimSequenceBase): 
    time (float): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.AnimationLibrary.is_valid_raw_animation_track_name"></a>

#### is_valid_raw_animation_track_name

```python
@classmethod
def is_valid_raw_animation_track_name(
        cls, animation_sequence_base: AnimSequenceBase,
        track_name: Name) -> bool
```

X.is_valid_raw_animation_track_name(animation_sequence_base, track_name) -> bool
Checks whether or not the given Animation Track Name is contained within the Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 
    track_name (Name): 

Returns:
    bool:

<a id="unreal.AnimationLibrary.is_valid_anim_notify_track_name"></a>

#### is_valid_anim_notify_track_name

```python
@classmethod
def is_valid_anim_notify_track_name(cls,
                                    animation_sequence_base: AnimSequenceBase,
                                    notify_track_name: Name) -> bool
```

X.is_valid_anim_notify_track_name(animation_sequence_base, notify_track_name) -> bool
Checks whether or not the given Track Name is a valid Animation Notify Track in the Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 
    notify_track_name (Name): 

Returns:
    bool:

<a id="unreal.AnimationLibrary.is_valid_animation_sync_marker_name"></a>

#### is_valid_animation_sync_marker_name

```python
@classmethod
def is_valid_animation_sync_marker_name(cls, animation_sequence: AnimSequence,
                                        marker_name: Name) -> bool
```

X.is_valid_animation_sync_marker_name(animation_sequence, marker_name) -> bool
Checks whether or not the given Marker Name is a valid Animation Sync Marker Name

Args:
    animation_sequence (AnimSequence): 
    marker_name (Name): 

Returns:
    bool:

<a id="unreal.AnimationLibrary.is_root_motion_lock_forced"></a>

#### is_root_motion_lock_forced

```python
@classmethod
def is_root_motion_lock_forced(cls, animation_sequence: AnimSequence) -> bool
```

X.is_root_motion_lock_forced(animation_sequence) -> bool
Checks whether or not Root Motion locking is Forced for the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 

Returns:
    bool:

<a id="unreal.AnimationLibrary.is_root_motion_enabled"></a>

#### is_root_motion_enabled

```python
@classmethod
def is_root_motion_enabled(cls, animation_sequence: AnimSequence) -> bool
```

X.is_root_motion_enabled(animation_sequence) -> bool
Checks whether or not Root Motion is Enabled for the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 

Returns:
    bool:

<a id="unreal.AnimationLibrary.get_vector_keys"></a>

#### get_vector_keys

```python
@classmethod
def get_vector_keys(cls, animation_sequence_base: AnimSequenceBase,
                    curve_name: Name) -> Tuple[Array[float], Array[Vector]]
```

X.get_vector_keys(animation_sequence_base, curve_name) -> (times=Array[float], values=Array[Vector])
Retrieves, a multiple of, Vector Key(s) from the specified Animation Curve inside of the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 
    curve_name (Name): 

Returns:
    tuple: 

    times (Array[float]): 

    values (Array[Vector]):

<a id="unreal.AnimationLibrary.get_variable_frame_stripping_settings"></a>

#### get_variable_frame_stripping_settings

```python
@classmethod
def get_variable_frame_stripping_settings(
        cls,
        animation_sequence: AnimSequence) -> VariableFrameStrippingSettings
```

X.get_variable_frame_stripping_settings(animation_sequence) -> VariableFrameStrippingSettings
Retrieves the Variable Frame Stripping Settings for the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 

Returns:
    VariableFrameStrippingSettings: 

    variable_frame_stripping_settings (VariableFrameStrippingSettings):

<a id="unreal.AnimationLibrary.get_unique_marker_names"></a>

#### get_unique_marker_names

```python
@classmethod
def get_unique_marker_names(cls,
                            animation_sequence: AnimSequence) -> Array[Name]
```

X.get_unique_marker_names(animation_sequence) -> Array[Name]
Retrieves all the Unique Names for the Animation Sync Markers contained by the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 

Returns:
    Array[Name]: 

    marker_names (Array[Name]):

<a id="unreal.AnimationLibrary.get_transformation_keys"></a>

#### get_transformation_keys

```python
@classmethod
def get_transformation_keys(
        cls, animation_sequence_base: AnimSequenceBase,
        curve_name: Name) -> Tuple[Array[float], Array[Transform]]
```

X.get_transformation_keys(animation_sequence_base, curve_name) -> (times=Array[float], values=Array[Transform])
Retrieves, a multiple of, Transformation Key(s) from the specified Animation Curve inside of the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 
    curve_name (Name): 

Returns:
    tuple: 

    times (Array[float]): 

    values (Array[Transform]):

<a id="unreal.AnimationLibrary.get_time_at_frame"></a>

#### get_time_at_frame

```python
@classmethod
def get_time_at_frame(cls, animation_sequence_base: AnimSequenceBase,
                      frame: int) -> float
```

X.get_time_at_frame(animation_sequence_base, frame) -> float
Retrieves the Time Value at the specified Frame Indexfor the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 
    frame (int32): 

Returns:
    float: 

    time (float):

<a id="unreal.AnimationLibrary.get_sequence_length"></a>

#### get_sequence_length

```python
@classmethod
def get_sequence_length(cls,
                        animation_sequence_base: AnimSequenceBase) -> float
```

X.get_sequence_length(animation_sequence_base) -> float
Retrieves the Length of the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 

Returns:
    float: 

    length (float):

<a id="unreal.AnimationLibrary.get_root_motion_lock_type"></a>

#### get_root_motion_lock_type

```python
@classmethod
def get_root_motion_lock_type(
        cls, animation_sequence: AnimSequence) -> RootMotionRootLock
```

X.get_root_motion_lock_type(animation_sequence) -> RootMotionRootLock
Retrieves the Root Motion Lock Type for the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 

Returns:
    RootMotionRootLock: 

    lock_type (RootMotionRootLock):

<a id="unreal.AnimationLibrary.get_raw_track_scale_data"></a>

#### get_raw_track_scale_data

```python
@classmethod
def get_raw_track_scale_data(cls, animation_sequence_base: AnimSequenceBase,
                             track_name: Name) -> Array[Vector]
```

X.get_raw_track_scale_data(animation_sequence_base, track_name) -> Array[Vector]
Get Raw Track Scale Data

Args:
    animation_sequence_base (AnimSequenceBase): 
    track_name (Name): 

Returns:
    Array[Vector]: 

    scale_data (Array[Vector]):

<a id="unreal.AnimationLibrary.get_raw_track_rotation_data"></a>

#### get_raw_track_rotation_data

```python
@classmethod
def get_raw_track_rotation_data(cls, animation_sequence_base: AnimSequenceBase,
                                track_name: Name) -> Array[Quat]
```

X.get_raw_track_rotation_data(animation_sequence_base, track_name) -> Array[Quat]
Get Raw Track Rotation Data

Args:
    animation_sequence_base (AnimSequenceBase): 
    track_name (Name): 

Returns:
    Array[Quat]: 

    rotation_data (Array[Quat]):

<a id="unreal.AnimationLibrary.get_raw_track_position_data"></a>

#### get_raw_track_position_data

```python
@classmethod
def get_raw_track_position_data(cls, animation_sequence_base: AnimSequenceBase,
                                track_name: Name) -> Array[Vector]
```

X.get_raw_track_position_data(animation_sequence_base, track_name) -> Array[Vector]
Get Raw Track Position Data

Args:
    animation_sequence_base (AnimSequenceBase): 
    track_name (Name): 

Returns:
    Array[Vector]: 

    position_data (Array[Vector]):

<a id="unreal.AnimationLibrary.get_raw_track_data"></a>

#### get_raw_track_data

```python
@classmethod
def get_raw_track_data(
        cls, animation_sequence_base: AnimSequenceBase,
        track_name: Name) -> Tuple[Array[Vector], Array[Quat], Array[Vector]]
```

X.get_raw_track_data(animation_sequence_base, track_name) -> (position_keys=Array[Vector], rotation_keys=Array[Quat], scaling_keys=Array[Vector])
Get Raw Track Data

Args:
    animation_sequence_base (AnimSequenceBase): 
    track_name (Name): 

Returns:
    tuple: 

    position_keys (Array[Vector]): 

    rotation_keys (Array[Quat]): 

    scaling_keys (Array[Vector]):

<a id="unreal.AnimationLibrary.get_rate_scale"></a>

#### get_rate_scale

```python
@classmethod
def get_rate_scale(cls, animation_sequence_base: AnimSequenceBase) -> float
```

X.get_rate_scale(animation_sequence_base) -> float
Retrieves the (Play) Rate Scale of the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 

Returns:
    float: 

    rate_scale (float):

<a id="unreal.AnimationLibrary.get_num_keys"></a>

#### get_num_keys

```python
@classmethod
def get_num_keys(cls, animation_sequence_base: AnimSequenceBase) -> int
```

X.get_num_keys(animation_sequence_base) -> int32
Retrieves the number of animation keys for the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 

Returns:
    int32: 

    num_keys (int32):

<a id="unreal.AnimationLibrary.get_num_frames"></a>

#### get_num_frames

```python
@classmethod
def get_num_frames(cls, animation_sequence_base: AnimSequenceBase) -> int
```

X.get_num_frames(animation_sequence_base) -> int32
Retrieves the number of animation frames for the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 

Returns:
    int32: 

    num_frames (int32):

<a id="unreal.AnimationLibrary.get_nodes_of_class"></a>

#### get_nodes_of_class

```python
@classmethod
def get_nodes_of_class(
        cls,
        animation_blueprint: AnimBlueprint,
        node_class: Class,
        include_child_classes: bool = True) -> Array[AnimGraphNode_Base]
```

X.get_nodes_of_class(animation_blueprint, node_class, include_child_classes=True) -> Array[AnimGraphNode_Base]
Returns all Animation Graph Nodes of the provided Node Class contained by the Animation Blueprint

Args:
    animation_blueprint (AnimBlueprint): 
    node_class (type(Class)): 
    include_child_classes (bool): 

Returns:
    Array[AnimGraphNode_Base]: 

    graph_nodes (Array[AnimGraphNode_Base]):

<a id="unreal.AnimationLibrary.get_montage_slot_names"></a>

#### get_montage_slot_names

```python
@classmethod
def get_montage_slot_names(cls, animation_montage: AnimMontage) -> Array[Name]
```

X.get_montage_slot_names(animation_montage) -> Array[Name]
Retrieves the Names of the Animation Slots used in the given Montage

Args:
    animation_montage (AnimMontage): 

Returns:
    Array[Name]: 

    slot_names (Array[Name]):

<a id="unreal.AnimationLibrary.get_meta_data_of_class"></a>

#### get_meta_data_of_class

```python
@classmethod
def get_meta_data_of_class(cls, animation_asset: AnimationAsset,
                           meta_data_class: Class) -> Array[AnimMetaData]
```

X.get_meta_data_of_class(animation_asset, meta_data_class) -> Array[AnimMetaData]
Retrieves all Meta Data Instances from the given Animation Asset

Args:
    animation_asset (AnimationAsset): 
    meta_data_class (type(Class)): 

Returns:
    Array[AnimMetaData]: 

    meta_data_of_class (Array[AnimMetaData]):

<a id="unreal.AnimationLibrary.get_meta_data"></a>

#### get_meta_data

```python
@classmethod
def get_meta_data(cls, animation_asset: AnimationAsset) -> Array[AnimMetaData]
```

X.get_meta_data(animation_asset) -> Array[AnimMetaData]
Retrieves all Meta Data Instances from the given Animation Asset

Args:
    animation_asset (AnimationAsset): 

Returns:
    Array[AnimMetaData]: 

    meta_data (Array[AnimMetaData]):

<a id="unreal.AnimationLibrary.get_frame_at_time"></a>

#### get_frame_at_time

```python
@classmethod
def get_frame_at_time(cls, animation_sequence_base: AnimSequenceBase,
                      time: float) -> int
```

X.get_frame_at_time(animation_sequence_base, time) -> int32
Retrieves the Frame Index at the specified Time Value for the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 
    time (float): 

Returns:
    int32: 

    frame (int32):

<a id="unreal.AnimationLibrary.get_float_value_at_time"></a>

#### get_float_value_at_time

```python
@classmethod
def get_float_value_at_time(cls, animation_sequence_base: AnimSequenceBase,
                            curve_name: Name, time: float) -> float
```

X.get_float_value_at_time(animation_sequence_base, curve_name, time) -> float
Retrieves an evaluated float value for a given time from the specified Animation Curve inside of the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 
    curve_name (Name): 
    time (float): 

Returns:
    float:

<a id="unreal.AnimationLibrary.get_float_keys"></a>

#### get_float_keys

```python
@classmethod
def get_float_keys(cls, animation_sequence_base: AnimSequenceBase,
                   curve_name: Name) -> Tuple[Array[float], Array[float]]
```

X.get_float_keys(animation_sequence_base, curve_name) -> (times=Array[float], values=Array[float])
Retrieves, a multiple of, Float Key(s) from the specified Animation Curve inside of the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 
    curve_name (Name): 

Returns:
    tuple: 

    times (Array[float]): 

    values (Array[float]):

<a id="unreal.AnimationLibrary.get_curve_compression_settings"></a>

#### get_curve_compression_settings

```python
@classmethod
def get_curve_compression_settings(
        cls, animation_sequence: AnimSequence) -> AnimCurveCompressionSettings
```

X.get_curve_compression_settings(animation_sequence) -> AnimCurveCompressionSettings
Retrieves the Curve Compression Settings for the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 

Returns:
    AnimCurveCompressionSettings: 

    compression_settings (AnimCurveCompressionSettings):

<a id="unreal.AnimationLibrary.get_bone_poses_for_time"></a>

#### get_bone_poses_for_time

```python
@classmethod
def get_bone_poses_for_time(
        cls,
        animation_sequence_base: AnimSequenceBase,
        bone_names: Array[Name],
        time: float,
        extract_root_motion: bool,
        preview_mesh: SkeletalMesh = None) -> Array[Transform]
```

X.get_bone_poses_for_time(animation_sequence_base, bone_names, time, extract_root_motion, preview_mesh=None) -> Array[Transform]
Get Bone Poses for Time

Args:
    animation_sequence_base (AnimSequenceBase): 
    bone_names (Array[Name]): 
    time (float): 
    extract_root_motion (bool): 
    preview_mesh (SkeletalMesh): 

Returns:
    Array[Transform]: 

    poses (Array[Transform]):

<a id="unreal.AnimationLibrary.get_bone_poses_for_frame"></a>

#### get_bone_poses_for_frame

```python
@classmethod
def get_bone_poses_for_frame(
        cls,
        animation_sequence_base: AnimSequenceBase,
        bone_names: Array[Name],
        frame: int,
        extract_root_motion: bool,
        preview_mesh: SkeletalMesh = None) -> Array[Transform]
```

X.get_bone_poses_for_frame(animation_sequence_base, bone_names, frame, extract_root_motion, preview_mesh=None) -> Array[Transform]
Get Bone Poses for Frame

Args:
    animation_sequence_base (AnimSequenceBase): 
    bone_names (Array[Name]): 
    frame (int32): 
    extract_root_motion (bool): 
    preview_mesh (SkeletalMesh): 

Returns:
    Array[Transform]: 

    poses (Array[Transform]):

<a id="unreal.AnimationLibrary.get_bone_pose_for_time"></a>

#### get_bone_pose_for_time

```python
@classmethod
def get_bone_pose_for_time(cls, animation_sequence_base: AnimSequenceBase,
                           bone_name: Name, time: float,
                           extract_root_motion: bool) -> Transform
```

X.get_bone_pose_for_time(animation_sequence_base, bone_name, time, extract_root_motion) -> Transform
Get Bone Pose for Time

Args:
    animation_sequence_base (AnimSequenceBase): 
    bone_name (Name): 
    time (float): 
    extract_root_motion (bool): 

Returns:
    Transform: 

    pose (Transform):

<a id="unreal.AnimationLibrary.get_bone_pose_for_frame"></a>

#### get_bone_pose_for_frame

```python
@classmethod
def get_bone_pose_for_frame(cls, animation_sequence_base: AnimSequenceBase,
                            bone_name: Name, frame: int,
                            extract_root_motion: bool) -> Transform
```

X.get_bone_pose_for_frame(animation_sequence_base, bone_name, frame, extract_root_motion) -> Transform
Get Bone Pose for Frame

Args:
    animation_sequence_base (AnimSequenceBase): 
    bone_name (Name): 
    frame (int32): 
    extract_root_motion (bool): 

Returns:
    Transform: 

    pose (Transform):

<a id="unreal.AnimationLibrary.get_bone_compression_settings"></a>

#### get_bone_compression_settings

```python
@classmethod
def get_bone_compression_settings(
        cls, animation_sequence: AnimSequence) -> AnimBoneCompressionSettings
```

X.get_bone_compression_settings(animation_sequence) -> AnimBoneCompressionSettings
Retrieves the Bone Compression Settings for the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 

Returns:
    AnimBoneCompressionSettings: 

    compression_settings (AnimBoneCompressionSettings):

<a id="unreal.AnimationLibrary.get_anim_notify_event_trigger_time"></a>

#### get_anim_notify_event_trigger_time

```python
@classmethod
def get_anim_notify_event_trigger_time(cls,
                                       notify_event: AnimNotifyEvent) -> float
```

X.get_anim_notify_event_trigger_time(notify_event) -> float
Returns the actual trigger time for a NotifyEvent

Args:
    notify_event (AnimNotifyEvent): 

Returns:
    float:

<a id="unreal.AnimationLibrary.get_anim_notify_event_duration"></a>

#### get_anim_notify_event_duration

```python
@classmethod
def get_anim_notify_event_duration(cls,
                                   notify_event: AnimNotifyEvent) -> float
```

X.get_anim_notify_event_duration(notify_event) -> float
Returns the duration for a NotifyEvent, only non-zero for Anim Notify States

Args:
    notify_event (AnimNotifyEvent): 

Returns:
    float:

<a id="unreal.AnimationLibrary.get_animation_track_names"></a>

#### get_animation_track_names

```python
@classmethod
def get_animation_track_names(
        cls, animation_sequence_base: AnimSequenceBase) -> Array[Name]
```

X.get_animation_track_names(animation_sequence_base) -> Array[Name]
Retrieves the Names of the individual ATracks for the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 

Returns:
    Array[Name]: 

    track_names (Array[Name]):

<a id="unreal.AnimationLibrary.get_animation_sync_markers_for_track"></a>

#### get_animation_sync_markers_for_track

```python
@classmethod
def get_animation_sync_markers_for_track(
        cls, animation_sequence: AnimSequence,
        notify_track_name: Name) -> Array[AnimSyncMarker]
```

X.get_animation_sync_markers_for_track(animation_sequence, notify_track_name) -> Array[AnimSyncMarker]
Retrieves all Animation Sync Markers for the given Notify Track Name from the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 
    notify_track_name (Name): 

Returns:
    Array[AnimSyncMarker]: 

    markers (Array[AnimSyncMarker]):

<a id="unreal.AnimationLibrary.get_animation_sync_markers"></a>

#### get_animation_sync_markers

```python
@classmethod
def get_animation_sync_markers(
        cls, animation_sequence: AnimSequence) -> Array[AnimSyncMarker]
```

X.get_animation_sync_markers(animation_sequence) -> Array[AnimSyncMarker]
Retrieves all the Animation Sync Markers for the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 

Returns:
    Array[AnimSyncMarker]: 

    markers (Array[AnimSyncMarker]):

<a id="unreal.AnimationLibrary.get_animation_notify_track_names"></a>

#### get_animation_notify_track_names

```python
@classmethod
def get_animation_notify_track_names(
        cls, animation_sequence_base: AnimSequenceBase) -> Array[Name]
```

X.get_animation_notify_track_names(animation_sequence_base) -> Array[Name]
Retrieves all Unique Animation Notify Track Names found within the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 

Returns:
    Array[Name]: 

    track_names (Array[Name]):

<a id="unreal.AnimationLibrary.get_animation_notify_events_for_track"></a>

#### get_animation_notify_events_for_track

```python
@classmethod
def get_animation_notify_events_for_track(
        cls, animation_sequence_base: AnimSequenceBase,
        notify_track_name: Name) -> Array[AnimNotifyEvent]
```

X.get_animation_notify_events_for_track(animation_sequence_base, notify_track_name) -> Array[AnimNotifyEvent]
Retrieves all Animation Notify Events for the given Notify Track Name from the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 
    notify_track_name (Name): 

Returns:
    Array[AnimNotifyEvent]: 

    events (Array[AnimNotifyEvent]):

<a id="unreal.AnimationLibrary.get_animation_notify_events"></a>

#### get_animation_notify_events

```python
@classmethod
def get_animation_notify_events(
        cls,
        animation_sequence_base: AnimSequenceBase) -> Array[AnimNotifyEvent]
```

X.get_animation_notify_events(animation_sequence_base) -> Array[AnimNotifyEvent]
Retrieves all Animation Notify Events found within the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 

Returns:
    Array[AnimNotifyEvent]: 

    notify_events (Array[AnimNotifyEvent]):

<a id="unreal.AnimationLibrary.get_animation_notify_event_names"></a>

#### get_animation_notify_event_names

```python
@classmethod
def get_animation_notify_event_names(
        cls, animation_sequence_base: AnimSequenceBase) -> Array[Name]
```

X.get_animation_notify_event_names(animation_sequence_base) -> Array[Name]
Retrieves all Unique Animation Notify Events found within the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 

Returns:
    Array[Name]: 

    event_names (Array[Name]):

<a id="unreal.AnimationLibrary.get_animation_interpolation_type"></a>

#### get_animation_interpolation_type

```python
@classmethod
def get_animation_interpolation_type(
        cls, animation_sequence: AnimSequence) -> AnimInterpolationType
```

X.get_animation_interpolation_type(animation_sequence) -> AnimInterpolationType
Retrieves the Animation Interpolation type for the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 

Returns:
    AnimInterpolationType: 

    interpolation_type (AnimInterpolationType):

<a id="unreal.AnimationLibrary.get_animation_graphs"></a>

#### get_animation_graphs

```python
@classmethod
def get_animation_graphs(
        cls, animation_blueprint: AnimBlueprint) -> Array[AnimationGraph]
```

X.get_animation_graphs(animation_blueprint) -> Array[AnimationGraph]
Returns all Animation Graphs contained by the provided Animation Blueprint

Args:
    animation_blueprint (AnimBlueprint): 

Returns:
    Array[AnimationGraph]: 

    animation_graphs (Array[AnimationGraph]):

<a id="unreal.AnimationLibrary.get_animation_curve_names"></a>

#### get_animation_curve_names

```python
@classmethod
def get_animation_curve_names(cls, animation_sequence_base: AnimSequenceBase,
                              curve_type: RawCurveTrackTypes) -> Array[Name]
```

X.get_animation_curve_names(animation_sequence_base, curve_type) -> Array[Name]
Retrieves the Names of the individual float curves for the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 
    curve_type (RawCurveTrackTypes): 

Returns:
    Array[Name]: 

    curve_names (Array[Name]):

<a id="unreal.AnimationLibrary.get_additive_base_pose_type"></a>

#### get_additive_base_pose_type

```python
@classmethod
def get_additive_base_pose_type(
        cls, animation_sequence: AnimSequence) -> AdditiveBasePoseType
```

X.get_additive_base_pose_type(animation_sequence) -> AdditiveBasePoseType
Retrieves the Additive Base Pose type for the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 

Returns:
    AdditiveBasePoseType: 

    additive_base_pose_type (AdditiveBasePoseType):

<a id="unreal.AnimationLibrary.get_additive_animation_type"></a>

#### get_additive_animation_type

```python
@classmethod
def get_additive_animation_type(
        cls, animation_sequence: AnimSequence) -> AdditiveAnimationType
```

X.get_additive_animation_type(animation_sequence) -> AdditiveAnimationType
Retrieves the Additive Animation type for the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 

Returns:
    AdditiveAnimationType: 

    additive_animation_type (AdditiveAnimationType):

<a id="unreal.AnimationLibrary.find_bone_path_to_root"></a>

#### find_bone_path_to_root

```python
@classmethod
def find_bone_path_to_root(cls, animation_sequence_base: AnimSequenceBase,
                           bone_name: Name) -> Array[Name]
```

X.find_bone_path_to_root(animation_sequence_base, bone_name) -> Array[Name]
Finds the Bone Path from the given Bone to the Root Bone

Args:
    animation_sequence_base (AnimSequenceBase): 
    bone_name (Name): 

Returns:
    Array[Name]: 

    bone_path (Array[Name]):

<a id="unreal.AnimationLibrary.finalize_bone_animation"></a>

#### finalize_bone_animation

```python
@classmethod
def finalize_bone_animation(cls, animation_sequence: AnimSequence) -> None
```

X.finalize_bone_animation(animation_sequence) -> None
Finalize Bone Animation
deprecated: FinalizeBoneAnimation has been deprecated, use UAnimDataController instead

Args:
    animation_sequence (AnimSequence):

<a id="unreal.AnimationLibrary.extract_root_track_transform"></a>

#### extract_root_track_transform

```python
@classmethod
def extract_root_track_transform(cls,
                                 animation_sequence_base: AnimSequenceBase,
                                 time: float) -> Transform
```

X.extract_root_track_transform(animation_sequence_base, time) -> Transform
Gets the root transform from the raw animation at Time

Args:
    animation_sequence_base (AnimSequenceBase): 
    time (float): 

Returns:
    Transform:

<a id="unreal.AnimationLibrary.evaluate_root_bone_timecode_subframe_attribute_at_time"></a>

#### evaluate_root_bone_timecode_subframe_attribute_at_time

```python
@classmethod
def evaluate_root_bone_timecode_subframe_attribute_at_time(
        cls, animation_sequence_base: AnimSequenceBase,
        eval_time: float) -> Optional[float]
```

X.evaluate_root_bone_timecode_subframe_attribute_at_time(animation_sequence_base, eval_time) -> float or None
Evaluates the subframe timecode attribute (e.g. "TCSubframe") of the root bone and returns the resulting value.

Since the subframe component of FFrameTime is clamped to the range [0.0, 1.0), it cannot accurately represent the use
case where the timecode metadata represents subframe values as whole numbered subframes instead of as a percentage of a
frame the way the engine does. The subframe component of the FQualifiedFrameTime returned by
EvaluateRootBoneTimecodeAttributesAtTime() may not reflect the authored subframe metadata in that case.

This function allows access to the subframe values that were actually authored in the timecode metadata.
return:: true if the root bone had a subframe timecode attribute that could be evaluated and a value was set, or false otherwise.

Args:
    animation_sequence_base (AnimSequenceBase): 
    eval_time (float): 

Returns:
    float or None: 

    out_subframe (float):

<a id="unreal.AnimationLibrary.evaluate_root_bone_timecode_attributes_at_time"></a>

#### evaluate_root_bone_timecode_attributes_at_time

```python
@classmethod
def evaluate_root_bone_timecode_attributes_at_time(
        cls, animation_sequence_base: AnimSequenceBase,
        eval_time: float) -> Optional[QualifiedTime]
```

X.evaluate_root_bone_timecode_attributes_at_time(animation_sequence_base, eval_time) -> QualifiedTime or None
Evaluates timecode attributes (e.g. "TCFrame", "TCSecond", etc.) of the root bone and returns the resulting qualified frame time.
return:: true if the root bone had timecode attributes that could be evaluated and a qualified frame time was set, or false otherwise.

Args:
    animation_sequence_base (AnimSequenceBase): 
    eval_time (float): 

Returns:
    QualifiedTime or None: 

    out_qualified_frame_time (QualifiedTime):

<a id="unreal.AnimationLibrary.evaluate_bone_timecode_and_slate_attributes_at_time"></a>

#### evaluate_bone_timecode_and_slate_attributes_at_time

```python
@classmethod
def evaluate_bone_timecode_and_slate_attributes_at_time(
        cls, bone_name: Name, animation_sequence_base: AnimSequenceBase,
        eval_time: float) -> Optional[Tuple[QualifiedTime, str]]
```

X.evaluate_bone_timecode_and_slate_attributes_at_time(bone_name, animation_sequence_base, eval_time) -> (out_qualified_frame_time=QualifiedTime, slate=str) or None
Evaluates timecode attributes (e.g. "TCFrame", "TCSecond", etc.) and TCSlate of the root bone and returns the resulting qualified frame time.
return:: true if the root bone had timecode attributes that could be evaluated and a qualified frame time was set, or false otherwise.

Args:
    bone_name (Name): 
    animation_sequence_base (AnimSequenceBase): 
    eval_time (float): 

Returns:
    tuple or None: 

    out_qualified_frame_time (QualifiedTime): 

    slate (str):

<a id="unreal.AnimationLibrary.does_curve_exist"></a>

#### does_curve_exist

```python
@classmethod
def does_curve_exist(cls, animation_sequence_base: AnimSequenceBase,
                     curve_name: Name, curve_type: RawCurveTrackTypes) -> bool
```

X.does_curve_exist(animation_sequence_base, curve_name, curve_type) -> bool
Checks whether or not the given Curve Name exist on the Skeleton referenced by the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 
    curve_name (Name): 
    curve_type (RawCurveTrackTypes): 

Returns:
    bool:

<a id="unreal.AnimationLibrary.does_bone_name_exist"></a>

#### does_bone_name_exist

```python
@classmethod
def does_bone_name_exist(cls, animation_sequence: AnimSequence,
                         bone_name: Name) -> bool
```

X.does_bone_name_exist(animation_sequence, bone_name) -> bool
Checks whether or not the given Bone Name exist on the Skeleton referenced by the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 
    bone_name (Name): 

Returns:
    bool: 

    exists (bool):

<a id="unreal.AnimationLibrary.copy_anim_notifies_from_sequence"></a>

#### copy_anim_notifies_from_sequence

```python
@classmethod
def copy_anim_notifies_from_sequence(
        cls,
        source_animation_sequence_base: AnimSequenceBase,
        destination_animation_sequence_base: AnimSequenceBase,
        delete_existing_notifies: bool = False) -> None
```

X.copy_anim_notifies_from_sequence(source_animation_sequence_base, destination_animation_sequence_base, delete_existing_notifies=False) -> None
Copies animation notifies from Src Animation Sequence to Dest. Creates anim notify tracks as necessary. Returns true on success.

Args:
    source_animation_sequence_base (AnimSequenceBase): 
    destination_animation_sequence_base (AnimSequenceBase): 
    delete_existing_notifies (bool):

<a id="unreal.AnimationLibrary.copy_animation_curve_names_to_skeleton"></a>

#### copy_animation_curve_names_to_skeleton

```python
@classmethod
def copy_animation_curve_names_to_skeleton(
        cls, old_skeleton: Skeleton, new_skeleton: Skeleton,
        sequence_base: AnimSequenceBase,
        curve_type: RawCurveTrackTypes) -> None
```

X.copy_animation_curve_names_to_skeleton(old_skeleton, new_skeleton, sequence_base, curve_type) -> None
Ensures that any curve names that do not exist on the NewSkeleton are added to it, in which case the SmartName on the actual curve itself will also be updated
deprecated: It is no longer necessary to copy curve names to the skeleton. If metadata is required to be updated, please use the metadata setting APIs.

Args:
    old_skeleton (Skeleton): 
    new_skeleton (Skeleton): 
    sequence_base (AnimSequenceBase): 
    curve_type (RawCurveTrackTypes):

<a id="unreal.AnimationLibrary.contains_meta_data_of_class"></a>

#### contains_meta_data_of_class

```python
@classmethod
def contains_meta_data_of_class(cls, animation_asset: AnimationAsset,
                                meta_data_class: Class) -> bool
```

X.contains_meta_data_of_class(animation_asset, meta_data_class) -> bool
Checks whether or not the given Animation Asset contains Meta Data Instance of the specified Meta Data Class

Args:
    animation_asset (AnimationAsset): 
    meta_data_class (type(Class)): 

Returns:
    bool:

<a id="unreal.AnimationLibrary.add_virtual_bone"></a>

#### add_virtual_bone

```python
@classmethod
def add_virtual_bone(cls, animation_sequence: AnimSequence,
                     source_bone_name: Name, target_bone_name: Name) -> Name
```

X.add_virtual_bone(animation_sequence, source_bone_name, target_bone_name) -> Name
Adds a Virtual Bone between the Source and Target Bones to the given Animation Sequence

Args:
    animation_sequence (AnimSequence): 
    source_bone_name (Name): 
    target_bone_name (Name): 

Returns:
    Name: 

    virtual_bone_name (Name):

<a id="unreal.AnimationLibrary.add_vector_curve_keys"></a>

#### add_vector_curve_keys

```python
@classmethod
def add_vector_curve_keys(cls, animation_sequence_base: AnimSequenceBase,
                          curve_name: Name, times: Array[float],
                          vectors: Array[Vector]) -> None
```

X.add_vector_curve_keys(animation_sequence_base, curve_name, times, vectors) -> None
Adds a multiple of Vector Keys to the specified Animation Curve inside of the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 
    curve_name (Name): 
    times (Array[float]): 
    vectors (Array[Vector]):

<a id="unreal.AnimationLibrary.add_vector_curve_key"></a>

#### add_vector_curve_key

```python
@classmethod
def add_vector_curve_key(cls, animation_sequence_base: AnimSequenceBase,
                         curve_name: Name, time: float,
                         vector: Vector) -> None
```

X.add_vector_curve_key(animation_sequence_base, curve_name, time, vector) -> None
Adds a Vector Key to the specified Animation Curve inside of the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 
    curve_name (Name): 
    time (float): 
    vector (Vector):

<a id="unreal.AnimationLibrary.add_transformation_curve_keys"></a>

#### add_transformation_curve_keys

```python
@classmethod
def add_transformation_curve_keys(cls,
                                  animation_sequence_base: AnimSequenceBase,
                                  curve_name: Name, times: Array[float],
                                  transforms: Array[Transform]) -> None
```

X.add_transformation_curve_keys(animation_sequence_base, curve_name, times, transforms) -> None
Adds a multiple of Transformation Keys to the specified Animation Curve inside of the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 
    curve_name (Name): 
    times (Array[float]): 
    transforms (Array[Transform]):

<a id="unreal.AnimationLibrary.add_transformation_curve_key"></a>

#### add_transformation_curve_key

```python
@classmethod
def add_transformation_curve_key(cls,
                                 animation_sequence_base: AnimSequenceBase,
                                 curve_name: Name, time: float,
                                 transform: Transform) -> None
```

X.add_transformation_curve_key(animation_sequence_base, curve_name, time, transform) -> None
Adds a Transformation Key to the specified Animation Curve inside of the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 
    curve_name (Name): 
    time (float): 
    transform (Transform):

<a id="unreal.AnimationLibrary.add_node_asset_override"></a>

#### add_node_asset_override

```python
@classmethod
def add_node_asset_override(cls,
                            anim_blueprint: AnimBlueprint,
                            target: AnimationAsset,
                            override: AnimationAsset,
                            print_applied_overrides: bool = False) -> None
```

X.add_node_asset_override(anim_blueprint, target, override, print_applied_overrides=False) -> None
Adds an Animation Asset override for the provided AnimationBlueprint, replacing any instance of Target with Override

Args:
    anim_blueprint (AnimBlueprint): The Animation Blueprint to add/set the Override for
    target (AnimationAsset): The Animation Asset to add an override for (overrides all instances of the asset)
    override (AnimationAsset): The Animation Asset to used to override the Target with (types have to match)
    print_applied_overrides (bool): Flag whether or not to print the applied overrides

<a id="unreal.AnimationLibrary.add_meta_data_object"></a>

#### add_meta_data_object

```python
@classmethod
def add_meta_data_object(cls, animation_asset: AnimationAsset,
                         meta_data_object: AnimMetaData) -> None
```

X.add_meta_data_object(animation_asset, meta_data_object) -> None
Adds an instance of the specified MetaData Class to the given Animation Asset (requires MetaDataObject's outer to be the Animation Asset)

Args:
    animation_asset (AnimationAsset): 
    meta_data_object (AnimMetaData):

<a id="unreal.AnimationLibrary.add_meta_data"></a>

#### add_meta_data

```python
@classmethod
def add_meta_data(cls, animation_asset: AnimationAsset,
                  meta_data_class: Class) -> AnimMetaData
```

X.add_meta_data(animation_asset, meta_data_class) -> AnimMetaData
Creates and Adds an instance of the specified MetaData Class to the given Animation Asset

Args:
    animation_asset (AnimationAsset): 
    meta_data_class (type(Class)): 

Returns:
    AnimMetaData: 

    meta_data_instance (AnimMetaData):

<a id="unreal.AnimationLibrary.add_float_curve_keys"></a>

#### add_float_curve_keys

```python
@classmethod
def add_float_curve_keys(cls, animation_sequence_base: AnimSequenceBase,
                         curve_name: Name, times: Array[float],
                         values: Array[float]) -> None
```

X.add_float_curve_keys(animation_sequence_base, curve_name, times, values) -> None
Adds a multiple of Float Keys to the specified Animation Curve inside of the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 
    curve_name (Name): 
    times (Array[float]): 
    values (Array[float]):

<a id="unreal.AnimationLibrary.add_float_curve_key"></a>

#### add_float_curve_key

```python
@classmethod
def add_float_curve_key(cls, animation_sequence_base: AnimSequenceBase,
                        curve_name: Name, time: float, value: float) -> None
```

X.add_float_curve_key(animation_sequence_base, curve_name, time, value) -> None
Adds a Float Key to the specified Animation Curve inside of the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 
    curve_name (Name): 
    time (float): 
    value (float):

<a id="unreal.AnimationLibrary.add_curve"></a>

#### add_curve

```python
@classmethod
def add_curve(cls,
              animation_sequence_base: AnimSequenceBase,
              curve_name: Name,
              curve_type: RawCurveTrackTypes = RawCurveTrackTypes.RCT_FLOAT,
              meta_data_curve: bool = False) -> None
```

X.add_curve(animation_sequence_base, curve_name, curve_type=RawCurveTrackTypes.RCT_FLOAT, meta_data_curve=False) -> None
Adds an Animation Curve by Type and Name to the given Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 
    curve_name (Name): 
    curve_type (RawCurveTrackTypes): 
    meta_data_curve (bool):

<a id="unreal.AnimationLibrary.add_animation_sync_marker"></a>

#### add_animation_sync_marker

```python
@classmethod
def add_animation_sync_marker(cls, animation_sequence: AnimSequence,
                              marker_name: Name, time: float,
                              notify_track_name: Name) -> None
```

X.add_animation_sync_marker(animation_sequence, marker_name, time, notify_track_name) -> None
Adds an Animation Sync Marker to Notify track in the given Animation with the corresponding Marker Name and Time

Args:
    animation_sequence (AnimSequence): 
    marker_name (Name): 
    time (float): 
    notify_track_name (Name):

<a id="unreal.AnimationLibrary.add_animation_notify_track"></a>

#### add_animation_notify_track

```python
@classmethod
def add_animation_notify_track(
    cls,
    animation_sequence_base: AnimSequenceBase,
    notify_track_name: Name,
    track_color: LinearColor = [1.000000, 1.000000, 1.000000,
                                1.000000]) -> None
```

X.add_animation_notify_track(animation_sequence_base, notify_track_name, track_color=[1.000000, 1.000000, 1.000000, 1.000000]) -> None
Adds an Animation Notify Track to the Animation Sequence

Args:
    animation_sequence_base (AnimSequenceBase): 
    notify_track_name (Name): 
    track_color (LinearColor):

<a id="unreal.AnimationLibrary.add_animation_notify_state_event_object"></a>

#### add_animation_notify_state_event_object

```python
@classmethod
def add_animation_notify_state_event_object(
        cls, animation_sequence_base: AnimSequenceBase, start_time: float,
        duration: float, notify_state: AnimNotifyState,
        notify_track_name: Name) -> None
```

X.add_animation_notify_state_event_object(animation_sequence_base, start_time, duration, notify_state, notify_track_name) -> None
Adds an the specific Animation Notify State to the Animation Sequence (requires Notify State's outer to be the Animation Sequence)

Args:
    animation_sequence_base (AnimSequenceBase): 
    start_time (float): 
    duration (float): 
    notify_state (AnimNotifyState): 
    notify_track_name (Name):

<a id="unreal.AnimationLibrary.add_animation_notify_state_event"></a>

#### add_animation_notify_state_event

```python
@classmethod
def add_animation_notify_state_event(
        cls, animation_sequence_base: AnimSequenceBase,
        notify_track_name: Name, start_time: float, duration: float,
        notify_state_class: Class) -> AnimNotifyState
```

X.add_animation_notify_state_event(animation_sequence_base, notify_track_name, start_time, duration, notify_state_class) -> AnimNotifyState
Adds an Animation Notify State Event to Notify track in the given Animation with the given Notify State creation data

Args:
    animation_sequence_base (AnimSequenceBase): 
    notify_track_name (Name): 
    start_time (float): 
    duration (float): 
    notify_state_class (type(Class)): 

Returns:
    AnimNotifyState:

<a id="unreal.AnimationLibrary.add_animation_notify_event_object"></a>

#### add_animation_notify_event_object

```python
@classmethod
def add_animation_notify_event_object(
        cls, animation_sequence_base: AnimSequenceBase, start_time: float,
        notify: AnimNotify, notify_track_name: Name) -> None
```

X.add_animation_notify_event_object(animation_sequence_base, start_time, notify, notify_track_name) -> None
Adds an the specific Animation Notify to the Animation Sequence (requires Notify's outer to be the Animation Sequence)

Args:
    animation_sequence_base (AnimSequenceBase): 
    start_time (float): 
    notify (AnimNotify): 
    notify_track_name (Name):

<a id="unreal.AnimationLibrary.add_animation_notify_event"></a>

#### add_animation_notify_event

```python
@classmethod
def add_animation_notify_event(cls, animation_sequence_base: AnimSequenceBase,
                               notify_track_name: Name, start_time: float,
                               notify_class: Class) -> AnimNotify
```

X.add_animation_notify_event(animation_sequence_base, notify_track_name, start_time, notify_class) -> AnimNotify
Adds an Animation Notify Event to Notify track in the given Animation with the given Notify creation data

Args:
    animation_sequence_base (AnimSequenceBase): 
    notify_track_name (Name): 
    start_time (float): 
    notify_class (type(Class)): 

Returns:
    AnimNotify:

<a id="unreal.Skeleton"></a>