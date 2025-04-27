## MovieGraphBurnInNode Objects

```python
class MovieGraphBurnInNode(MovieGraphWidgetRendererBaseNode)
```

A node which generates a widget burn-in, rendered to a standalone image or composited on top of a render layer.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphBurnInNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``burn_in_class`` (SoftClassPath):  [Read-Write] The widget that the burn-in should use.
- ``composite_onto_final_image`` (bool):  [Read-Write] If true, the pass will be composited onto each render. Does not apply to multi-layer EXR files.
- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``override_b_composite_onto_final_image`` (bool):  [Read-Write]
- ``override_burn_in_class`` (bool):  [Read-Write]
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.

<a id="unreal.MovieGraphBurnInNode.override_burn_in_class"></a>

#### override_burn_in_class

```python
@property
def override_burn_in_class() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphBurnInNode.override_burn_in_class"></a>

#### override_burn_in_class

```python
@override_burn_in_class.setter
def override_burn_in_class(value: bool) -> None
```

<a id="unreal.MovieGraphBurnInNode.burn_in_class"></a>

#### burn_in_class

```python
@property
def burn_in_class() -> SoftClassPath
```

(SoftClassPath):  [Read-Write] The widget that the burn-in should use.

<a id="unreal.MovieGraphBurnInNode.burn_in_class"></a>

#### burn_in_class

```python
@burn_in_class.setter
def burn_in_class(value: SoftClassPath) -> None
```

<a id="unreal.MovieGraphBurnInWidget"></a>