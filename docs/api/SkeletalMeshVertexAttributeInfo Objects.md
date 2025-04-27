## SkeletalMeshVertexAttributeInfo Objects

```python
class SkeletalMeshVertexAttributeInfo(StructBase)
```

A structure to store user-controllable settings for attributes

**C++ Source:**

- **Module**: Engine
- **File**: SkeletalMeshVertexAttribute.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``data_type`` (SkeletalMeshVertexAttributeDataType):  [Read-Write] The data type to store the vertex data as for rendering
- ``enabled_for_render`` (PerPlatformBool):  [Read-Write] Whether this vertex attribute should be included in the render data. Requires a rebuild of the render mesh.
- ``name`` (Name):  [Read-Only] The name of the vertex attribute

<a id="unreal.SkeletalMeshVertexAttributeInfo.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.SkeletalMeshSamplingRegion"></a>