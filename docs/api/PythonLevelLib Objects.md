## PythonLevelLib Objects

```python
class PythonLevelLib(BlueprintFunctionLibrary)
```

Python Level Lib

**C++ Source:**

- **Plugin**: TAPython
- **Module**: TAPython
- **File**: PythonLevelLib.h

<a id="unreal.PythonLevelLib.remove_level_from_world"></a>

#### remove\_level\_from\_world

```python
@classmethod
def remove_level_from_world(cls, level_short_name: str) -> bool
```

X.remove_level_from_world(level_short_name) -> bool
Remove specified level from current world.

Args:
    level_short_name (str): The short name of level to be removed.

Returns:
    bool: Succeed or not.

<a id="unreal.PythonLevelLib.get_levels"></a>

#### get\_levels

```python
@classmethod
def get_levels(cls, world_in: World) -> Array[Level]
```

X.get_levels(world_in) -> Array[Level]
Get all levels in the world.

Args:
    world_in (World): The world owned the Levels.

Returns:
    Array[Level]: The Levels in the world.

<a id="unreal.PythonLevelLib.delete_umap"></a>

#### delete\_umap

```python
@classmethod
def delete_umap(cls, level: Object) -> None
```

X.delete_umap(level) -> None
Delete Umap

Args:
    level (Object):

<a id="unreal.PythonLevelLib.apply_world_offset"></a>

#### apply\_world\_offset

```python
@classmethod
def apply_world_offset(cls, level: Level, position: IntVector) -> None
```

X.apply_world_offset(level, position) -> None
UFUNCTION(BlueprintCallable, meta = (Keywords = "Python Editor"), Category = "PythonEditor")
FIntVector GetAbsoluteLevelPosition(ULevel* Level);

Args:
    level (Level): 
    position (IntVector):

<a id="unreal.PythonMaterialLib"></a>