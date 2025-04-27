## AlembicImportType Objects

```python
class AlembicImportType(EnumBase)
```

Enum that describes type of asset to import

**C++ Source:**

- **Plugin**: AlembicImporter
- **Module**: AlembicLibrary
- **File**: AbcImportSettings.h

<a id="unreal.AlembicImportType.STATIC_MESH"></a>

#### STATIC_MESH

0: Imports only the first frame as one or multiple static meshes

<a id="unreal.AlembicImportType.GEOMETRY_CACHE"></a>

#### GEOMETRY_CACHE

1: Imports the Alembic file as flipbook and matrix animated objects

<a id="unreal.AlembicImportType.SKELETAL"></a>

#### SKELETAL

2: Imports the Alembic file as a skeletal mesh containing base poses as morph targets and blending between them to achieve the correct animation frame

<a id="unreal.BaseCalculationType"></a>