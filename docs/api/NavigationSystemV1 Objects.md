## NavigationSystemV1 Objects

```python
class NavigationSystemV1(NavigationSystemBase)
```

Navigation System V1

**C++ Source:**

- **Module**: NavigationSystem
- **File**: NavigationSystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active_tiles_update_interval`` (float):  [Read-Write] Minimal time, in seconds, between active tiles set update
- ``allow_client_side_navigation`` (bool):  [Read-Write] If false, will not create nav collision when connecting as a client
- ``auto_create_navigation_data`` (bool):  [Read-Write] Should navigation system spawn default Navigation Data when there's none and there are navigation bounds present?
- ``crowd_manager_class`` (Class):  [Read-Write]
- ``data_gathering_mode`` (NavDataGatheringModeConfig):  [Read-Write] Sets how navigation data should be gathered when building collision information
- ``default_agent_name`` (Name):  [Read-Write] If not None indicates which of navigation datas and supported agents are
  going to be used as the default ones. If navigation agent of this type does
  not exist or is not enabled then the first available nav data will be used
  as the default one
- ``dirty_area_warning_size_threshold`` (float):  [Read-Write] -1 by default, if set to a positive value dirty areas with any dimensions in 2d over the threshold created at runtime will be logged
- ``gathering_nav_modifiers_warning_limit_time`` (float):  [Read-Write] -1.0f by default, if set to a positive value, all calls to GetNavigationData will be timed and compared to it.
       Over the limit calls will be logged as warnings.
       In seconds. Non-shipping build only.
- ``generate_navigation_only_around_navigation_invokers`` (bool):  [Read-Write] If set to true navigation will be generated only around registered "navigation enforcers"
       This has a range of consequences (including how navigation octree operates) so it needs to
       be a conscious decision.
       Once enabled results in whole world being navigable.
  see: RegisterNavigationInvoker
- ``geometry_export_triangle_count_warning_threshold`` (int32):  [Read-Write] Warnings are logged if exporting the navigation collision for an object exceed this triangle count.
  Use -1 to disable.
- ``initial_building_locked`` (bool):  [Read-Write] if set to true will result navigation system not rebuild navigation until
      a call to ReleaseInitialBuildingLock() is called. Does not influence
      editor-time generation (i.e. does influence PIE and Game).
      Defaults to false.
- ``invokers_maximum_distance_from_seed`` (double):  [Read-Write] When in use, invokers farther away from any invoker seed will be ignored (set to -1 to disable).
- ``on_navigation_generation_finished_delegate`` (OnNavDataGenericEvent):  [Read-Write]
- ``should_discard_sub_level_nav_data`` (bool):  [Read-Write] If true, games should ignore navigation data inside loaded sublevels
- ``skip_agent_height_check_when_picking_nav_data`` (bool):  [Read-Write] false by default, if set to true will result in not caring about nav agent height
      when trying to match navigation data to passed in nav agent
- ``spawn_nav_data_in_nav_bounds_level`` (bool):  [Read-Write] If true will try to spawn the navigation data instance in the sublevel with navigation bounds, if false it will spawn in the persistent level
- ``supported_agents`` (Array[NavDataConfig]):  [Read-Write] List of agents types supported by this navigation system
- ``supported_agents_mask`` (NavAgentSelector):  [Read-Write] NavigationSystem's properties in Project Settings define all possible supported agents,
      but a specific navigation system can choose to support only a subset of agents. Set via
      NavigationSystemConfig
- ``tick_while_paused`` (bool):  [Read-Write] If true, will update navigation even when the game is paused

<a id="unreal.NavigationSystemV1.default_agent_name"></a>

#### default_agent_name

```python
@property
def default_agent_name() -> Name
```

(Name):  [Read-Only] If not None indicates which of navigation datas and supported agents are
going to be used as the default ones. If navigation agent of this type does
not exist or is not enabled then the first available nav data will be used
as the default one

<a id="unreal.NavigationSystemV1.crowd_manager_class"></a>

#### crowd_manager_class

```python
@property
def crowd_manager_class() -> Class
```

(Class):  [Read-Only]

<a id="unreal.NavigationSystemV1.on_navigation_generation_finished_delegate"></a>

#### on_navigation_generation_finished_delegate

```python
@property
def on_navigation_generation_finished_delegate() -> OnNavDataGenericEvent
```

(OnNavDataGenericEvent):  [Read-Write]

<a id="unreal.NavigationSystemV1.on_navigation_generation_finished_delegate"></a>

#### on_navigation_generation_finished_delegate

```python
@on_navigation_generation_finished_delegate.setter
def on_navigation_generation_finished_delegate(
        value: OnNavDataGenericEvent) -> None
```

<a id="unreal.NavigationSystemV1.unregister_navigation_invoker"></a>

#### unregister_navigation_invoker

```python
def unregister_navigation_invoker(invoker: Actor) -> None
```

x.unregister_navigation_invoker(invoker) -> None
Removes given actor from the list of active navigation enforcers.
see: RegisterNavigationInvoker for more details

Args:
    invoker (Actor):

<a id="unreal.NavigationSystemV1.set_max_simultaneous_tile_generation_jobs_count"></a>

#### set_max_simultaneous_tile_generation_jobs_count

```python
def set_max_simultaneous_tile_generation_jobs_count(
        max_number_of_jobs: int) -> None
```

x.set_max_simultaneous_tile_generation_jobs_count(max_number_of_jobs) -> None
will limit the number of simultaneously running navmesh tile generation jobs to specified number.

Args:
    max_number_of_jobs (int32): gets trimmed to be at least 1. You cannot use this function to pause navmesh generation

<a id="unreal.NavigationSystemV1.set_geometry_gathering_mode"></a>

#### set_geometry_gathering_mode

```python
def set_geometry_gathering_mode(new_mode: NavDataGatheringModeConfig) -> None
```

x.set_geometry_gathering_mode(new_mode) -> None
Set Geometry Gathering Mode

Args:
    new_mode (NavDataGatheringModeConfig):

<a id="unreal.NavigationSystemV1.reset_max_simultaneous_tile_generation_jobs_count"></a>

#### reset_max_simultaneous_tile_generation_jobs_count

```python
def reset_max_simultaneous_tile_generation_jobs_count() -> None
```

x.reset_max_simultaneous_tile_generation_jobs_count() -> None
Brings limit of simultaneous navmesh tile generation jobs back to Project Setting's default value

<a id="unreal.NavigationSystemV1.register_navigation_invoker"></a>

#### register_navigation_invoker

```python
def register_navigation_invoker(
        invoker: Actor,
        tile_generation_radius: float = 3000.000000,
        tile_removal_radius: float = 5000.000000) -> None
```

x.register_navigation_invoker(invoker, tile_generation_radius=3000.000000, tile_removal_radius=5000.000000) -> None
Registers given actor as a "navigation enforcer" which means navigation system will
    make sure navigation is being generated in specified radius around it.
note:: you need NavigationSystem's GenerateNavigationOnlyAroundNavigationInvokers to be set to true to take advantage of this feature

Args:
    invoker (Actor): 
    tile_generation_radius (float): 
    tile_removal_radius (float):

<a id="unreal.NavigationSystemV1.on_navigation_bounds_updated"></a>

#### on_navigation_bounds_updated

```python
def on_navigation_bounds_updated(nav_volume: NavMeshBoundsVolume) -> None
```

x.on_navigation_bounds_updated(nav_volume) -> None

todo: document

Args:
    nav_volume (NavMeshBoundsVolume):

<a id="unreal.NavigationSystemV1.navigation_raycast"></a>

#### navigation_raycast

```python
@classmethod
def navigation_raycast(cls,
                       world_context_object: Object,
                       ray_start: Vector,
                       ray_end: Vector,
                       filter_class: Class = None,
                       querier: Controller = None) -> Optional[Vector]
```

X.navigation_raycast(world_context_object, ray_start, ray_end, filter_class=None, querier=None) -> Vector or None
Performs navigation raycast on NavigationData appropriate for given Querier.

Args:
    world_context_object (Object): 
    ray_start (Vector): 
    ray_end (Vector): 
    filter_class (type(Class)): 
    querier (Controller): if not passed default navigation data will be used

Returns:
    Vector or None: true if line from RayStart to RayEnd was obstructed. Also, true when no navigation data present

    hit_location (Vector): if line was obstructed this will be set to hit location. Otherwise it contains SegmentEnd

<a id="unreal.NavigationSystemV1.k2_replace_area_in_octree_data"></a>

#### k2_replace_area_in_octree_data

```python
def k2_replace_area_in_octree_data(object: Object, old_area: Class,
                                   new_area: Class) -> bool
```

x.k2_replace_area_in_octree_data(object, old_area, new_area) -> bool
K2 Replace Area in Octree Data

Args:
    object (Object): 
    old_area (type(Class)): 
    new_area (type(Class)): 

Returns:
    bool:

<a id="unreal.NavigationSystemV1.project_point_to_navigation"></a>

#### project_point_to_navigation

```python
@classmethod
def project_point_to_navigation(
        cls,
        world_context_object: Object,
        point: Vector,
        nav_data: NavigationData,
        filter_class: Class,
        query_extent: Vector = [0.000000, 0.000000,
                                0.000000]) -> Optional[Vector]
```

X.project_point_to_navigation(world_context_object, point, nav_data, filter_class, query_extent=[0.000000, 0.000000, 0.000000]) -> Vector or None
Project a point onto the NavigationData

Args:
    world_context_object (Object): 
    point (Vector): 
    nav_data (NavigationData): 
    filter_class (type(Class)): 
    query_extent (Vector): 

Returns:
    Vector or None: 

    projected_location (Vector):

<a id="unreal.NavigationSystemV1.get_random_reachable_point_in_radius"></a>

#### get_random_reachable_point_in_radius

```python
@classmethod
def get_random_reachable_point_in_radius(
        cls,
        world_context_object: Object,
        origin: Vector,
        radius: float,
        nav_data: NavigationData = None,
        filter_class: Class = None) -> Optional[Vector]
```

X.get_random_reachable_point_in_radius(world_context_object, origin, radius, nav_data=None, filter_class=None) -> Vector or None
Generates a random location reachable from given Origin location.

Args:
    world_context_object (Object): 
    origin (Vector): 
    radius (float): 
    nav_data (NavigationData): 
    filter_class (type(Class)): 

Returns:
    Vector or None: Return Value represents if the call was successful

    random_location (Vector):

<a id="unreal.NavigationSystemV1.get_random_point_in_navigable_radius"></a>

#### get_random_point_in_navigable_radius

```python
@classmethod
def get_random_point_in_navigable_radius(
        cls,
        world_context_object: Object,
        origin: Vector,
        radius: float,
        nav_data: NavigationData = None,
        filter_class: Class = None) -> Optional[Vector]
```

X.get_random_point_in_navigable_radius(world_context_object, origin, radius, nav_data=None, filter_class=None) -> Vector or None
K2 Get Random Point in Navigable Radius
deprecated: GetRandomPointInNavigableRadius is deprecated. Use GetRandomLocationInNavigableRadius instead

Args:
    world_context_object (Object): 
    origin (Vector): 
    radius (float): 
    nav_data (NavigationData): 
    filter_class (type(Class)): 

Returns:
    Vector or None: 

    random_location (Vector):

<a id="unreal.NavigationSystemV1.get_random_location_in_navigable_radius"></a>

#### get_random_location_in_navigable_radius

```python
@classmethod
def get_random_location_in_navigable_radius(
        cls,
        world_context_object: Object,
        origin: Vector,
        radius: float,
        nav_data: NavigationData = None,
        filter_class: Class = None) -> Optional[Vector]
```

X.get_random_location_in_navigable_radius(world_context_object, origin, radius, nav_data=None, filter_class=None) -> Vector or None
Generates a random location in navigable space within given radius of Origin.

Args:
    world_context_object (Object): 
    origin (Vector): 
    radius (float): 
    nav_data (NavigationData): 
    filter_class (type(Class)): 

Returns:
    Vector or None: Return Value represents if the call was successful

    random_location (Vector):

<a id="unreal.NavigationSystemV1.is_navigation_being_built_or_locked"></a>

#### is_navigation_being_built_or_locked

```python
@classmethod
def is_navigation_being_built_or_locked(cls,
                                        world_context_object: Object) -> bool
```

X.is_navigation_being_built_or_locked(world_context_object) -> bool
Is Navigation Being Built or Locked

Args:
    world_context_object (Object): 

Returns:
    bool:

<a id="unreal.NavigationSystemV1.is_navigation_being_built"></a>

#### is_navigation_being_built

```python
@classmethod
def is_navigation_being_built(cls, world_context_object: Object) -> bool
```

X.is_navigation_being_built(world_context_object) -> bool
Is Navigation Being Built

Args:
    world_context_object (Object): 

Returns:
    bool:

<a id="unreal.NavigationSystemV1.get_path_length"></a>

#### get_path_length

```python
@classmethod
def get_path_length(
        cls,
        world_context_object: Object,
        path_start: Vector,
        path_end: Vector,
        nav_data: NavigationData = None,
        filter_class: Class = None) -> Tuple[NavigationQueryResult, float]
```

X.get_path_length(world_context_object, path_start, path_end, nav_data=None, filter_class=None) -> (NavigationQueryResult, path_length=double)
Potentially expensive. Use with caution

Args:
    world_context_object (Object): 
    path_start (Vector): 
    path_end (Vector): 
    nav_data (NavigationData): 
    filter_class (type(Class)): 

Returns:
    double: 

    path_length (double):

<a id="unreal.NavigationSystemV1.get_path_cost"></a>

#### get_path_cost

```python
@classmethod
def get_path_cost(
        cls,
        world_context_object: Object,
        path_start: Vector,
        path_end: Vector,
        nav_data: NavigationData = None,
        filter_class: Class = None) -> Tuple[NavigationQueryResult, float]
```

X.get_path_cost(world_context_object, path_start, path_end, nav_data=None, filter_class=None) -> (NavigationQueryResult, path_cost=double)
Potentially expensive. Use with caution. Consider using UPathFollowingComponent::GetRemainingPathCost instead

Args:
    world_context_object (Object): 
    path_start (Vector): 
    path_end (Vector): 
    nav_data (NavigationData): 
    filter_class (type(Class)): 

Returns:
    double: 

    path_cost (double):

<a id="unreal.NavigationSystemV1.get_navigation_system"></a>

#### get_navigation_system

```python
@classmethod
def get_navigation_system(cls,
                          world_context_object: Object) -> NavigationSystemV1
```

X.get_navigation_system(world_context_object) -> NavigationSystemV1
Blueprint functions

Args:
    world_context_object (Object): 

Returns:
    NavigationSystemV1:

<a id="unreal.NavigationSystemV1.find_path_to_location_synchronously"></a>

#### find_path_to_location_synchronously

```python
@classmethod
def find_path_to_location_synchronously(
        cls,
        world_context_object: Object,
        path_start: Vector,
        path_end: Vector,
        pathfinding_context: Actor = None,
        filter_class: Class = None) -> NavigationPath
```

X.find_path_to_location_synchronously(world_context_object, path_start, path_end, pathfinding_context=None, filter_class=None) -> NavigationPath
Finds path instantly, in a FindPath Synchronously.

Args:
    world_context_object (Object): 
    path_start (Vector): 
    path_end (Vector): 
    pathfinding_context (Actor): could be one of following: NavigationData (like Navmesh actor), Pawn or Controller. This parameter determines parameters of specific pathfinding query
    filter_class (type(Class)): 

Returns:
    NavigationPath:

<a id="unreal.NavigationSystemV1.find_path_to_actor_synchronously"></a>

#### find_path_to_actor_synchronously

```python
@classmethod
def find_path_to_actor_synchronously(
        cls,
        world_context_object: Object,
        path_start: Vector,
        goal_actor: Actor,
        tether_distance: float = 50.000000,
        pathfinding_context: Actor = None,
        filter_class: Class = None) -> NavigationPath
```

X.find_path_to_actor_synchronously(world_context_object, path_start, goal_actor, tether_distance=50.000000, pathfinding_context=None, filter_class=None) -> NavigationPath
Finds path instantly, in a FindPath Synchronously. Main advantage over FindPathToLocationSynchronously is that
    the resulting path will automatically get updated if goal actor moves more than TetherDistance away from last path node

Args:
    world_context_object (Object): 
    path_start (Vector): 
    goal_actor (Actor): 
    tether_distance (float): 
    pathfinding_context (Actor): could be one of following: NavigationData (like Navmesh actor), Pawn or Controller. This parameter determines parameters of specific pathfinding query
    filter_class (type(Class)): 

Returns:
    NavigationPath:

<a id="unreal.NavigationSystem"></a>