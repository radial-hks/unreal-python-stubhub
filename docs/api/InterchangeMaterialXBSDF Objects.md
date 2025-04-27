## InterchangeMaterialXBSDF Objects

```python
class InterchangeMaterialXBSDF(EnumBase)
```

Data type representing a Bidirectional Scattering Distribution Function.

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeCommon
- **File**: InterchangeMaterialXDefinitions.h

<a id="unreal.InterchangeMaterialXBSDF.OREN_NAYAR_DIFFUSE"></a>

#### OREN_NAYAR_DIFFUSE

0: A BSDF node for diffuse reflections.

<a id="unreal.InterchangeMaterialXBSDF.BURLEY_DIFFUSE"></a>

#### BURLEY_DIFFUSE

1: A BSDF node for Burley diffuse reflections.

<a id="unreal.InterchangeMaterialXBSDF.TRANSLUCENT"></a>

#### TRANSLUCENT

2: A BSDF node for pure diffuse transmission.

<a id="unreal.InterchangeMaterialXBSDF.DIELECTRIC"></a>

#### DIELECTRIC

3: A reflection/transmission BSDF node based on a microfacet model and a Fresnel curve for dielectrics.

<a id="unreal.InterchangeMaterialXBSDF.CONDUCTOR"></a>

#### CONDUCTOR

4: A reflection BSDF node based on a microfacet model and a Fresnel curve for conductors/metals.

<a id="unreal.InterchangeMaterialXBSDF.GENERALIZED_SCHLICK"></a>

#### GENERALIZED_SCHLICK

5: A reflection/transmission BSDF node based on a microfacet model and a generalized Schlick Fresnel curve.

<a id="unreal.InterchangeMaterialXBSDF.SUBSURFACE"></a>

#### SUBSURFACE

6: A subsurface scattering BSDF for true subsurface scattering.

<a id="unreal.InterchangeMaterialXBSDF.SHEEN"></a>

#### SHEEN

7: A microfacet BSDF for the back-scattering properties of cloth-like materials.

<a id="unreal.InterchangeMaterialXBSDF.THIN_FILM"></a>

#### THIN_FILM

8: Adds an iridescent thin film layer over a microfacet base BSDF.

<a id="unreal.InterchangeMaterialXEDF"></a>