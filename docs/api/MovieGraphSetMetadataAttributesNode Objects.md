## MovieGraphSetMetadataAttributesNode Objects

```python
class MovieGraphSetMetadataAttributesNode(MovieGraphSettingNode)
```

A node which can set a specific metadata attributes.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphSetMetadataAttributesNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``metadata_attribute_collection`` (MovieGraphMetadataAttributeCollection):  [Read-Only] A container of metadata attributes to be added to the file.
- ``override_metadata_attribute_collection`` (bool):  [Read-Write]
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.

<a id="unreal.MovieGraphSetMetadataAttributesNode.override_metadata_attribute_collection"></a>

#### override_metadata_attribute_collection

```python
@property
def override_metadata_attribute_collection() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphSetMetadataAttributesNode.override_metadata_attribute_collection"></a>

#### override_metadata_attribute_collection

```python
@override_metadata_attribute_collection.setter
def override_metadata_attribute_collection(value: bool) -> None
```

<a id="unreal.MovieGraphSetMetadataAttributesNode.metadata_attribute_collection"></a>

#### metadata_attribute_collection

```python
@property
def metadata_attribute_collection() -> MovieGraphMetadataAttributeCollection
```

(MovieGraphMetadataAttributeCollection):  [Read-Only] A container of metadata attributes to be added to the file.

<a id="unreal.MovieGraphStartEndConsoleCommands"></a>