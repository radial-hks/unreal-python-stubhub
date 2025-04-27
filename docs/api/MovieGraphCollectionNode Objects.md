## MovieGraphCollectionNode Objects

```python
class MovieGraphCollectionNode(MovieGraphSettingNode)
```

A collection node specifies an interface for doing dynamic scene queries for actors in the world. Collections work in tandem with
UMovieGraphModifiers to select which actors the modifiers should be run on.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphCollectionNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collection`` (MovieGraphCollection):  [Read-Only] The collection is customized in the details panel, so the override should always be enabled
- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``override_collection`` (bool):  [Read-Write]
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.

<a id="unreal.MovieGraphCollectionNode.override_collection"></a>

#### override_collection

```python
@property
def override_collection() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphCollectionNode.override_collection"></a>

#### override_collection

```python
@override_collection.setter
def override_collection(value: bool) -> None
```

<a id="unreal.MovieGraphCollectionNode.collection"></a>

#### collection

```python
@property
def collection() -> MovieGraphCollection
```

(MovieGraphCollection):  [Read-Only] The collection is customized in the details panel, so the override should always be enabled

<a id="unreal.MovieGraphCommandLineEncoderNode"></a>