## AbcGeometryCacheMotionVectorsImport Objects

```python
class AbcGeometryCacheMotionVectorsImport(EnumBase)
```

EAbc Geometry Cache Motion Vectors Import

**C++ Source:**

- **Plugin**: AlembicImporter
- **Module**: AlembicLibrary
- **File**: AbcImportSettings.h

<a id="unreal.AbcGeometryCacheMotionVectorsImport.NO_MOTION_VECTORS"></a>

#### NO_MOTION_VECTORS

0: No motion vectors will be present in the geometry cache.

<a id="unreal.AbcGeometryCacheMotionVectorsImport.IMPORT_ABC_VELOCITIES_AS_MOTION_VECTORS"></a>

#### IMPORT_ABC_VELOCITIES_AS_MOTION_VECTORS

1: Imports the Velocities from the Alembic file and converts them to motion vectors. This will increase file size as the motion vectors will be stored on disc.

<a id="unreal.AbcGeometryCacheMotionVectorsImport.CALCULATE_MOTION_VECTORS_DURING_IMPORT"></a>

#### CALCULATE_MOTION_VECTORS_DURING_IMPORT

2: Force calculation of motion vectors during import. This will increase file size as the motion vectors will be stored on disc.

<a id="unreal.MotionExtractor_MotionType"></a>