## WdpGlobalSettingsResolutionResults Objects

```python
class WdpGlobalSettingsResolutionResults(ResultBase)
```

Wdp Global Settings Resolution Results

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: ApplicationAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``resolution_x`` (double):  [Read-Write]
- ``resolution_y`` (double):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.WdpGlobalSettingsResolutionResults.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             resolution_x: float = 0.000000,
             resolution_y: float = 0.000000) -> None
```

<a id="unreal.WdpGlobalSettingsResolutionResults.resolution_x"></a>

#### resolution\_x

```python
@property
def resolution_x() -> float
```

(double):  [Read-Write]

<a id="unreal.WdpGlobalSettingsResolutionResults.resolution_x"></a>

#### resolution\_x

```python
@resolution_x.setter
def resolution_x(value: float) -> None
```

<a id="unreal.WdpGlobalSettingsResolutionResults.resolution_y"></a>

#### resolution\_y

```python
@property
def resolution_y() -> float
```

(double):  [Read-Write]

<a id="unreal.WdpGlobalSettingsResolutionResults.resolution_y"></a>

#### resolution\_y

```python
@resolution_y.setter
def resolution_y(value: float) -> None
```

<a id="unreal.WdpGlobalSettingsScreenPercentageParams"></a>