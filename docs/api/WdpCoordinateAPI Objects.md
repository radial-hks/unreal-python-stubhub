## WdpCoordinateAPI Objects

```python
class WdpCoordinateAPI(StandardApiClassBase)
```

Wdp Coordinate API

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCoordinateAPI.h

<a id="unreal.WdpCoordinateAPI.world_pos_to_screen_pos"></a>

#### world\_pos\_to\_screen\_pos

```python
def world_pos_to_screen_pos(
        world_pos: WdpWorldPosParams) -> Optional[WdpScreenPosResult]
```

x.world_pos_to_screen_pos(world_pos) -> WdpScreenPosResult or None
World Pos to Screen Pos

Args:
    world_pos (WdpWorldPosParams): 

Returns:
    WdpScreenPosResult or None: 

    screen_pos (WdpScreenPosResult):

<a id="unreal.WdpCoordinateAPI.local_to_global_geo_ref"></a>

#### local\_to\_global\_geo\_ref

```python
def local_to_global_geo_ref(
    params: WdpLocalToGlobalGeoRefParams
) -> Optional[WdpLocalToGlobalGeoRefResult]
```

x.local_to_global_geo_ref(params) -> WdpLocalToGlobalGeoRefResult or None
Local to Global Geo Ref

Args:
    params (WdpLocalToGlobalGeoRefParams): 

Returns:
    WdpLocalToGlobalGeoRefResult or None: 

    result (WdpLocalToGlobalGeoRefResult):

<a id="unreal.WdpCoordinateAPI.global_to_local_geo_ref"></a>

#### global\_to\_local\_geo\_ref

```python
def global_to_local_geo_ref(
    params: WdpLocalToGlobalGeoRefParams
) -> Optional[WdpLocalToGlobalGeoRefResult]
```

x.global_to_local_geo_ref(params) -> WdpLocalToGlobalGeoRefResult or None
Global to Local Geo Ref

Args:
    params (WdpLocalToGlobalGeoRefParams): 

Returns:
    WdpLocalToGlobalGeoRefResult or None: 

    result (WdpLocalToGlobalGeoRefResult):

<a id="unreal.WdpCoordinateAPI.gis_to_screen_pos"></a>

#### gis\_to\_screen\_pos

```python
def gis_to_screen_pos(
        params: WdpCoordinateTransformParams
) -> Optional[WdpScreenPositionResult]
```

x.gis_to_screen_pos(params) -> WdpScreenPositionResult or None
GISTo Screen Pos

Args:
    params (WdpCoordinateTransformParams): 

Returns:
    WdpScreenPositionResult or None: 

    results (WdpScreenPositionResult):

<a id="unreal.WdpCoordinateAPI.gis_to_cartesian"></a>

#### gis\_to\_cartesian

```python
def gis_to_cartesian(
    params: WdpCoordinateTransformParams
) -> Optional[WdpCoordinateTransformResults]
```

x.gis_to_cartesian(params) -> WdpCoordinateTransformResults or None
APIs

Args:
    params (WdpCoordinateTransformParams): 

Returns:
    WdpCoordinateTransformResults or None: 

    results (WdpCoordinateTransformResults):

<a id="unreal.WdpCoordinateAPI.create_cad_geo_ref"></a>

#### create\_cad\_geo\_ref

```python
def create_cad_geo_ref(
        params: WdpCreateCADGeoRefParams) -> Optional[EidResult]
```

x.create_cad_geo_ref(params) -> EidResult or None
Create CADGeo Ref

Args:
    params (WdpCreateCADGeoRefParams): 

Returns:
    EidResult or None: 

    result (EidResult):

<a id="unreal.WdpCoordinateAPI.cartesian_to_gis"></a>

#### cartesian\_to\_gis

```python
def cartesian_to_gis(
    params: WdpCoordinateTransformParams
) -> Optional[WdpCoordinateTransformResults]
```

x.cartesian_to_gis(params) -> WdpCoordinateTransformResults or None
Cartesian to GIS

Args:
    params (WdpCoordinateTransformParams): 

Returns:
    WdpCoordinateTransformResults or None: 

    results (WdpCoordinateTransformResults):

<a id="unreal.WdpEnvironmentAPI"></a>