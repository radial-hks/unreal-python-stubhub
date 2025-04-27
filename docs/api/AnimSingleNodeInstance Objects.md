## AnimSingleNodeInstance Objects

```python
class AnimSingleNodeInstance(AnimInstance)
```

Anim Single Node Instance

**C++ Source:**

- **Module**: Engine
- **File**: AnimSingleNodeInstance.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_all_montage_instances_ended`` (OnAllMontageInstancesEndedMCDelegate):  [Read-Write] Called when all Montage instances have ended.
- ``on_montage_blended_in`` (OnMontageBlendedInEndedMCDelegate):  [Read-Write] Called when a montage finishes blending in
- ``on_montage_blending_out`` (OnMontageBlendingOutStartedMCDelegate):  [Read-Write] Called when a montage starts blending out, whether interrupted or finished
- ``on_montage_ended`` (OnMontageEndedMCDelegate):  [Read-Write] Called when a montage has ended, whether interrupted or finished
- ``on_montage_started`` (OnMontageStartedMCDelegate):  [Read-Write] Called when a montage has started
- ``propagate_notifies_to_linked_instances`` (bool):  [Read-Write] Whether to propagate notifies to any linked anim instances
- ``receive_notifies_from_linked_instances`` (bool):  [Read-Write] Whether to process notifies from any linked anim instances
- ``root_motion_mode`` (RootMotionMode):  [Read-Write] Sets where this blueprint pulls Root Motion from
- ``use_main_instance_montage_evaluation_data`` (bool):  [Read-Write] If true, linked instances will use the main instance's montage data. (i.e. playing a montage on a main instance will play it on the linked layer too.)

<a id="unreal.AnimSingleNodeInstance.stop_anim"></a>

#### stop_anim

```python
def stop_anim() -> None
```

x.stop_anim() -> None
Stop Anim

<a id="unreal.AnimSingleNodeInstance.set_reverse"></a>

#### set_reverse

```python
def set_reverse(reverse: bool) -> None
```

x.set_reverse(reverse) -> None
Set Reverse

Args:
    reverse (bool):

<a id="unreal.AnimSingleNodeInstance.set_preview_curve_override"></a>

#### set_preview_curve_override

```python
def set_preview_curve_override(pose_name: Name, value: float,
                               remove_if_zero: bool) -> None
```

x.set_preview_curve_override(pose_name, value, remove_if_zero) -> None
Set pose value

Args:
    pose_name (Name): 
    value (float): 
    remove_if_zero (bool):

<a id="unreal.AnimSingleNodeInstance.set_position_with_previous_time"></a>

#### set_position_with_previous_time

```python
def set_position_with_previous_time(position: float,
                                    previous_time: float,
                                    fire_notifies: bool = True) -> None
```

x.set_position_with_previous_time(position, previous_time, fire_notifies=True) -> None
Set Position with Previous Time

Args:
    position (float): 
    previous_time (float): 
    fire_notifies (bool):

<a id="unreal.AnimSingleNodeInstance.set_position"></a>

#### set_position

```python
def set_position(position: float, fire_notifies: bool = True) -> None
```

x.set_position(position, fire_notifies=True) -> None
Set Position

Args:
    position (float): 
    fire_notifies (bool):

<a id="unreal.AnimSingleNodeInstance.set_play_rate"></a>

#### set_play_rate

```python
def set_play_rate(play_rate: float) -> None
```

x.set_play_rate(play_rate) -> None
Set Play Rate

Args:
    play_rate (float):

<a id="unreal.AnimSingleNodeInstance.set_playing"></a>

#### set_playing

```python
def set_playing(is_playing: bool) -> None
```

x.set_playing(is_playing) -> None
Set Playing

Args:
    is_playing (bool):

<a id="unreal.AnimSingleNodeInstance.set_mirror_data_table"></a>

#### set_mirror_data_table

```python
def set_mirror_data_table(mirror_data_table: MirrorDataTable) -> None
```

x.set_mirror_data_table(mirror_data_table) -> None
Set Mirror Data Table

Args:
    mirror_data_table (MirrorDataTable):

<a id="unreal.AnimSingleNodeInstance.set_looping"></a>

#### set_looping

```python
def set_looping(is_looping: bool) -> None
```

x.set_looping(is_looping) -> None
Set Looping

Args:
    is_looping (bool):

<a id="unreal.AnimSingleNodeInstance.set_blend_space_position"></a>

#### set_blend_space_position

```python
def set_blend_space_position(position: Vector) -> None
```

x.set_blend_space_position(position) -> None
Set Blend Space Position

Args:
    position (Vector):

<a id="unreal.AnimSingleNodeInstance.set_animation_asset"></a>

#### set_animation_asset

```python
def set_animation_asset(new_asset: AnimationAsset,
                        is_looping: bool = True,
                        play_rate: float = 1.000000) -> None
```

x.set_animation_asset(new_asset, is_looping=True, play_rate=1.000000) -> None
Set New Asset - calls InitializeAnimation, for now we need MeshComponent *

Args:
    new_asset (AnimationAsset): 
    is_looping (bool): 
    play_rate (float):

<a id="unreal.AnimSingleNodeInstance.play_anim"></a>

#### play_anim

```python
def play_anim(is_looping: bool = False,
              play_rate: float = 1.000000,
              start_position: float = 0.000000) -> None
```

x.play_anim(is_looping=False, play_rate=1.000000, start_position=0.000000) -> None
For AnimSequence specific *

Args:
    is_looping (bool): 
    play_rate (float): 
    start_position (float):

<a id="unreal.AnimSingleNodeInstance.get_mirror_data_table"></a>

#### get_mirror_data_table

```python
def get_mirror_data_table() -> MirrorDataTable
```

x.get_mirror_data_table() -> MirrorDataTable
Get Mirror Data Table

Returns:
    MirrorDataTable:

<a id="unreal.AnimSingleNodeInstance.get_length"></a>

#### get_length

```python
def get_length() -> float
```

x.get_length() -> float
Get Length

Returns:
    float:

<a id="unreal.AnimSingleNodeInstance.get_animation_asset"></a>

#### get_animation_asset

```python
def get_animation_asset() -> AnimationAsset
```

x.get_animation_asset() -> AnimationAsset
Get the currently used asset

Returns:
    AnimationAsset:

<a id="unreal.AnimPreviewInstance"></a>