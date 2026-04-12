## PickAesTilesNodesByRectParam Objects

```python
class PickAesTilesNodesByRectParam(ParamsBase)
```

Pick Aes Tiles Nodes by Rect Param

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpPickerAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``must_be_fully_enclosed`` (bool):  [Read-Write]
- ``select_mode`` (WdpSelectionMode):  [Read-Write]

<a id="unreal.PickAesTilesNodesByRectParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(must_be_fully_enclosed: bool = False,
             select_mode: WdpSelectionMode = WdpSelectionMode.NONE) -> None
```

<a id="unreal.PickAesTilesNodesByRectParam.must_be_fully_enclosed"></a>

#### must\_be\_fully\_enclosed

```python
@property
def must_be_fully_enclosed() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PickAesTilesNodesByRectParam.must_be_fully_enclosed"></a>

#### must\_be\_fully\_enclosed

```python
@must_be_fully_enclosed.setter
def must_be_fully_enclosed(value: bool) -> None
```

<a id="unreal.PickAesTilesNodesByRectParam.select_mode"></a>

#### select\_mode

```python
@property
def select_mode() -> WdpSelectionMode
```

(WdpSelectionMode):  [Read-Write]

<a id="unreal.PickAesTilesNodesByRectParam.select_mode"></a>

#### select\_mode

```python
@select_mode.setter
def select_mode(value: WdpSelectionMode) -> None
```

<a id="unreal.PickAesTilesNodesByScreenPointsParam"></a>