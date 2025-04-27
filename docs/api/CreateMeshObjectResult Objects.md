## CreateMeshObjectResult Objects

```python
class CreateMeshObjectResult(StructBase)
```

FCreateMeshObjectResult is returned by UModelingObjectsCreationAPI::CreateMeshObject()
to indicate success/failure and provide information about created mesh objects

**C++ Source:**

- **Plugin**: MeshModelingToolset
- **Module**: ModelingComponents
- **File**: ModelingObjectsCreationAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``new_actor`` (Actor):  [Read-Only] A pointer to a newly-created Actor for the mesh object, if applicable (eg StaticMeshActor)
- ``new_asset`` (Object):  [Read-Only] A pointer to a newly-created Asset for the mesh object, if applicable (eg StaticMeshAsset)
- ``new_component`` (PrimitiveComponent):  [Read-Only] A pointer to a newly-created PrimitiveComponent for the mesh object, if applicable (eg StaticMeshComponent)
- ``result_code`` (CreateModelingObjectResult):  [Read-Only] Success/Failure status for the requested operation

<a id="unreal.CreateMeshObjectResult.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.CreateTextureObjectParams"></a>