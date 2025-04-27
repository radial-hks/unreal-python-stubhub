## NavLocalGridManager Objects

```python
class NavLocalGridManager(Object)
```

Manager for local navigation grids

Builds non overlapping grid from multiple sources, that can be used later for pathfinding.
Check also: UGridPathFollowingComponent, FNavLocalGridData

**C++ Source:**

- **Module**: AIModule
- **File**: NavLocalGridManager.h

<a id="unreal.NavLocalGridManager.set_local_navigation_grid_density"></a>

#### set_local_navigation_grid_density

```python
@classmethod
def set_local_navigation_grid_density(cls, world_context_object: Object,
                                      cell_size: float) -> bool
```

X.set_local_navigation_grid_density(world_context_object, cell_size) -> bool
Set Local Navigation Grid Density

Args:
    world_context_object (Object): 
    cell_size (float): 

Returns:
    bool:

<a id="unreal.NavLocalGridManager.remove_local_navigation_grid"></a>

#### remove_local_navigation_grid

```python
@classmethod
def remove_local_navigation_grid(cls,
                                 world_context_object: Object,
                                 grid_id: int,
                                 rebuild_grids: bool = True) -> None
```

X.remove_local_navigation_grid(world_context_object, grid_id, rebuild_grids=True) -> None
Remove Local Navigation Grid

Args:
    world_context_object (Object): 
    grid_id (int32): 
    rebuild_grids (bool):

<a id="unreal.NavLocalGridManager.find_local_navigation_grid_path"></a>

#### find_local_navigation_grid_path

```python
@classmethod
def find_local_navigation_grid_path(cls, world_context_object: Object,
                                    start: Vector,
                                    end: Vector) -> Optional[Array[Vector]]
```

X.find_local_navigation_grid_path(world_context_object, start, end) -> Array[Vector] or None
Find Local Navigation Grid Path

Args:
    world_context_object (Object): 
    start (Vector): 
    end (Vector): 

Returns:
    Array[Vector] or None: 

    path_points (Array[Vector]):

<a id="unreal.NavLocalGridManager.add_local_navigation_grid_for_points"></a>

#### add_local_navigation_grid_for_points

```python
@classmethod
def add_local_navigation_grid_for_points(cls,
                                         world_context_object: Object,
                                         locations: Array[Vector],
                                         radius2d: int = 5,
                                         height: float = 100.000000,
                                         rebuild_grids: bool = True) -> int
```

X.add_local_navigation_grid_for_points(world_context_object, locations, radius2d=5, height=100.000000, rebuild_grids=True) -> int32
creates single grid data for set of points

Args:
    world_context_object (Object): 
    locations (Array[Vector]): 
    radius2d (int32): 
    height (float): 
    rebuild_grids (bool): 

Returns:
    int32:

<a id="unreal.NavLocalGridManager.add_local_navigation_grid_for_point"></a>

#### add_local_navigation_grid_for_point

```python
@classmethod
def add_local_navigation_grid_for_point(cls,
                                        world_context_object: Object,
                                        location: Vector,
                                        radius2d: int = 5,
                                        height: float = 100.000000,
                                        rebuild_grids: bool = True) -> int
```

X.add_local_navigation_grid_for_point(world_context_object, location, radius2d=5, height=100.000000, rebuild_grids=True) -> int32
creates new grid data for single point

Args:
    world_context_object (Object): 
    location (Vector): 
    radius2d (int32): 
    height (float): 
    rebuild_grids (bool): 

Returns:
    int32:

<a id="unreal.NavLocalGridManager.add_local_navigation_grid_for_capsule"></a>

#### add_local_navigation_grid_for_capsule

```python
@classmethod
def add_local_navigation_grid_for_capsule(cls,
                                          world_context_object: Object,
                                          location: Vector,
                                          capsule_radius: float,
                                          capsule_half_height: float,
                                          radius2d: int = 5,
                                          height: float = 100.000000,
                                          rebuild_grids: bool = True) -> int
```

X.add_local_navigation_grid_for_capsule(world_context_object, location, capsule_radius, capsule_half_height, radius2d=5, height=100.000000, rebuild_grids=True) -> int32
Add Local Navigation Grid for Capsule

Args:
    world_context_object (Object): 
    location (Vector): 
    capsule_radius (float): 
    capsule_half_height (float): 
    radius2d (int32): 
    height (float): 
    rebuild_grids (bool): 

Returns:
    int32:

<a id="unreal.NavLocalGridManager.add_local_navigation_grid_for_box"></a>

#### add_local_navigation_grid_for_box

```python
@classmethod
def add_local_navigation_grid_for_box(cls,
                                      world_context_object: Object,
                                      location: Vector,
                                      extent: Vector = [
                                          1.000000, 1.000000, 1.000000
                                      ],
                                      rotation: Rotator = [
                                          0.000000, 0.000000, 0.000000
                                      ],
                                      radius2d: int = 5,
                                      height: float = 100.000000,
                                      rebuild_grids: bool = True) -> int
```

X.add_local_navigation_grid_for_box(world_context_object, location, extent=[1.000000, 1.000000, 1.000000], rotation=[0.000000, 0.000000, 0.000000], radius2d=5, height=100.000000, rebuild_grids=True) -> int32
Add Local Navigation Grid for Box

Args:
    world_context_object (Object): 
    location (Vector): 
    extent (Vector): 
    rotation (Rotator): 
    radius2d (int32): 
    height (float): 
    rebuild_grids (bool): 

Returns:
    int32:

<a id="unreal.AIPerceptionComponent"></a>