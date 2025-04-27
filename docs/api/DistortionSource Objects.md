## DistortionSource Objects

```python
class DistortionSource(EnumBase)
```

Specifies from where the distortion state information comes

**C++ Source:**

- **Plugin**: LensComponent
- **Module**: LensComponent
- **File**: LensComponent.h

<a id="unreal.DistortionSource.LENS_FILE"></a>

#### LENS_FILE

0: Distortion state is evaluated using the LensFile

<a id="unreal.DistortionSource.LIVE_LINK_LENS_SUBJECT"></a>

#### LIVE_LINK_LENS_SUBJECT

1: Distortion state is inputted directly from a LiveLink subject

<a id="unreal.DistortionSource.MANUAL"></a>

#### MANUAL

2: Distortion state is set manually by the user using the Distortion State setting below

<a id="unreal.DistortionRenderingMode"></a>