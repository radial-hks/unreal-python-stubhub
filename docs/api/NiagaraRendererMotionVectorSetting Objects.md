## NiagaraRendererMotionVectorSetting Objects

```python
class NiagaraRendererMotionVectorSetting(EnumBase)
```

How a given Niagara renderer should handle motion vector generation.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraCommon.h

<a id="unreal.NiagaraRendererMotionVectorSetting.AUTO_DETECT"></a>

#### AUTO_DETECT

0: Determines the best method to employ when generating motion vectors (accurate vs. approximate) based on project and renderer settings

<a id="unreal.NiagaraRendererMotionVectorSetting.PRECISE"></a>

#### PRECISE

1: Force motion vectors to be precise for this renderer.

<a id="unreal.NiagaraRendererMotionVectorSetting.APPROXIMATE"></a>

#### APPROXIMATE

2: Force motion vectors to be approximate for this renderer (higher performance, lower particle memory usage).

<a id="unreal.NiagaraRendererMotionVectorSetting.DISABLE"></a>

#### DISABLE

3: Do not generate motion vectors (i.e. render the object as though it is stationary).

<a id="unreal.NiagaraRendererSourceDataMode"></a>