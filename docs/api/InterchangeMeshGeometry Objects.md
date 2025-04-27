## InterchangeMeshGeometry Objects

```python
class InterchangeMeshGeometry(StructBase)
```

* A mesh geometry is a description of a translated mesh asset node that defines a geometry.

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangePipelines
- **File**: InterchangePipelineMeshesUtilities.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attached_socket_uids`` (Array[str]):  [Read-Write] A list of all scene nodes that represent sockets attached to this mesh.
- ``mesh_node`` (InterchangeMeshNode):  [Read-Write] The UInterchangeMeshNode pointer represented by this structure.
- ``mesh_uid`` (str):  [Read-Write] The unique ID of the UInterchangeMeshNode represented by this structure.
- ``referencing_mesh_instance_uids`` (Array[str]):  [Read-Write] All mesh instances that refer to this UInterchangeMeshNode pointer.

<a id="unreal.InterchangeMeshGeometry.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.InterchangePipelineMeshesUtilitiesContext"></a>