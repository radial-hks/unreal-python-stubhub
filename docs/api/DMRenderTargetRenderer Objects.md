## DMRenderTargetRenderer Objects

```python
class DMRenderTargetRenderer(DMMaterialComponent)
```

A component responsible for rendering something to a texture render target (value).

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMRenderTargetRenderer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]

<a id="unreal.DMRenderTargetRenderer.update_render_target"></a>

#### update_render_target

```python
def update_render_target() -> None
```

x.update_render_target() -> None
Updates the contents of the render target, redrawing and possibly resizing it.

<a id="unreal.DMRenderTargetRenderer.is_updating"></a>

#### is_updating

```python
def is_updating() -> bool
```

x.is_updating() -> bool
Returns true is this target is currently being re-rendering.

Returns:
    bool:

<a id="unreal.DMRenderTargetRenderer.get_render_target_value"></a>

#### get_render_target_value

```python
def get_render_target_value() -> DMMaterialValueRenderTarget
```

x.get_render_target_value() -> DMMaterialValueRenderTarget
Returns the render target value (the object's Outer).

Returns:
    DMMaterialValueRenderTarget:

<a id="unreal.DMRenderTargetRenderer.create_render_target_renderer"></a>

#### create_render_target_renderer

```python
@classmethod
def create_render_target_renderer(
    cls, renderer_class: Class,
    render_target_value: DMMaterialValueRenderTarget
) -> DMRenderTargetRenderer
```

X.create_render_target_renderer(renderer_class, render_target_value) -> DMRenderTargetRenderer
Creates a render of the given class and initializes it.

Args:
    renderer_class (type(Class)): 
    render_target_value (DMMaterialValueRenderTarget): 

Returns:
    DMRenderTargetRenderer:

<a id="unreal.DMRenderTargetRenderer.async_update_render_target"></a>

#### async_update_render_target

```python
def async_update_render_target() -> None
```

x.async_update_render_target() -> None
Updates the contents of the render target, redrawing and possibly resizing it, at the end of the frame.

<a id="unreal.DMRenderTargetWidgetRendererBase"></a>