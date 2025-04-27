## NavArea_LowHeight Objects

```python
class NavArea_LowHeight(NavArea)
```

Special area that can be generated in spaces with insufficient free height above. Cannot be traversed by anyone.

**C++ Source:**

- **Module**: NavigationSystem
- **File**: NavArea_LowHeight.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_cost`` (float):  [Read-Write] travel cost multiplier for path distance
- ``draw_color`` (Color):  [Read-Write] area color in navigation view
- ``fixed_area_entering_cost`` (float):  [Read-Write] entering cost
- ``supported_agents`` (NavAgentSelector):  [Read-Write] restrict area only to specified agents

<a id="unreal.NavArea_Null"></a>