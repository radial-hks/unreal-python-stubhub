## RemoteControlLevelDependantBinding Objects

```python
class RemoteControlLevelDependantBinding(RemoteControlBinding)
```

Remote Control Level Dependant Binding

**C++ Source:**

- **Plugin**: RemoteControl
- **Module**: RemoteControl
- **File**: RemoteControlBinding.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bound_object_map`` (Map[Level, Object]):  [Read-Write]
  deprecated: BoundObjectMap is deprecated, please use BoundObjectMapByPath instead.
- ``name`` (str):  [Read-Write] The name of this binding. Defaults to the bound object's name.
- ``sub_level_selection_map`` (Map[World, Level]):  [Read-Write]
  deprecated: SubLevelSelectionMap is deprecated, please use SubLevelSelectionMapByPath instead.

<a id="unreal.RemoteControlLevelDependantBinding.bound_object_map"></a>

#### bound_object_map

```python
@property
def bound_object_map() -> Map[Level, Object]
```

(Map[Level, Object]):  [Read-Write]
deprecated: BoundObjectMap is deprecated, please use BoundObjectMapByPath instead.

<a id="unreal.RemoteControlLevelDependantBinding.bound_object_map"></a>

#### bound_object_map

```python
@bound_object_map.setter
def bound_object_map(value: Map[Level, Object]) -> None
```

<a id="unreal.RemoteControlLevelDependantBinding.sub_level_selection_map"></a>

#### sub_level_selection_map

```python
@property
def sub_level_selection_map() -> Map[World, Level]
```

(Map[World, Level]):  [Read-Write]
deprecated: SubLevelSelectionMap is deprecated, please use SubLevelSelectionMapByPath instead.

<a id="unreal.RemoteControlLevelDependantBinding.sub_level_selection_map"></a>

#### sub_level_selection_map

```python
@sub_level_selection_map.setter
def sub_level_selection_map(value: Map[World, Level]) -> None
```

<a id="unreal.RemoteControlDeltaAPITestObject"></a>