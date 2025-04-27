## CompositingElementPass Objects

```python
class CompositingElementPass(Object)
```

UCompositingElementPass

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: CompositingElementPasses.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write]
- ``pass_name`` (Name):  [Read-Write]

<a id="unreal.CompositingElementPass.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.CompositingElementPass.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.CompositingElementPass.pass_name"></a>

#### pass_name

```python
@property
def pass_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.CompositingElementPass.pass_name"></a>

#### pass_name

```python
@pass_name.setter
def pass_name(value: Name) -> None
```

<a id="unreal.CompositingElementPass.reset"></a>

#### reset

```python
def reset() -> None
```

x.reset() -> None
Reset

<a id="unreal.CompositingElementPass.request_render_target"></a>

#### request_render_target

```python
def request_render_target(
        dimensions: IntPoint,
        format: TextureRenderTargetFormat) -> TextureRenderTarget2D
```

x.request_render_target(dimensions, format) -> TextureRenderTarget2D
, meta = (BlueprintProtected = "true")

Args:
    dimensions (IntPoint): 
    format (TextureRenderTargetFormat): 

Returns:
    TextureRenderTarget2D:

<a id="unreal.CompositingElementPass.request_natively_formatted_target"></a>

#### request_natively_formatted_target

```python
def request_natively_formatted_target(
        render_scale: float = 1.000000) -> TextureRenderTarget2D
```

x.request_natively_formatted_target(render_scale=1.000000) -> TextureRenderTarget2D
, meta = (BlueprintProtected = "true")

Args:
    render_scale (float): 

Returns:
    TextureRenderTarget2D:

<a id="unreal.CompositingElementPass.release_render_target"></a>

#### release_render_target

```python
def release_render_target(assigned_target: TextureRenderTarget2D) -> bool
```

x.release_render_target(assigned_target) -> bool
, meta = (BlueprintProtected = "true")

Args:
    assigned_target (TextureRenderTarget2D): 

Returns:
    bool:

<a id="unreal.CompositingElementPass.on_frame_end"></a>

#### on_frame_end

```python
def on_frame_end() -> None
```

x.on_frame_end() -> None
On Frame End

<a id="unreal.CompositingElementPass.on_frame_begin"></a>

#### on_frame_begin

```python
def on_frame_begin(camera_cut_this_frame: bool) -> None
```

x.on_frame_begin(camera_cut_this_frame) -> None
On Frame Begin

Args:
    camera_cut_this_frame (bool):

<a id="unreal.CompositingElementPass.on_enabled"></a>

#### on_enabled

```python
def on_enabled() -> None
```

x.on_enabled() -> None
On Enabled

<a id="unreal.CompositingElementPass.on_disabled"></a>

#### on_disabled

```python
def on_disabled() -> None
```

x.on_disabled() -> None
On Disabled

<a id="unreal.CompositingElementInput"></a>