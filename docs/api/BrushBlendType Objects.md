## BrushBlendType Objects

```python
class BrushBlendType(EnumBase)
```

The blend mode changes how the brush material is applied to the terrain.

**C++ Source:**

- **Plugin**: Landmass
- **Module**: Landmass
- **File**: TerrainCarvingSettings.h

<a id="unreal.BrushBlendType.ALPHA_BLEND"></a>

#### ALPHA_BLEND

0: Alpha Blend will affect the heightmap both upwards and downwards.

<a id="unreal.BrushBlendType.MIN"></a>

#### MIN

1: Limits the brush to only lowering the terrain.

<a id="unreal.BrushBlendType.MAX"></a>

#### MAX

2: Limits the brush to only raising the terrain.

<a id="unreal.BrushBlendType.ADDITIVE"></a>

#### ADDITIVE

3: Performs an additive blend, using a flat Z=0 terrain as the input. Useful when you want to preserve underlying detail or ramps.

<a id="unreal.WaterBrushBlendType"></a>