## RangeAPI Objects

```python
class RangeAPI(ApiClassBase)
```

Range API

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: RangeAPI.h

<a id="unreal.RangeAPI.get_range_info"></a>

#### get\_range\_info

```python
def get_range_info(range_eid_parms: EidParams) -> Optional[GetRangeInfoRes]
```

x.get_range_info(range_eid_parms) -> GetRangeInfoRes or None
UFUNCTION(BlueprintCallable, Category = "Wdp Scene")
       bool GetRangeInfo(const FEidParams& RangeEidParms, FGetRangeParams& OutResult);

Args:
    range_eid_parms (EidParams): 

Returns:
    GetRangeInfoRes or None: 

    out_result (GetRangeInfoRes):

<a id="unreal.RasterAPI"></a>