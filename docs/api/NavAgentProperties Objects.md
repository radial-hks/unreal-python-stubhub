## NavAgentProperties Objects

```python
class NavAgentProperties(MovementProperties)
```

Properties of representation of an 'agent' (or Pawn) used by AI navigation/pathfinding.

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
- ``nav_walking_search_height_scale`` (float):  [Read-Write] Scale factor to apply to height of bounds when searching for navmesh to project to when nav walking
- ``preferred_nav_data`` (SoftClassPath):  [Read-Write] Type of navigation data used by agent, null means "any"

<a id="unreal.NavAgentProperties.__init__"></a>

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
             preferred_nav_data: SoftClassPath = [""]) -> None
```

<a id="unreal.NavAgentProperties.agent_radius"></a>

#### agent_radius

```python
@property
def agent_radius() -> float
```

(float):  [Read-Write] Radius of the capsule used for navigation/pathfinding.

<a id="unreal.NavAgentProperties.agent_radius"></a>

#### agent_radius

```python
@agent_radius.setter
def agent_radius(value: float) -> None
```

<a id="unreal.NavAgentProperties.agent_height"></a>

#### agent_height

```python
@property
def agent_height() -> float
```

(float):  [Read-Write] Total height of the capsule used for navigation/pathfinding.

<a id="unreal.NavAgentProperties.agent_height"></a>

#### agent_height

```python
@agent_height.setter
def agent_height(value: float) -> None
```

<a id="unreal.NavAgentProperties.agent_step_height"></a>

#### agent_step_height

```python
@property
def agent_step_height() -> float
```

(float):  [Read-Write] Step height to use, or -1 for default value from navdata's config.

<a id="unreal.NavAgentProperties.agent_step_height"></a>

#### agent_step_height

```python
@agent_step_height.setter
def agent_step_height(value: float) -> None
```

<a id="unreal.NavAgentProperties.nav_walking_search_height_scale"></a>

#### nav_walking_search_height_scale

```python
@property
def nav_walking_search_height_scale() -> float
```

(float):  [Read-Write] Scale factor to apply to height of bounds when searching for navmesh to project to when nav walking

<a id="unreal.NavAgentProperties.nav_walking_search_height_scale"></a>

#### nav_walking_search_height_scale

```python
@nav_walking_search_height_scale.setter
def nav_walking_search_height_scale(value: float) -> None
```

<a id="unreal.NavAgentProperties.preferred_nav_data"></a>

#### preferred_nav_data

```python
@property
def preferred_nav_data() -> SoftClassPath
```

(SoftClassPath):  [Read-Write] Type of navigation data used by agent, null means "any"

<a id="unreal.NavAgentProperties.preferred_nav_data"></a>

#### preferred_nav_data

```python
@preferred_nav_data.setter
def preferred_nav_data(value: SoftClassPath) -> None
```

<a id="unreal.NavDataConfig"></a>