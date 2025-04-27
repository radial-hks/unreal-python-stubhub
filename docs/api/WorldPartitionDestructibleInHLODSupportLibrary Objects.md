## WorldPartitionDestructibleInHLODSupportLibrary Objects

```python
class WorldPartitionDestructibleInHLODSupportLibrary(BlueprintFunctionLibrary)
```

World Partition Destructible in HLODSupport Library

**C++ Source:**

- **Module**: Engine
- **File**: HLODDestruction.h

<a id="unreal.WorldPartitionDestructibleInHLODSupportLibrary.destroy_in_hlod"></a>

#### destroy_in_hlod

```python
@classmethod
def destroy_in_hlod(
        cls, destructible_in_hlod: WorldPartitionDestructibleInHLODInterface
) -> None
```

X.destroy_in_hlod(destructible_in_hlod) -> None
Destroy in HLOD

Args:
    destructible_in_hlod (WorldPartitionDestructibleInHLODInterface):

<a id="unreal.WorldPartitionDestructibleInHLODSupportLibrary.damage_in_hlod"></a>

#### damage_in_hlod

```python
@classmethod
def damage_in_hlod(
        cls, destructible_in_hlod: WorldPartitionDestructibleInHLODInterface,
        damage_percent: float) -> None
```

X.damage_in_hlod(destructible_in_hlod, damage_percent) -> None
Damage in HLOD

Args:
    destructible_in_hlod (WorldPartitionDestructibleInHLODInterface): 
    damage_percent (float):

<a id="unreal.HLODLayer"></a>