## WdpVisualAPI Objects

```python
class WdpVisualAPI(StandardApiClassBase)
```

Wdp Visual API

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpVisualAPI.h

<a id="unreal.WdpVisualAPI.set_visual_color_style"></a>

#### set\_visual\_color\_style

```python
def set_visual_color_style(
        params: WdpVisualColorStyleParams) -> Optional[ResultBase]
```

x.set_visual_color_style(params) -> ResultBase or None
Set Visual Color Style

Args:
    params (WdpVisualColorStyleParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpVisualAPI.set_outline_thickness"></a>

#### set\_outline\_thickness

```python
def set_outline_thickness(
        params: WdpOutlineThicknessParams) -> Optional[ResultBase]
```

x.set_outline_thickness(params) -> ResultBase or None
Visual Setting

Args:
    params (WdpOutlineThicknessParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpVisualAPI.set_entity_outline"></a>

#### set\_entity\_outline

```python
def set_entity_outline(params: VisualOutlineParams) -> Optional[ResultBase]
```

x.set_entity_outline(params) -> ResultBase or None
Model

Args:
    params (VisualOutlineParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpVisualAPI.set_entity_highlight"></a>

#### set\_entity\_highlight

```python
def set_entity_highlight(
        params: VisualHighlightParams) -> Optional[ResultBase]
```

x.set_entity_highlight(params) -> ResultBase or None
Set Entity Highlight

Args:
    params (VisualHighlightParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpVisualAPI.get_visual_color_style"></a>

#### get\_visual\_color\_style

```python
def get_visual_color_style(
        params: ParamsBase) -> Optional[WdpVisualColorStyleResult]
```

x.get_visual_color_style(params) -> WdpVisualColorStyleResult or None
Get Visual Color Style

Args:
    params (ParamsBase): 

Returns:
    WdpVisualColorStyleResult or None: 

    out_result (WdpVisualColorStyleResult):

<a id="unreal.WdpVisualAPI.get_outline_thickness"></a>

#### get\_outline\_thickness

```python
def get_outline_thickness(
        params: ParamsBase) -> Optional[WdpOutlineThicknessResult]
```

x.get_outline_thickness(params) -> WdpOutlineThicknessResult or None
Get Outline Thickness

Args:
    params (ParamsBase): 

Returns:
    WdpOutlineThicknessResult or None: 

    out_result (WdpOutlineThicknessResult):

<a id="unreal.WdpApiDescriptorTool"></a>