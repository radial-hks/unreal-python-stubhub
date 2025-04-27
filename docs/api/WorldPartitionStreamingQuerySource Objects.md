## WorldPartitionStreamingQuerySource Objects

```python
class WorldPartitionStreamingQuerySource(StructBase)
```

Structure containing all properties required to query a streaming state

**C++ Source:**

- **Module**: Engine
- **File**: WorldPartitionStreamingSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``data_layers`` (Array[Name]):  [Read-Write] Optional list of data layers to specialize the query. If empty only non data layer cells will be returned by the query.
- ``data_layers_only`` (bool):  [Read-Write] If True, Only cells that are in a data layer found in DataLayers property will be returned by the query.
- ``location`` (Vector):  [Read-Write] Location to query. (not used if bSpatialQuery is false)
- ``radius`` (float):  [Read-Write] Radius to query. (not used if bSpatialQuery is false)
- ``spatial_query`` (bool):  [Read-Write] If False, Location/Radius will not be used to find the cells. Only AlwaysLoaded cells will be returned by the query.
- ``use_grid_loading_range`` (bool):  [Read-Write] If True, Instead of providing a query radius, query can be bound to loading range radius.

<a id="unreal.WorldPartitionStreamingQuerySource.__init__"></a>

#### __init__

```python
def __init__(location: Vector = [0.000000, 0.000000, 0.000000],
             radius: float = 0.000000,
             use_grid_loading_range: bool = False,
             data_layers: Array[Name] = [],
             data_layers_only: bool = False,
             spatial_query: bool = False) -> None
```

<a id="unreal.WorldPartitionStreamingQuerySource.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write] Location to query. (not used if bSpatialQuery is false)

<a id="unreal.WorldPartitionStreamingQuerySource.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.WorldPartitionStreamingQuerySource.radius"></a>

#### radius

```python
@property
def radius() -> float
```

(float):  [Read-Write] Radius to query. (not used if bSpatialQuery is false)

<a id="unreal.WorldPartitionStreamingQuerySource.radius"></a>

#### radius

```python
@radius.setter
def radius(value: float) -> None
```

<a id="unreal.WorldPartitionStreamingQuerySource.use_grid_loading_range"></a>

#### use_grid_loading_range

```python
@property
def use_grid_loading_range() -> bool
```

(bool):  [Read-Write] If True, Instead of providing a query radius, query can be bound to loading range radius.

<a id="unreal.WorldPartitionStreamingQuerySource.use_grid_loading_range"></a>

#### use_grid_loading_range

```python
@use_grid_loading_range.setter
def use_grid_loading_range(value: bool) -> None
```

<a id="unreal.WorldPartitionStreamingQuerySource.data_layers"></a>

#### data_layers

```python
@property
def data_layers() -> Array[Name]
```

(Array[Name]):  [Read-Write] Optional list of data layers to specialize the query. If empty only non data layer cells will be returned by the query.

<a id="unreal.WorldPartitionStreamingQuerySource.data_layers"></a>

#### data_layers

```python
@data_layers.setter
def data_layers(value: Array[Name]) -> None
```

<a id="unreal.WorldPartitionStreamingQuerySource.data_layers_only"></a>

#### data_layers_only

```python
@property
def data_layers_only() -> bool
```

(bool):  [Read-Write] If True, Only cells that are in a data layer found in DataLayers property will be returned by the query.

<a id="unreal.WorldPartitionStreamingQuerySource.data_layers_only"></a>

#### data_layers_only

```python
@data_layers_only.setter
def data_layers_only(value: bool) -> None
```

<a id="unreal.WorldPartitionStreamingQuerySource.spatial_query"></a>

#### spatial_query

```python
@property
def spatial_query() -> bool
```

(bool):  [Read-Write] If False, Location/Radius will not be used to find the cells. Only AlwaysLoaded cells will be returned by the query.

<a id="unreal.WorldPartitionStreamingQuerySource.spatial_query"></a>

#### spatial_query

```python
@spatial_query.setter
def spatial_query(value: bool) -> None
```

<a id="unreal.ObservedComponent"></a>