## CustomDepthParameters Objects

```python
class CustomDepthParameters(StructBase)
```

Custom Depth Parameters

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CustomDepthParameters.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``custom_depth_stencil_value`` (int32):  [Read-Write] Optionally write this 0-255 value to the stencil buffer in CustomDepth
  pass (Requires project setting or r.CustomDepth == 3)
- ``custom_depth_stencil_write_mask`` (RendererStencilMask):  [Read-Write] Mask used for stencil buffer writes.
- ``render_custom_depth`` (bool):  [Read-Write] If true, this component will be rendered in the CustomDepth pass (usually
  used for outlines)

<a id="unreal.CustomDepthParameters.__init__"></a>

#### \_\_init\_\_

```python
def __init__(render_custom_depth: bool = False,
             custom_depth_stencil_write_mask:
             RendererStencilMask = RendererStencilMask.ERSM_DEFAULT,
             custom_depth_stencil_value: int = 0) -> None
```

<a id="unreal.CustomDepthParameters.render_custom_depth"></a>

#### render\_custom\_depth

```python
@property
def render_custom_depth() -> bool
```

(bool):  [Read-Only] If true, this component will be rendered in the CustomDepth pass (usually
used for outlines)

<a id="unreal.CustomDepthParameters.custom_depth_stencil_write_mask"></a>

#### custom\_depth\_stencil\_write\_mask

```python
@property
def custom_depth_stencil_write_mask() -> RendererStencilMask
```

(RendererStencilMask):  [Read-Only] Mask used for stencil buffer writes.

<a id="unreal.CustomDepthParameters.custom_depth_stencil_value"></a>

#### custom\_depth\_stencil\_value

```python
@property
def custom_depth_stencil_value() -> int
```

(int32):  [Read-Only] Optionally write this 0-255 value to the stencil buffer in CustomDepth
pass (Requires project setting or r.CustomDepth == 3)

<a id="unreal.AesRuntimeResourceMountInfoResult"></a>