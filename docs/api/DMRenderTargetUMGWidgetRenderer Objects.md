## DMRenderTargetUMGWidgetRenderer Objects

```python
class DMRenderTargetUMGWidgetRenderer(DMRenderTargetWidgetRendererBase)
```

DMRender Target UMGWidget Renderer

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMRenderTargetUMGWidgetRenderer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``widget_class`` (type(Class)):  [Read-Write]

<a id="unreal.DMRenderTargetUMGWidgetRenderer.widget_class"></a>

#### widget_class

```python
@property
def widget_class() -> Class
```

(type(Class)):  [Read-Write]

<a id="unreal.DMRenderTargetUMGWidgetRenderer.widget_class"></a>

#### widget_class

```python
@widget_class.setter
def widget_class(value: Class) -> None
```

<a id="unreal.DMRenderTargetUMGWidgetRenderer.set_widget_class"></a>

#### set_widget_class

```python
def set_widget_class(widget_class: Class) -> None
```

x.set_widget_class(widget_class) -> None
Set Widget Class

Args:
    widget_class (type(Class)):

<a id="unreal.DMRenderTargetUMGWidgetRenderer.get_widget_class"></a>

#### get_widget_class

```python
def get_widget_class() -> Class
```

x.get_widget_class() -> type(Class)
Get Widget Class

Returns:
    type(Class):

<a id="unreal.DMTextureUV"></a>