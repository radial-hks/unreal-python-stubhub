## WdpSetDefaultActionSettingParams Objects

```python
class WdpSetDefaultActionSettingParams(ParamsBase)
```

Wdp Set Default Action Setting Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpActionSettingsAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``edit_pivot_mode`` (bool):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``pick_filter`` (WdpPickFilter):  [Read-Write]
- ``selection_mode`` (WdpSelectionMode):  [Read-Write]

<a id="unreal.WdpSetDefaultActionSettingParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(pick_filter: WdpPickFilter = [[], True, []],
             selection_mode: WdpSelectionMode = WdpSelectionMode.NONE,
             edit_pivot_mode: bool = False) -> None
```

<a id="unreal.WdpSetDefaultActionSettingParams.pick_filter"></a>

#### pick\_filter

```python
@property
def pick_filter() -> WdpPickFilter
```

(WdpPickFilter):  [Read-Write]

<a id="unreal.WdpSetDefaultActionSettingParams.pick_filter"></a>

#### pick\_filter

```python
@pick_filter.setter
def pick_filter(value: WdpPickFilter) -> None
```

<a id="unreal.WdpSetDefaultActionSettingParams.selection_mode"></a>

#### selection\_mode

```python
@property
def selection_mode() -> WdpSelectionMode
```

(WdpSelectionMode):  [Read-Write]

<a id="unreal.WdpSetDefaultActionSettingParams.selection_mode"></a>

#### selection\_mode

```python
@selection_mode.setter
def selection_mode(value: WdpSelectionMode) -> None
```

<a id="unreal.WdpSetDefaultActionSettingParams.edit_pivot_mode"></a>

#### edit\_pivot\_mode

```python
@property
def edit_pivot_mode() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WdpSetDefaultActionSettingParams.edit_pivot_mode"></a>

#### edit\_pivot\_mode

```python
@edit_pivot_mode.setter
def edit_pivot_mode(value: bool) -> None
```

<a id="unreal.WdpSetShapeEditorEditModeParams"></a>