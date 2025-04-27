## SkeletalMeshSocket Objects

```python
class SkeletalMeshSocket(Object)
```

Skeletal Mesh Socket

**C++ Source:**

- **Module**: Engine
- **File**: SkeletalMeshSocket.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_name`` (Name):  [Read-Only]
- ``force_always_animated`` (bool):  [Read-Write] If true then the hierarchy of bones this socket is attached to will always be
            evaluated, even if it had previously been removed due to the current lod setting
- ``relative_location`` (Vector):  [Read-Write]
- ``relative_rotation`` (Rotator):  [Read-Write]
- ``relative_scale`` (Vector):  [Read-Write]
- ``socket_name`` (Name):  [Read-Only] Defines a named attachment location on the USkeletalMesh.
  These are set up in editor and used as a shortcut instead of specifying
  everything explicitly to AttachComponent in the SkeletalMeshComponent.
  The Outer of a SkeletalMeshSocket should always be the USkeletalMesh.

<a id="unreal.SkeletalMeshSocket.socket_name"></a>

#### socket_name

```python
@property
def socket_name() -> Name
```

(Name):  [Read-Only] Defines a named attachment location on the USkeletalMesh.
These are set up in editor and used as a shortcut instead of specifying
everything explicitly to AttachComponent in the SkeletalMeshComponent.
The Outer of a SkeletalMeshSocket should always be the USkeletalMesh.

<a id="unreal.SkeletalMeshSocket.bone_name"></a>

#### bone_name

```python
@property
def bone_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.SkeletalMeshSocket.relative_location"></a>

#### relative_location

```python
@property
def relative_location() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.SkeletalMeshSocket.relative_rotation"></a>

#### relative_rotation

```python
@property
def relative_rotation() -> Rotator
```

(Rotator):  [Read-Only]

<a id="unreal.SkeletalMeshSocket.relative_scale"></a>

#### relative_scale

```python
@property
def relative_scale() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.SkeletalMeshSocket.force_always_animated"></a>

#### force_always_animated

```python
@property
def force_always_animated() -> bool
```

(bool):  [Read-Only] If true then the hierarchy of bones this socket is attached to will always be
          evaluated, even if it had previously been removed due to the current lod setting

<a id="unreal.SkeletalMeshSocket.initialize_socket_from_location"></a>

#### initialize_socket_from_location

```python
def initialize_socket_from_location(skel_comp: SkeletalMeshComponent,
                                    world_location: Vector,
                                    world_normal: Vector) -> None
```

x.initialize_socket_from_location(skel_comp, world_location, world_normal) -> None
Sets BoneName, RelativeLocation and RelativeRotation based on closest bone to WorldLocation and WorldNormal

Args:
    skel_comp (SkeletalMeshComponent): 
    world_location (Vector): 
    world_normal (Vector):

<a id="unreal.SkeletalMeshSocket.get_socket_location"></a>

#### get_socket_location

```python
def get_socket_location(skel_comp: SkeletalMeshComponent) -> Vector
```

x.get_socket_location(skel_comp) -> Vector
Get Socket Location

Args:
    skel_comp (SkeletalMeshComponent): 

Returns:
    Vector:

<a id="unreal.SkyLight"></a>