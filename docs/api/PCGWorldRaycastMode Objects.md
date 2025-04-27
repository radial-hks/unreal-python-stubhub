## PCGWorldRaycastMode Objects

```python
class PCGWorldRaycastMode(EnumBase)
```

EPCGWorld Raycast Mode

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGWorldQueryHelpers.h

<a id="unreal.PCGWorldRaycastMode.INFINITE"></a>

#### INFINITE

0: Use the direction vector with 'infinite' magnitude.

<a id="unreal.PCGWorldRaycastMode.SCALED_VECTOR"></a>

#### SCALED_VECTOR

1: Use the direction vector 'as-is' for casting the ray with its current magnitude.

<a id="unreal.PCGWorldRaycastMode.NORMALIZED_WITH_LENGTH"></a>

#### NORMALIZED_WITH_LENGTH

2: Normalize the direction vector and apply the length directly.

<a id="unreal.PCGWorldRaycastMode.SEGMENTS"></a>

#### SEGMENTS

3: User provided end points. Must match input points N:N, N:1, or 1:N.

<a id="unreal.PCGLandscapeCacheSerializationMode"></a>