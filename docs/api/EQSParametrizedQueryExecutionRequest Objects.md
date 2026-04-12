## EQSParametrizedQueryExecutionRequest Objects

```python
class EQSParametrizedQueryExecutionRequest(StructBase)
```

EQSParametrized Query Execution Request

**C++ Source:**

- **Module**: AIModule
- **File**: EnvQueryTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eqs_query_blackboard_key`` (BlackboardKeySelector):  [Read-Write] blackboard key storing an EQS query template
- ``query_config`` (Array[AIDynamicParam]):  [Read-Write]
- ``query_template`` (EnvQuery):  [Read-Write]
- ``run_mode`` (EnvQueryRunMode):  [Read-Write] determines which item will be stored (All = only first matching)
- ``use_bb_key_for_query_template`` (bool):  [Read-Write]

<a id="unreal.EQSParametrizedQueryExecutionRequest.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.ZoneGraphTagFilter"></a>