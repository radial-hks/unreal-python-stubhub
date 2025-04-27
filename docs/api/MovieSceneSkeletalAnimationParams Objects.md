## MovieSceneSkeletalAnimationParams Objects

```python
class MovieSceneSkeletalAnimationParams(StructBase)
```

Movie Scene Skeletal Animation Params

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneSkeletalAnimationSection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``animation`` (AnimSequenceBase):  [Read-Write] The animation this section plays
- ``end_frame_offset`` (FrameNumber):  [Read-Write] The offset into the end of the animation clip
- ``first_loop_start_frame_offset`` (FrameNumber):  [Read-Write] The offset into the beginning of the animation clip for the first loop of play.
- ``force_custom_mode`` (bool):  [Read-Write] If on animation sequence will always play when active even if the animation is controlled by a Blueprint or Anim Instance Class
- ``mirror_data_table`` (MirrorDataTable):  [Read-Write]
- ``play_rate`` (MovieSceneTimeWarpVariant):  [Read-Write] The playback rate of the animation clip
- ``reverse`` (bool):  [Read-Write] Reverse the playback of the animation clip
- ``skip_anim_notifiers`` (bool):  [Read-Write] If on will skip sending animation notifies
- ``slot_name`` (Name):  [Read-Write] The slot name to use for the animation
- ``start_frame_offset`` (FrameNumber):  [Read-Write] The offset into the beginning of the animation clip
- ``swap_root_bone`` (SwapRootBone):  [Read-Write] If on the root bone transform will be swapped to the specified root

<a id="unreal.MovieSceneSkeletalAnimationParams.__init__"></a>

#### __init__

```python
def __init__(
    animation: AnimSequenceBase = None,
    first_loop_start_frame_offset: FrameNumber = [0],
    start_frame_offset: FrameNumber = [0],
    end_frame_offset: FrameNumber = [0],
    play_rate: MovieSceneTimeWarpVariant = [1.000000],
    reverse: bool = False,
    slot_name: Name = "None",
    mirror_data_table: MirrorDataTable = None,
    skip_anim_notifiers: bool = False,
    force_custom_mode: bool = False,
    swap_root_bone: SwapRootBone = SwapRootBone.SWAP_ROOT_BONE_COMPONENT
) -> None
```

<a id="unreal.MovieSceneSkeletalAnimationParams.animation"></a>

#### animation

```python
@property
def animation() -> AnimSequenceBase
```

(AnimSequenceBase):  [Read-Write] The animation this section plays

<a id="unreal.MovieSceneSkeletalAnimationParams.animation"></a>

#### animation

```python
@animation.setter
def animation(value: AnimSequenceBase) -> None
```

<a id="unreal.MovieSceneSkeletalAnimationParams.first_loop_start_frame_offset"></a>

#### first_loop_start_frame_offset

```python
@property
def first_loop_start_frame_offset() -> FrameNumber
```

(FrameNumber):  [Read-Write] The offset into the beginning of the animation clip for the first loop of play.

<a id="unreal.MovieSceneSkeletalAnimationParams.first_loop_start_frame_offset"></a>

#### first_loop_start_frame_offset

```python
@first_loop_start_frame_offset.setter
def first_loop_start_frame_offset(value: FrameNumber) -> None
```

<a id="unreal.MovieSceneSkeletalAnimationParams.start_frame_offset"></a>

#### start_frame_offset

```python
@property
def start_frame_offset() -> FrameNumber
```

(FrameNumber):  [Read-Write] The offset into the beginning of the animation clip

<a id="unreal.MovieSceneSkeletalAnimationParams.start_frame_offset"></a>

#### start_frame_offset

```python
@start_frame_offset.setter
def start_frame_offset(value: FrameNumber) -> None
```

<a id="unreal.MovieSceneSkeletalAnimationParams.end_frame_offset"></a>

#### end_frame_offset

```python
@property
def end_frame_offset() -> FrameNumber
```

(FrameNumber):  [Read-Write] The offset into the end of the animation clip

<a id="unreal.MovieSceneSkeletalAnimationParams.end_frame_offset"></a>

#### end_frame_offset

```python
@end_frame_offset.setter
def end_frame_offset(value: FrameNumber) -> None
```

<a id="unreal.MovieSceneSkeletalAnimationParams.play_rate"></a>

#### play_rate

```python
@property
def play_rate() -> MovieSceneTimeWarpVariant
```

(MovieSceneTimeWarpVariant):  [Read-Write] The playback rate of the animation clip

<a id="unreal.MovieSceneSkeletalAnimationParams.play_rate"></a>

#### play_rate

```python
@play_rate.setter
def play_rate(value: MovieSceneTimeWarpVariant) -> None
```

<a id="unreal.MovieSceneSkeletalAnimationParams.reverse"></a>

#### reverse

```python
@property
def reverse() -> bool
```

(bool):  [Read-Write] Reverse the playback of the animation clip

<a id="unreal.MovieSceneSkeletalAnimationParams.reverse"></a>

#### reverse

```python
@reverse.setter
def reverse(value: bool) -> None
```

<a id="unreal.MovieSceneSkeletalAnimationParams.slot_name"></a>

#### slot_name

```python
@property
def slot_name() -> Name
```

(Name):  [Read-Write] The slot name to use for the animation

<a id="unreal.MovieSceneSkeletalAnimationParams.slot_name"></a>

#### slot_name

```python
@slot_name.setter
def slot_name(value: Name) -> None
```

<a id="unreal.MovieSceneSkeletalAnimationParams.mirror_data_table"></a>

#### mirror_data_table

```python
@property
def mirror_data_table() -> MirrorDataTable
```

(MirrorDataTable):  [Read-Write]

<a id="unreal.MovieSceneSkeletalAnimationParams.mirror_data_table"></a>

#### mirror_data_table

```python
@mirror_data_table.setter
def mirror_data_table(value: MirrorDataTable) -> None
```

<a id="unreal.MovieSceneSkeletalAnimationParams.skip_anim_notifiers"></a>

#### skip_anim_notifiers

```python
@property
def skip_anim_notifiers() -> bool
```

(bool):  [Read-Write] If on will skip sending animation notifies

<a id="unreal.MovieSceneSkeletalAnimationParams.skip_anim_notifiers"></a>

#### skip_anim_notifiers

```python
@skip_anim_notifiers.setter
def skip_anim_notifiers(value: bool) -> None
```

<a id="unreal.MovieSceneSkeletalAnimationParams.force_custom_mode"></a>

#### force_custom_mode

```python
@property
def force_custom_mode() -> bool
```

(bool):  [Read-Write] If on animation sequence will always play when active even if the animation is controlled by a Blueprint or Anim Instance Class

<a id="unreal.MovieSceneSkeletalAnimationParams.force_custom_mode"></a>

#### force_custom_mode

```python
@force_custom_mode.setter
def force_custom_mode(value: bool) -> None
```

<a id="unreal.MovieSceneSkeletalAnimationParams.swap_root_bone"></a>

#### swap_root_bone

```python
@property
def swap_root_bone() -> SwapRootBone
```

(SwapRootBone):  [Read-Write] If on the root bone transform will be swapped to the specified root

<a id="unreal.MovieSceneSkeletalAnimationParams.swap_root_bone"></a>

#### swap_root_bone

```python
@swap_root_bone.setter
def swap_root_bone(value: SwapRootBone) -> None
```

<a id="unreal.MovieSceneTimeWarpVariant"></a>