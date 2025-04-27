## NavArea_Obstacle Objects

```python
class NavArea_Obstacle(NavArea)
```

In general represents a high cost area, that shouldn't be traversed by anyone unless no other path exist.

**C++ Source:**

- **Module**: NavigationSystem
- **File**: NavArea_Obstacle.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_cost`` (float):  [Read-Write] travel cost multiplier for path distance
- ``draw_color`` (Color):  [Read-Write] area color in navigation view
- ``fixed_area_entering_cost`` (float):  [Read-Write] entering cost
- ``supported_agents`` (NavAgentSelector):  [Read-Write] restrict area only to specified agents

<a id="unreal.RecastFilter_UseDefaultArea"></a>