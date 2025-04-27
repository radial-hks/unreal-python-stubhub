## ProceduralFoliageSpawner Objects

```python
class ProceduralFoliageSpawner(Object)
```

Procedural Foliage Spawner

**C++ Source:**

- **Module**: Foliage
- **File**: ProceduralFoliageSpawner.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``foliage_types`` (Array[FoliageTypeObject]):  [Read-Write] The types of foliage to procedurally spawn.
- ``minimum_quad_tree_size`` (float):  [Read-Write] Minimum size of the quad tree used during the simulation. Reduce if too many instances are in splittable leaf quads (as warned in the log).
- ``num_unique_tiles`` (int32):  [Read-Write] The number of unique tiles to generate. The final simulation is a procedurally determined combination of the various unique tiles.
- ``override_foliage_terrain_materials`` (Array[MaterialInterface]):  [Read-Write] Procedural foliage will only spawn on materials specified here. These are only used if 'Use Override Foliage Terrain Materials' is checked.
- ``random_seed`` (int32):  [Read-Write] The seed used for generating the randomness of the simulation.
- ``tile_size`` (float):  [Read-Write] Length of the tile (in cm) along one axis. The total area of the tile will be TileSize*TileSize.
- ``use_override_foliage_terrain_materials`` (bool):  [Read-Write] If checked, will override the default behavior of using the global foliage material list and instead use the Override Foliage Terrain Materials defined here.
  If the override is used, you must manually provide ALL materials this procedural foliage spawner should spawn on top of.

<a id="unreal.ProceduralFoliageSpawner.random_seed"></a>

#### random_seed

```python
@property
def random_seed() -> int
```

(int32):  [Read-Only] The seed used for generating the randomness of the simulation.

<a id="unreal.ProceduralFoliageSpawner.tile_size"></a>

#### tile_size

```python
@property
def tile_size() -> float
```

(float):  [Read-Only] Length of the tile (in cm) along one axis. The total area of the tile will be TileSize*TileSize.

<a id="unreal.ProceduralFoliageSpawner.num_unique_tiles"></a>

#### num_unique_tiles

```python
@property
def num_unique_tiles() -> int
```

(int32):  [Read-Only] The number of unique tiles to generate. The final simulation is a procedurally determined combination of the various unique tiles.

<a id="unreal.ProceduralFoliageSpawner.minimum_quad_tree_size"></a>

#### minimum_quad_tree_size

```python
@property
def minimum_quad_tree_size() -> float
```

(float):  [Read-Only] Minimum size of the quad tree used during the simulation. Reduce if too many instances are in splittable leaf quads (as warned in the log).

<a id="unreal.ProceduralFoliageSpawner.simulate"></a>

#### simulate

```python
def simulate(num_steps: int = -1) -> None
```

x.simulate(num_steps=-1) -> None
Simulate

Args:
    num_steps (int32):

<a id="unreal.ProceduralFoliage"></a>