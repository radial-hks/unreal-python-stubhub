## PCGOctreeQueries Objects

```python
class PCGOctreeQueries(BlueprintFunctionLibrary)
```

PCGOctree Queries

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGOctreeQueries.h

<a id="unreal.PCGOctreeQueries.get_points_inside_sphere"></a>

#### get_points_inside_sphere

```python
@classmethod
def get_points_inside_sphere(cls, point_data: PCGPointData, center: Vector,
                             radius: float) -> Array[PCGPoint]
```

X.get_points_inside_sphere(point_data, center, radius) -> Array[PCGPoint]
Query the internal octree to return all the points within some sphere.

Args:
    point_data (PCGPointData): 
    center (Vector): 
    radius (double): 

Returns:
    Array[PCGPoint]:

<a id="unreal.PCGOctreeQueries.get_points_inside_bounds"></a>

#### get_points_inside_bounds

```python
@classmethod
def get_points_inside_bounds(cls, point_data: PCGPointData,
                             bounds: Box) -> Array[PCGPoint]
```

X.get_points_inside_bounds(point_data, bounds) -> Array[PCGPoint]
Query the internal octree to return all the points within some bounds.

Args:
    point_data (PCGPointData): 
    bounds (Box): 

Returns:
    Array[PCGPoint]:

<a id="unreal.PCGOctreeQueries.get_farthest_point_from_other_point"></a>

#### get_farthest_point_from_other_point

```python
@classmethod
def get_farthest_point_from_other_point(
        cls,
        point_data: PCGPointData,
        point_index: int,
        search_distance: float = 20000.000000) -> Tuple[bool, PCGPoint]
```

X.get_farthest_point_from_other_point(point_data, point_index, search_distance=20000.000000) -> (out_found=bool, out_point=PCGPoint)
Get the farthest point from a given point within the search distance. The point is referenced by its point index in this point data.

Args:
    point_data (PCGPointData): 
    point_index (int32): 
    search_distance (double): 

Returns:
    tuple: 

    out_found (bool): 

    out_point (PCGPoint):

<a id="unreal.PCGOctreeQueries.get_farthest_point"></a>

#### get_farthest_point

```python
@classmethod
def get_farthest_point(
        cls,
        point_data: PCGPointData,
        center: Vector,
        search_distance: float = 20000.000000) -> Tuple[bool, PCGPoint]
```

X.get_farthest_point(point_data, center, search_distance=20000.000000) -> (out_found=bool, out_point=PCGPoint)
Get the farthest point from a given position, within the search distance.

Args:
    point_data (PCGPointData): 
    center (Vector): 
    search_distance (double): 

Returns:
    tuple: 

    out_found (bool): 

    out_point (PCGPoint):

<a id="unreal.PCGOctreeQueries.get_closest_point_from_other_point"></a>

#### get_closest_point_from_other_point

```python
@classmethod
def get_closest_point_from_other_point(
        cls,
        point_data: PCGPointData,
        point_index: int,
        search_distance: float = 20000.000000) -> Tuple[bool, PCGPoint]
```

X.get_closest_point_from_other_point(point_data, point_index, search_distance=20000.000000) -> (out_found=bool, out_point=PCGPoint)
Get the nearest point to a given point within the search distance. The point is referenced by its point index in this point data.

Args:
    point_data (PCGPointData): 
    point_index (int32): 
    search_distance (double): 

Returns:
    tuple: 

    out_found (bool): 

    out_point (PCGPoint):

<a id="unreal.PCGOctreeQueries.get_closest_point"></a>

#### get_closest_point

```python
@classmethod
def get_closest_point(
        cls,
        point_data: PCGPointData,
        center: Vector,
        discard_center: bool,
        search_distance: float = 20000.000000) -> Tuple[bool, PCGPoint]
```

X.get_closest_point(point_data, center, discard_center, search_distance=20000.000000) -> (out_found=bool, out_point=PCGPoint)
Get the closest point to a given position within the search distance. If bInDiscardCenter is true, will reject any points that is at the center exactly.

Args:
    point_data (PCGPointData): 
    center (Vector): 
    discard_center (bool): 
    search_distance (double): 

Returns:
    tuple: 

    out_found (bool): 

    out_point (PCGPoint):

<a id="unreal.PCGSettingsWithDynamicInputs"></a>