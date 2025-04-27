## LandscapeGrassType Objects

```python
class LandscapeGrassType(Object)
```

Landscape Grass Type

**C++ Source:**

- **Module**: Landscape
- **File**: LandscapeGrassType.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable_density_scaling`` (bool):  [Read-Write] Whether this grass type should be affected by the Engine Scalability system's Foliage grass.DensityScale setting.
  This is enabled by default but can be disabled should this grass type be important for gameplay reasons.
- ``grass_varieties`` (Array[GrassVariety]):  [Read-Write]

<a id="unreal.LandscapeGrassType.grass_varieties"></a>

#### grass_varieties

```python
@property
def grass_varieties() -> Array[GrassVariety]
```

(Array[GrassVariety]):  [Read-Only]

<a id="unreal.LandscapeGrassType.enable_density_scaling"></a>

#### enable_density_scaling

```python
@property
def enable_density_scaling() -> bool
```

(bool):  [Read-Only] Whether this grass type should be affected by the Engine Scalability system's Foliage grass.DensityScale setting.
This is enabled by default but can be disabled should this grass type be important for gameplay reasons.

<a id="unreal.LandscapeHeightfieldCollisionComponent"></a>