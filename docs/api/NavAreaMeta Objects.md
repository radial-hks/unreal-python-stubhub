## NavAreaMeta Objects

```python
class NavAreaMeta(NavArea)
```

A convenience class for an area that has IsMetaArea() == true.
   Do not use this class when determining whether an area class is "meta".
   Call IsMetaArea instead.

**C++ Source:**

- **Module**: NavigationSystem
- **File**: NavAreaMeta.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_cost`` (float):  [Read-Write] travel cost multiplier for path distance
- ``draw_color`` (Color):  [Read-Write] area color in navigation view
- ``fixed_area_entering_cost`` (float):  [Read-Write] entering cost
- ``supported_agents`` (NavAgentSelector):  [Read-Write] restrict area only to specified agents

<a id="unreal.NavAreaMeta_SwitchByAgent"></a>