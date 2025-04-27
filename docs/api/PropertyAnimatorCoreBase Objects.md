## PropertyAnimatorCoreBase Objects

```python
class PropertyAnimatorCoreBase(Object)
```

Abstract base class for any Animator, holds a set of linked properties

**C++ Source:**

- **Plugin**: PropertyAnimatorCore
- **Module**: PropertyAnimatorCore
- **File**: PropertyAnimatorCoreBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active_time_source`` (PropertyAnimatorCoreTimeSourceBase):  [Read-Only] Active time source with its options, determined by its name
- ``animator_display_name`` (Name):  [Read-Only] Display name as title property for component array, hide it but must be visible to editor for array title property
- ``animator_enabled`` (bool):  [Read-Write] Enable control of properties linked to this Animator
- ``linked_properties`` (Array[PropertyAnimatorCoreContext]):  [Read-Write] Context for properties linked to this Animator
- ``override_time_source`` (bool):  [Read-Write] Use the global time source or override it on this animator
- ``time_source_name`` (Name):  [Read-Write] The time source to use
- ``time_sources_instances`` (Map[Name, PropertyAnimatorCoreTimeSourceBase]):  [Read-Write]
  deprecated: Use TimeSources instead

<a id="unreal.PropertyAnimatorCoreBase.time_sources_instances"></a>

#### time_sources_instances

```python
@property
def time_sources_instances() -> Map[Name, PropertyAnimatorCoreTimeSourceBase]
```

(Map[Name, PropertyAnimatorCoreTimeSourceBase]):  [Read-Write]
deprecated: Use TimeSources instead

<a id="unreal.PropertyAnimatorCoreBase.time_sources_instances"></a>

#### time_sources_instances

```python
@time_sources_instances.setter
def time_sources_instances(
        value: Map[Name, PropertyAnimatorCoreTimeSourceBase]) -> None
```

<a id="unreal.CustomPropertyControlControllerBase"></a>