## NiagaraMeshFacingMode Objects

```python
class NiagaraMeshFacingMode(EnumBase)
```

This enum decides how a mesh particle will orient its "facing" axis relative to camera. Must keep these in sync with NiagaraMeshVertexFactory.ush

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraMeshRendererProperties.h

<a id="unreal.NiagaraMeshFacingMode.DEFAULT"></a>

#### DEFAULT

0: Ignores the camera altogether. The mesh aligns its local-space X-axis with the particles' local-space X-axis, after transforming by the Particles.Transform vector (if it exists).

<a id="unreal.NiagaraMeshFacingMode.VELOCITY"></a>

#### VELOCITY

1: The mesh aligns it's local-space X-axis with the particle's Particles.Velocity vector.

<a id="unreal.NiagaraMeshFacingMode.CAMERA_POSITION"></a>

#### CAMERA_POSITION

2: Has the mesh local-space X-axis point towards the camera's position.

<a id="unreal.NiagaraMeshFacingMode.CAMERA_PLANE"></a>

#### CAMERA_PLANE

3: Has the mesh local-space X-axis point towards the closest point on the camera view plane.

<a id="unreal.MovieSceneKeyInterpolation"></a>