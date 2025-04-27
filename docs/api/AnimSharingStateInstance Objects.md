## AnimSharingStateInstance Objects

```python
class AnimSharingStateInstance(AnimInstance)
```

Anim Sharing State Instance

**C++ Source:**

- **Plugin**: AnimationSharing
- **Module**: AnimationSharing
- **File**: AnimationSharingInstances.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``animation_to_play`` (AnimSequence):  [Read-Write]
- ``on_all_montage_instances_ended`` (OnAllMontageInstancesEndedMCDelegate):  [Read-Write] Called when all Montage instances have ended.
- ``on_montage_blended_in`` (OnMontageBlendedInEndedMCDelegate):  [Read-Write] Called when a montage finishes blending in
- ``on_montage_blending_out`` (OnMontageBlendingOutStartedMCDelegate):  [Read-Write] Called when a montage starts blending out, whether interrupted or finished
- ``on_montage_ended`` (OnMontageEndedMCDelegate):  [Read-Write] Called when a montage has ended, whether interrupted or finished
- ``on_montage_started`` (OnMontageStartedMCDelegate):  [Read-Write] Called when a montage has started
- ``permutation_time_offset`` (float):  [Read-Write]
- ``play_rate`` (float):  [Read-Write]
- ``propagate_notifies_to_linked_instances`` (bool):  [Read-Write] Whether to propagate notifies to any linked anim instances
- ``receive_notifies_from_linked_instances`` (bool):  [Read-Write] Whether to process notifies from any linked anim instances
- ``root_motion_mode`` (RootMotionMode):  [Read-Write] Sets where this blueprint pulls Root Motion from
- ``state_bool`` (bool):  [Read-Write]
- ``use_main_instance_montage_evaluation_data`` (bool):  [Read-Write] If true, linked instances will use the main instance's montage data. (i.e. playing a montage on a main instance will play it on the linked layer too.)

<a id="unreal.AnimSharingStateInstance.animation_to_play"></a>

#### animation_to_play

```python
@property
def animation_to_play() -> AnimSequence
```

(AnimSequence):  [Read-Only]

<a id="unreal.AnimSharingStateInstance.permutation_time_offset"></a>

#### permutation_time_offset

```python
@property
def permutation_time_offset() -> float
```

(float):  [Read-Only]

<a id="unreal.AnimSharingStateInstance.play_rate"></a>

#### play_rate

```python
@property
def play_rate() -> float
```

(float):  [Read-Only]

<a id="unreal.AnimSharingStateInstance.state_bool"></a>

#### state_bool

```python
@property
def state_bool() -> bool
```

(bool):  [Read-Only]

<a id="unreal.AnimSharingStateInstance.get_instanced_actors"></a>

#### get_instanced_actors

```python
def get_instanced_actors() -> Array[Actor]
```

x.get_instanced_actors() -> Array[Actor]
Get Instanced Actors

Returns:
    Array[Actor]: 

    actors (Array[Actor]):

<a id="unreal.AnimSharingTransitionInstance"></a>