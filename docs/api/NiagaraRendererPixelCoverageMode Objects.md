## NiagaraRendererPixelCoverageMode Objects

```python
class NiagaraRendererPixelCoverageMode(EnumBase)
```

ENiagara Renderer Pixel Coverage Mode

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraSpriteRendererProperties.h

<a id="unreal.NiagaraRendererPixelCoverageMode.AUTOMATIC"></a>

#### AUTOMATIC

0: Automatically determine if we want pixel coverage enabled or disabled, based on project setting and the material used on the renderer.

<a id="unreal.NiagaraRendererPixelCoverageMode.DISABLED"></a>

#### DISABLED

1: Disable pixel coverage.

<a id="unreal.NiagaraRendererPixelCoverageMode.ENABLED"></a>

#### ENABLED

2: Enable pixel coverage with no color adjustment based on coverage.

<a id="unreal.NiagaraRendererPixelCoverageMode.ENABLED_RGBA"></a>

#### ENABLED_RGBA

3: Enable pixel coverage and adjust the RGBA channels according to coverage.

<a id="unreal.NiagaraRendererPixelCoverageMode.ENABLED_RGB"></a>

#### ENABLED_RGB

4: Enable pixel coverage and adjust the RGB channels according to coverage.

<a id="unreal.NiagaraRendererPixelCoverageMode.ENABLED_A"></a>

#### ENABLED_A

5: Enable pixel coverage and adjust the Alpha channel only according to coverage.

<a id="unreal.SubUVBoundingVertexCount"></a>