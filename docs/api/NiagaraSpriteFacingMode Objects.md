## NiagaraSpriteFacingMode Objects

```python
class NiagaraSpriteFacingMode(EnumBase)
```

This enum decides how a sprite particle will orient its "facing" axis. Must keep these in sync with NiagaraSpriteVertexFactory.ush

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraSpriteRendererProperties.h

<a id="unreal.NiagaraSpriteFacingMode.FACE_CAMERA"></a>

#### FACE_CAMERA

0: The sprite billboard origin is always "looking at" the camera origin, trying to keep its up axis aligned to the camera's up axis.

<a id="unreal.NiagaraSpriteFacingMode.FACE_CAMERA_PLANE"></a>

#### FACE_CAMERA_PLANE

1: The sprite billboard plane is completely parallel to the camera plane. Particle always looks "flat"

<a id="unreal.NiagaraSpriteFacingMode.CUSTOM_FACING_VECTOR"></a>

#### CUSTOM_FACING_VECTOR

2: The sprite billboard faces toward the "Particles.SpriteFacing" vector attribute. If the "Particles.SpriteFacing" attribute is missing, this falls back to FaceCamera mode.

<a id="unreal.NiagaraSpriteFacingMode.FACE_CAMERA_POSITION"></a>

#### FACE_CAMERA_POSITION

3: Faces the camera position, but is not dependent on the camera rotation.  This method produces more stable particles under camera rotation. Uses the up axis of (0,0,1).

<a id="unreal.NiagaraSpriteFacingMode.FACE_CAMERA_DISTANCE_BLEND"></a>

#### FACE_CAMERA_DISTANCE_BLEND

4: Blends between FaceCamera and FaceCameraPosition.

<a id="unreal.NiagaraSpriteFacingMode.AUTOMATIC"></a>

#### AUTOMATIC

5: Automatically select between FaceCamera & CustomFacingVector depending on if SpriteFacing binding is valid.

<a id="unreal.NiagaraSortMode"></a>