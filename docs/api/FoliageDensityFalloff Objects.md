## FoliageDensityFalloff Objects

```python
class FoliageDensityFalloff(StructBase)
```

Foliage Density Falloff

**C++ Source:**

- **Module**: Foliage
- **File**: FoliageType.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``falloff_curve`` (RuntimeFloatCurve):  [Read-Write] Density as a function of normalized distance (i.e. distance from Procedural Foliage Volume / Max Volume Extent).
  X = 0 corresponds to Normalized distance = 0, X = 1 corresponds to Normalized distance = Max distance.
  Y = 0 corresponds to 0% probability of keeping instance, Y = 1 corresponds to 100% probability of keeping instance.
- ``use_falloff_curve`` (bool):  [Read-Write]

<a id="unreal.FoliageDensityFalloff.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.FoliageTypeObject"></a>