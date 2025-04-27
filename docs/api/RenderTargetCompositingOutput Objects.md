## RenderTargetCompositingOutput Objects

```python
class RenderTargetCompositingOutput(CompositingElementOutput)
```

Render Target Compositing Output

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: CompositingElementOutputs.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write]
- ``pass_name`` (Name):  [Read-Write]
- ``render_target`` (TextureRenderTarget2D):  [Read-Write]

<a id="unreal.RenderTargetCompositingOutput.render_target"></a>

#### render_target

```python
@property
def render_target() -> TextureRenderTarget2D
```

(TextureRenderTarget2D):  [Read-Write]

<a id="unreal.RenderTargetCompositingOutput.render_target"></a>

#### render_target

```python
@render_target.setter
def render_target(value: TextureRenderTarget2D) -> None
```

<a id="unreal.EXRFileCompositingOutput"></a>