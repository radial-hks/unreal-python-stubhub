## DCPNodeAPIRegister Objects

```python
class DCPNodeAPIRegister(ApiClassBase)
```

DCPNode APIRegister

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPNodeAPIRegister.h

<a id="unreal.DCPNodeAPIRegister.dcp_set_other_nodes_visibility"></a>

#### dcp\_set\_other\_nodes\_visibility

```python
def dcp_set_other_nodes_visibility(
        in_params: SetOtherNodesVisibilityParam) -> Optional[ResultBase]
```

x.dcp_set_other_nodes_visibility(in_params) -> ResultBase or None
Dcp Set Other Nodes Visibility

Args:
    in_params (SetOtherNodesVisibilityParam): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.DCPNodeAPIRegister.dcp_set_node_visibility"></a>

#### dcp\_set\_node\_visibility

```python
def dcp_set_node_visibility(
        in_params: DCPNodeVisibilityParam) -> Optional[ResultBase]
```

x.dcp_set_node_visibility(in_params) -> ResultBase or None
Dcp Set Node Visibility

Args:
    in_params (DCPNodeVisibilityParam): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.DCPNodeAPIRegister.dcp_set_node_location"></a>

#### dcp\_set\_node\_location

```python
def dcp_set_node_location(
        params: DCPNodeLocationParam) -> Optional[ResultBase]
```

x.dcp_set_node_location(params) -> ResultBase or None
Dcp Set Node Location

Args:
    params (DCPNodeLocationParam): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.DCPNodeAPIRegister.dcp_set_node_highlight"></a>

#### dcp\_set\_node\_highlight

```python
def dcp_set_node_highlight(
        in_params: DCPNodeHightLightParam) -> Optional[ResultBase]
```

x.dcp_set_node_highlight(in_params) -> ResultBase or None
UFUNCTION(BlueprintCallable, Category = "DCP|API|Node")
       bool DcpSetNodeVisibilityOnly(const FDCPNodeVisibilityParam& inParams, FResultBase& OutResult);

Args:
    in_params (DCPNodeHightLightParam): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.DCPNodeAPIRegister.dcp_set_highlight_style"></a>

#### dcp\_set\_highlight\_style

```python
def dcp_set_highlight_style(
        in_params: DCPNodeHighLightStyleParam) -> Optional[ResultBase]
```

x.dcp_set_highlight_style(in_params) -> ResultBase or None
Dcp Set Highlight Style

Args:
    in_params (DCPNodeHighLightStyleParam): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.DCPNodeAPIRegister.dcp_room_high_light"></a>

#### dcp\_room\_high\_light

```python
def dcp_room_high_light(
        in_params: DCPRoomHighLightParam) -> Optional[ResultBase]
```

x.dcp_room_high_light(in_params) -> ResultBase or None
Dcp Room High Light

Args:
    in_params (DCPRoomHighLightParam): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.DCPNodeAPIRegister.dcp_room_focus"></a>

#### dcp\_room\_focus

```python
def dcp_room_focus(in_params: DCPRoomFocusParam) -> Optional[ResultBase]
```

x.dcp_room_focus(in_params) -> ResultBase or None
Dcp Room Focus

Args:
    in_params (DCPRoomFocusParam): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.DCPNodeAPIRegister.dcp_node_show_all"></a>

#### dcp\_node\_show\_all

```python
def dcp_node_show_all(in_params: ParamsBase) -> Optional[ResultBase]
```

x.dcp_node_show_all(in_params) -> ResultBase or None
Dcp Node Show All

Args:
    in_params (ParamsBase): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.DCPNodeAPIRegister.dcp_node_isolate"></a>

#### dcp\_node\_isolate

```python
def dcp_node_isolate(in_params: DCPNodeBaseParam) -> Optional[ResultBase]
```

x.dcp_node_isolate(in_params) -> ResultBase or None
Dcp Node Isolate

Args:
    in_params (DCPNodeBaseParam): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.DCPNodeAPIRegister.dcp_node_focus"></a>

#### dcp\_node\_focus

```python
def dcp_node_focus(in_params: DCPNodeFocusParam) -> Optional[ResultBase]
```

x.dcp_node_focus(in_params) -> ResultBase or None
Dcp Node Focus

Args:
    in_params (DCPNodeFocusParam): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.DCPNodeAPIRegister.dcp_get_node_transform"></a>

#### dcp\_get\_node\_transform

```python
def dcp_get_node_transform(
        in_params: GetDCPNodeTransformParam
) -> Optional[DCPNodeTransformResult]
```

x.dcp_get_node_transform(in_params) -> DCPNodeTransformResult or None
Dcp Get Node Transform

Args:
    in_params (GetDCPNodeTransformParam): 

Returns:
    DCPNodeTransformResult or None: 

    out_result (DCPNodeTransformResult):

<a id="unreal.DCPNodeAPIRegister.dcp_get_node_info"></a>

#### dcp\_get\_node\_info

```python
def dcp_get_node_info(
        in_params: DCPNodeBaseParam) -> Optional[DCPNodePropertyResult]
```

x.dcp_get_node_info(in_params) -> DCPNodePropertyResult or None
Dcp Get Node Info

Args:
    in_params (DCPNodeBaseParam): 

Returns:
    DCPNodePropertyResult or None: 

    out_result (DCPNodePropertyResult):

<a id="unreal.DCPNodeAPIRegister.dcp_get_model_tree"></a>

#### dcp\_get\_model\_tree

```python
def dcp_get_model_tree(in_params: ParamsBase) -> Optional[DCPNodeInfoResult]
```

x.dcp_get_model_tree(in_params) -> DCPNodeInfoResult or None
APIs

Args:
    in_params (ParamsBase): 

Returns:
    DCPNodeInfoResult or None: 

    out_result (DCPNodeInfoResult):

<a id="unreal.DCPNodeAPIRegister.dcp_get_model_sub_tree"></a>

#### dcp\_get\_model\_sub\_tree

```python
def dcp_get_model_sub_tree(
        in_params: DCPNodeLevelParam) -> Optional[DCPNodeInfoResult]
```

x.dcp_get_model_sub_tree(in_params) -> DCPNodeInfoResult or None
Dcp Get Model Sub Tree

Args:
    in_params (DCPNodeLevelParam): 

Returns:
    DCPNodeInfoResult or None: 

    out_result (DCPNodeInfoResult):

<a id="unreal.DCPNodeAPIRegister.dcp_get_highlight_style"></a>

#### dcp\_get\_highlight\_style

```python
def dcp_get_highlight_style(
        in_params: ParamsBase) -> Optional[DCPNodeHighLightStyleGetParam]
```

x.dcp_get_highlight_style(in_params) -> DCPNodeHighLightStyleGetParam or None
Dcp Get Highlight Style

Args:
    in_params (ParamsBase): 

Returns:
    DCPNodeHighLightStyleGetParam or None: 

    out_result (DCPNodeHighLightStyleGetParam):

<a id="unreal.DCPNodeAPIRegister.dcp_clear_room_high_light"></a>

#### dcp\_clear\_room\_high\_light

```python
def dcp_clear_room_high_light(in_params: ParamsBase) -> Optional[ResultBase]
```

x.dcp_clear_room_high_light(in_params) -> ResultBase or None
Dcp Clear Room High Light

Args:
    in_params (ParamsBase): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.DCPNodeAPIRegister.dcp_clear_node_highlight"></a>

#### dcp\_clear\_node\_highlight

```python
def dcp_clear_node_highlight(in_params: ParamsBase) -> Optional[ResultBase]
```

x.dcp_clear_node_highlight(in_params) -> ResultBase or None
Dcp Clear Node Highlight

Args:
    in_params (ParamsBase): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.DCPSectionAPIRegister"></a>