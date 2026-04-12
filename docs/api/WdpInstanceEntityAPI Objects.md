## WdpInstanceEntityAPI Objects

```python
class WdpInstanceEntityAPI(StandardApiClassBase)
```

Wdp Instance Entity API

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpInstanceEntityAPI.h

<a id="unreal.WdpInstanceEntityAPI.set_nodes_transform"></a>

#### set\_nodes\_transform

```python
def set_nodes_transform(params: NodesTrParams) -> Optional[ResultBase]
```

x.set_nodes_transform(params) -> ResultBase or None
Set Nodes Transform

Args:
    params (NodesTrParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpInstanceEntityAPI.set_components_transform"></a>

#### set\_components\_transform

```python
def set_components_transform(
        params: ComponentTrParams) -> Optional[ResultBase]
```

x.set_components_transform(params) -> ResultBase or None
Set Components Transform

Args:
    params (ComponentTrParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpInstanceEntityAPI.outline_components"></a>

#### outline\_components

```python
def outline_components(params: OutlineComponentParams) -> Optional[ResultBase]
```

x.outline_components(params) -> ResultBase or None
APIs

Args:
    params (OutlineComponentParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpInstanceEntityAPI.focus_components"></a>

#### focus\_components

```python
def focus_components(params: ComponentNameParams) -> Optional[ResultBase]
```

x.focus_components(params) -> ResultBase or None
Focus Components

Args:
    params (ComponentNameParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpInstanceEntityAPI.delete_nodes"></a>

#### delete\_nodes

```python
def delete_nodes(params: FocusToNodesParams) -> Optional[ResultBase]
```

x.delete_nodes(params) -> ResultBase or None
Delete Nodes

Args:
    params (FocusToNodesParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpInstanceEntityAPI.delete_components"></a>

#### delete\_components

```python
def delete_components(params: ComponentNameParams) -> Optional[ResultBase]
```

x.delete_components(params) -> ResultBase or None
Delete Components

Args:
    params (ComponentNameParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpLogAPI"></a>