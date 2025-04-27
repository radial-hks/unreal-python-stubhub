## TextureMipValueMode Objects

```python
class TextureMipValueMode(EnumBase)
```

defines how MipValue is used

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.TextureMipValueMode.TMVM_NONE"></a>

#### TMVM_NONE

0: Use hardware computed sample's mip level with automatic anisotropic filtering support.

<a id="unreal.TextureMipValueMode.TMVM_MIP_LEVEL"></a>

#### TMVM_MIP_LEVEL

1: Explicitly compute the sample's mip level. Disables anisotropic filtering.

<a id="unreal.TextureMipValueMode.TMVM_MIP_BIAS"></a>

#### TMVM_MIP_BIAS

2: Bias the hardware computed sample's mip level. Disables anisotropic filtering.

<a id="unreal.TextureMipValueMode.TMVM_DERIVATIVE"></a>

#### TMVM_DERIVATIVE

3: Explicitly compute the sample's DDX and DDY for anisotropic filtering.

<a id="unreal.SamplerSourceMode"></a>