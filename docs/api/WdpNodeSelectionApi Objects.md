## WdpNodeSelectionApi Objects

```python
class WdpNodeSelectionApi(StandardApiClassBase)
```

Wdp Node Selection Api

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpNodeSelectionApi.h

<a id="unreal.WdpNodeSelectionApi.remove"></a>

#### remove

```python
def remove(params: NodeSelectionParams) -> Optional[EidResult]
```

x.remove(params) -> EidResult or None
Remove

Args:
    params (NodeSelectionParams): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.WdpNodeSelectionApi.draw_selection"></a>

#### draw\_selection

```python
def draw_selection(params: ParamsBase) -> Optional[ResultBase]
```

x.draw_selection(params) -> ResultBase or None
Draw Selection

Args:
    params (ParamsBase): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpNodeSelectionApi.clear_selection"></a>

#### clear\_selection

```python
def clear_selection(params: ParamsBase) -> Optional[ResultBase]
```

x.clear_selection(params) -> ResultBase or None
Clear Selection

Args:
    params (ParamsBase): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpNodeSelectionApi.add"></a>

#### add

```python
def add(params: NodeSelectionParams) -> Optional[EidResult]
```

x.add(params) -> EidResult or None
Add

Args:
    params (NodeSelectionParams): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.WdpPickerAPI"></a>