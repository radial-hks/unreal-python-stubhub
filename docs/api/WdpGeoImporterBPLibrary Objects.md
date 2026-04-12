## WdpGeoImporterBPLibrary Objects

```python
class WdpGeoImporterBPLibrary(BlueprintFunctionLibrary)
```

Wdp Geo Importer BPLibrary

**C++ Source:**

- **Plugin**: WdpDataModel
- **Module**: WdpGeoImporter
- **File**: WdpGeoImporterBPLibrary.h

<a id="unreal.WdpGeoImporterBPLibrary.import_shapefile"></a>

#### import\_shapefile

```python
@classmethod
def import_shapefile(
    cls, file_path: str
) -> Optional[Tuple[Array[Vector], Array[WdpPolyline], Array[WdpPolygon]]]
```

X.import_shapefile(file_path) -> (points=Array[Vector], lines=Array[WdpPolyline], polygons=Array[WdpPolygon]) or None
Import Shapefile

Args:
    file_path (str): 

Returns:
    tuple or None: 

    points (Array[Vector]): 

    lines (Array[WdpPolyline]): 

    polygons (Array[WdpPolygon]):

<a id="unreal.WdpGeoImporterBPLibrary.import_geo_json"></a>

#### import\_geo\_json

```python
@classmethod
def import_geo_json(
    cls, file_path: str
) -> Optional[Tuple[Array[Vector], Array[WdpPolyline], Array[WdpPolygon]]]
```

X.import_geo_json(file_path) -> (points=Array[Vector], lines=Array[WdpPolyline], polygons=Array[WdpPolygon]) or None
Import Geo Json

Args:
    file_path (str): 

Returns:
    tuple or None: 

    points (Array[Vector]): 

    lines (Array[WdpPolyline]): 

    polygons (Array[WdpPolygon]):

<a id="unreal.Player"></a>