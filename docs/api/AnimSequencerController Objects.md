## AnimSequencerController Objects

```python
class AnimSequencerController(Object)
```

Anim Sequencer Controller

**C++ Source:**

- **Plugin**: AnimationData
- **Module**: AnimationData
- **File**: AnimSequencerController.h

<a id="unreal.AnimSequencerController.update_curve_names_from_skeleton"></a>

#### update_curve_names_from_skeleton

```python
def update_curve_names_from_skeleton(skeleton: Skeleton,
                                     supported_curve_type: RawCurveTrackTypes,
                                     should_transact: bool = True) -> None
```

x.update_curve_names_from_skeleton(skeleton, supported_curve_type, should_transact=True) -> None
Update Curve Names from Skeleton
deprecated: This function is no longer used.

Args:
    skeleton (Skeleton): 
    supported_curve_type (RawCurveTrackTypes): 
    should_transact (bool):

<a id="unreal.AnimSequencerController.set_transform_curve_keys"></a>

#### set_transform_curve_keys

```python
def set_transform_curve_keys(curve_id: AnimationCurveIdentifier,
                             transform_values: Array[Transform],
                             time_keys: Array[float],
                             should_transact: bool = True) -> bool
```

x.set_transform_curve_keys(curve_id, transform_values, time_keys, should_transact=True) -> bool
Replace the keys for the transform curve with provided identifier. Broadcasts a EAnimDataModelNotifyType::CurveChanged notify if successful.

Args:
    curve_id (AnimationCurveIdentifier): Identifier for the transform curve for which the keys are to be set
    transform_values (Array[Transform]): Transform Values with which the existing values are to be replaced
    time_keys (Array[float]): Time Keys with which the existing keys are to be replaced
    should_transact (bool): Whether or not any undo-redo changes should be generated

Returns:
    bool: Whether or not the transform curve keys were successfully set

<a id="unreal.AnimSequencerController.set_transform_curve_key"></a>

#### set_transform_curve_key

```python
def set_transform_curve_key(curve_id: AnimationCurveIdentifier,
                            time: float,
                            value: Transform,
                            should_transact: bool = True) -> bool
```

x.set_transform_curve_key(curve_id, time, value, should_transact=True) -> bool
Sets a single key for the transform curve with provided identifier. Broadcasts a EAnimDataModelNotifyType::CurveChanged notify if successful.
In case a key for any of the individual transform channel curves already exists the value is replaced.

Args:
    curve_id (AnimationCurveIdentifier): Identifier for the transform curve for which the key is to be set
    time (float): Time of the key to be set
    value (Transform): Value of the key to be set
    should_transact (bool): Whether or not any undo-redo changes should be generated

Returns:
    bool: Whether or not the transform curve key was successfully set

<a id="unreal.AnimSequencerController.set_play_length"></a>

#### set_play_length

```python
def set_play_length(length: float, should_transact: bool = True) -> None
```

x.set_play_length(length, should_transact=True) -> None
Set Play Length
deprecated: SetPlayLength is deprecated use SetNumberOfFrames instead.

Args:
    length (float): 
    should_transact (bool):

<a id="unreal.AnimSequencerController.set_number_of_frames"></a>

#### set_number_of_frames

```python
def set_number_of_frames(new_length_in_frames: FrameNumber,
                         should_transact: bool = True) -> None
```

x.set_number_of_frames(new_length_in_frames, should_transact=True) -> None
Sets the total play-able length in seconds. Broadcasts a EAnimDataModelNotifyType::SequenceLengthChanged notify if successful.
The number of frames and keys for the provided length is recalculated according to the current value of UAnimDataModel::FrameRate.

Args:
    new_length_in_frames (FrameNumber): Total new play-able number of frames value (according to frame rate), has to be positive and non-zero
    should_transact (bool): Whether or not any undo-redo changes should be generated

<a id="unreal.AnimSequencerController.set_model"></a>

#### set_model

```python
def set_model(model: AnimationDataModel) -> None
```

x.set_model(model) -> None
Sets the AnimDataModel instance this controller is supposed to be targeting

Args:
    model (AnimationDataModel): IAnimationDataModel instance to target

<a id="unreal.AnimSequencerController.set_frame_rate"></a>

#### set_frame_rate

```python
def set_frame_rate(frame_rate: FrameRate,
                   should_transact: bool = True) -> None
```

x.set_frame_rate(frame_rate, should_transact=True) -> None
Sets the frame rate according to which the bone animation is expected to be sampled. Broadcasts a EAnimDataModelNotifyType::FrameRateChanged notify if successful.
The number of frames and keys for the provided frame rate is recalculated according to the current value of UAnimDataModel::PlayLength.

Args:
    frame_rate (FrameRate): The new sampling frame rate, has to be positive and non-zero
    should_transact (bool): Whether or not any undo-redo changes should be generated

<a id="unreal.AnimSequencerController.set_curve_keys"></a>

#### set_curve_keys

```python
def set_curve_keys(curve_id: AnimationCurveIdentifier,
                   curve_keys: Array[RichCurveKey],
                   should_transact: bool = True) -> bool
```

x.set_curve_keys(curve_id, curve_keys, should_transact=True) -> bool
Replace the keys for the curve with provided identifier and name. Broadcasts a EAnimDataModelNotifyType::CurveChanged notify if successful.

Args:
    curve_id (AnimationCurveIdentifier): Identifier for the curve for which the keys are to be replaced
    curve_keys (Array[RichCurveKey]): Keys with which the existing keys are to be replaced
    should_transact (bool): Whether or not any undo-redo changes should be generated

Returns:
    bool: Whether or not replacing curve keys was successful

<a id="unreal.AnimSequencerController.set_curve_key"></a>

#### set_curve_key

```python
def set_curve_key(curve_id: AnimationCurveIdentifier,
                  key: RichCurveKey,
                  should_transact: bool = True) -> bool
```

x.set_curve_key(curve_id, key, should_transact=True) -> bool
Sets a single key for the curve with provided identifier and name. Broadcasts a EAnimDataModelNotifyType::CurveChanged notify if successful.
In case a key for the provided key time already exists the key is replaced.

Args:
    curve_id (AnimationCurveIdentifier): Identifier for the curve for which the key is to be set
    key (RichCurveKey): Key to be set
    should_transact (bool): Whether or not any undo-redo changes should be generated

Returns:
    bool: Whether or not the curve key was successfully set

<a id="unreal.AnimSequencerController.set_curve_flags"></a>

#### set_curve_flags

```python
def set_curve_flags(curve_id: AnimationCurveIdentifier,
                    flags: int,
                    should_transact: bool = True) -> bool
```

x.set_curve_flags(curve_id, flags, should_transact=True) -> bool
Replace the flags for the curve with provided identifier. Broadcasts a EAnimDataModelNotifyType::CurveFlagsChanged notify if successful.

Args:
    curve_id (AnimationCurveIdentifier): Identifier for the curve for which the flag state is to be set
    flags (int32): Flag mask with which the existing flags are to be replaced
    should_transact (bool): Whether or not any undo-redo changes should be generated

Returns:
    bool: Whether or not the flag mask was successfully set

<a id="unreal.AnimSequencerController.set_curve_flag"></a>

#### set_curve_flag

```python
def set_curve_flag(curve_id: AnimationCurveIdentifier,
                   flag: AnimAssetCurveFlags,
                   state: bool = True,
                   should_transact: bool = True) -> bool
```

x.set_curve_flag(curve_id, flag, state=True, should_transact=True) -> bool
Set an individual flag for the curve with provided identifier. Broadcasts a EAnimDataModelNotifyType::CurveFlagsChanged notify if successful.

Args:
    curve_id (AnimationCurveIdentifier): Identifier for the curve for which the flag state is to be set
    flag (AnimAssetCurveFlags): Flag for which the state is supposed to be set
    state (bool): State of the flag to be, true=set/false=not set
    should_transact (bool): Whether or not any undo-redo changes should be generated

Returns:
    bool: Whether or not the flag state was successfully set

<a id="unreal.AnimSequencerController.set_curve_comment"></a>

#### set_curve_comment

```python
def set_curve_comment(
        curve_id: AnimationCurveIdentifier,
        comment:
    str = "/**\n\t* Changes the comment of the curve with provided identifier. Broadcasts a EAnimDataModelNotifyType::CurveCommentChanged notify if successful.\n\t* Currently changing curve comments is only supported for float curves.\n\t*\n\t* @param\tCurveId\t\t\t\tIdentifier of the curve to change the comment for\n\t* @param\tComment\t\t\t\tComment to which the curve is to be set\n\t* @param\tbShouldTransact\t\tWhether or not any undo-redo changes should be generated\n\t*\n\t* @return\tWhether or not the curve comment was successfully changed\n\t*/",
        should_transact: bool = True) -> bool
```

x.set_curve_comment(curve_id, comment="/**\n\t* Changes the comment of the curve with provided identifier. Broadcasts a EAnimDataModelNotifyType::CurveCommentChanged notify if successful.\n\t* Currently changing curve comments is only supported for float curves.\n\t*\n\t* @param\tCurveId\t\t\t\tIdentifier of the curve to change the comment for\n\t* @param\tComment\t\t\t\tComment to which the curve is to be set\n\t* @param\tbShouldTransact\t\tWhether or not any undo-redo changes should be generated\n\t*\n\t* @return\tWhether or not the curve comment was successfully changed\n\t*/", should_transact=True) -> bool
Changes the comment of the curve with provided identifier. Broadcasts a EAnimDataModelNotifyType::CurveCommentChanged notify if successful.
Currently changing curve comments is only supported for float curves.

Args:
    curve_id (AnimationCurveIdentifier): Identifier of the curve to change the comment for
    comment (str): Comment to which the curve is to be set
    should_transact (bool): Whether or not any undo-redo changes should be generated

Returns:
    bool: Whether or not the curve comment was successfully changed

<a id="unreal.AnimSequencerController.set_curve_color"></a>

#### set_curve_color

```python
def set_curve_color(curve_id: AnimationCurveIdentifier,
                    color: LinearColor,
                    should_transact: bool = True) -> bool
```

x.set_curve_color(curve_id, color, should_transact=True) -> bool
Changes the color of the curve with provided identifier. Broadcasts a EAnimDataModelNotifyType::CurveColorChanged notify if successful.
Currently changing curve colors is only supported for float curves.

Args:
    curve_id (AnimationCurveIdentifier): Identifier of the curve to change the color for
    color (LinearColor): Color to which the curve is to be set
    should_transact (bool): Whether or not any undo-redo changes should be generated

Returns:
    bool: Whether or not the curve color was successfully changed

<a id="unreal.AnimSequencerController.set_bone_track_keys"></a>

#### set_bone_track_keys

```python
def set_bone_track_keys(bone_name: Name,
                        positional_keys: Array[Vector],
                        rotational_keys: Array[Quat],
                        scaling_keys: Array[Vector],
                        should_transact: bool = True) -> bool
```

x.set_bone_track_keys(bone_name, positional_keys, rotational_keys, scaling_keys, should_transact=True) -> bool
Removes an existing bone animation track with the provided name. Broadcasts a EAnimDataModelNotifyType::TrackChanged notify if successful.
The provided number of keys provided is expected to match for each component, and be non-zero.

Args:
    bone_name (Name): Bone name of the track for which the keys should be set
    positional_keys (Array[Vector]): Array of keys for the translation component
    rotational_keys (Array[Quat]): Array of keys for the rotation component
    scaling_keys (Array[Vector]): Array of keys for the scale component
    should_transact (bool): Whether or not any undo-redo changes should be generated

Returns:
    bool: Whether or not the keys were successfully set

<a id="unreal.AnimSequencerController.scale_curve"></a>

#### scale_curve

```python
def scale_curve(curve_id: AnimationCurveIdentifier,
                origin: float,
                factor: float,
                should_transact: bool = True) -> bool
```

x.scale_curve(curve_id, origin, factor, should_transact=True) -> bool
Scales the curve with provided identifier. Broadcasts a EAnimDataModelNotifyType::CurveScaled notify if successful.

Args:
    curve_id (AnimationCurveIdentifier): Identifier of the curve to scale
    origin (float): Time to use as the origin when scaling the curve
    factor (float): Factor with which the curve is supposed to be scaled
    should_transact (bool): Whether or not any undo-redo changes should be generated

Returns:
    bool: Whether or not scaling the curve was successful

<a id="unreal.AnimSequencerController.resize_play_length"></a>

#### resize_play_length

```python
def resize_play_length(new_length: float,
                       t0: float,
                       t1: float,
                       should_transact: bool = True) -> None
```

x.resize_play_length(new_length, t0, t1, should_transact=True) -> None
Resize Play Length
deprecated: ResizePlayLength is deprecated use ResizeNumberOfFrames instead.

Args:
    new_length (float): 
    t0 (float): 
    t1 (float): 
    should_transact (bool):

<a id="unreal.AnimSequencerController.resize_number_of_frames"></a>

#### resize_number_of_frames

```python
def resize_number_of_frames(new_length_in_frames: FrameNumber,
                            t0: FrameNumber,
                            t1: FrameNumber,
                            should_transact: bool = True) -> None
```

x.resize_number_of_frames(new_length_in_frames, t0, t1, should_transact=True) -> None
Sets the total play-able length in seconds. Broadcasts a EAnimDataModelNotifyType::SequenceLengthChanged notify if successful.
T0 and T1 are expected to represent the window of time that was either added or removed. E.g. for insertion T0 indicates the time
at which additional time starts and T1 were it ends. For removal T0 indicates the time at which time should be started to remove, and T1 indicates the end. Giving a total of T1 - T0 added or removed length.
The number of frames and keys for the provided length is recalculated according to the current value of UAnimDataModel::FrameRate.

Args:
    new_length_in_frames (FrameNumber): Total new play-able number of frames value (according to frame rate), has to be positive and non-zero
    t0 (FrameNumber): Point between 0 and NewLengthInFrames at which the change in length starts
    t1 (FrameNumber): Point between 0 and NewLengthInFrames at which the change in length ends
    should_transact (bool): Whether or not any undo-redo changes should be generated

<a id="unreal.AnimSequencerController.resize_in_frames"></a>

#### resize_in_frames

```python
def resize_in_frames(new_length_in_frames: FrameNumber,
                     t0: FrameNumber,
                     t1: FrameNumber,
                     should_transact: bool = True) -> None
```

x.resize_in_frames(new_length_in_frames, t0, t1, should_transact=True) -> None
Sets the total play-able length in seconds and resizes curves. Broadcasts EAnimDataModelNotifyType::SequenceLengthChanged
and EAnimDataModelNotifyType::CurveChanged notifies if successful.
T0 and T1 are expected to represent the window of time that was either added or removed. E.g. for insertion T0 indicates the time
at which additional time starts and T1 were it ends. For removal T0 indicates the time at which time should be started to remove, and T1 indicates the end. Giving a total of T1 - T0 added or removed length.
The number of frames and keys for the provided length is recalculated according to the current value of UAnimDataModel::FrameRate.

Args:
    new_length_in_frames (FrameNumber): Total new play-able number of frames value (according to frame rate), has to be positive and non-zero
    t0 (FrameNumber): Point between 0 and NewLengthInFrames at which the change in length starts
    t1 (FrameNumber): Point between 0 and NewLengthInFrames at which the change in length ends
    should_transact (bool): Whether or not any undo-redo changes should be generated

<a id="unreal.AnimSequencerController.resize"></a>

#### resize

```python
def resize(length: float,
           t0: float,
           t1: float,
           should_transact: bool = True) -> None
```

x.resize(length, t0, t1, should_transact=True) -> None
Resize
deprecated: Resize is deprecated use ResizeInFrames instead.

Args:
    length (float): 
    t0 (float): 
    t1 (float): 
    should_transact (bool):

<a id="unreal.AnimSequencerController.rename_curve"></a>

#### rename_curve

```python
def rename_curve(curve_to_rename_id: AnimationCurveIdentifier,
                 new_curve_id: AnimationCurveIdentifier,
                 should_transact: bool = True) -> bool
```

x.rename_curve(curve_to_rename_id, new_curve_id, should_transact=True) -> bool
Renames the curve with provided identifier. Broadcasts a EAnimDataModelNotifyType::CurveRenamed notify if successful.

Args:
    curve_to_rename_id (AnimationCurveIdentifier): Identifier for the curve to be renamed
    new_curve_id (AnimationCurveIdentifier): Time of the key to be removed
    should_transact (bool): Whether or not any undo-redo changes should be generated

Returns:
    bool: Whether or not the curve was successfully renamed

<a id="unreal.AnimSequencerController.remove_transform_curve_key"></a>

#### remove_transform_curve_key

```python
def remove_transform_curve_key(curve_id: AnimationCurveIdentifier,
                               time: float,
                               should_transact: bool = True) -> bool
```

x.remove_transform_curve_key(curve_id, time, should_transact=True) -> bool
Removes a single key for the transform curve with provided identifier. Broadcasts a EAnimDataModelNotifyType::CurveChanged notify if successful.

Args:
    curve_id (AnimationCurveIdentifier): Identifier for the transform curve for which the key is to be removed
    time (float): Time of the key to be removed
    should_transact (bool): Whether or not any undo-redo changes should be generated

Returns:
    bool: Whether or not the transform curve key was successfully removed

<a id="unreal.AnimSequencerController.remove_curve_key"></a>

#### remove_curve_key

```python
def remove_curve_key(curve_id: AnimationCurveIdentifier,
                     time: float,
                     should_transact: bool = True) -> bool
```

x.remove_curve_key(curve_id, time, should_transact=True) -> bool
Remove a single key from the curve with provided identifier and name. Broadcasts a EAnimDataModelNotifyType::CurveChanged notify if successful.

Args:
    curve_id (AnimationCurveIdentifier): Identifier for the curve for which the key is to be removed
    time (float): Time of the key to be removed
    should_transact (bool): Whether or not any undo-redo changes should be generated

Returns:
    bool: Whether or not the curve key was successfully removed

<a id="unreal.AnimSequencerController.remove_curve"></a>

#### remove_curve

```python
def remove_curve(curve_id: AnimationCurveIdentifier,
                 should_transact: bool = True) -> bool
```

x.remove_curve(curve_id, should_transact=True) -> bool
Remove the curve with provided identifier. Broadcasts a EAnimDataModelNotifyType::CurveRemoved notify if successful.

Args:
    curve_id (AnimationCurveIdentifier): Identifier for the to-be-removed curve
    should_transact (bool): Whether or not any undo-redo changes should be generated

Returns:
    bool: Whether or not the curve was successfully removed

<a id="unreal.AnimSequencerController.remove_bone_track"></a>

#### remove_bone_track

```python
def remove_bone_track(bone_name: Name, should_transact: bool = True) -> bool
```

x.remove_bone_track(bone_name, should_transact=True) -> bool
Removes an existing bone animation track with the provided name. Broadcasts a EAnimDataModelNotifyType::TrackRemoved notify if successful.

Args:
    bone_name (Name): Bone name of the track which should be removed
    should_transact (bool): Whether or not any undo-redo changes should be generated

Returns:
    bool: Whether or not the removal was successful

<a id="unreal.AnimSequencerController.remove_attribute_key"></a>

#### remove_attribute_key

```python
def remove_attribute_key(attribute_identifier: AnimationAttributeIdentifier,
                         time: float,
                         should_transact: bool = True) -> bool
```

x.remove_attribute_key(attribute_identifier, time, should_transact=True) -> bool
Remove a single key from the attribute with provided identifier. Broadcasts a EAnimDataModelNotifyType::AttributeChanged notify if successful.

Args:
    attribute_identifier (AnimationAttributeIdentifier): Identifier for the attribute from which the key is to be removed
    time (float): Time of the key to be removed
    should_transact (bool): Whether or not any undo-redo changes should be generated

Returns:
    bool: Whether or not the attribute key was successfully removed

<a id="unreal.AnimSequencerController.remove_attribute"></a>

#### remove_attribute

```python
def remove_attribute(attribute_identifier: AnimationAttributeIdentifier,
                     should_transact: bool = True) -> bool
```

x.remove_attribute(attribute_identifier, should_transact=True) -> bool
Removes an attribute, if found, with the provided information. Broadcasts a EAnimDataModelNotifyType::AttributeRemoved notify if successful.

Args:
    attribute_identifier (AnimationAttributeIdentifier): Identifier for the to-be-removed attribute
    should_transact (bool): Whether or not any undo-redo changes should be generated

Returns:
    bool: Whether or not the attribute was successfully removed

<a id="unreal.AnimSequencerController.remove_all_curves_of_type"></a>

#### remove_all_curves_of_type

```python
def remove_all_curves_of_type(supported_curve_type: RawCurveTrackTypes,
                              should_transact: bool = True) -> None
```

x.remove_all_curves_of_type(supported_curve_type, should_transact=True) -> None
Removes all the curves of the provided type. Broadcasts a EAnimDataModelNotifyType::CurveRemoved for each removed curve, wrapped within BracketOpened/BracketClosed notifies.

Args:
    supported_curve_type (RawCurveTrackTypes): Type for which all curves are to be removed
    should_transact (bool): Whether or not any undo-redo changes should be generated

<a id="unreal.AnimSequencerController.remove_all_bone_tracks"></a>

#### remove_all_bone_tracks

```python
def remove_all_bone_tracks(should_transact: bool = True) -> None
```

x.remove_all_bone_tracks(should_transact=True) -> None
Removes all existing Bone Animation tracks. Broadcasts a EAnimDataModelNotifyType::TrackRemoved for each removed track, wrapped within BracketOpened/BracketClosed notifies.

Args:
    should_transact (bool): Whether or not any undo-redo changes should be generated

<a id="unreal.AnimSequencerController.remove_all_attributes_for_bone"></a>

#### remove_all_attributes_for_bone

```python
def remove_all_attributes_for_bone(bone_name: Name,
                                   should_transact: bool = True) -> int
```

x.remove_all_attributes_for_bone(bone_name, should_transact=True) -> int32
Removes all attributes for the specified bone name, if any. Broadcasts a EAnimDataModelNotifyType::AttributeRemoved notify for each removed attribute.

Args:
    bone_name (Name): Name of the bone to remove attributes for
    should_transact (bool): Whether or not any undo-redo changes should be generated

Returns:
    int32: Total number of removes attributes

<a id="unreal.AnimSequencerController.remove_all_attributes"></a>

#### remove_all_attributes

```python
def remove_all_attributes(should_transact: bool = True) -> int
```

x.remove_all_attributes(should_transact=True) -> int32
Removes all stored attributes. Broadcasts a EAnimDataModelNotifyType::AttributeRemoved notify for each removed attribute.

Args:
    should_transact (bool): Whether or not any undo-redo changes should be generated

Returns:
    int32: Total number of removes attributes

<a id="unreal.AnimSequencerController.open_bracket"></a>

#### open_bracket

```python
def open_bracket(title: Text, should_transact: bool = True) -> None
```

x.open_bracket(title, should_transact=True) -> None
Opens an interaction bracket, used for combining a set of controller actions. Broadcasts a EAnimDataModelNotifyType::BracketOpened notify,
this can be used by any Views or dependent systems to halt any unnecessary or invalid operations until the (last) bracket is closed.

Args:
    title (Text): Description of the bracket, e.g. "Generating Curve Data"
    should_transact (bool): Whether or not any undo-redo changes should be generated

<a id="unreal.AnimSequencerController.insert_bone_track"></a>

#### insert_bone_track

```python
def insert_bone_track(bone_name: Name,
                      desired_index: int,
                      should_transact: bool = True) -> int
```

x.insert_bone_track(bone_name, desired_index, should_transact=True) -> int32
Insert Bone Track
deprecated: InsertBoneTrack is deprecated use AddBoneTrack instead.

Args:
    bone_name (Name): 
    desired_index (int32): 
    should_transact (bool): 

Returns:
    int32:

<a id="unreal.AnimSequencerController.get_model_interface"></a>

#### get_model_interface

```python
def get_model_interface() -> AnimationDataModel
```

x.get_model_interface() -> AnimationDataModel


Returns:
    AnimationDataModel: The IAnimationDataModel instance this controller is currently targeting

<a id="unreal.AnimSequencerController.find_or_add_curve_names_on_skeleton"></a>

#### find_or_add_curve_names_on_skeleton

```python
def find_or_add_curve_names_on_skeleton(
        skeleton: Skeleton,
        supported_curve_type: RawCurveTrackTypes,
        should_transact: bool = True) -> None
```

x.find_or_add_curve_names_on_skeleton(skeleton, supported_curve_type, should_transact=True) -> None
Find or Add Curve Names on Skeleton
deprecated: This function is no longer used.

Args:
    skeleton (Skeleton): 
    supported_curve_type (RawCurveTrackTypes): 
    should_transact (bool):

<a id="unreal.AnimSequencerController.duplicate_curve"></a>

#### duplicate_curve

```python
def duplicate_curve(copy_curve_id: AnimationCurveIdentifier,
                    new_curve_id: AnimationCurveIdentifier,
                    should_transact: bool = True) -> bool
```

x.duplicate_curve(copy_curve_id, new_curve_id, should_transact=True) -> bool
Duplicated the curve with the identifier. Broadcasts a EAnimDataModelNotifyType::CurveAdded notify if successful.

Args:
    copy_curve_id (AnimationCurveIdentifier): Identifier for the to-be-duplicated curve
    new_curve_id (AnimationCurveIdentifier): Identifier for the to-be-added curve
    should_transact (bool): Whether or not any undo-redo changes should be generated

Returns:
    bool: Whether or not the curve was successfully duplicated

<a id="unreal.AnimSequencerController.duplicate_attribute"></a>

#### duplicate_attribute

```python
def duplicate_attribute(attribute_identifier: AnimationAttributeIdentifier,
                        new_attribute_identifier: AnimationAttributeIdentifier,
                        should_transact: bool = True) -> bool
```

x.duplicate_attribute(attribute_identifier, new_attribute_identifier, should_transact=True) -> bool
Duplicated the attribute (curve) with the identifier. Broadcasts a EAnimDataModelNotifyType::AttributeAdded notify if successful.

Args:
    attribute_identifier (AnimationAttributeIdentifier): Identifier for the to-be-duplicated attribute
    new_attribute_identifier (AnimationAttributeIdentifier): Identifier for the to-be-added attribute
    should_transact (bool): Whether or not any undo-redo changes should be generated

Returns:
    bool: Whether or not the attribute was successfully duplicated

<a id="unreal.AnimSequencerController.close_bracket"></a>

#### close_bracket

```python
def close_bracket(should_transact: bool = True) -> None
```

x.close_bracket(should_transact=True) -> None
Closes a previously opened interaction bracket, used for combining a set of controller actions. Broadcasts a EAnimDataModelNotifyType::BracketClosed notify.

Args:
    should_transact (bool): Whether or not any undo-redo changes should be generated

<a id="unreal.AnimSequencerController.add_curve"></a>

#### add_curve

```python
def add_curve(curve_id: AnimationCurveIdentifier,
              curve_flags: int = 4,
              should_transact: bool = True) -> bool
```

x.add_curve(curve_id, curve_flags=4, should_transact=True) -> bool
Adds a new curve with the provided information. Broadcasts a EAnimDataModelNotifyType::CurveAdded notify if successful.

Args:
    curve_id (AnimationCurveIdentifier): Identifier for the to-be-added curve
    curve_flags (int32): Flags to be set for the curve
    should_transact (bool): Whether or not any undo-redo changes should be generated

Returns:
    bool: Whether or not the curve was successfully added

<a id="unreal.AnimSequencerController.add_bone_track"></a>

#### add_bone_track

```python
def add_bone_track(bone_name: Name, should_transact: bool = True) -> int
```

x.add_bone_track(bone_name, should_transact=True) -> int32
Add Bone Track
deprecated: AddBoneTrack returning index is deprecated use AddBoneCurve returning bool instead.

Args:
    bone_name (Name): 
    should_transact (bool): 

Returns:
    int32:

<a id="unreal.AnimSequencerController.add_bone_curve"></a>

#### add_bone_curve

```python
def add_bone_curve(bone_name: Name, should_transact: bool = True) -> bool
```

x.add_bone_curve(bone_name, should_transact=True) -> bool
Add Bone Curve

Args:
    bone_name (Name): 
    should_transact (bool): 

Returns:
    bool:

<a id="unreal.AnimSequencerController.add_attribute"></a>

#### add_attribute

```python
def add_attribute(attribute_identifier: AnimationAttributeIdentifier,
                  should_transact: bool = True) -> bool
```

x.add_attribute(attribute_identifier, should_transact=True) -> bool
Adds a new attribute with the provided information. Broadcasts a EAnimDataModelNotifyType::AttributeAdded notify if successful.

Args:
    attribute_identifier (AnimationAttributeIdentifier): Identifier for the to-be-added attribute
    should_transact (bool): Whether or not any undo-redo changes should be generated

Returns:
    bool: Whether or not the attribute was successfully added

<a id="unreal.AnimationSequencerDataModel"></a>