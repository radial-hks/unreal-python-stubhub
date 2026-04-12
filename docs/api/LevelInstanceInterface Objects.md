## LevelInstanceInterface Objects

```python
class LevelInstanceInterface(Interface)
```

Level Instance Interface

**C++ Source:**

- **Module**: Engine
- **File**: LevelInstanceInterface.h

<a id="unreal.LevelInstanceInterface.unload_level_instance"></a>

#### unload\_level\_instance

```python
def unload_level_instance() -> None
```

x.unload_level_instance() -> None
Unload Level Instance

<a id="unreal.LevelInstanceInterface.set_world_asset"></a>

#### set\_world\_asset

```python
def set_world_asset(world_asset: World) -> bool
```

x.set_world_asset(world_asset) -> bool
Sets the UWorld asset reference when loading a LevelInstance

Args:
    world_asset (World): 

Returns:
    bool:

<a id="unreal.LevelInstanceInterface.load_level_instance"></a>

#### load\_level\_instance

```python
def load_level_instance() -> None
```

x.load_level_instance() -> None
Load Level Instance

<a id="unreal.LevelInstanceInterface.is_loaded"></a>

#### is\_loaded

```python
def is_loaded() -> bool
```

x.is_loaded() -> bool
Is Loaded

Returns:
    bool:

<a id="unreal.LevelInstanceInterface.get_world_asset"></a>

#### get\_world\_asset

```python
def get_world_asset() -> World
```

x.get_world_asset() -> World
Get World Asset

Returns:
    World:

<a id="unreal.LevelInstanceInterface.get_loaded_level"></a>

#### get\_loaded\_level

```python
def get_loaded_level() -> Level
```

x.get_loaded_level() -> Level
Get Loaded Level

Returns:
    Level:

<a id="unreal.LevelStreamingLevelInstance"></a>