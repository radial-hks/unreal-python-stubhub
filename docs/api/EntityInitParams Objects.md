## EntityInitParams Objects

```python
class EntityInitParams(StructBase)
```

Entity Init Params

**C++ Source:**

- **Plugin**: AesRuntimeCore
- **Module**: WdpDataModel
- **File**: WdpEntityInterface.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``operate_entity_time`` (OperateEntityTime):  [Read-Write]

<a id="unreal.EntityInitParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        operate_entity_time: OperateEntityTime = OperateEntityTime.CREATE
) -> None
```

<a id="unreal.EntityInitParams.operate_entity_time"></a>

#### operate\_entity\_time

```python
@property
def operate_entity_time() -> OperateEntityTime
```

(OperateEntityTime):  [Read-Write]

<a id="unreal.EntityInitParams.operate_entity_time"></a>

#### operate\_entity\_time

```python
@operate_entity_time.setter
def operate_entity_time(value: OperateEntityTime) -> None
```

<a id="unreal.SunPositionData"></a>