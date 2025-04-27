## AnimNode_PoseByName Objects

```python
class AnimNode_PoseByName(AnimNode_PoseHandler)
```

Evaluates a point in an anim sequence, using a specific time input rather than advancing time internally.
Typically the playback position of the animation for this node will represent something other than time, like jump height.
This node will not trigger any notifies present in the associated sequence.

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_PoseByName.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_weight`` (float):  [Read-Write] Last encountered blendweight for this node
- ``internal_time_accumulator`` (float):  [Read-Write] Accumulated time used to reference the asset in this node
- ``pose_asset`` (PoseAsset):  [Read-Write] The animation sequence asset to evaluate
- ``pose_name`` (Name):  [Read-Write]
- ``pose_weight`` (float):  [Read-Write]

<a id="unreal.AnimNode_PoseByName.__init__"></a>

#### __init__

```python
def __init__(blend_weight: float = 0.000000,
             internal_time_accumulator: float = 0.000000,
             pose_asset: PoseAsset = None,
             pose_name: Name = "None",
             pose_weight: float = 0.000000) -> None
```

<a id="unreal.AnimNode_PoseByName.pose_name"></a>

#### pose_name

```python
@property
def pose_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.AnimNode_PoseByName.pose_name"></a>

#### pose_name

```python
@pose_name.setter
def pose_name(value: Name) -> None
```

<a id="unreal.AnimNode_PoseByName.pose_weight"></a>

#### pose_weight

```python
@property
def pose_weight() -> float
```

(float):  [Read-Write]

<a id="unreal.AnimNode_PoseByName.pose_weight"></a>

#### pose_weight

```python
@pose_weight.setter
def pose_weight(value: float) -> None
```

<a id="unreal.AnimNode_PoseDriver"></a>