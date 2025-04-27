## PixelFormat Objects

```python
class PixelFormat(EnumBase)
```

Describes the format of a each pixel in a graphics buffer.
warning:: When you update this, you must add an entry to GPixelFormats(see RenderUtils.cpp)
warning:: When you update this, you must add an entries to PixelFormat.h, usually just copy the generated section on the header into EPixelFormat
warning:: The *Tools DLLs will also need to be recompiled if the ordering is changed, but should not need code changes.

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

<a id="unreal.PixelFormat.PF_UNKNOWN"></a>

#### PF_UNKNOWN

0

<a id="unreal.PixelFormat.PF_A32B32G32R32F"></a>

#### PF_A32B32G32R32F

1

<a id="unreal.PixelFormat.PF_B8G8R8A8"></a>

#### PF_B8G8R8A8

2: UNORM (0..1), corresponds to FColor.  Unpacks as rgba in the shader.

<a id="unreal.PixelFormat.PF_G8"></a>

#### PF_G8

3: UNORM red (0..1)

<a id="unreal.PixelFormat.PF_G16"></a>

#### PF_G16

4

<a id="unreal.PixelFormat.PF_DXT1"></a>

#### PF_DXT1

5

<a id="unreal.PixelFormat.PF_DXT3"></a>

#### PF_DXT3

6

<a id="unreal.PixelFormat.PF_DXT5"></a>

#### PF_DXT5

7

<a id="unreal.PixelFormat.PF_UYVY"></a>

#### PF_UYVY

8

<a id="unreal.PixelFormat.PF_FLOAT_RGB"></a>

#### PF_FLOAT_RGB

9: Same as PF_FloatR11G11B10

<a id="unreal.PixelFormat.PF_FLOAT_RGBA"></a>

#### PF_FLOAT_RGBA

10: RGBA 16 bit signed FP format.  Use FFloat16Color on the CPU.

<a id="unreal.PixelFormat.PF_DEPTH_STENCIL"></a>

#### PF_DEPTH_STENCIL

11: A depth+stencil format with platform-specific implementation, for use with render targets.

<a id="unreal.PixelFormat.PF_SHADOW_DEPTH"></a>

#### PF_SHADOW_DEPTH

12: A depth format with platform-specific implementation, for use with render targets.

<a id="unreal.PixelFormat.PF_R32_FLOAT"></a>

#### PF_R32_FLOAT

13

<a id="unreal.PixelFormat.PF_G16R16"></a>

#### PF_G16R16

14

<a id="unreal.PixelFormat.PF_G16R16F"></a>

#### PF_G16R16F

15

<a id="unreal.PixelFormat.PF_G16R16F_FILTER"></a>

#### PF_G16R16F_FILTER

16

<a id="unreal.PixelFormat.PF_G32R32F"></a>

#### PF_G32R32F

17

<a id="unreal.PixelFormat.PF_A2B10G10R10"></a>

#### PF_A2B10G10R10

18

<a id="unreal.PixelFormat.PF_A16B16G16R16"></a>

#### PF_A16B16G16R16

19

<a id="unreal.PixelFormat.PF_D24"></a>

#### PF_D24

20

<a id="unreal.PixelFormat.PF_R16F"></a>

#### PF_R16F

21

<a id="unreal.PixelFormat.PF_R16F_FILTER"></a>

#### PF_R16F_FILTER

22

<a id="unreal.PixelFormat.PF_BC5"></a>

#### PF_BC5

23

<a id="unreal.PixelFormat.PF_V8U8"></a>

#### PF_V8U8

24: SNORM red, green (-1..1). Not supported on all RHI e.g. Metal

<a id="unreal.PixelFormat.PF_A1"></a>

#### PF_A1

25

<a id="unreal.PixelFormat.PF_FLOAT_R11G11B10"></a>

#### PF_FLOAT_R11G11B10

26: A low precision floating point format, unsigned.  Use FFloat3Packed on the CPU.

<a id="unreal.PixelFormat.PF_A8"></a>

#### PF_A8

27

<a id="unreal.PixelFormat.PF_R32_UINT"></a>

#### PF_R32_UINT

28

<a id="unreal.PixelFormat.PF_R32_SINT"></a>

#### PF_R32_SINT

29

<a id="unreal.PixelFormat.PF_PVRTC2"></a>

#### PF_PVRTC2

30

<a id="unreal.PixelFormat.PF_PVRTC4"></a>

#### PF_PVRTC4

31

<a id="unreal.PixelFormat.PF_R16_UINT"></a>

#### PF_R16_UINT

32

<a id="unreal.PixelFormat.PF_R16_SINT"></a>

#### PF_R16_SINT

33

<a id="unreal.PixelFormat.PF_R16G16B16A16_UINT"></a>

#### PF_R16G16B16A16_UINT

34

<a id="unreal.PixelFormat.PF_R16G16B16A16_SINT"></a>

#### PF_R16G16B16A16_SINT

35

<a id="unreal.PixelFormat.PF_R5G6B5_UNORM"></a>

#### PF_R5G6B5_UNORM

36

<a id="unreal.PixelFormat.PF_R8G8B8A8"></a>

#### PF_R8G8B8A8

37

<a id="unreal.PixelFormat.PF_A8R8G8B8"></a>

#### PF_A8R8G8B8

38: Only used for legacy loading; do NOT use!

<a id="unreal.PixelFormat.PF_BC4"></a>

#### PF_BC4

39: High precision single channel block compressed, equivalent to a single channel BC5, 8 bytes per 4x4 block.

<a id="unreal.PixelFormat.PF_R8G8"></a>

#### PF_R8G8

40: UNORM red, green (0..1).

<a id="unreal.PixelFormat.PF_ATC_RGB"></a>

#### PF_ATC_RGB

41: ATITC format.

<a id="unreal.PixelFormat.PF_ATC_RGBA_E"></a>

#### PF_ATC_RGBA_E

42: ATITC format.

<a id="unreal.PixelFormat.PF_ATC_RGBA_I"></a>

#### PF_ATC_RGBA_I

43: ATITC format.

<a id="unreal.PixelFormat.PF_X24_G8"></a>

#### PF_X24_G8

44: Used for creating SRVs to alias a DepthStencil buffer to read Stencil.  Don't use for creating textures.

<a id="unreal.PixelFormat.PF_ETC1"></a>

#### PF_ETC1

45

<a id="unreal.PixelFormat.PF_ETC2_RGB"></a>

#### PF_ETC2_RGB

46

<a id="unreal.PixelFormat.PF_ETC2_RGBA"></a>

#### PF_ETC2_RGBA

47

<a id="unreal.PixelFormat.PF_R32G32B32A32_UINT"></a>

#### PF_R32G32B32A32_UINT

48

<a id="unreal.PixelFormat.PF_R16G16_UINT"></a>

#### PF_R16G16_UINT

49

<a id="unreal.PixelFormat.PF_ASTC_4X4"></a>

#### PF_ASTC_4X4

50: 8.00 bpp

<a id="unreal.PixelFormat.PF_ASTC_6X6"></a>

#### PF_ASTC_6X6

51: 3.56 bpp

<a id="unreal.PixelFormat.PF_ASTC_8X8"></a>

#### PF_ASTC_8X8

52: 2.00 bpp

<a id="unreal.PixelFormat.PF_ASTC_10X10"></a>

#### PF_ASTC_10X10

53: 1.28 bpp

<a id="unreal.PixelFormat.PF_ASTC_12X12"></a>

#### PF_ASTC_12X12

54: 0.89 bpp

<a id="unreal.PixelFormat.PF_BC6H"></a>

#### PF_BC6H

55

<a id="unreal.PixelFormat.PF_BC7"></a>

#### PF_BC7

56

<a id="unreal.PixelFormat.PF_R8_UINT"></a>

#### PF_R8_UINT

57

<a id="unreal.PixelFormat.PF_L8"></a>

#### PF_L8

58

<a id="unreal.PixelFormat.PF_XGXR8"></a>

#### PF_XGXR8

59

<a id="unreal.PixelFormat.PF_R8G8B8A8_UINT"></a>

#### PF_R8G8B8A8_UINT

60

<a id="unreal.PixelFormat.PF_R8G8B8A8_SNORM"></a>

#### PF_R8G8B8A8_SNORM

61: SNORM (-1..1), corresponds to FFixedRGBASigned8.

<a id="unreal.PixelFormat.PF_R16G16B16A16_UNORM"></a>

#### PF_R16G16B16A16_UNORM

62

<a id="unreal.PixelFormat.PF_R16G16B16A16_SNORM"></a>

#### PF_R16G16B16A16_SNORM

63

<a id="unreal.PixelFormat.PF_PLATFORM_HDR_0"></a>

#### PF_PLATFORM_HDR_0

64

<a id="unreal.PixelFormat.PF_PLATFORM_HDR_1"></a>

#### PF_PLATFORM_HDR_1

65

<a id="unreal.PixelFormat.PF_PLATFORM_HDR_2"></a>

#### PF_PLATFORM_HDR_2

66

<a id="unreal.PixelFormat.PF_NV12"></a>

#### PF_NV12

67

<a id="unreal.PixelFormat.PF_R32G32_UINT"></a>

#### PF_R32G32_UINT

68

<a id="unreal.PixelFormat.PF_ETC2_R11_EAC"></a>

#### PF_ETC2_R11_EAC

69

<a id="unreal.PixelFormat.PF_ETC2_RG11_EAC"></a>

#### PF_ETC2_RG11_EAC

70

<a id="unreal.PixelFormat.PF_R8"></a>

#### PF_R8

71

<a id="unreal.PixelFormat.PF_B5G5R5A1_UNORM"></a>

#### PF_B5G5R5A1_UNORM

72

<a id="unreal.PixelFormat.PF_ASTC_4X4_HDR"></a>

#### PF_ASTC_4X4_HDR

73

<a id="unreal.PixelFormat.PF_ASTC_6X6_HDR"></a>

#### PF_ASTC_6X6_HDR

74

<a id="unreal.PixelFormat.PF_ASTC_8X8_HDR"></a>

#### PF_ASTC_8X8_HDR

75

<a id="unreal.PixelFormat.PF_ASTC_10X10_HDR"></a>

#### PF_ASTC_10X10_HDR

76

<a id="unreal.PixelFormat.PF_ASTC_12X12_HDR"></a>

#### PF_ASTC_12X12_HDR

77

<a id="unreal.PixelFormat.PF_G16R16_SNORM"></a>

#### PF_G16R16_SNORM

78

<a id="unreal.PixelFormat.PF_R8G8_UINT"></a>

#### PF_R8G8_UINT

79

<a id="unreal.PixelFormat.PF_R32G32B32_UINT"></a>

#### PF_R32G32B32_UINT

80

<a id="unreal.PixelFormat.PF_R32G32B32_SINT"></a>

#### PF_R32G32B32_SINT

81

<a id="unreal.PixelFormat.PF_R32G32B32F"></a>

#### PF_R32G32B32F

82

<a id="unreal.PixelFormat.PF_R8_SINT"></a>

#### PF_R8_SINT

83

<a id="unreal.PixelFormat.PF_R64_UINT"></a>

#### PF_R64_UINT

84

<a id="unreal.PixelFormat.PF_R9G9B9EXP5"></a>

#### PF_R9G9B9EXP5

85

<a id="unreal.PixelFormat.PF_P010"></a>

#### PF_P010

86

<a id="unreal.PixelFormat.PF_ASTC_4X4_NORM_RG"></a>

#### PF_ASTC_4X4_NORM_RG

87

<a id="unreal.PixelFormat.PF_ASTC_6X6_NORM_RG"></a>

#### PF_ASTC_6X6_NORM_RG

88

<a id="unreal.PixelFormat.PF_ASTC_8X8_NORM_RG"></a>

#### PF_ASTC_8X8_NORM_RG

89

<a id="unreal.PixelFormat.PF_ASTC_10X10_NORM_RG"></a>

#### PF_ASTC_10X10_NORM_RG

90

<a id="unreal.PixelFormat.PF_ASTC_12X12_NORM_RG"></a>

#### PF_ASTC_12X12_NORM_RG

91

<a id="unreal.PixelFormat.PF_R16G16_SINT"></a>

#### PF_R16G16_SINT

92

<a id="unreal.StereoLayerType"></a>