## AnimNode_ControlRigBase Objects

```python
class AnimNode_ControlRigBase(AnimNode_CustomProperty)
```

Animation node that allows animation ControlRig output to be used in an animation graph

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: AnimNode_ControlRigBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write]
- ``event_queue`` (Array[ControlRigAnimNodeEventName]):  [Read-Write] The customized event queue to run
- ``reset_input_pose_to_initial`` (bool):  [Read-Write] If this is checked the rig's pose needs to be reset to its initial
  prior to evaluating the rig.
- ``source`` (PoseLink):  [Read-Write]
- ``transfer_input_curves`` (bool):  [Read-Write] If this is checked the curves coming from the AnimBP will be
  transferred into the Control Rig.
- ``transfer_input_pose`` (bool):  [Read-Write] If this is checked the bone pose coming from the AnimBP will be
  transferred into the Control Rig.
- ``transfer_pose_in_global_space`` (bool):  [Read-Write] Transferring the pose in global space guarantees a global pose match,
  while transferring in local space ensures a match of the local transforms.
  In general transforms only differ if the hierarchy topology differs
  between the Control Rig and the skeleton used in the AnimBP.
  Note: Turning this off can potentially improve performance.

<a id="unreal.AnimNode_ControlRigBase.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AnimNode_ControlRig"></a>