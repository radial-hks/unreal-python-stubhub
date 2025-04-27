## NiagaraDefaultRendererMotionVectorSetting Objects

```python
class NiagaraDefaultRendererMotionVectorSetting(EnumBase)
```

How to handle how Niagara rendered effects should generate motion vectors by default (can still be overridden on a case-by-case basis)

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraCommon.h

<a id="unreal.NiagaraDefaultRendererMotionVectorSetting.PRECISE"></a>

#### PRECISE

0: Motion vectors generated are precise (ideal for motion blur and temporal anti-aliasing).
Requires relevant emitters to store more data per particle, and may affect vertex processing performance.

<a id="unreal.NiagaraDefaultRendererMotionVectorSetting.APPROXIMATE"></a>

#### APPROXIMATE

1: Approximates the motion vectors from current velocity.
Saves memory and performance, but can result in lower quality motion blur and/or anti-aliasing.

<a id="unreal.NiagaraDefaultRendererPixelCoverageMode"></a>