## DCPSectionAPIRegister Objects

```python
class DCPSectionAPIRegister(ApiClassBase)
```

DCPSection APIRegister

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPSectionAPIRegister.h

<a id="unreal.DCPSectionAPIRegister.start_model_section"></a>

#### start\_model\_section

```python
def start_model_section(in_params: DCPSectionParam) -> Optional[EidResult]
```

x.start_model_section(in_params) -> EidResult or None
APIs

Args:
    in_params (DCPSectionParam): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.DCPSectionAPIRegister.reset_model_section"></a>

#### reset\_model\_section

```python
def reset_model_section(in_params: EidParams) -> Optional[ResultBase]
```

x.reset_model_section(in_params) -> ResultBase or None
Reset Model Section

Args:
    in_params (EidParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.DCPSectionAPIRegister.end_model_section"></a>

#### end\_model\_section

```python
def end_model_section(in_params: EidParams) -> Optional[ResultBase]
```

x.end_model_section(in_params) -> ResultBase or None
End Model Section

Args:
    in_params (EidParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.DCPSwitchAPIRegister"></a>