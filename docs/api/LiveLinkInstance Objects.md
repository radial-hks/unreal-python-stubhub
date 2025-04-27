## LiveLinkInstance Objects

```python
class LiveLinkInstance(AnimInstance)
```

Live Link Instance

**C++ Source:**

- **Module**: LiveLinkAnimationCore
- **File**: LiveLinkInstance.h

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

<a id="unreal.LiveLinkInstance.set_subject"></a>

#### set_subject

```python
def set_subject(subject_name: LiveLinkSubjectName) -> None
```

x.set_subject(subject_name) -> None
Set Subject

Args:
    subject_name (LiveLinkSubjectName):

<a id="unreal.LiveLinkInstance.set_retarget_asset"></a>

#### set_retarget_asset

```python
def set_retarget_asset(retarget_asset: Class) -> None
```

x.set_retarget_asset(retarget_asset) -> None
Set Retarget Asset

Args:
    retarget_asset (type(Class)):

<a id="unreal.LiveLinkInstance.enable_live_link_evaluation"></a>

#### enable_live_link_evaluation

```python
def enable_live_link_evaluation(do_enable: bool) -> None
```

x.enable_live_link_evaluation(do_enable) -> None
Enable Live Link Evaluation

Args:
    do_enable (bool):

<a id="unreal.LiveLinkRetargetAsset"></a>