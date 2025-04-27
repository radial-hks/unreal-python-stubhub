## CreateObjectTypeHint Objects

```python
class CreateObjectTypeHint(EnumBase)
```

Hint for the type of mesh object a UModelingObjectsCreationAPI might create based
on FCreateMeshObjectParams data. This can be used by clients to try to specify
the type of object to emit, however there is no guarantee that an API implementation
supports creating all types.

**C++ Source:**

- **Plugin**: MeshModelingToolset
- **Module**: ModelingComponents
- **File**: ModelingObjectsCreationAPI.h

<a id="unreal.CreateObjectTypeHint.UNDEFINED"></a>

#### UNDEFINED

0

<a id="unreal.CreateObjectTypeHint.STATIC_MESH"></a>

#### STATIC_MESH

1

<a id="unreal.CreateObjectTypeHint.VOLUME"></a>

#### VOLUME

2

<a id="unreal.CreateObjectTypeHint.DYNAMIC_MESH_ACTOR"></a>

#### DYNAMIC_MESH_ACTOR

3

<a id="unreal.GeometryScriptOutcomePins"></a>