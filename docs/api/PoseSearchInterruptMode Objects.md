## PoseSearchInterruptMode Objects

```python
class PoseSearchInterruptMode(EnumBase)
```

EPose Search Interrupt Mode

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchLibrary.h

<a id="unreal.PoseSearchInterruptMode.DO_NOT_INTERRUPT"></a>

#### DO_NOT_INTERRUPT

0: continuing pose search will be performed if valid

<a id="unreal.PoseSearchInterruptMode.INTERRUPT_ON_DATABASE_CHANGE"></a>

#### INTERRUPT_ON_DATABASE_CHANGE

1: continuing pose search will be interrupted if its database is not listed in the searchable databases

<a id="unreal.PoseSearchInterruptMode.INTERRUPT_ON_DATABASE_CHANGE_AND_INVALIDATE_CONTINUING_POSE"></a>

#### INTERRUPT_ON_DATABASE_CHANGE_AND_INVALIDATE_CONTINUING_POSE

2: continuing pose search will be interrupted if its database is not listed in the searchable databases,
and continuing pose will be invalidated (forcing the schema to use pose history to build the query)

<a id="unreal.PoseSearchInterruptMode.FORCE_INTERRUPT"></a>

#### FORCE_INTERRUPT

3: continuing pose search will always be interrupted

<a id="unreal.PoseSearchInterruptMode.FORCE_INTERRUPT_AND_INVALIDATE_CONTINUING_POSE"></a>

#### FORCE_INTERRUPT_AND_INVALIDATE_CONTINUING_POSE

4: continuing pose search will always be interrupted
and continuing pose will be invalidated (forcing the schema to use pose history to build the query)

<a id="unreal.PoseSearchAssetSamplerSpace"></a>