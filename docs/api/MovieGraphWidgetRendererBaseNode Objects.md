## MovieGraphWidgetRendererBaseNode Objects

```python
class MovieGraphWidgetRendererBaseNode(MovieGraphRenderPassNode)
```

Base node containing common logic for nodes that render widgets.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphWidgetRendererBaseNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``composite_onto_final_image`` (bool):  [Read-Write] If true, the pass will be composited onto each render. Does not apply to multi-layer EXR files.
- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``override_b_composite_onto_final_image`` (bool):  [Read-Write]
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.

<a id="unreal.MovieGraphWidgetRendererBaseNode.override_b_composite_onto_final_image"></a>

#### override_b_composite_onto_final_image

```python
@property
def override_b_composite_onto_final_image() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphWidgetRendererBaseNode.override_b_composite_onto_final_image"></a>

#### override_b_composite_onto_final_image

```python
@override_b_composite_onto_final_image.setter
def override_b_composite_onto_final_image(value: bool) -> None
```

<a id="unreal.MovieGraphWidgetRendererBaseNode.composite_onto_final_image"></a>

#### composite_onto_final_image

```python
@property
def composite_onto_final_image() -> bool
```

(bool):  [Read-Write] If true, the pass will be composited onto each render. Does not apply to multi-layer EXR files.

<a id="unreal.MovieGraphWidgetRendererBaseNode.composite_onto_final_image"></a>

#### composite_onto_final_image

```python
@composite_onto_final_image.setter
def composite_onto_final_image(value: bool) -> None
```

<a id="unreal.MovieGraphBurnInNode"></a>