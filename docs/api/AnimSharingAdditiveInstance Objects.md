## AnimSharingAdditiveInstance Objects

```python
class AnimSharingAdditiveInstance(AnimInstance)
```

Anim Sharing Additive Instance

**C++ Source:**

- **Plugin**: AnimationSharing
- **Module**: AnimationSharing
- **File**: AnimationSharingInstances.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additive_animation`` (AnimSequence):  [Read-Write]
- ``alpha`` (float):  [Read-Write]
- ``base_component`` (SkeletalMeshComponent):  [Read-Write]
- ``on_all_montage_instances_ended`` (OnAllMontageInstancesEndedMCDelegate):  [Read-Write] Called when all Montage instances have ended.
- ``on_montage_blended_in`` (OnMontageBlendedInEndedMCDelegate):  [Read-Write] Called when a montage finishes blending in
- ``on_montage_blending_out`` (OnMontageBlendingOutStartedMCDelegate):  [Read-Write] Called when a montage starts blending out, whether interrupted or finished
- ``on_montage_ended`` (OnMontageEndedMCDelegate):  [Read-Write] Called when a montage has ended, whether interrupted or finished
- ``on_montage_started`` (OnMontageStartedMCDelegate):  [Read-Write] Called when a montage has started
- ``propagate_notifies_to_linked_instances`` (bool):  [Read-Write] Whether to propagate notifies to any linked anim instances
- ``receive_notifies_from_linked_instances`` (bool):  [Read-Write] Whether to process notifies from any linked anim instances
- ``root_motion_mode`` (RootMotionMode):  [Read-Write] Sets where this blueprint pulls Root Motion from
- ``state_bool`` (bool):  [Read-Write]
- ``use_main_instance_montage_evaluation_data`` (bool):  [Read-Write] If true, linked instances will use the main instance's montage data. (i.e. playing a montage on a main instance will play it on the linked layer too.)

<a id="unreal.AnimSharingAdditiveInstance.base_component"></a>

#### base_component

```python
@property
def base_component() -> SkeletalMeshComponent
```

(SkeletalMeshComponent):  [Read-Only]

<a id="unreal.AnimSharingAdditiveInstance.additive_animation"></a>

#### additive_animation

```python
@property
def additive_animation() -> AnimSequence
```

(AnimSequence):  [Read-Only]

<a id="unreal.AnimSharingAdditiveInstance.alpha"></a>

#### alpha

```python
@property
def alpha() -> float
```

(float):  [Read-Only]

<a id="unreal.AnimSharingAdditiveInstance.state_bool"></a>

#### state_bool

```python
@property
def state_bool() -> bool
```

(bool):  [Read-Only]

<a id="unreal.AnimationSharingManager"></a>