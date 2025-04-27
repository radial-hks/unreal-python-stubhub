## AnimNode_ControlRig Objects

```python
class AnimNode_ControlRig(AnimNode_ControlRigBase)
```

Animation node that allows animation ControlRig output to be used in an animation graph

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: AnimNode_ControlRig.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha`` (float):  [Read-Write] alpha value handler
- ``alpha_bool_blend`` (InputAlphaBoolBlend):  [Read-Write]
- ``alpha_bool_enabled`` (bool):  [Read-Write]
- ``alpha_curve_name`` (Name):  [Read-Write]
- ``alpha_input_type`` (AnimAlphaInputType):  [Read-Write]
- ``alpha_scale_bias`` (InputScaleBias):  [Read-Write]
- ``alpha_scale_bias_clamp`` (InputScaleBiasClamp):  [Read-Write]
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write]
- ``control_rig_class`` (type(Class)):  [Read-Write] The class to use for the rig.
- ``event_queue`` (Array[ControlRigAnimNodeEventName]):  [Read-Write] The customized event queue to run
- ``lod_threshold`` (int32):  [Read-Write] * Max LOD that this node is allowed to run
  * For example if you have LODThreshold to be 2, it will run until LOD 2 (based on 0 index)
  * when the component LOD becomes 3, it will stop update/evaluate
  * currently transition would be issue and that has to be re-visited
- ``reset_input_pose_to_initial`` (bool):  [Read-Write] If this is checked the rig's pose needs to be reset to its initial
  prior to evaluating the rig.
- ``set_ref_pose_from_skeleton`` (bool):  [Read-Write] Override the initial transforms with those taken from the mesh component
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

<a id="unreal.AnimNode_ControlRig.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.RigHierarchySettings"></a>