## DCPModelAPIRegister Objects

```python
class DCPModelAPIRegister(ApiClassBase)
```

DCPModel APIRegister

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPModelAPIRegister.h

<a id="unreal.DCPModelAPIRegister.dcp_set_model_visibility"></a>

#### dcp\_set\_model\_visibility

```python
def dcp_set_model_visibility(
        in_params: DCModelVisibilityParams) -> Optional[ResultBase]
```

x.dcp_set_model_visibility(in_params) -> ResultBase or None
Dcp Set Model Visibility

Args:
    in_params (DCModelVisibilityParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.DCPModelAPIRegister.dcp_model_focus"></a>

#### dcp\_model\_focus

```python
def dcp_model_focus(in_params: EidParams) -> Optional[ResultBase]
```

x.dcp_model_focus(in_params) -> ResultBase or None
Dcp Model Focus

Args:
    in_params (EidParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.DCPModelAPIRegister.dcp_model_active"></a>

#### dcp\_model\_active

```python
def dcp_model_active(in_params: DCPModelActiveParams) -> Optional[ResultBase]
```

x.dcp_model_active(in_params) -> ResultBase or None
APIs

Args:
    in_params (DCPModelActiveParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.DCPModelAPIRegister.dcp_get_model_actived"></a>

#### dcp\_get\_model\_actived

```python
def dcp_get_model_actived(in_params: ParamsBase) -> Optional[EidResult]
```

x.dcp_get_model_actived(in_params) -> EidResult or None
Dcp Get Model Actived

Args:
    in_params (ParamsBase): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.DCPNodeAPIRegister"></a>