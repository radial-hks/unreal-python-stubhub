## PCGTextureFilter Objects

```python
class PCGTextureFilter(EnumBase)
```

Method used to determine the value for a sample based on the value of nearby texels.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGTextureData.h

<a id="unreal.PCGTextureFilter.POINT"></a>

#### POINT

0: Takes the value of whatever texel the sample lands in.

<a id="unreal.PCGTextureFilter.BILINEAR"></a>

#### BILINEAR

1: Bilinearly interpolates the values of the four nearest texels to the sample location.

<a id="unreal.PCGAttributeNoiseMode"></a>