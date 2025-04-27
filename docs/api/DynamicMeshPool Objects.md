## DynamicMeshPool Objects

```python
class DynamicMeshPool(Object)
```

UDynamicMeshPool manages a Pool of UDynamicMesh objects. This allows
the meshes to be re-used instead of being garbage-collected. This
is intended to be used by Blueprints that need to do procedural geometry
operations that generate temporary meshes, as these will commonly run their
construction scripts many times as the user (eg) manipulates parameters,
and constantly spawning new UDynamicMesh instances will result in enormous
memory usage hanging around until GC runs.

Usage is to call RequestMesh() to take ownership of an available UDynamicMesh (which
will allocate a new one if the pool is empty) and ReturnMesh() to return it to the pool.

ReturnAllMeshes() can be called to return all allocated meshes.

In both cases, there is nothing preventing you from still holding on to the mesh.
So, be careful.

FreeAllMeshes() calls ReturnAllMeshes() and then releases the pool's references to
the allocated meshes, so they can be Garbage Collected

If you Request() more meshes than you Return(), the Pool will still be holding on to
references to those meshes, and they will never be Garbage Collected (ie memory leak).
As a failsafe, if the number of allocated meshes exceeds geometry.DynamicMesh.MaxPoolSize,
the Pool will release all it's references and run garbage collection on the next call to RequestMesh().
(Do not rely on this as a memory management strategy)

An alternate strategy that could be employed here is for the Pool to not hold
references to meshes it has provided, only those that have been explicitly returned.
Then non-returned meshes would simply be garbage-collected, however it allows
potentially a large amount of memory to be consumed until that occurs.

UDynamicMesh::Reset() is called on the object returned to the Pool, which clears
the internal FDynamicMesh3 (which uses normal C++ memory management, so no garbage collection involved)
So the Pool does not re-use mesh memory, only the UObject containers.

**C++ Source:**

- **Module**: GeometryFramework
- **File**: UDynamicMesh.h

<a id="unreal.DynamicMeshPool.return_mesh"></a>

#### return_mesh

```python
def return_mesh(mesh: DynamicMesh) -> None
```

x.return_mesh(mesh) -> None
Release a UDynamicMesh returned by RequestMesh() back to the pool

Args:
    mesh (DynamicMesh):

<a id="unreal.DynamicMeshPool.return_all_meshes"></a>

#### return_all_meshes

```python
def return_all_meshes() -> None
```

x.return_all_meshes() -> None
Release all GeneratedMeshes back to the pool

<a id="unreal.DynamicMeshPool.request_mesh"></a>

#### request_mesh

```python
def request_mesh() -> DynamicMesh
```

x.request_mesh() -> DynamicMesh


Returns:
    DynamicMesh: an available UDynamicMesh from the pool (possibly allocating a new mesh)

<a id="unreal.DynamicMeshPool.free_all_meshes"></a>

#### free_all_meshes

```python
def free_all_meshes() -> None
```

x.free_all_meshes() -> None
Release all GeneratedMeshes back to the pool and allow them to be garbage collected

<a id="unreal.AvaSequence"></a>