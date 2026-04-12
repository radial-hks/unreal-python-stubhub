## AesMaterialLevelRange Objects

```python
class AesMaterialLevelRange(StructBase)
```

材质 Level 范围配置

用于配置指定 Level 范围使用的材质。在 TArray 中配置多个 Range 时，
如果 Range 之间有重叠，数组中后面的 Range 会覆盖前面的 Range（后覆盖优先）。

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesEarth
- **File**: AesTerrainComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write] 是否启用（用于临时禁用而不删除配置）
- ``end_level`` (int32):  [Read-Write] 结束 Level（包含）
- ``material`` (MaterialInterface):  [Read-Write] 材质引用（硬引用，与现有代码保持一致）
- ``start_level`` (int32):  [Read-Write] 起始 Level（包含）

<a id="unreal.AesMaterialLevelRange.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.AesVegetationTypeMapTableTow"></a>