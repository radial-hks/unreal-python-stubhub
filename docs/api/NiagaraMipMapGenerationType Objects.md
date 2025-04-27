## NiagaraMipMapGenerationType Objects

```python
class NiagaraMipMapGenerationType(EnumBase)
```

ENiagara Mip Map Generation Type

**C++ Source:**

- **Plugin**: Niagara
- **Module**: NiagaraShader
- **File**: NiagaraGenerateMips.h

<a id="unreal.NiagaraMipMapGenerationType.UNFILTERED"></a>

#### UNFILTERED

0: Result is taken from whatever texel the sample lies on, aka Point Sampling.

<a id="unreal.NiagaraMipMapGenerationType.LINEAR"></a>

#### LINEAR

1: Linear blending is performed between a 2x2 (or 2x2x2) region of texels, aka Bilinear / Trilinear.

<a id="unreal.NiagaraMipMapGenerationType.BLUR1"></a>

#### BLUR1

2: A blur filter across a 3x3 (or 3x3x3) region of texels.

<a id="unreal.NiagaraMipMapGenerationType.BLUR2"></a>

#### BLUR2

3: A blur filter across a 5x5 (or 5x5x5) region of texels.

<a id="unreal.NiagaraMipMapGenerationType.BLUR3"></a>

#### BLUR3

4: A blur filter across a 7x7 (or 7x7x7) region of texels.

<a id="unreal.NiagaraMipMapGenerationType.BLUR4"></a>

#### BLUR4

5: A blur filter across a 9x9 (or 9x9x9) region of texels.

<a id="unreal.NCPoolMethod"></a>