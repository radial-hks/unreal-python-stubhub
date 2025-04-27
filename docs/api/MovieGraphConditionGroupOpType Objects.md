## MovieGraphConditionGroupOpType Objects

```python
class MovieGraphConditionGroupOpType(EnumBase)
```

Operation types available on condition groups.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphRenderLayerSubsystem.h

<a id="unreal.MovieGraphConditionGroupOpType.ADD"></a>

#### ADD

0: Adds the contents of the condition group to the results from the previous condition group (if any).

<a id="unreal.MovieGraphConditionGroupOpType.SUBTRACT"></a>

#### SUBTRACT

1: Removes the contents of the condition group from the result of the previous condition group (if any). Any items in this condition group that aren't also found in the previous condition group will be ignored.

<a id="unreal.MovieGraphConditionGroupOpType.AND"></a>

#### AND

2: Replaces the results of the previous condition group(s) with only the elements that exist in both that group, and this group. Intersecting with an empty condition group will result in an empty condition group.

<a id="unreal.MovieGraphConditionGroupQueryOpType"></a>