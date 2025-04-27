## AnimNode_SequencePlayerBase Objects

```python
class AnimNode_SequencePlayerBase(AnimNode_AssetPlayerBase)
```

Sequence player node. Not instantiated directly, use FAnimNode_SequencePlayer or FAnimNode_SequencePlayer_Standalone

**C++ Source:**

- **Module**: Engine
- **File**: AnimNode_SequencePlayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_weight`` (float):  [Read-Write] Last encountered blendweight for this node
- ``internal_time_accumulator`` (float):  [Read-Write] Accumulated time used to reference the asset in this node

<a id="unreal.AnimNode_SequencePlayerBase.__init__"></a>

#### __init__

```python
def __init__(blend_weight: float = 0.000000,
             internal_time_accumulator: float = 0.000000) -> None
```

<a id="unreal.InputScaleBiasClampState"></a>