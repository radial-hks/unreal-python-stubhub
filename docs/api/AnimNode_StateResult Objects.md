## AnimNode_StateResult Objects

```python
class AnimNode_StateResult(AnimNode_Root)
```

Root node of an state machine state (sink node).
We dont use AnimNode_Root to let us distinguish these nodes in the property list at link time.

**C++ Source:**

- **Module**: Engine
- **File**: AnimNode_StateResult.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``group`` (Name):  [Read-Write]
  deprecated: Please, use LayerGroup
- ``result`` (PoseLink):  [Read-Write]

<a id="unreal.AnimNode_StateResult.__init__"></a>

#### __init__

```python
def __init__(result: PoseLink = []) -> None
```

<a id="unreal.AnimNode_TransitionPoseEvaluator"></a>