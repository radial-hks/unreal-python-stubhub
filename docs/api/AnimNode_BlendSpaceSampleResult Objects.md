## AnimNode_BlendSpaceSampleResult Objects

```python
class AnimNode_BlendSpaceSampleResult(AnimNode_Root)
```

Root node of a blend space sample (sink node).
We dont use AnimNode_Root to let us distinguish these nodes in the property list at link time.

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_BlendSpaceSampleResult.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``group`` (Name):  [Read-Write]
  deprecated: Please, use LayerGroup
- ``result`` (PoseLink):  [Read-Write]

<a id="unreal.AnimNode_BlendSpaceSampleResult.__init__"></a>

#### __init__

```python
def __init__(result: PoseLink = []) -> None
```

<a id="unreal.AnimNode_SkeletalControlBase"></a>