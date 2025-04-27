## HairLODSettings Objects

```python
class HairLODSettings(StructBase)
```

Hair LODSettings

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomAssetInterpolation.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angular_threshold`` (float):  [Read-Write] Max angular difference between adjacents vertices to remove vertices during simplification, in degrees
- ``binding_type`` (GroomBindingType):  [Read-Write] Defines the type of attachment
- ``curve_decimation`` (float):  [Read-Write] Reduce the number of hair strands in a uniform manner
- ``geometry_type`` (GroomGeometryType):  [Read-Write] Defines the type of geometry used by this LOD (Strands, Cards, or Meshes)
- ``global_interpolation`` (GroomOverrideType):  [Read-Write] Global interpolation
- ``screen_size`` (float):  [Read-Write] Screen size at which this LOD should be enabled
- ``simulation`` (GroomOverrideType):  [Read-Write] Groom simulation
- ``thickness_scale`` (float):  [Read-Write] Scales the hair Strands radius. This can be used for manually compensating the reduction of curves.
- ``vertex_decimation`` (float):  [Read-Write] Reduce the number of points for each hair strands
- ``visible`` (bool):  [Read-Write] If disable, the hair strands won't be rendered

<a id="unreal.HairLODSettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.HairDecimationSettings"></a>