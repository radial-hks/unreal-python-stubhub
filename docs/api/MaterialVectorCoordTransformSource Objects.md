## MaterialVectorCoordTransformSource Objects

```python
class MaterialVectorCoordTransformSource(EnumBase)
```

EMaterial Vector Coord Transform Source

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionTransform.h

<a id="unreal.MaterialVectorCoordTransformSource.TRANSFORMSOURCE_TANGENT"></a>

#### TRANSFORMSOURCE_TANGENT

0: Tangent space (relative to the surface)

<a id="unreal.MaterialVectorCoordTransformSource.TRANSFORMSOURCE_LOCAL"></a>

#### TRANSFORMSOURCE_LOCAL

1: Local space (relative to the rendered object, = object space)

<a id="unreal.MaterialVectorCoordTransformSource.TRANSFORMSOURCE_WORLD"></a>

#### TRANSFORMSOURCE_WORLD

2: World space, a unit is 1cm

<a id="unreal.MaterialVectorCoordTransformSource.TRANSFORMSOURCE_VIEW"></a>

#### TRANSFORMSOURCE_VIEW

3: View space (relative to the camera/eye, = camera space, differs from camera space in the shadow passes)

<a id="unreal.MaterialVectorCoordTransformSource.TRANSFORMSOURCE_CAMERA"></a>

#### TRANSFORMSOURCE_CAMERA

4: Camera space

<a id="unreal.MaterialVectorCoordTransformSource.TRANSFORMSOURCE_INSTANCE"></a>

#### TRANSFORMSOURCE_INSTANCE

6: Instance space (used to provide per instance transform, i.e. for Instanced Static Mesh / Particles).

<a id="unreal.MaterialVectorCoordTransform"></a>