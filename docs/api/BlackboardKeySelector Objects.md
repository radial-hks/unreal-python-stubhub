## BlackboardKeySelector Objects

```python
class BlackboardKeySelector(StructBase)
```

helper struct for defining types of allowed blackboard entries
(e.g. only entries holding points and objects derived form actor class)

**C++ Source:**

- **Module**: AIModule
- **File**: BehaviorTreeTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allowed_types`` (Array[BlackboardKeyType]):  [Read-Write] array of allowed types with additional properties (e.g. uobject's base class)
  EditAnywhere is required for FBlackboardSelectorDetails::CacheBlackboardData()
- ``none_is_allowed_value`` (bool):  [Read-Write]
- ``selected_key_id`` (int32):  [Read-Write] ID of selected key
- ``selected_key_name`` (Name):  [Read-Write] name of selected key
- ``selected_key_type`` (type(Class)):  [Read-Write] class of selected key

<a id="unreal.BlackboardKeySelector.__init__"></a>

#### \_\_init\_\_

```python
def __init__(allowed_types: Array[BlackboardKeyType] = [],
             selected_key_name: Name = "None",
             selected_key_type: Class = None,
             selected_key_id: int = 0,
             none_is_allowed_value: bool = False) -> None
```

<a id="unreal.BlackboardKeySelector.allowed_types"></a>

#### allowed\_types

```python
@property
def allowed_types() -> Array[BlackboardKeyType]
```

(Array[BlackboardKeyType]):  [Read-Write] array of allowed types with additional properties (e.g. uobject's base class)
EditAnywhere is required for FBlackboardSelectorDetails::CacheBlackboardData()

<a id="unreal.BlackboardKeySelector.allowed_types"></a>

#### allowed\_types

```python
@allowed_types.setter
def allowed_types(value: Array[BlackboardKeyType]) -> None
```

<a id="unreal.BlackboardKeySelector.selected_key_name"></a>

#### selected\_key\_name

```python
@property
def selected_key_name() -> Name
```

(Name):  [Read-Write] name of selected key

<a id="unreal.BlackboardKeySelector.selected_key_name"></a>

#### selected\_key\_name

```python
@selected_key_name.setter
def selected_key_name(value: Name) -> None
```

<a id="unreal.BlackboardKeySelector.selected_key_type"></a>

#### selected\_key\_type

```python
@property
def selected_key_type() -> Class
```

(type(Class)):  [Read-Write] class of selected key

<a id="unreal.BlackboardKeySelector.selected_key_type"></a>

#### selected\_key\_type

```python
@selected_key_type.setter
def selected_key_type(value: Class) -> None
```

<a id="unreal.BlackboardKeySelector.selected_key_id"></a>

#### selected\_key\_id

```python
@property
def selected_key_id() -> int
```

(int32):  [Read-Write] ID of selected key

<a id="unreal.BlackboardKeySelector.selected_key_id"></a>

#### selected\_key\_id

```python
@selected_key_id.setter
def selected_key_id(value: int) -> None
```

<a id="unreal.BlackboardKeySelector.none_is_allowed_value"></a>

#### none\_is\_allowed\_value

```python
@property
def none_is_allowed_value() -> bool
```

(bool):  [Read-Write]

<a id="unreal.BlackboardKeySelector.none_is_allowed_value"></a>

#### none\_is\_allowed\_value

```python
@none_is_allowed_value.setter
def none_is_allowed_value(value: bool) -> None
```

<a id="unreal.GenericTeamId"></a>