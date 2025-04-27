## NavigationSystemConfig Objects

```python
class NavigationSystemConfig(Object)
```

Navigation System Config

**C++ Source:**

- **Module**: Engine
- **File**: NavigationSystemConfig.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_agent_name`` (Name):  [Read-Write] If not None indicates which of navigation datas and supported agents are
  going to be used as the default ones. If navigation agent of this type does
  not exist or is not enabled then the first available nav data will be used
  as the default one
- ``is_overriden`` (bool):  [Read-Only] If true it means the navigation system settings are overridden from another source (like a NavConfigOverrideActor)
- ``navigation_system_class`` (SoftClassPath):  [Read-Write]
- ``supported_agents_mask`` (NavAgentSelector):  [Read-Write] NavigationSystem's properties in Project Settings define all possible supported agents,
      but a specific navigation system can choose to support only a subset of agents.

<a id="unreal.ClothConfigBase"></a>