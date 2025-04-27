## CreateMaterialObjectResult Objects

```python
class CreateMaterialObjectResult(StructBase)
```

FCreateMaterialObjectResult is returned by UModelingObjectsCreationAPI::CreateMaterialObject()
to indicate success/failure and provide information about created texture objects

**C++ Source:**

- **Plugin**: MeshModelingToolset
- **Module**: ModelingComponents
- **File**: ModelingObjectsCreationAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``new_asset`` (Object):  [Read-Only] A pointer to a newly-created Asset for the material object
- ``result_code`` (CreateModelingObjectResult):  [Read-Only] Success/Failure status for the requested operation

<a id="unreal.CreateMaterialObjectResult.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.CreateActorParams"></a>