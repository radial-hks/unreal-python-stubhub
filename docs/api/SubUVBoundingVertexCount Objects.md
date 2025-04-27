## SubUVBoundingVertexCount Objects

```python
class SubUVBoundingVertexCount(EnumBase)
```

More bounding vertices results in reduced overdraw, but adds more triangle overhead.
The eight vertex mode is best used when the SubUV texture has a lot of space to cut out that is not captured by the four vertex version,
and when the particles using the texture will be few and large.

**C++ Source:**

- **Module**: Engine
- **File**: SubUVAnimation.h

<a id="unreal.SubUVBoundingVertexCount.BVC_FOUR_VERTICES"></a>

#### BVC_FOUR_VERTICES

0

<a id="unreal.SubUVBoundingVertexCount.BVC_EIGHT_VERTICES"></a>

#### BVC_EIGHT_VERTICES

1

<a id="unreal.OpacitySourceMode"></a>