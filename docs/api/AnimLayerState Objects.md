## AnimLayerState Objects

```python
class AnimLayerState(StructBase)
```

state and properties of a layer

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRigEditor
- **File**: AnimLayers.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active`` (bool):  [Read-Write]
- ``keyed`` (CheckBoxState):  [Read-Write]
- ``lock`` (bool):  [Read-Write]
- ``name`` (Text):  [Read-Write]
- ``selected`` (CheckBoxState):  [Read-Write]
- ``type`` (int32):  [Read-Write]
- ``weight`` (double):  [Read-Write]

<a id="unreal.AnimLayerState.__init__"></a>

#### __init__

```python
def __init__(keyed: CheckBoxState = CheckBoxState.UNCHECKED,
             selected: CheckBoxState = CheckBoxState.UNCHECKED,
             active: bool = False,
             lock: bool = False,
             name: Text = "",
             weight: float = 0.000000,
             type: int = 0) -> None
```

<a id="unreal.AnimLayerState.keyed"></a>

#### keyed

```python
@property
def keyed() -> CheckBoxState
```

(CheckBoxState):  [Read-Write]

<a id="unreal.AnimLayerState.keyed"></a>

#### keyed

```python
@keyed.setter
def keyed(value: CheckBoxState) -> None
```

<a id="unreal.AnimLayerState.selected"></a>

#### selected

```python
@property
def selected() -> CheckBoxState
```

(CheckBoxState):  [Read-Write]

<a id="unreal.AnimLayerState.selected"></a>

#### selected

```python
@selected.setter
def selected(value: CheckBoxState) -> None
```

<a id="unreal.AnimLayerState.active"></a>

#### active

```python
@property
def active() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AnimLayerState.active"></a>

#### active

```python
@active.setter
def active(value: bool) -> None
```

<a id="unreal.AnimLayerState.lock"></a>

#### lock

```python
@property
def lock() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AnimLayerState.lock"></a>

#### lock

```python
@lock.setter
def lock(value: bool) -> None
```

<a id="unreal.AnimLayerState.name"></a>

#### name

```python
@property
def name() -> Text
```

(Text):  [Read-Write]

<a id="unreal.AnimLayerState.name"></a>

#### name

```python
@name.setter
def name(value: Text) -> None
```

<a id="unreal.AnimLayerState.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(double):  [Read-Write]

<a id="unreal.AnimLayerState.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.AnimLayerState.type"></a>

#### type

```python
@property
def type() -> int
```

(int32):  [Read-Write]

<a id="unreal.AnimLayerState.type"></a>

#### type

```python
@type.setter
def type(value: int) -> None
```

<a id="unreal.AnimLayerControlRigObject"></a>