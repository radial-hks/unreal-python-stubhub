## CreateTextureObjectResult Objects

```python
class CreateTextureObjectResult(StructBase)
```

FCreateTextureObjectResult is returned by UModelingObjectsCreationAPI::CreateTextureObject()
to indicate success/failure and provide information about created texture objects

**C++ Source:**

- **Plugin**: MeshModelingToolset
- **Module**: ModelingComponents
- **File**: ModelingObjectsCreationAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``new_asset`` (Object):  [Read-Only] A pointer to a newly-created Asset for the texture object
- ``result_code`` (CreateModelingObjectResult):  [Read-Only] Success/Failure status for the requested operation

<a id="unreal.CreateTextureObjectResult.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.CreateMaterialObjectParams"></a>