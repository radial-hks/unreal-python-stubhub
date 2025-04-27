## InterchangeMeshInstance Objects

```python
class InterchangeMeshInstance(StructBase)
```

* A mesh instance is a description of a translated scene node that points to a translated mesh asset.
* A mesh instance that points to an LOD group can have many LODs and many scene mesh nodes per LOD index.
* A mesh instance that points to a mesh node will have only LOD 0 and will point to one scene mesh node.

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangePipelines
- **File**: InterchangePipelineMeshesUtilities.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``has_morph_targets`` (bool):  [Read-Write]
- ``lod_group_node`` (InterchangeSceneNode):  [Read-Write] This member is null unless the mesh instance represents a LOD group.
- ``mesh_instance_uid`` (str):  [Read-Write] This ID represents either a LOD group scene node UID or a mesh scene node UID.
- ``reference_morph_target`` (bool):  [Read-Write]
- ``reference_skinned_mesh`` (bool):  [Read-Write]
- ``referencing_mesh_geometry_uids`` (Array[str]):  [Read-Write] All mesh geometry referenced by this MeshInstance.
- ``scene_node_per_lod_index`` (Map[int32, InterchangeLodSceneNodeContainer]):  [Read-Write] Each scene node here represents a mesh scene node. If it represents a LOD group, there may be more then one mesh scene node for a specific LOD index.

<a id="unreal.InterchangeMeshInstance.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.InterchangeMeshGeometry"></a>