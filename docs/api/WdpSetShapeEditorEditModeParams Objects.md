## WdpSetShapeEditorEditModeParams Objects

```python
class WdpSetShapeEditorEditModeParams(ParamsBase)
```

Wdp Set Shape Editor Edit Mode Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpActionSettingsAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``edit_mode`` (WdpShapeEditorEditMode):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``line_width`` (float):  [Read-Write]

<a id="unreal.WdpSetShapeEditorEditModeParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(edit_mode: WdpShapeEditorEditMode = WdpShapeEditorEditMode.NONE,
             line_width: float = 0.000000) -> None
```

<a id="unreal.WdpSetShapeEditorEditModeParams.edit_mode"></a>

#### edit\_mode

```python
@property
def edit_mode() -> WdpShapeEditorEditMode
```

(WdpShapeEditorEditMode):  [Read-Write]

<a id="unreal.WdpSetShapeEditorEditModeParams.edit_mode"></a>

#### edit\_mode

```python
@edit_mode.setter
def edit_mode(value: WdpShapeEditorEditMode) -> None
```

<a id="unreal.WdpSetShapeEditorEditModeParams.line_width"></a>

#### line\_width

```python
@property
def line_width() -> float
```

(float):  [Read-Write]

<a id="unreal.WdpSetShapeEditorEditModeParams.line_width"></a>

#### line\_width

```python
@line_width.setter
def line_width(value: float) -> None
```

<a id="unreal.MeasureLoopEventArgs"></a>