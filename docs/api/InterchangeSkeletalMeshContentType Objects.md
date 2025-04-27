## InterchangeSkeletalMeshContentType Objects

```python
class InterchangeSkeletalMeshContentType(EnumBase)
```

EInterchange Skeletal Mesh Content Type

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeFactoryNodes
- **File**: InterchangeSkeletalMeshFactoryNode.h

<a id="unreal.InterchangeSkeletalMeshContentType.ALL"></a>

#### ALL

0: Imports all skeletal mesh content: geometry and skin weights.

<a id="unreal.InterchangeSkeletalMeshContentType.GEOMETRY"></a>

#### GEOMETRY

1: Imports the skeletal mesh geometry only. This creates a default skeleton, or maps the geometry to the existing one. You can import morph targets and LODs with the mesh.

<a id="unreal.InterchangeSkeletalMeshContentType.SKINNING_WEIGHTS"></a>

#### SKINNING_WEIGHTS

2: Imports the skeletal mesh skin weights only. No geometry, morph targets, or LODs are imported.

<a id="unreal.UsdDuplicateType"></a>