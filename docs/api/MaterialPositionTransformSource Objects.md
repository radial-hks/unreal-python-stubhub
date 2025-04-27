## MaterialPositionTransformSource Objects

```python
class MaterialPositionTransformSource(EnumBase)
```

EMaterial Position Transform Source

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionTransformPosition.h

<a id="unreal.MaterialPositionTransformSource.TRANSFORMPOSSOURCE_LOCAL"></a>

#### TRANSFORMPOSSOURCE_LOCAL

0: Local space

<a id="unreal.MaterialPositionTransformSource.TRANSFORMPOSSOURCE_WORLD"></a>

#### TRANSFORMPOSSOURCE_WORLD

1: Absolute world space

<a id="unreal.MaterialPositionTransformSource.TRANSFORMPOSSOURCE_PERIODIC_WORLD"></a>

#### TRANSFORMPOSSOURCE_PERIODIC_WORLD

2: Like absolute world space, but the world origin is moved to the center of the tile the camera is in.
Logically similar to `fmod(CameraAbsoluteWorldPosition, TileSize) + CameraRelativeWorldPosition`.
This offers better precision and scalability than absolute world position.
Suitable as a position input for functions that tile based on world position, e.g. frac(Position / TileSize).
Works best when the tile size is a power of two.

<a id="unreal.MaterialPositionTransformSource.TRANSFORMPOSSOURCE_TRANSLATED_WORLD"></a>

#### TRANSFORMPOSSOURCE_TRANSLATED_WORLD

3: Translated world space, i.e. world space rotation and scale but with a position relative to the camera

<a id="unreal.MaterialPositionTransformSource.TRANSFORMPOSSOURCE_VIEW"></a>

#### TRANSFORMPOSSOURCE_VIEW

4: View space (differs from camera space in the shadow passes)

<a id="unreal.MaterialPositionTransformSource.TRANSFORMPOSSOURCE_CAMERA"></a>

#### TRANSFORMPOSSOURCE_CAMERA

5: Camera space

<a id="unreal.MaterialPositionTransformSource.TRANSFORMPOSSOURCE_INSTANCE"></a>

#### TRANSFORMPOSSOURCE_INSTANCE

7: Instance space (used to provide per instance transform, i.e. for Instanced Static Mesh / Particles).

<a id="unreal.VectorNoiseFunction"></a>