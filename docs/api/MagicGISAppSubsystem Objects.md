## MagicGISAppSubsystem Objects

```python
class MagicGISAppSubsystem(WorldSubsystem)
```

brief: GIS应用系统

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISCore
- **File**: MagicGISAppSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``geo_feature_clicked_notify_event`` (GeoFeatureClickedEvent):  [Read-Write] 交互事件，后续事件增多后可以放入单独的事件管理器中
  要素点击事件

<a id="unreal.MagicGISAppSubsystem.geo_feature_clicked_notify_event"></a>

#### geo\_feature\_clicked\_notify\_event

```python
@property
def geo_feature_clicked_notify_event() -> GeoFeatureClickedEvent
```

(GeoFeatureClickedEvent):  [Read-Write] 交互事件，后续事件增多后可以放入单独的事件管理器中
要素点击事件

<a id="unreal.MagicGISAppSubsystem.geo_feature_clicked_notify_event"></a>

#### geo\_feature\_clicked\_notify\_event

```python
@geo_feature_clicked_notify_event.setter
def geo_feature_clicked_notify_event(value: GeoFeatureClickedEvent) -> None
```

<a id="unreal.MagicGISAppSubsystem.set_local_lon_lat"></a>

#### set\_local\_lon\_lat

```python
def set_local_lon_lat(lon_lat: Vector2D) -> None
```

x.set_local_lon_lat(lon_lat) -> None
Set Local Lon Lat

Args:
    lon_lat (Vector2D):

<a id="unreal.MagicGISAppSubsystem.get_gis_reference_lon_lat"></a>

#### get\_gis\_reference\_lon\_lat

```python
def get_gis_reference_lon_lat() -> Vector2D
```

x.get_gis_reference_lon_lat() -> Vector2D
Get GISReference Lon Lat

Returns:
    Vector2D:

<a id="unreal.MagicGISInstancedStaticMeshComponent"></a>