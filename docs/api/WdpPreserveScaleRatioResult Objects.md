## WdpPreserveScaleRatioResult Objects

```python
class WdpPreserveScaleRatioResult(ResultBase)
```

Wdp Preserve Scale Ratio Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: ApplicationAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``preserve_scale_ratio`` (bool):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.WdpPreserveScaleRatioResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             preserve_scale_ratio: bool = False) -> None
```

<a id="unreal.WdpPreserveScaleRatioResult.preserve_scale_ratio"></a>

#### preserve\_scale\_ratio

```python
@property
def preserve_scale_ratio() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WdpPreserveScaleRatioResult.preserve_scale_ratio"></a>

#### preserve\_scale\_ratio

```python
@preserve_scale_ratio.setter
def preserve_scale_ratio(value: bool) -> None
```

<a id="unreal.WdpSetGeoReferenceParams"></a>