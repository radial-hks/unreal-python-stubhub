## NavDataConfig Objects

```python
class NavDataConfig(NavAgentProperties)
```

Nav Data Config

**C++ Source:**

- **Module**: Engine
- **File**: NavigationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``agent_height`` (float):  [Read-Write] Total height of the capsule used for navigation/pathfinding.
- ``agent_radius`` (float):  [Read-Write] Radius of the capsule used for navigation/pathfinding.
- ``agent_step_height`` (float):  [Read-Write] Step height to use, or -1 for default value from navdata's config.
- ``can_crouch`` (bool):  [Read-Write] If true, this Pawn is capable of crouching.
- ``can_fly`` (bool):  [Read-Write] If true, this Pawn is capable of flying.
- ``can_jump`` (bool):  [Read-Write] If true, this Pawn is capable of jumping.
- ``can_swim`` (bool):  [Read-Write] If true, this Pawn is capable of swimming or moving through fluid volumes.
- ``can_walk`` (bool):  [Read-Write] If true, this Pawn is capable of walking or moving on the ground.
- ``color`` (Color):  [Read-Write] Color used to represent this agent in the editor and for debugging
- ``default_query_extent`` (Vector):  [Read-Write] Rough size of this agent, used when projecting unto navigation mesh
- ``name`` (Name):  [Read-Write] Internal/debug name of this agent
- ``nav_data_class`` (Class):  [Read-Write] Class to use when spawning navigation data instance
- ``nav_walking_search_height_scale`` (float):  [Read-Write] Scale factor to apply to height of bounds when searching for navmesh to project to when nav walking
- ``preferred_nav_data`` (SoftClassPath):  [Read-Write] Type of navigation data used by agent, null means "any"

<a id="unreal.NavDataConfig.__init__"></a>

#### __init__

```python
def __init__(can_crouch: bool = False,
             can_jump: bool = False,
             can_walk: bool = False,
             can_swim: bool = False,
             can_fly: bool = False,
             agent_radius: float = 0.000000,
             agent_height: float = 0.000000,
             agent_step_height: float = 0.000000,
             nav_walking_search_height_scale: float = 0.000000,
             preferred_nav_data: SoftClassPath = [""],
             name: Name = "None",
             color: Color = [0, 0, 0, 0],
             default_query_extent: Vector = [0.000000, 0.000000, 0.000000],
             nav_data_class: Class = None) -> None
```

<a id="unreal.NavDataConfig.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write] Internal/debug name of this agent

<a id="unreal.NavDataConfig.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.NavDataConfig.color"></a>

#### color

```python
@property
def color() -> Color
```

(Color):  [Read-Write] Color used to represent this agent in the editor and for debugging

<a id="unreal.NavDataConfig.color"></a>

#### color

```python
@color.setter
def color(value: Color) -> None
```

<a id="unreal.NavDataConfig.default_query_extent"></a>

#### default_query_extent

```python
@property
def default_query_extent() -> Vector
```

(Vector):  [Read-Only] Rough size of this agent, used when projecting unto navigation mesh

<a id="unreal.NavDataConfig.nav_data_class"></a>

#### nav_data_class

```python
@property
def nav_data_class() -> Class
```

(Class):  [Read-Write] Class to use when spawning navigation data instance

<a id="unreal.NavDataConfig.nav_data_class"></a>

#### nav_data_class

```python
@nav_data_class.setter
def nav_data_class(value: Class) -> None
```

<a id="unreal.NavDataConfig.navigation_data_class_name"></a>

#### navigation_data_class_name

```python
@property
def navigation_data_class_name() -> Class
```

deprecated: 'navigation_data_class_name' was renamed to 'nav_data_class'.

<a id="unreal.NavDataConfig.navigation_data_class_name"></a>

#### navigation_data_class_name

```python
@navigation_data_class_name.setter
def navigation_data_class_name(value: Class) -> None
```

<a id="unreal.AlphaBlendArgs"></a>