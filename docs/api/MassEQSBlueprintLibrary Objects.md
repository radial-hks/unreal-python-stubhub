## MassEQSBlueprintLibrary Objects

```python
class MassEQSBlueprintLibrary(BlueprintFunctionLibrary)
```

Function library for interfacing with EntityInfo inside blueprints.

**C++ Source:**

- **Plugin**: MassGameplay
- **Module**: MassEQS
- **File**: MassEQSBlueprintLibrary.h

<a id="unreal.MassEQSBlueprintLibrary.send_signal_to_entity"></a>

#### send\_signal\_to\_entity

```python
@classmethod
def send_signal_to_entity(cls, owner: Actor,
                          entity_info: MassEnvQueryEntityInfoBlueprintWrapper,
                          signal: Name) -> None
```

X.send_signal_to_entity(owner, entity_info, signal) -> None
Sends the input Signal to the Entity defined by EntityInfo.EntityHandle using the UMassSignalSubsystem.

Args:
    owner (Actor): 
    entity_info (MassEnvQueryEntityInfoBlueprintWrapper): 
    signal (Name):

<a id="unreal.MassEQSBlueprintLibrary.get_enviroment_query_result_as_entity_info"></a>

#### get\_enviroment\_query\_result\_as\_entity\_info

```python
@classmethod
def get_enviroment_query_result_as_entity_info(
    cls, query_instance: EnvQueryInstanceBlueprintWrapper
) -> Array[MassEnvQueryEntityInfoBlueprintWrapper]
```

X.get_enviroment_query_result_as_entity_info(query_instance) -> Array[MassEnvQueryEntityInfoBlueprintWrapper]
Outputs an array filled with resulting EntityInfos. Note that it makes sense only if ItemType is a EnvQueryItemType_MassEntityHandle-derived type.

Args:
    query_instance (EnvQueryInstanceBlueprintWrapper): 

Returns:
    Array[MassEnvQueryEntityInfoBlueprintWrapper]:

<a id="unreal.MassEQSBlueprintLibrary.get_current_entity_position"></a>

#### get\_current\_entity\_position

```python
@classmethod
def get_current_entity_position(
        cls, owner: Actor,
        entity_info: MassEnvQueryEntityInfoBlueprintWrapper) -> Vector
```

X.get_current_entity_position(owner, entity_info) -> Vector
Get Current Entity Position

Args:
    owner (Actor): 
    entity_info (MassEnvQueryEntityInfoBlueprintWrapper): 

Returns:
    Vector:

<a id="unreal.MassEQSBlueprintLibrary.get_cached_entity_position"></a>

#### get\_cached\_entity\_position

```python
@classmethod
def get_cached_entity_position(
        cls, entity_info: MassEnvQueryEntityInfoBlueprintWrapper) -> Vector
```

X.get_cached_entity_position(entity_info) -> Vector
Get Cached Entity Position

Args:
    entity_info (MassEnvQueryEntityInfoBlueprintWrapper): 

Returns:
    Vector:

<a id="unreal.MassEQSBlueprintLibrary.entity_to_string"></a>

#### entity\_to\_string

```python
@classmethod
def entity_to_string(
        cls, entity_info: MassEnvQueryEntityInfoBlueprintWrapper) -> str
```

X.entity_to_string(entity_info) -> str
Utils

Args:
    entity_info (MassEnvQueryEntityInfoBlueprintWrapper): 

Returns:
    str:

<a id="unreal.MassEQSBlueprintLibrary.entity_comparison"></a>

#### entity\_comparison

```python
@classmethod
def entity_comparison(cls, a: MassEnvQueryEntityInfoBlueprintWrapper,
                      b: MassEnvQueryEntityInfoBlueprintWrapper) -> bool
```

X.entity_comparison(a, b) -> bool
Custom comparison function, as the Blueprint Equals did not seem to work.

Args:
    a (MassEnvQueryEntityInfoBlueprintWrapper): 
    b (MassEnvQueryEntityInfoBlueprintWrapper): 

Returns:
    bool:

<a id="unreal.MassEQSBlueprintLibrary.contains_entity"></a>

#### contains\_entity

```python
@classmethod
def contains_entity(
        cls, entity_list: Array[MassEnvQueryEntityInfoBlueprintWrapper],
        entity_info: MassEnvQueryEntityInfoBlueprintWrapper) -> bool
```

X.contains_entity(entity_list, entity_info) -> bool
Custom array-contains function, as the Blueprint version did not seem to work.

Args:
    entity_list (Array[MassEnvQueryEntityInfoBlueprintWrapper]): 
    entity_info (MassEnvQueryEntityInfoBlueprintWrapper): 

Returns:
    bool:

<a id="unreal.ZoneGraphAnnotationComponent"></a>