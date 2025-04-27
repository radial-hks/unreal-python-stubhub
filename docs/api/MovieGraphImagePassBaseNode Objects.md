## MovieGraphImagePassBaseNode Objects

```python
class MovieGraphImagePassBaseNode(MovieGraphRenderPassNode)
```

The UMovieGraphImagePassBaseNode is an abstract base-class for render nodes that wish to create
renders of the 3d scene. You are not required to inherit from this node (can inherit from
UMovieGraphRenderPassNode), but this node provides a helpful set of functions and default values
for constructing the required matrices and settings for viewport-like renders.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineRenderPasses
- **File**: MovieGraphImagePassBaseNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``override_show_flags`` (bool):  [Read-Write] Note: Since *individual* show flags are overridden instead of the entire ShowFlags property, manually set to
  overridden so the traversal picks the changes up (otherwise they will be ignored).
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.
- ``show_flags`` (MovieGraphShowFlags):  [Read-Only] The show flags that should be active during a render for this node.

<a id="unreal.MovieGraphImagePassBaseNode.override_show_flags"></a>

#### override_show_flags

```python
@property
def override_show_flags() -> bool
```

(bool):  [Read-Write] Note: Since *individual* show flags are overridden instead of the entire ShowFlags property, manually set to
overridden so the traversal picks the changes up (otherwise they will be ignored).

<a id="unreal.MovieGraphImagePassBaseNode.override_show_flags"></a>

#### override_show_flags

```python
@override_show_flags.setter
def override_show_flags(value: bool) -> None
```

<a id="unreal.MovieGraphImagePassBaseNode.show_flags"></a>

#### show_flags

```python
@property
def show_flags() -> MovieGraphShowFlags
```

(MovieGraphShowFlags):  [Read-Only] The show flags that should be active during a render for this node.

<a id="unreal.MovieGraphDeferredRenderPassNode"></a>