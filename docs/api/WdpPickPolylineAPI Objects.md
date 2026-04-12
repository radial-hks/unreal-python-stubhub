## WdpPickPolylineAPI Objects

```python
class WdpPickPolylineAPI(StandardApiClassBase)
```

Wdp Pick Polyline API

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpPickPolylineAPI.h

<a id="unreal.WdpPickPolylineAPI.start_pick_polyline"></a>

#### start\_pick\_polyline

```python
def start_pick_polyline(params: ParamsBase) -> Optional[ResultBase]
```

x.start_pick_polyline(params) -> ResultBase or None
Start Pick Polyline

Args:
    params (ParamsBase): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpPickPolylineAPI.get_picked_polylines"></a>

#### get\_picked\_polylines

```python
def get_picked_polylines(
    params: WdpGetPickedPolylinesParams
) -> Optional[WdpGetPickedPolylinesResult]
```

x.get_picked_polylines(params) -> WdpGetPickedPolylinesResult or None
Get Picked Polylines

Args:
    params (WdpGetPickedPolylinesParams): 

Returns:
    WdpGetPickedPolylinesResult or None: 

    out_result (WdpGetPickedPolylinesResult):

<a id="unreal.WdpPickPolylineAPI.end_pick_polyline"></a>

#### end\_pick\_polyline

```python
def end_pick_polyline(params: ParamsBase) -> Optional[ResultBase]
```

x.end_pick_polyline(params) -> ResultBase or None
End Pick Polyline

Args:
    params (ParamsBase): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpSelectionApi"></a>