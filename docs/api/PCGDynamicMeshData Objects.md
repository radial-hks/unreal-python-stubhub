## PCGDynamicMeshData Objects

```python
class PCGDynamicMeshData(PCGSpatialData)
```

PCGDynamic Mesh Data

**C++ Source:**

- **Plugin**: PCGGeometryScriptInterop
- **Module**: PCGGeometryScriptInterop
- **File**: PCGDynamicMeshData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dynamic_mesh`` (DynamicMesh):  [Read-Only]
- ``keep_zero_density_points`` (bool):  [Read-Write]
- ``materials`` (Array[MaterialInterface]):  [Read-Only]
- ``metadata`` (PCGMetadata):  [Read-Only] Not accessible through blueprint to make sure the constness is preserved
- ``target_actor`` (Actor):  [Read-Write] Recipient of any artifacts generated using this data.

<a id="unreal.PCGDynamicMeshData.dynamic_mesh"></a>

#### dynamic_mesh

```python
@property
def dynamic_mesh() -> DynamicMesh
```

(DynamicMesh):  [Read-Only]

<a id="unreal.PCGDynamicMeshData.materials"></a>

#### materials

```python
@property
def materials() -> Array[MaterialInterface]
```

(Array[MaterialInterface]):  [Read-Only]

<a id="unreal.PCGDynamicMeshData.set_materials"></a>

#### set_materials

```python
def set_materials(materials: Array[MaterialInterface]) -> None
```

x.set_materials(materials) -> None
Set Materials

Args:
    materials (Array[MaterialInterface]):

<a id="unreal.PCGDynamicMeshData.k2_initialize"></a>

#### k2_initialize

```python
def k2_initialize(mesh: DynamicMesh,
                  materials: Array[MaterialInterface],
                  can_take_ownership: bool = False) -> None
```

x.k2_initialize(mesh, materials, can_take_ownership=False) -> None
Initialize the dynamic mesh data from an input dynamic mesh object.
If the input dynamic mesh is not meant to be re-used after this initialization, you can set Can Take Ownership to true. Be careful as it
will put the previous object in an invalid state.
You can also pass an array of materials that correspond to the referenced materials in the dynamic mesh.

Args:
    mesh (DynamicMesh): 
    materials (Array[MaterialInterface]): 
    can_take_ownership (bool):

<a id="unreal.PCGDynamicMeshManagedComponent"></a>