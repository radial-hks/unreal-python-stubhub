## AnimNode_PoseDriver Objects

```python
class AnimNode_PoseDriver(AnimNode_PoseHandler)
```

RBF based orientation driver

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_PoseDriver.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_weight`` (float):  [Read-Write] Last encountered blendweight for this node
- ``drive_output`` (PoseDriverOutput):  [Read-Write] Whether we should drive poses or curves
- ``drive_source`` (PoseDriverSource):  [Read-Write] Which part of the transform is read
- ``eval_from_ref_pose`` (bool):  [Read-Write] Evaluate SourceBone transform relative from its Reference Pose.
  This is recommended when using Swing and Twist Angle as Distance Method, since the twist will be computed from RefPose.

  If not specified, the local space of SourceBone will be used. (ie relative to parent bone)
  This mode won't work in conjunction with EvalSpaceBone;
- ``eval_space_bone`` (BoneReference):  [Read-Write] Optional other bone space to use when reading SourceBone transform.
  If not specified, the local space of SourceBone will be used. (ie relative to parent bone)
- ``internal_time_accumulator`` (float):  [Read-Write] Accumulated time used to reference the asset in this node
- ``lod_threshold`` (int32):  [Read-Write] * Max LOD that this node is allowed to run
  * For example if you have LODThreshold to be 2, it will run until LOD 2 (based on 0 index)
  * when the component LOD becomes 3, it will stop update/evaluate
  * currently transition would be issue and that has to be re-visited
- ``only_drive_bones`` (Array[BoneReference]):  [Read-Write] List of bones that will modified by this node. If no list is provided, all bones bones with a track in the PoseAsset will be modified
- ``pose_asset`` (PoseAsset):  [Read-Write] The animation sequence asset to evaluate
- ``pose_targets`` (Array[PoseDriverTarget]):  [Read-Write] Targets used to compare with current pose and drive morphs/poses
- ``rbf_params`` (RBFParams):  [Read-Write] Parameters used by RBF solver
- ``source_bones`` (Array[BoneReference]):  [Read-Write] Bone to use for driving parameters based on its orientation
- ``source_pose`` (PoseLink):  [Read-Write] Bones to use for driving parameters based on their transform

<a id="unreal.AnimNode_PoseDriver.__init__"></a>

#### __init__

```python
def __init__(blend_weight: float = 0.000000,
             internal_time_accumulator: float = 0.000000,
             pose_asset: PoseAsset = None,
             source_pose: PoseLink = []) -> None
```

<a id="unreal.AnimNode_PoseDriver.source_pose"></a>

#### source_pose

```python
@property
def source_pose() -> PoseLink
```

(PoseLink):  [Read-Write] Bones to use for driving parameters based on their transform

<a id="unreal.AnimNode_PoseDriver.source_pose"></a>

#### source_pose

```python
@source_pose.setter
def source_pose(value: PoseLink) -> None
```

<a id="unreal.AnimNode_OrientationDriver"></a>