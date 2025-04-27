## ModelingObjectsCreationAPI Objects

```python
class ModelingObjectsCreationAPI(Object)
```

UModelingObjectsCreationAPI is a base interface for functions that can be used to
create various types of objects from Modeling Tools, or other sources. The "type" is
very generic here - "Mesh", "Texture", etc - because this API is meant to provide
an abstraction for Tools to emit different types of objects in different situations.
For example an Tool might emit StaticMesh Asset/Actors in-Editor, but ProceduralMeshComponents at Runtime.

The creation inputs are specified via the structs above (eg FCreateMeshObjectParams, FCreateTextureObjectParams),
which are very extensive, kitchen-sink sort of structs. Generally "New Mesh Object"
creation behavior will be very complex and so this API is really just a way to route
the data, and very few guarantees can be made about any specific implementation.

The assumed (but not really required) usage of instances of this type are that they
will be registered with an InteractiveToolsContext's ContextObjectStore, and then
fetched from there by Tools/Algorithms/etc that need to use these capabilities can
use the UE::Modeling::CreateXObject() helper functions below. However the interface
does not have any dependencies on this usage model.

See UEditorModelingObjectsCreationAPI for an example implementation suitable for in-Editor use.

**C++ Source:**

- **Plugin**: MeshModelingToolset
- **Module**: ModelingComponents
- **File**: ModelingObjectsCreationAPI.h

<a id="unreal.ModelingObjectsCreationAPI.create_texture_object"></a>

#### create_texture_object

```python
def create_texture_object(
        create_tex_params: CreateTextureObjectParams
) -> CreateTextureObjectResult
```

x.create_texture_object(create_tex_params) -> CreateTextureObjectResult
Create a new texture object based on the data in CreateTexParams

Args:
    create_tex_params (CreateTextureObjectParams): 

Returns:
    CreateTextureObjectResult: a results data structure, containing a result code and information about any new objects created

<a id="unreal.ModelingObjectsCreationAPI.create_new_actor"></a>

#### create_new_actor

```python
def create_new_actor(
        create_actor_params: CreateActorParams) -> CreateActorResult
```

x.create_new_actor(create_actor_params) -> CreateActorResult
Create a new material object based on the data in CreateMaterialParams

Args:
    create_actor_params (CreateActorParams): 

Returns:
    CreateActorResult: a results data structure, containing a result code and information about any new objects created

<a id="unreal.ModelingObjectsCreationAPI.create_mesh_object"></a>

#### create_mesh_object

```python
def create_mesh_object(
        create_mesh_params: CreateMeshObjectParams) -> CreateMeshObjectResult
```

x.create_mesh_object(create_mesh_params) -> CreateMeshObjectResult
Create a new mesh object based on the data in CreateMeshParams

Args:
    create_mesh_params (CreateMeshObjectParams): 

Returns:
    CreateMeshObjectResult: a results data structure, containing a result code and information about any new objects created

<a id="unreal.ModelingObjectsCreationAPI.create_material_object"></a>

#### create_material_object

```python
def create_material_object(
    create_material_params: CreateMaterialObjectParams
) -> CreateMaterialObjectResult
```

x.create_material_object(create_material_params) -> CreateMaterialObjectResult
Create a new material object based on the data in CreateMaterialParams

Args:
    create_material_params (CreateMaterialObjectParams): 

Returns:
    CreateMaterialObjectResult: a results data structure, containing a result code and information about any new objects created

<a id="unreal.PreviewMeshActor"></a>