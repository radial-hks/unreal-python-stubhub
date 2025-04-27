## MaterialVectorCoordTransform Objects

```python
class MaterialVectorCoordTransform(EnumBase)
```

EMaterial Vector Coord Transform

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionTransform.h

<a id="unreal.MaterialVectorCoordTransform.TRANSFORM_TANGENT"></a>

#### TRANSFORM_TANGENT

0: Tangent space (relative to the surface)

<a id="unreal.MaterialVectorCoordTransform.TRANSFORM_LOCAL"></a>

#### TRANSFORM_LOCAL

1: Local space (relative to the rendered object, = object space)

<a id="unreal.MaterialVectorCoordTransform.TRANSFORM_WORLD"></a>

#### TRANSFORM_WORLD

2: World space, a unit is 1cm

<a id="unreal.MaterialVectorCoordTransform.TRANSFORM_VIEW"></a>

#### TRANSFORM_VIEW

3: View space (relative to the camera/eye, = camera space, differs from camera space in the shadow passes)

<a id="unreal.MaterialVectorCoordTransform.TRANSFORM_CAMERA"></a>

#### TRANSFORM_CAMERA

4: Camera space

<a id="unreal.MaterialVectorCoordTransform.TRANSFORM_INSTANCE"></a>

#### TRANSFORM_INSTANCE

6: Instance space (used to provide per instance transform, i.e. for Instanced Static Mesh / Particles).

<a id="unreal.MaterialPositionTransformSource"></a>