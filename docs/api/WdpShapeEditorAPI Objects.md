## WdpShapeEditorAPI Objects

```python
class WdpShapeEditorAPI(StandardApiClassBase)
```

Wdp Shape Editor API

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpShapeEditorAPI.h

<a id="unreal.WdpShapeEditorAPI.update_shape_points"></a>

#### update\_shape\_points

```python
def update_shape_points(
        params: WdpUpdateShapePointsParams) -> Optional[ResultBase]
```

x.update_shape_points(params) -> ResultBase or None
Update Shape Points

Args:
    params (WdpUpdateShapePointsParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpShapeEditorAPI.range_pick_shape_points"></a>

#### range\_pick\_shape\_points

```python
def range_pick_shape_points(
        params: WdpRangePickShapePointsParams) -> Optional[ResultBase]
```

x.range_pick_shape_points(params) -> ResultBase or None
Range Pick Shape Points

Args:
    params (WdpRangePickShapePointsParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpVisualAPI"></a>