## WdpActionManagerAPI Objects

```python
class WdpActionManagerAPI(StandardApiClassBase)
```

Wdp Action Manager API

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpActionManagerAPI.h

<a id="unreal.WdpActionManagerAPI.update_current_action_params"></a>

#### update\_current\_action\_params

```python
def update_current_action_params(
        params: WdpStartActionParams) -> Optional[ResultBase]
```

x.update_current_action_params(params) -> ResultBase or None
Update Current Action Params

Args:
    params (WdpStartActionParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpActionManagerAPI.run_action"></a>

#### run\_action

```python
def run_action(params: WdpStartActionParams) -> Optional[ResultBase]
```

x.run_action(params) -> ResultBase or None
APIs

Args:
    params (WdpStartActionParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpActionManagerAPI.get_current_action"></a>

#### get\_current\_action

```python
def get_current_action(
        params: ParamsBase) -> Optional[WdpGetCurrentActionResult]
```

x.get_current_action(params) -> WdpGetCurrentActionResult or None
Get Current Action

Args:
    params (ParamsBase): 

Returns:
    WdpGetCurrentActionResult or None: 

    out_result (WdpGetCurrentActionResult):

<a id="unreal.WdpActionManagerAPI.end_current_action"></a>

#### end\_current\_action

```python
def end_current_action(params: WdpEndActionParams) -> Optional[ResultBase]
```

x.end_current_action(params) -> ResultBase or None
End Current Action

Args:
    params (WdpEndActionParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpActionSettingsAPI"></a>