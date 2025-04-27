## AnimNode_SequenceEvaluatorBase Objects

```python
class AnimNode_SequenceEvaluatorBase(AnimNode_AssetPlayerBase)
```

Abstract base class. Evaluates a point in an anim sequence, using a specific time input rather than advancing time internally.
Typically the playback position of the animation for this node will represent something other than time, like jump height.
This node will not trigger any notifies present in the associated sequence.

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_SequenceEvaluator.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_weight`` (float):  [Read-Write] Last encountered blendweight for this node
- ``internal_time_accumulator`` (float):  [Read-Write] Accumulated time used to reference the asset in this node

<a id="unreal.AnimNode_SequenceEvaluatorBase.__init__"></a>

#### __init__

```python
def __init__(blend_weight: float = 0.000000,
             internal_time_accumulator: float = 0.000000) -> None
```

<a id="unreal.AnimNode_SequenceEvaluator"></a>