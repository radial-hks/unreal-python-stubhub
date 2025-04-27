## LocalPositionOrigin Objects

```python
class LocalPositionOrigin(EnumBase)
```

Specifies the reference point of the local position. This can be different in some cases, e.g. for instanced meshes.

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionLocalPosition.h

<a id="unreal.LocalPositionOrigin.INSTANCE"></a>

#### INSTANCE

0: Position relative to instance

<a id="unreal.LocalPositionOrigin.INSTANCE_PRE_SKINNING"></a>

#### INSTANCE_PRE_SKINNING

1: Returns pre-skinned local position for skeletal meshes, usable in vertex shader only.
      Returns the instance position for non-skeletal meshes. Incompatible with GPU skin cache feature.

<a id="unreal.LocalPositionOrigin.PRIMITIVE"></a>

#### PRIMITIVE

2: Position relative to primitive actor component

<a id="unreal.NeuralIndexType"></a>