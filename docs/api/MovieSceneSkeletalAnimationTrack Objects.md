## MovieSceneSkeletalAnimationTrack Objects

```python
class MovieSceneSkeletalAnimationTrack(MovieSceneNameableTrack)
```

Handles animation of skeletal mesh actors

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneSkeletalAnimationTrack.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_first_child_of_root`` (bool):  [Read-Write] Whether to blend and adjust the first child node with animation instead of the root, this should be true for blending when the root is static, false if the animations have proper root motion
- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this track/any of the sections on this track evaluates at runtime.
- ``display_name`` (Text):  [Read-Write] The track's human readable display name.
- ``display_options`` (MovieSceneTrackDisplayOptions):  [Read-Write] General display options for a given track
- ``eval_options`` (MovieSceneTrackEvalOptions):  [Read-Write] General evaluation options for a given track
- ``show_root_motion_trail`` (bool):  [Read-Write] Whether to show the position of the root for this sections
- ``swap_root_bone`` (SwapRootBone):  [Read-Write] If on the root bone transform will be swapped to the specified root
- ``track_row_display_names`` (Array[Text]):  [Read-Write] The track display name per row.
- ``track_tint`` (Color):  [Read-Write] This track's tint color

<a id="unreal.MovieSceneSkeletalAnimationTrack.swap_root_bone"></a>

#### swap_root_bone

```python
@property
def swap_root_bone() -> SwapRootBone
```

(SwapRootBone):  [Read-Write] If on the root bone transform will be swapped to the specified root

<a id="unreal.MovieSceneSkeletalAnimationTrack.swap_root_bone"></a>

#### swap_root_bone

```python
@swap_root_bone.setter
def swap_root_bone(value: SwapRootBone) -> None
```

<a id="unreal.MovieSceneSlomoTrack"></a>