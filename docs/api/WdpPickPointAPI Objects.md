## WdpPickPointAPI Objects

```python
class WdpPickPointAPI(StandardApiClassBase)
```

Wdp Pick Point API

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpPickPointAPI.h

<a id="unreal.WdpPickPointAPI.start_pick_point"></a>

#### start\_pick\_point

```python
def start_pick_point(params: WdpStartPickPointParams) -> Optional[ResultBase]
```

x.start_pick_point(params) -> ResultBase or None
APIs

Args:
    params (WdpStartPickPointParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpPickPointAPI.get_picked_points"></a>

#### get\_picked\_points

```python
def get_picked_points(
        params: WdpGetPickedPointsParams
) -> Optional[WdpGetPickedPointsResult]
```

x.get_picked_points(params) -> WdpGetPickedPointsResult or None
Get Picked Points

Args:
    params (WdpGetPickedPointsParams): 

Returns:
    WdpGetPickedPointsResult or None: 

    out_result (WdpGetPickedPointsResult):

<a id="unreal.WdpPickPointAPI.end_pick_point"></a>

#### end\_pick\_point

```python
def end_pick_point(params: ParamsBase) -> Optional[ResultBase]
```

x.end_pick_point(params) -> ResultBase or None
End Pick Point

Args:
    params (ParamsBase): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpPickPolylineAPI"></a>