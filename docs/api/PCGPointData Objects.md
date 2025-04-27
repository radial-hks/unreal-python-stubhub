## PCGPointData Objects

```python
class PCGPointData(PCGSpatialData)
```

TODO: Split this in "concrete" vs "api" class (needed for views)

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGPointData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``keep_zero_density_points`` (bool):  [Read-Write]
- ``metadata`` (PCGMetadata):  [Read-Only] Not accessible through blueprint to make sure the constness is preserved
- ``target_actor`` (Actor):  [Read-Write] Recipient of any artifacts generated using this data.

<a id="unreal.PCGPointData.set_points"></a>

#### set_points

```python
def set_points(points: Array[PCGPoint]) -> None
```

x.set_points(points) -> None
Set Points

Args:
    points (Array[PCGPoint]):

<a id="unreal.PCGPointData.is_empty"></a>

#### is_empty

```python
def is_empty() -> bool
```

x.is_empty() -> bool
Is Empty

Returns:
    bool:

<a id="unreal.PCGPointData.get_points_copy"></a>

#### get_points_copy

```python
def get_points_copy() -> Array[PCGPoint]
```

x.get_points_copy() -> Array[PCGPoint]
Get Points Copy

Returns:
    Array[PCGPoint]:

<a id="unreal.PCGPointData.get_points"></a>

#### get_points

```python
def get_points() -> Array[PCGPoint]
```

x.get_points() -> Array[PCGPoint]
Get Points

Returns:
    Array[PCGPoint]:

<a id="unreal.PCGPointData.get_point"></a>

#### get_point

```python
def get_point(index: int) -> PCGPoint
```

x.get_point(index) -> PCGPoint
Get Point

Args:
    index (int32): 

Returns:
    PCGPoint:

<a id="unreal.PCGPointData.get_num_points"></a>

#### get_num_points

```python
def get_num_points() -> int
```

x.get_num_points() -> int32
Get Num Points

Returns:
    int32:

<a id="unreal.PCGPointData.copy_points_from"></a>

#### copy_points_from

```python
def copy_points_from(data: PCGPointData, data_indices: Array[int]) -> None
```

x.copy_points_from(data, data_indices) -> None
Copy Points From

Args:
    data (PCGPointData): 
    data_indices (Array[int32]):

<a id="unreal.PCGPrimitiveData"></a>