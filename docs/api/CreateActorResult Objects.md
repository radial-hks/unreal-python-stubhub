## CreateActorResult Objects

```python
class CreateActorResult(StructBase)
```

FCreateActorResult is returned by UModelingObjectsCreationAPI::FCreateActorParams()
to indicate success/failure and provide information about created actors

**C++ Source:**

- **Plugin**: MeshModelingToolset
- **Module**: ModelingComponents
- **File**: ModelingObjectsCreationAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``new_actor`` (Actor):  [Read-Only] A pointer to a newly-created Actor
- ``result_code`` (CreateModelingObjectResult):  [Read-Only] Success/Failure status for the requested operation

<a id="unreal.CreateActorResult.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.GeometryScriptMeshReadLOD"></a>