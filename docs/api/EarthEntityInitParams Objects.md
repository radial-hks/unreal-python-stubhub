## EarthEntityInitParams Objects

```python
class EarthEntityInitParams(StructBase)
```

Earth Entity Init Params

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthCore
- **File**: EarthEntityInterface.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``operate_entity_time`` (EarthOperateEntityTime):  [Read-Write]

<a id="unreal.EarthEntityInitParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    operate_entity_time: EarthOperateEntityTime = EarthOperateEntityTime.CREATE
) -> None
```

<a id="unreal.EarthEntityInitParams.operate_entity_time"></a>

#### operate\_entity\_time

```python
@property
def operate_entity_time() -> EarthOperateEntityTime
```

(EarthOperateEntityTime):  [Read-Write]

<a id="unreal.EarthEntityInitParams.operate_entity_time"></a>

#### operate\_entity\_time

```python
@operate_entity_time.setter
def operate_entity_time(value: EarthOperateEntityTime) -> None
```

<a id="unreal.EarthEntityChanges"></a>