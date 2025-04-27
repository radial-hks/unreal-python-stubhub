## MovieGraphConditionGroupQueryOpType Objects

```python
class MovieGraphConditionGroupQueryOpType(EnumBase)
```

Operation types available on condition group queries.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphRenderLayerSubsystem.h

<a id="unreal.MovieGraphConditionGroupQueryOpType.ADD"></a>

#### ADD

0: Adds the results of the query to the results from the previous query (if any).

<a id="unreal.MovieGraphConditionGroupQueryOpType.SUBTRACT"></a>

#### SUBTRACT

1: Removes the results of the query from the results of the previous query (if any). Any items in this query result that aren't also found in the previous query result will be ignored.

<a id="unreal.MovieGraphConditionGroupQueryOpType.AND"></a>

#### AND

2: Replaces the results of the previous queries with only the items that exist in both those queries, and this query result. Intersecting with a query which returns nothing will create an empty query result.

<a id="unreal.MoviePipelineEncodeQuality"></a>