## MaterialTranslucencyPass Objects

```python
class MaterialTranslucencyPass(EnumBase)
```

Specifies which separate translucency pass to render in.

**C++ Source:**

- **Module**: Engine
- **File**: Material.h

<a id="unreal.MaterialTranslucencyPass.MTP_BEFORE_DOF"></a>

#### MTP_BEFORE_DOF

0: Render before depth of field.

<a id="unreal.MaterialTranslucencyPass.MTP_AFTER_DOF"></a>

#### MTP_AFTER_DOF

1: Render after depth of field.

<a id="unreal.MaterialTranslucencyPass.MTP_AFTER_MOTION_BLUR"></a>

#### MTP_AFTER_MOTION_BLUR

2: Render after motion blur. Disables depth test (the reconstruction post MB and TSR would otherwise flicker due to the TSR camera jittering making the depth buffer unstable). Because of that Lumen high quality reflections is also disabled to avoid visual discrepancy at depth intersection.

<a id="unreal.TranslucencyLightingMode"></a>