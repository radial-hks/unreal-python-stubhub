## AesFileSystemLibrary Objects

```python
class AesFileSystemLibrary(BlueprintFunctionLibrary)
```

Aes Runtime Blueprint Library

**C++ Source:**

- **Plugin**: AesRuntime
- **Module**: AesRuntime
- **File**: AesRuntimeBlueprintLibrary.h

<a id="unreal.AesFileSystemLibrary.try_mount_mesh_by_id"></a>

#### try\_mount\_mesh\_by\_id

```python
@classmethod
def try_mount_mesh_by_id(cls,
                         mesh_id: str) -> Optional[Array[StaticMeshActor]]
```

X.try_mount_mesh_by_id(mesh_id) -> Array[StaticMeshActor] or None
Try Mount Mesh by Id

Args:
    mesh_id (str): 

Returns:
    Array[StaticMeshActor] or None: 

    out_static_mesh_actors (Array[StaticMeshActor]):

<a id="unreal.AesFileSystemLibrary.modify_nanite_enable"></a>

#### modify\_nanite\_enable

```python
@classmethod
def modify_nanite_enable(cls, mesh: Array[StaticMesh],
                         nanite_enable: bool) -> bool
```

X.modify_nanite_enable(mesh, nanite_enable) -> bool
Modify Nanite Enable

Args:
    mesh (Array[StaticMesh]): 
    nanite_enable (bool): 

Returns:
    bool:

<a id="unreal.AesBaseResourceLoader"></a>