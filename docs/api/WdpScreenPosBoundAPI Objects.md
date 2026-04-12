## WdpScreenPosBoundAPI Objects

```python
class WdpScreenPosBoundAPI(StandardApiClassBase)
```

Wdp Screen Pos Bound API

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpScreenPosBoundAPI.h

<a id="unreal.WdpScreenPosBoundAPI.update_screen_pos_bound"></a>

#### update\_screen\_pos\_bound

```python
def update_screen_pos_bound(
    params: WDPUpdateScreenPosBoundParams
) -> Optional[WDPUpdateScreenPosBoundResult]
```

x.update_screen_pos_bound(params) -> WDPUpdateScreenPosBoundResult or None
Update Screen Pos Bound

Args:
    params (WDPUpdateScreenPosBoundParams): 

Returns:
    WDPUpdateScreenPosBoundResult or None: 

    out_result (WDPUpdateScreenPosBoundResult):

<a id="unreal.WdpScreenPosBoundAPI.remove_screen_pos_bound"></a>

#### remove\_screen\_pos\_bound

```python
def remove_screen_pos_bound(
        params: WDPScreenPosBoundRemoveParams) -> Optional[ResultBase]
```

x.remove_screen_pos_bound(params) -> ResultBase or None
Remove Screen Pos Bound

Args:
    params (WDPScreenPosBoundRemoveParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpScreenPosBoundAPI.add_screen_pos_bound"></a>

#### add\_screen\_pos\_bound

```python
def add_screen_pos_bound(
    params: WDPScreenPosBoundAddParams
) -> Optional[WDPScreenPosBoundAddResult]
```

x.add_screen_pos_bound(params) -> WDPScreenPosBoundAddResult or None
APIs

Args:
    params (WDPScreenPosBoundAddParams): 

Returns:
    WDPScreenPosBoundAddResult or None: 

    out_result (WDPScreenPosBoundAddResult):

<a id="unreal.WdpShapeEditorAPI"></a>