## UIFrameworkGameLayerSlot Objects

```python
class UIFrameworkGameLayerSlot(UIFrameworkSlotBase)
```

UIFramework Game Layer Slot

**C++ Source:**

- **Plugin**: UIFramework
- **Module**: UIFramework
- **File**: UIFPlayerComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``input_mode`` (UIFrameworkInputMode):  [Read-Write]
- ``type`` (UIFrameworkGameLayerType):  [Read-Write]
- ``widget`` (UIFrameworkWidget):  [Read-Write]
- ``z_order`` (int32):  [Read-Write]

<a id="unreal.UIFrameworkGameLayerSlot.__init__"></a>

#### __init__

```python
def __init__(
    widget: UIFrameworkWidget = None,
    z_order: int = 0,
    input_mode: UIFrameworkInputMode = UIFrameworkInputMode.UI,
    type: UIFrameworkGameLayerType = UIFrameworkGameLayerType.VIEWPORT
) -> None
```

<a id="unreal.UIFrameworkGameLayerSlot.z_order"></a>

#### z_order

```python
@property
def z_order() -> int
```

(int32):  [Read-Write]

<a id="unreal.UIFrameworkGameLayerSlot.z_order"></a>

#### z_order

```python
@z_order.setter
def z_order(value: int) -> None
```

<a id="unreal.UIFrameworkGameLayerSlot.input_mode"></a>

#### input_mode

```python
@property
def input_mode() -> UIFrameworkInputMode
```

(UIFrameworkInputMode):  [Read-Write]

<a id="unreal.UIFrameworkGameLayerSlot.input_mode"></a>

#### input_mode

```python
@input_mode.setter
def input_mode(value: UIFrameworkInputMode) -> None
```

<a id="unreal.UIFrameworkGameLayerSlot.type"></a>

#### type

```python
@property
def type() -> UIFrameworkGameLayerType
```

(UIFrameworkGameLayerType):  [Read-Write]

<a id="unreal.UIFrameworkGameLayerSlot.type"></a>

#### type

```python
@type.setter
def type(value: UIFrameworkGameLayerType) -> None
```

<a id="unreal.UIFrameworkCanvasBoxSlot"></a>