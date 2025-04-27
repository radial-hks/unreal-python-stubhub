## DMMaterialValueRenderTarget Objects

```python
class DMMaterialValueRenderTarget(DMMaterialValueTexture)
```

Component representing a render target texture value. Manages its own parameter.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMMaterialValueRenderTarget.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cached_parameter_name`` (Name):  [Read-Only]
- ``clear_color`` (LinearColor):  [Read-Write]
- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``default_value`` (Texture):  [Read-Write]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``expose_parameter`` (bool):  [Read-Only]
- ``local`` (bool):  [Read-Only] True: The value is local to the stage it is used in.
  False: The value is a global value owned directly by the Model.
- ``parameter`` (DMMaterialParameter):  [Read-Only] The parameter name used to expose this value in a material.
  If it isn't provided, an automatic name will be generated.
- ``renderer`` (DMRenderTargetRenderer):  [Read-Write]
- ``texture_format`` (TextureRenderTargetFormat):  [Read-Write]
- ``texture_size`` (IntPoint):  [Read-Write]
- ``type`` (DMValueType):  [Read-Only]
- ``value`` (Texture):  [Read-Write]

<a id="unreal.DMMaterialValueRenderTarget.texture_size"></a>

#### texture_size

```python
@property
def texture_size() -> IntPoint
```

(IntPoint):  [Read-Write]

<a id="unreal.DMMaterialValueRenderTarget.texture_size"></a>

#### texture_size

```python
@texture_size.setter
def texture_size(value: IntPoint) -> None
```

<a id="unreal.DMMaterialValueRenderTarget.texture_format"></a>

#### texture_format

```python
@property
def texture_format() -> TextureRenderTargetFormat
```

(TextureRenderTargetFormat):  [Read-Write]

<a id="unreal.DMMaterialValueRenderTarget.texture_format"></a>

#### texture_format

```python
@texture_format.setter
def texture_format(value: TextureRenderTargetFormat) -> None
```

<a id="unreal.DMMaterialValueRenderTarget.clear_color"></a>

#### clear_color

```python
@property
def clear_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.DMMaterialValueRenderTarget.clear_color"></a>

#### clear_color

```python
@clear_color.setter
def clear_color(value: LinearColor) -> None
```

<a id="unreal.DMMaterialValueRenderTarget.renderer"></a>

#### renderer

```python
@property
def renderer() -> DMRenderTargetRenderer
```

(DMRenderTargetRenderer):  [Read-Write]

<a id="unreal.DMMaterialValueRenderTarget.renderer"></a>

#### renderer

```python
@renderer.setter
def renderer(value: DMRenderTargetRenderer) -> None
```

<a id="unreal.DMMaterialValueRenderTarget.set_texture_size"></a>

#### set_texture_size

```python
def set_texture_size(texture_size: IntPoint) -> None
```

x.set_texture_size(texture_size) -> None
Set Texture Size

Args:
    texture_size (IntPoint):

<a id="unreal.DMMaterialValueRenderTarget.set_texture_format"></a>

#### set_texture_format

```python
def set_texture_format(texture_format: TextureRenderTargetFormat) -> None
```

x.set_texture_format(texture_format) -> None
Set Texture Format

Args:
    texture_format (TextureRenderTargetFormat):

<a id="unreal.DMMaterialValueRenderTarget.set_renderer"></a>

#### set_renderer

```python
def set_renderer(renderer: DMRenderTargetRenderer) -> None
```

x.set_renderer(renderer) -> None
Set Renderer

Args:
    renderer (DMRenderTargetRenderer):

<a id="unreal.DMMaterialValueRenderTarget.set_clear_color"></a>

#### set_clear_color

```python
def set_clear_color(clear_color: LinearColor) -> None
```

x.set_clear_color(clear_color) -> None
Set Clear Color

Args:
    clear_color (LinearColor):

<a id="unreal.DMMaterialValueRenderTarget.get_texture_size"></a>

#### get_texture_size

```python
def get_texture_size() -> IntPoint
```

x.get_texture_size() -> IntPoint
Get Texture Size

Returns:
    IntPoint:

<a id="unreal.DMMaterialValueRenderTarget.get_texture_format"></a>

#### get_texture_format

```python
def get_texture_format() -> TextureRenderTargetFormat
```

x.get_texture_format() -> TextureRenderTargetFormat
Get Texture Format

Returns:
    TextureRenderTargetFormat:

<a id="unreal.DMMaterialValueRenderTarget.get_render_target"></a>

#### get_render_target

```python
def get_render_target() -> TextureRenderTarget2D
```

x.get_render_target() -> TextureRenderTarget2D
Get Render Target

Returns:
    TextureRenderTarget2D:

<a id="unreal.DMMaterialValueRenderTarget.get_renderer"></a>

#### get_renderer

```python
def get_renderer() -> DMRenderTargetRenderer
```

x.get_renderer() -> DMRenderTargetRenderer
Get Renderer

Returns:
    DMRenderTargetRenderer:

<a id="unreal.DMMaterialValueRenderTarget.get_clear_color"></a>

#### get_clear_color

```python
def get_clear_color() -> LinearColor
```

x.get_clear_color() -> LinearColor
Get Clear Color

Returns:
    LinearColor:

<a id="unreal.DMMaterialValueRenderTargetDynamic"></a>