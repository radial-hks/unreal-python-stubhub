## GeometryCacheTrack_FlipbookAnimation Objects

```python
class GeometryCacheTrack_FlipbookAnimation(GeometryCacheTrack)
```

Derived GeometryCacheTrack class, used for Transform animation.

**C++ Source:**

- **Plugin**: GeometryCache
- **Module**: GeometryCache
- **File**: GeometryCacheTrackFlipbookAnimation.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``duration`` (float):  [Read-Only] The duration of this track's animation. This is an open ended interval [0..Duration[.
  If the animation is looping this is also the length of the loop.

  Note: This is set by the importer possibly based on user preferences. There may be less actual frames available.
  E.g. the animation has data for the first 2 seconds, but duration is set to 5, so it will loop every 5 seconds
  with the last three seconds showing a static scene.
- ``num_mesh_samples`` (uint32):  [Read-Only] Number of Mesh Sample within this track

<a id="unreal.GeometryCacheTrackStreamable"></a>