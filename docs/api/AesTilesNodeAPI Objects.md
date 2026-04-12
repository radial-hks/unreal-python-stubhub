## AesTilesNodeAPI Objects

```python
class AesTilesNodeAPI(StandardApiClassBase)
```

Aes Tiles Node API

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: AesTilesAPI
- **File**: AesTilesNodeAPI.h

<a id="unreal.AesTilesNodeAPI.update_visibility_group"></a>

#### update\_visibility\_group

```python
def update_visibility_group(
        params: AesTilesVisibilityGroupUpdateParam) -> Optional[ResultBase]
```

x.update_visibility_group(params) -> ResultBase or None
Update Visibility Group

Args:
    params (AesTilesVisibilityGroupUpdateParam): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.AesTilesNodeAPI.set_nodes_visibility"></a>

#### set\_nodes\_visibility

```python
def set_nodes_visibility(
        params: AesTilesVisibilityNodesParam) -> Optional[ResultBase]
```

x.set_nodes_visibility(params) -> ResultBase or None
Visibility nodes

Args:
    params (AesTilesVisibilityNodesParam): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.AesTilesNodeAPI.set_nodes_outline"></a>

#### set\_nodes\_outline

```python
def set_nodes_outline(
        params: AesTilesOutlineNodeIdParam) -> Optional[ResultBase]
```

x.set_nodes_outline(params) -> ResultBase or None
Outline

Args:
    params (AesTilesOutlineNodeIdParam): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.AesTilesNodeAPI.set_nodes_highlight"></a>

#### set\_nodes\_highlight

```python
def set_nodes_highlight(
        params: AesTilesHighlightNodeIdParam) -> Optional[ResultBase]
```

x.set_nodes_highlight(params) -> ResultBase or None
Highlight

Args:
    params (AesTilesHighlightNodeIdParam): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.AesTilesNodeAPI.remove_visibility_group"></a>

#### remove\_visibility\_group

```python
def remove_visibility_group(
        params: AesTilesVisibilityGroupRemoveParam) -> Optional[ResultBase]
```

x.remove_visibility_group(params) -> ResultBase or None
Remove Visibility Group

Args:
    params (AesTilesVisibilityGroupRemoveParam): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.AesTilesNodeAPI.get_visibility_group"></a>

#### get\_visibility\_group

```python
def get_visibility_group(
    params: AesTilesVisualApiParamBase
) -> Optional[AesTilesVisibilityGroupResult]
```

x.get_visibility_group(params) -> AesTilesVisibilityGroupResult or None
Get Visibility Group

Args:
    params (AesTilesVisualApiParamBase): 

Returns:
    AesTilesVisibilityGroupResult or None: 

    out_result (AesTilesVisibilityGroupResult):

<a id="unreal.AesTilesNodeAPI.add_visibility_group"></a>

#### add\_visibility\_group

```python
def add_visibility_group(
        params: AesTilesVisibilityGroupAddParam) -> Optional[ResultBase]
```

x.add_visibility_group(params) -> ResultBase or None
Visibility nodes group CRUD

Args:
    params (AesTilesVisibilityGroupAddParam): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.EarthEditorAPI"></a>