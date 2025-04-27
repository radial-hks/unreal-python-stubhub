## MoviePipelineWidgetRenderer Objects

```python
class MoviePipelineWidgetRenderer(MoviePipelineRenderPass)
```

Movie Pipeline Widget Renderer

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineSettings
- **File**: MoviePipelineWidgetRenderSetting.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``composite_onto_final_image`` (bool):  [Read-Write] If true, the widget renderer image will be composited into the Final Image pass. Doesn't apply to multi-layer EXR files.

<a id="unreal.MoviePipelineWidgetRenderer.composite_onto_final_image"></a>

#### composite_onto_final_image

```python
@property
def composite_onto_final_image() -> bool
```

(bool):  [Read-Write] If true, the widget renderer image will be composited into the Final Image pass. Doesn't apply to multi-layer EXR files.

<a id="unreal.MoviePipelineWidgetRenderer.composite_onto_final_image"></a>

#### composite_onto_final_image

```python
@composite_onto_final_image.setter
def composite_onto_final_image(value: bool) -> None
```

<a id="unreal.DummyRenderLayerOnlyNode"></a>