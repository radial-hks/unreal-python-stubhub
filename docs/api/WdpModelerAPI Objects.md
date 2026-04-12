## WdpModelerAPI Objects

```python
class WdpModelerAPI(StandardApiClassBase)
```

Wdp Modeler API

**C++ Source:**

- **Plugin**: AesRuntimeModeler
- **Module**: RuntimeModelerAPI
- **File**: WdpModelerAPI.h

<a id="unreal.WdpModelerAPI.update_region_name"></a>

#### update\_region\_name

```python
def update_region_name(
        params: WdpModelerRegionNameParams) -> Optional[ResultBase]
```

x.update_region_name(params) -> ResultBase or None
Update Region Name

Args:
    params (WdpModelerRegionNameParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpModelerAPI.toggle_region"></a>

#### toggle\_region

```python
def toggle_region(
        params: WdpModelerRegionSwitchParams) -> Optional[ResultBase]
```

x.toggle_region(params) -> ResultBase or None
Toggle Region

Args:
    params (WdpModelerRegionSwitchParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpModelerAPI.remove_region"></a>

#### remove\_region

```python
def remove_region(params: WdpModelerRegionIndexParams) -> Optional[ResultBase]
```

x.remove_region(params) -> ResultBase or None
regions

Args:
    params (WdpModelerRegionIndexParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpModelerAPI.query_region"></a>

#### query\_region

```python
def query_region(params: EidParams) -> Optional[WdpModelerRegionResult]
```

x.query_region(params) -> WdpModelerRegionResult or None
Query Region

Args:
    params (EidParams): 

Returns:
    WdpModelerRegionResult or None: 

    out_result (WdpModelerRegionResult):

<a id="unreal.WdpModelerAPI.generate_modeler_water"></a>

#### generate\_modeler\_water

```python
def generate_modeler_water(
        params: WdpModelerWaterDataParams) -> Optional[ResultBase]
```

x.generate_modeler_water(params) -> ResultBase or None
Generate Modeler Water

Args:
    params (WdpModelerWaterDataParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.BatchRangeEntityAtom"></a>