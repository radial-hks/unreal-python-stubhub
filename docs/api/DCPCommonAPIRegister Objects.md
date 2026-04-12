## DCPCommonAPIRegister Objects

```python
class DCPCommonAPIRegister(ApiClassBase)
```

DCPCommon APIRegister

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPCommonAPIRegister.h

<a id="unreal.DCPCommonAPIRegister.dcp_muti_pick_start"></a>

#### dcp\_muti\_pick\_start

```python
def dcp_muti_pick_start(in_params: ParamsBase) -> Optional[ResultBase]
```

x.dcp_muti_pick_start(in_params) -> ResultBase or None
APIs

Args:
    in_params (ParamsBase): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.DCPCommonAPIRegister.dcp_muti_pick_end"></a>

#### dcp\_muti\_pick\_end

```python
def dcp_muti_pick_end(in_params: ParamsBase) -> Optional[DCPMutiPickResult]
```

x.dcp_muti_pick_end(in_params) -> DCPMutiPickResult or None
Dcp Muti Pick End

Args:
    in_params (ParamsBase): 

Returns:
    DCPMutiPickResult or None: 

    out_result (DCPMutiPickResult):

<a id="unreal.DCPEffectSelectAPIRegister"></a>