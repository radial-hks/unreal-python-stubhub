## RuntimeVirtualTextureMipValueMode Objects

```python
class RuntimeVirtualTextureMipValueMode(EnumBase)
```

Set how Mip levels are calculated.
Internally we will convert to ETextureMipValueMode which is used by internal APIs.

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionRuntimeVirtualTextureSample.h

<a id="unreal.RuntimeVirtualTextureMipValueMode.RVTMVM_NONE"></a>

#### RVTMVM\_NONE

0: * Use default computed mip level. Takes into account UV scaling from using the WorldPosition pin.

<a id="unreal.RuntimeVirtualTextureMipValueMode.RVTMVM_MIP_LEVEL"></a>

#### RVTMVM\_MIP\_LEVEL

1: * Use an absolute mip level from the MipLevel pin.
* 0 is full resolution.

<a id="unreal.RuntimeVirtualTextureMipValueMode.RVTMVM_MIP_BIAS"></a>

#### RVTMVM\_MIP\_BIAS

2: * Bias the default computed mip level using the MipBias pin.
* Negative values increase resolution.

<a id="unreal.RuntimeVirtualTextureMipValueMode.RVTMVM_DERIVATIVE_UV"></a>

#### RVTMVM\_DERIVATIVE\_UV

4: * Compute mip level from explicitly provided DDX and DDY derivatives of the virtual texture UV coordinates.

<a id="unreal.RuntimeVirtualTextureMipValueMode.RVTMVM_DERIVATIVE_WORLD"></a>

#### RVTMVM\_DERIVATIVE\_WORLD

5: * Compute mip level from explicitly provided DDX and DDY derivatives of the world position.

<a id="unreal.MaterialSceneAttributeInputMode"></a>