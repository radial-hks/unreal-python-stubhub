## SkinnedAsset Objects

```python
class SkinnedAsset(StreamableRenderAsset)
```

Skinned Asset

**C++ Source:**

- **Module**: Engine
- **File**: SkinnedAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``global_force_mip_levels_to_be_resident`` (bool):  [Read-Write] Global and serialized version of ForceMiplevelsToBeResident.
- ``never_stream`` (bool):  [Read-Write]
- ``num_cinematic_mip_levels`` (int32):  [Read-Write] Number of mip-levels to use for cinematic quality.

<a id="unreal.SkinnedAsset.find_socket_info"></a>

#### find_socket_info

```python
def find_socket_info(
        socket_name: Name) -> Tuple[SkeletalMeshSocket, Transform, int, int]
```

x.find_socket_info(socket_name) -> (SkeletalMeshSocket, out_transform=Transform, out_bone_index=int32, out_index=int32)
Find a socket object and associated info in this SkeletalMesh by name.
Entering NAME_None will return NULL. If there are multiple sockets with the same name, will return the first one.
Also returns the index for the socket allowing for future fast access via GetSocketByIndex()
Also returns the socket transform and the bone index (if any)

Args:
    socket_name (Name): 

Returns:
    tuple: 

    out_transform (Transform): 

    out_bone_index (int32): 

    out_index (int32):

<a id="unreal.SkinnedAsset.find_socket"></a>

#### find_socket

```python
def find_socket(socket_name: Name) -> SkeletalMeshSocket
```

x.find_socket(socket_name) -> SkeletalMeshSocket
Find a socket object in this SkeletalMesh by name.
Entering NAME_None will return NULL. If there are multiple sockets with the same name, will return the first one.

Args:
    socket_name (Name): 

Returns:
    SkeletalMeshSocket:

<a id="unreal.SkeletalMesh"></a>