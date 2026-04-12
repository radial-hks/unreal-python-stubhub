## WdpGeometryAPI Objects

```python
class WdpGeometryAPI(StandardApiClassBase)
```

Wdp Geometry API

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: WdpGeometryAPI.h

<a id="unreal.WdpGeometryAPI.start_show_coord"></a>

#### start\_show\_coord

```python
def start_show_coord(params: WdpStartShowCoordParams) -> Optional[ResultBase]
```

x.start_show_coord(params) -> ResultBase or None
Start Show Coord

Args:
    params (WdpStartShowCoordParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpGeometryAPI.end_show_coord"></a>

#### end\_show\_coord

```python
def end_show_coord(params: ParamsBase) -> Optional[ResultBase]
```

x.end_show_coord(params) -> ResultBase or None
End Show Coord

Args:
    params (ParamsBase): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpGeometryAPI.enable_geometry_draw"></a>

#### enable\_geometry\_draw

```python
def enable_geometry_draw(params: ParamsBase) -> Optional[ResultBase]
```

x.enable_geometry_draw(params) -> ResultBase or None
2D APIs

Args:
    params (ParamsBase): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpGeometryAPI.disable_geometry_draw"></a>

#### disable\_geometry\_draw

```python
def disable_geometry_draw(params: ParamsBase) -> Optional[ResultBase]
```

x.disable_geometry_draw(params) -> ResultBase or None
Disable Geometry Draw

Args:
    params (ParamsBase): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpGeometryAPI.create_geometry_entities_from_shapefile"></a>

#### create\_geometry\_entities\_from\_shapefile

```python
def create_geometry_entities_from_shapefile(
    params: CreateGeometryEntitiesParams
) -> Optional[CreateGeometryEntitiesResult]
```

x.create_geometry_entities_from_shapefile(params) -> CreateGeometryEntitiesResult or None
Create Geometry Entities from Shapefile

Args:
    params (CreateGeometryEntitiesParams): 

Returns:
    CreateGeometryEntitiesResult or None: 

    out_result (CreateGeometryEntitiesResult):

<a id="unreal.WdpGeometryAPI.create_geometry_entities_from_geo_json"></a>

#### create\_geometry\_entities\_from\_geo\_json

```python
def create_geometry_entities_from_geo_json(
    params: CreateGeometryEntitiesParams
) -> Optional[CreateGeometryEntitiesResult]
```

x.create_geometry_entities_from_geo_json(params) -> CreateGeometryEntitiesResult or None
Create Geometry Entities from Geo Json

Args:
    params (CreateGeometryEntitiesParams): 

Returns:
    CreateGeometryEntitiesResult or None: 

    out_result (CreateGeometryEntitiesResult):

<a id="unreal.WdpSceneAPI"></a>