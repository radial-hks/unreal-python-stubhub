## FBXImportContentType Objects

```python
class FBXImportContentType(EnumBase)
```

EFBXImport Content Type

**C++ Source:**

- **Module**: UnrealEd
- **File**: FbxSkeletalMeshImportData.h

<a id="unreal.FBXImportContentType.FBXICT_ALL"></a>

#### FBXICT_ALL

0: Import all fbx content: geometry, skinning and weights.

<a id="unreal.FBXImportContentType.FBXICT_GEOMETRY"></a>

#### FBXICT_GEOMETRY

1: Import the skeletal mesh geometry only (will create a default skeleton, or map the geometry to the existing one). Morph and LOD can be imported with it.

<a id="unreal.FBXImportContentType.FBXICT_SKINNING_WEIGHTS"></a>

#### FBXICT_SKINNING_WEIGHTS

2: Import the skeletal mesh skinning and weights only (no geometry will be imported). Morph and LOD will not be imported with this settings.

<a id="unreal.MaterialSearchLocation"></a>