## AnimNode_RigLogic Objects

```python
class AnimNode_RigLogic(AnimNode_Base)
```

Anim Node Rig Logic

**C++ Source:**

- **Plugin**: RigLogic
- **Module**: RigLogicModule
- **File**: AnimNode_RigLogic.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``anim_sequence`` (PoseLink):  [Read-Write]
- ``lod_threshold`` (int32):  [Read-Write] * Max LOD level that post-process AnimBPs are evaluated.
  * For example if you have the threshold set to 2, it will evaluate until including LOD 2 (based on 0 index). In case the LOD level gets set to 3, it will stop evaluating the post-process AnimBP.
  * Setting it to -1 will always evaluate it and disable LODing.

<a id="unreal.AnimNode_RigLogic.__init__"></a>

#### __init__

```python
def __init__(anim_sequence: PoseLink = []) -> None
```

<a id="unreal.AnimNode_RigLogic.anim_sequence"></a>

#### anim_sequence

```python
@property
def anim_sequence() -> PoseLink
```

(PoseLink):  [Read-Write]

<a id="unreal.AnimNode_RigLogic.anim_sequence"></a>

#### anim_sequence

```python
@anim_sequence.setter
def anim_sequence(value: PoseLink) -> None
```

<a id="unreal.RigUnit_RigLogic"></a>