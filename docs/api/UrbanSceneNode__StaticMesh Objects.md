## UrbanSceneNode\_StaticMesh Objects

```python
class UrbanSceneNode_StaticMesh(UrbanSceneNode_Base)
```

For final mesh resource or preview static mesh

**C++ Source:**

- **Plugin**: AesRuntime
- **Module**: UrbanScene
- **File**: UrbanSceneNode_StaticMesh.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``fid_buffs`` (Array[UrbanLodFIDArray]):  [Read-Only]
- ``local_to_parent_transform`` (Transform):  [Read-Only]
- ``primitive_data`` (Array[float]):  [Read-Only]
- ``resource_class`` (SoftClassPath):  [Read-Only]
- ``resource_key`` (Name):  [Read-Only]
- ``static_mesh`` (StaticMesh):  [Read-Only]

<a id="unreal.UrbanSceneNode_StaticMesh.load_mesh_and_fi_ds"></a>

#### load\_mesh\_and\_fi\_ds

```python
def load_mesh_and_fi_ds(actor: Actor) -> Array[StaticMeshComponent]
```

x.load_mesh_and_fi_ds(actor) -> Array[StaticMeshComponent]
Load Mesh and FIDs

Args:
    actor (Actor): 

Returns:
    Array[StaticMeshComponent]:

<a id="unreal.UrbanScenePayloadComponent"></a>