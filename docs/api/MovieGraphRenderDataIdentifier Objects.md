## MovieGraphRenderDataIdentifier Objects

```python
class MovieGraphRenderDataIdentifier(StructBase)
```

This data structure can be used to identify what render data a set of pixels represents
by knowing what the render layer name is, what renderer produced it, if it's a sub-resource,
and what camera it is for. Can be used as the key in a TMap.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphRenderDataIdentifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``camera_name`` (str):  [Read-Write] The name of the camera being used for this render.
- ``layer_name`` (str):  [Read-Write] The Render Layer name (as defined by the "Render Layer" node.). This is effectively a
  "display" name for identifiers. If there is no Render Layer node then this will be the
  RootBranchName (so that the {render_layer} token works in the case of data from things
  on the Globals branch).
- ``renderer_name`` (str):  [Read-Write] Which renderer was used to produce this image ("panoramic" "deferred" "path tracer", etc.)
- ``root_branch_name`` (Name):  [Read-Write] The root branch name from the Outputs node that this identifier is for. This is useful to
  know which branch it came from, as RenderLayer is user-defined and can be redefined multiple
  times within one graph.
- ``sub_resource_name`` (str):  [Read-Write] A sub-resource name for the renderer (ie: "beauty", "object id", "depth", etc.)

<a id="unreal.MovieGraphRenderDataIdentifier.__init__"></a>

#### __init__

```python
def __init__(root_branch_name: Name = "None",
             layer_name: str = "",
             renderer_name: str = "",
             sub_resource_name: str = "",
             camera_name: str = "") -> None
```

<a id="unreal.MovieGraphRenderDataIdentifier.root_branch_name"></a>

#### root_branch_name

```python
@property
def root_branch_name() -> Name
```

(Name):  [Read-Write] The root branch name from the Outputs node that this identifier is for. This is useful to
know which branch it came from, as RenderLayer is user-defined and can be redefined multiple
times within one graph.

<a id="unreal.MovieGraphRenderDataIdentifier.root_branch_name"></a>

#### root_branch_name

```python
@root_branch_name.setter
def root_branch_name(value: Name) -> None
```

<a id="unreal.MovieGraphRenderDataIdentifier.layer_name"></a>

#### layer_name

```python
@property
def layer_name() -> str
```

(str):  [Read-Write] The Render Layer name (as defined by the "Render Layer" node.). This is effectively a
"display" name for identifiers. If there is no Render Layer node then this will be the
RootBranchName (so that the {render_layer} token works in the case of data from things
on the Globals branch).

<a id="unreal.MovieGraphRenderDataIdentifier.layer_name"></a>

#### layer_name

```python
@layer_name.setter
def layer_name(value: str) -> None
```

<a id="unreal.MovieGraphRenderDataIdentifier.renderer_name"></a>

#### renderer_name

```python
@property
def renderer_name() -> str
```

(str):  [Read-Write] Which renderer was used to produce this image ("panoramic" "deferred" "path tracer", etc.)

<a id="unreal.MovieGraphRenderDataIdentifier.renderer_name"></a>

#### renderer_name

```python
@renderer_name.setter
def renderer_name(value: str) -> None
```

<a id="unreal.MovieGraphRenderDataIdentifier.sub_resource_name"></a>

#### sub_resource_name

```python
@property
def sub_resource_name() -> str
```

(str):  [Read-Write] A sub-resource name for the renderer (ie: "beauty", "object id", "depth", etc.)

<a id="unreal.MovieGraphRenderDataIdentifier.sub_resource_name"></a>

#### sub_resource_name

```python
@sub_resource_name.setter
def sub_resource_name(value: str) -> None
```

<a id="unreal.MovieGraphRenderDataIdentifier.camera_name"></a>

#### camera_name

```python
@property
def camera_name() -> str
```

(str):  [Read-Write] The name of the camera being used for this render.

<a id="unreal.MovieGraphRenderDataIdentifier.camera_name"></a>

#### camera_name

```python
@camera_name.setter
def camera_name(value: str) -> None
```

<a id="unreal.MovieGraphRenderLayerOutputData"></a>