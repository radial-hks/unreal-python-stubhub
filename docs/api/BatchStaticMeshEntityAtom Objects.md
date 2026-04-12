## BatchStaticMeshEntityAtom Objects

```python
class BatchStaticMeshEntityAtom(EntityAtomBase)
```

Batch Static Mesh Entity Atom

**C++ Source:**

- **Plugin**: WdpAssetLoader
- **Module**: StaticMeshAssetLoader
- **File**: BatchStaticMeshEntityAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``line_cells`` (Map[int64, MeshCellsInfo]):  [Read-Write]
- ``region_cells`` (Map[int64, MeshCellsInfo]):  [Read-Write]

<a id="unreal.BatchStaticMeshEntityAtom.line_cells"></a>

#### line\_cells

```python
@property
def line_cells() -> Map[int, MeshCellsInfo]
```

(Map[int64, MeshCellsInfo]):  [Read-Only]

<a id="unreal.BatchStaticMeshEntityAtom.region_cells"></a>

#### region\_cells

```python
@property
def region_cells() -> Map[int, MeshCellsInfo]
```

(Map[int64, MeshCellsInfo]):  [Read-Only]

<a id="unreal.IsmEntityAtom"></a>