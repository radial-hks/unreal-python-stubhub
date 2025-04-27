## WarpingEvaluationMode Objects

```python
class WarpingEvaluationMode(EnumBase)
```

Specifies the evaluation mode of an animation warping node

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: BoneControllerTypes.h

<a id="unreal.WarpingEvaluationMode.MANUAL"></a>

#### MANUAL

0: Animation warping evaluation parameters are driven by user settings.

<a id="unreal.WarpingEvaluationMode.GRAPH"></a>

#### GRAPH

1: Animation warping evaluation parameters are graph-driven. This means some
properties of the node are automatically computed using the accumulated
root motion delta contribution of the animation graph leading into it.

<a id="unreal.WarpingVectorMode"></a>