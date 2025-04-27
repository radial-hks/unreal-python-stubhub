## StreamingSourceShape Objects

```python
class StreamingSourceShape(StructBase)
```

Streaming Source Shape

**C++ Source:**

- **Module**: Engine
- **File**: WorldPartitionStreamingSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_sector`` (bool):  [Read-Write] Whether the source shape is a spherical sector instead of a regular sphere source.
- ``loading_range_scale`` (float):  [Read-Write] Applies a scale to the grid's loading range (used if bUseGridLoadingRange is True).
- ``location`` (Vector):  [Read-Write] Streaming source shape location (local to streaming source).
- ``radius`` (float):  [Read-Write] Custom streaming source shape radius (not used if bUseGridLoadingRange is True).
- ``rotation`` (Rotator):  [Read-Write] Streaming source shape rotation (local to streaming source).
- ``sector_angle`` (float):  [Read-Write] Shape's spherical sector angle in degree (not used if bIsSector is False).
- ``use_grid_loading_range`` (bool):  [Read-Write] If True, streaming source shape radius is bound to loading range radius.

<a id="unreal.StreamingSourceShape.__init__"></a>

#### __init__

```python
def __init__(use_grid_loading_range: bool = False,
             loading_range_scale: float = 0.000000,
             radius: float = 0.000000,
             is_sector: bool = False,
             sector_angle: float = 0.000000,
             location: Vector = [0.000000, 0.000000, 0.000000],
             rotation: Rotator = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.StreamingSourceShape.use_grid_loading_range"></a>

#### use_grid_loading_range

```python
@property
def use_grid_loading_range() -> bool
```

(bool):  [Read-Write] If True, streaming source shape radius is bound to loading range radius.

<a id="unreal.StreamingSourceShape.use_grid_loading_range"></a>

#### use_grid_loading_range

```python
@use_grid_loading_range.setter
def use_grid_loading_range(value: bool) -> None
```

<a id="unreal.StreamingSourceShape.loading_range_scale"></a>

#### loading_range_scale

```python
@property
def loading_range_scale() -> float
```

(float):  [Read-Write] Applies a scale to the grid's loading range (used if bUseGridLoadingRange is True).

<a id="unreal.StreamingSourceShape.loading_range_scale"></a>

#### loading_range_scale

```python
@loading_range_scale.setter
def loading_range_scale(value: float) -> None
```

<a id="unreal.StreamingSourceShape.radius"></a>

#### radius

```python
@property
def radius() -> float
```

(float):  [Read-Write] Custom streaming source shape radius (not used if bUseGridLoadingRange is True).

<a id="unreal.StreamingSourceShape.radius"></a>

#### radius

```python
@radius.setter
def radius(value: float) -> None
```

<a id="unreal.StreamingSourceShape.is_sector"></a>

#### is_sector

```python
@property
def is_sector() -> bool
```

(bool):  [Read-Write] Whether the source shape is a spherical sector instead of a regular sphere source.

<a id="unreal.StreamingSourceShape.is_sector"></a>

#### is_sector

```python
@is_sector.setter
def is_sector(value: bool) -> None
```

<a id="unreal.StreamingSourceShape.sector_angle"></a>

#### sector_angle

```python
@property
def sector_angle() -> float
```

(float):  [Read-Write] Shape's spherical sector angle in degree (not used if bIsSector is False).

<a id="unreal.StreamingSourceShape.sector_angle"></a>

#### sector_angle

```python
@sector_angle.setter
def sector_angle(value: float) -> None
```

<a id="unreal.StreamingSourceShape.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write] Streaming source shape location (local to streaming source).

<a id="unreal.StreamingSourceShape.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.StreamingSourceShape.rotation"></a>

#### rotation

```python
@property
def rotation() -> Rotator
```

(Rotator):  [Read-Write] Streaming source shape rotation (local to streaming source).

<a id="unreal.StreamingSourceShape.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Rotator) -> None
```

<a id="unreal.WorldPartitionStreamingQuerySource"></a>