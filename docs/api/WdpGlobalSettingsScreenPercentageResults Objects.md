## WdpGlobalSettingsScreenPercentageResults Objects

```python
class WdpGlobalSettingsScreenPercentageResults(ResultBase)
```

Wdp Global Settings Screen Percentage Results

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: ApplicationAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``screen_percentage`` (float):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.WdpGlobalSettingsScreenPercentageResults.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             screen_percentage: float = 0.000000) -> None
```

<a id="unreal.WdpGlobalSettingsScreenPercentageResults.screen_percentage"></a>

#### screen\_percentage

```python
@property
def screen_percentage() -> float
```

(float):  [Read-Write]

<a id="unreal.WdpGlobalSettingsScreenPercentageResults.screen_percentage"></a>

#### screen\_percentage

```python
@screen_percentage.setter
def screen_percentage(value: float) -> None
```

<a id="unreal.WdpGlobalGetVersionParams"></a>