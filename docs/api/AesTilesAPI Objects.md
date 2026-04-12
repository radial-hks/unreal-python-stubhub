## AesTilesAPI Objects

```python
class AesTilesAPI(StandardApiClassBase)
```

Aes Tiles API

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: AesTilesAPI
- **File**: AesTilesAPI.h

<a id="unreal.AesTilesAPI.set_layers_visibility"></a>

#### set\_layers\_visibility

```python
def set_layers_visibility(
        params: AesTilesVisibilityLayerParam) -> Optional[ResultBase]
```

x.set_layers_visibility(params) -> ResultBase or None
Set Layers Visibility

Args:
    params (AesTilesVisibilityLayerParam): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.AesTilesAPI.set_layers_outline"></a>

#### set\_layers\_outline

```python
def set_layers_outline(
        params: AesTilesOutlineLayerParam) -> Optional[ResultBase]
```

x.set_layers_outline(params) -> ResultBase or None
Set Layers Outline

Args:
    params (AesTilesOutlineLayerParam): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.AesTilesAPI.set_layers_highlight"></a>

#### set\_layers\_highlight

```python
def set_layers_highlight(
        params: AesTilesHighlightLayerParam) -> Optional[ResultBase]
```

x.set_layers_highlight(params) -> ResultBase or None
Set Layers Highlight

Args:
    params (AesTilesHighlightLayerParam): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.AesTilesAPI.is_activated"></a>

#### is\_activated

```python
def is_activated(params: EidParams) -> Optional[IsActivatedResult]
```

x.is_activated(params) -> IsActivatedResult or None
Is Activated

Args:
    params (EidParams): 

Returns:
    IsActivatedResult or None: 

    out_result (IsActivatedResult):

<a id="unreal.AesTilesAPI.get_layers"></a>

#### get\_layers

```python
def get_layers(
        params: AesTilesVisualApiParamBase) -> Optional[AesTilesLayersResult]
```

x.get_layers(params) -> AesTilesLayersResult or None
Get Layers

Args:
    params (AesTilesVisualApiParamBase): 

Returns:
    AesTilesLayersResult or None: 

    out_result (AesTilesLayersResult):

<a id="unreal.AesTilesAPI.deactivate_aes_tiles"></a>

#### deactivate\_aes\_tiles

```python
def deactivate_aes_tiles(params: EidParams) -> Optional[ResultBase]
```

x.deactivate_aes_tiles(params) -> ResultBase or None
Deactivate Aes Tiles

Args:
    params (EidParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.AesTilesAPI.create_aes_tiles_entity_with_out_grpc"></a>

#### create\_aes\_tiles\_entity\_with\_out\_grpc

```python
def create_aes_tiles_entity_with_out_grpc(
    create_tile_params: CreateTile_WithOutGRPCParams
) -> Optional[CreateTileResult]
```

x.create_aes_tiles_entity_with_out_grpc(create_tile_params) -> CreateTileResult or None
Create Aes Tiles Entity with Out GRPC

Args:
    create_tile_params (CreateTile_WithOutGRPCParams): 

Returns:
    CreateTileResult or None: 

    out_result (CreateTileResult):

<a id="unreal.AesTilesAPI.activate_aes_tiles"></a>

#### activate\_aes\_tiles

```python
def activate_aes_tiles(params: EidParams) -> Optional[ResultBase]
```

x.activate_aes_tiles(params) -> ResultBase or None
APIs

Args:
    params (EidParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.AesTilesNodeAPI"></a>