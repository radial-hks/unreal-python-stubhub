## AnimNode_PoseBlendNode Objects

```python
class AnimNode_PoseBlendNode(AnimNode_PoseHandler)
```

Evaluates a point in an anim sequence, using a specific time input rather than advancing time internally.
Typically the playback position of the animation for this node will represent something other than time, like jump height.
This node will not trigger any notifies present in the associated sequence.

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_PoseBlendNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_option`` (AlphaBlendOption):  [Read-Write] Type of blending used (Linear, Cubic, etc.)
- ``blend_weight`` (float):  [Read-Write] Last encountered blendweight for this node
- ``custom_curve`` (CurveFloat):  [Read-Write] If you're using Custom BlendOption, you can specify curve
- ``internal_time_accumulator`` (float):  [Read-Write] Accumulated time used to reference the asset in this node
- ``pose_asset`` (PoseAsset):  [Read-Write] The animation sequence asset to evaluate
- ``source_pose`` (PoseLink):  [Read-Write]

<a id="unreal.AnimNode_PoseBlendNode.__init__"></a>

#### __init__

```python
def __init__(blend_weight: float = 0.000000,
             internal_time_accumulator: float = 0.000000,
             pose_asset: PoseAsset = None,
             source_pose: PoseLink = []) -> None
```

<a id="unreal.AnimNode_PoseBlendNode.source_pose"></a>

#### source_pose

```python
@property
def source_pose() -> PoseLink
```

(PoseLink):  [Read-Write]

<a id="unreal.AnimNode_PoseBlendNode.source_pose"></a>

#### source_pose

```python
@source_pose.setter
def source_pose(value: PoseLink) -> None
```

<a id="unreal.AnimNode_PoseByName"></a>