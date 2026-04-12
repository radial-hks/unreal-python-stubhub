## CesiumSubLevel Objects

```python
class CesiumSubLevel(StructBase)
```

* Sublevels can be georeferenced to the globe by filling out this struct.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumSubLevel.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``can_be_enabled`` (bool):  [Read-Only]
- ``enabled`` (bool):  [Read-Write] Whether this sub-level is enabled. An enabled sub-level will be
  automatically loaded when the camera moves within its LoadRadius and
  no other levels are closer, and the Georeference will be updated so that
  this level's Longitude, Latitude, and Height bcome (0, 0, 0) in the Unreal
  World. A sub-level that is not enabled will be ignored by Cesium.

  If this option is greyed out, check that World Composition is enabled
  in the World Settings and that this sub-level is in a Layer that has
  Distance-based streaming DISABLED.
- ``level_height`` (double):  [Read-Write] The height in meters above the WGS84 globe this level should sit.
- ``level_latitude`` (double):  [Read-Write] The WGS84 latitude in degrees of where this level should sit on the globe,
  in the range [-90, 90]
- ``level_longitude`` (double):  [Read-Write] The WGS84 longitude in degrees of where this level should sit on the
  globe, in the range [-180, 180]
- ``level_name`` (str):  [Read-Only] The plain name of the sub level, without any prefixes.
- ``load_radius`` (double):  [Read-Write] How far in meters from the sublevel local origin the camera needs to be to
  load the level.

<a id="unreal.CesiumSubLevel.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.UrbanWorldProjectionSetting"></a>