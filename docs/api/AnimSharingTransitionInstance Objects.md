## AnimSharingTransitionInstance Objects

```python
class AnimSharingTransitionInstance(AnimInstance)
```

Anim Sharing Transition Instance

**C++ Source:**

- **Plugin**: AnimationSharing
- **Module**: AnimationSharing
- **File**: AnimationSharingInstances.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_bool`` (bool):  [Read-Write]
- ``blend_time`` (float):  [Read-Write]
- ``from_component`` (SkeletalMeshComponent):  [Read-Write]
- ``on_all_montage_instances_ended`` (OnAllMontageInstancesEndedMCDelegate):  [Read-Write] Called when all Montage instances have ended.
- ``on_montage_blended_in`` (OnMontageBlendedInEndedMCDelegate):  [Read-Write] Called when a montage finishes blending in
- ``on_montage_blending_out`` (OnMontageBlendingOutStartedMCDelegate):  [Read-Write] Called when a montage starts blending out, whether interrupted or finished
- ``on_montage_ended`` (OnMontageEndedMCDelegate):  [Read-Write] Called when a montage has ended, whether interrupted or finished
- ``on_montage_started`` (OnMontageStartedMCDelegate):  [Read-Write] Called when a montage has started
- ``propagate_notifies_to_linked_instances`` (bool):  [Read-Write] Whether to propagate notifies to any linked anim instances
- ``receive_notifies_from_linked_instances`` (bool):  [Read-Write] Whether to process notifies from any linked anim instances
- ``root_motion_mode`` (RootMotionMode):  [Read-Write] Sets where this blueprint pulls Root Motion from
- ``to_component`` (SkeletalMeshComponent):  [Read-Write]
- ``use_main_instance_montage_evaluation_data`` (bool):  [Read-Write] If true, linked instances will use the main instance's montage data. (i.e. playing a montage on a main instance will play it on the linked layer too.)

<a id="unreal.AnimSharingTransitionInstance.from_component"></a>

#### from_component

```python
@property
def from_component() -> SkeletalMeshComponent
```

(SkeletalMeshComponent):  [Read-Only]

<a id="unreal.AnimSharingTransitionInstance.to_component"></a>

#### to_component

```python
@property
def to_component() -> SkeletalMeshComponent
```

(SkeletalMeshComponent):  [Read-Only]

<a id="unreal.AnimSharingTransitionInstance.blend_time"></a>

#### blend_time

```python
@property
def blend_time() -> float
```

(float):  [Read-Only]

<a id="unreal.AnimSharingTransitionInstance.blend_bool"></a>

#### blend_bool

```python
@property
def blend_bool() -> bool
```

(bool):  [Read-Only]

<a id="unreal.AnimSharingAdditiveInstance"></a>