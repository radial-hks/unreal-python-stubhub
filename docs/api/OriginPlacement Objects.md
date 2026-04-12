## OriginPlacement Objects

```python
class OriginPlacement(EnumBase)
```

An enumeration of the possible strategies for placing the origin of
a Georeference.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: OriginPlacement.h

<a id="unreal.OriginPlacement.TRUE_ORIGIN"></a>

#### TRUE\_ORIGIN

0: Use the tileset's true origin as the Actor's origin. For georeferenced
tilesets, this usually means the Actor's origin will be at the center
of the Earth, which is not recommended. For a non-georeferenced tileset,
however, such as a detailed building with a local origin, putting the
Actor's origin at the same location as the tileset's origin can be useful.

<a id="unreal.OriginPlacement.CARTOGRAPHIC_ORIGIN"></a>

#### CARTOGRAPHIC\_ORIGIN

1: Use a custom position within the tileset as the Actor's origin. The
position is expressed as a longitude, latitude, and height, and that
position within the tileset will be at coordinate (0,0,0) in the Actor's
coordinate system.

<a id="unreal.WdpFileSystemType"></a>