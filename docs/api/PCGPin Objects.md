## PCGPin Objects

```python
class PCGPin(Object)
```

PCGPin

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGPin.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``edges`` (Array[PCGEdge]):  [Read-Write]
- ``node`` (PCGNode):  [Read-Write] ~End UObject interface
- ``properties`` (PCGPinProperties):  [Read-Write]

<a id="unreal.PCGPin.node"></a>

#### node

```python
@property
def node() -> PCGNode
```

(PCGNode):  [Read-Only] ~End UObject interface

<a id="unreal.PCGPin.edges"></a>

#### edges

```python
@property
def edges() -> Array[PCGEdge]
```

(Array[PCGEdge]):  [Read-Only]

<a id="unreal.PCGPin.properties"></a>

#### properties

```python
@property
def properties() -> PCGPinProperties
```

(PCGPinProperties):  [Read-Only]

<a id="unreal.PCGPin.set_tooltip"></a>

#### set_tooltip

```python
def set_tooltip(tooltip: Text) -> None
```

x.set_tooltip(tooltip) -> None
Set Tooltip

Args:
    tooltip (Text):

<a id="unreal.PCGPin.is_output_pin"></a>

#### is_output_pin

```python
def is_output_pin() -> bool
```

x.is_output_pin() -> bool
Is Output Pin

Returns:
    bool:

<a id="unreal.PCGPin.is_connected"></a>

#### is_connected

```python
def is_connected() -> bool
```

x.is_connected() -> bool
Is Connected

Returns:
    bool:

<a id="unreal.PCGPin.get_tooltip"></a>

#### get_tooltip

```python
def get_tooltip() -> Text
```

x.get_tooltip() -> Text
Get Tooltip

Returns:
    Text:

<a id="unreal.PCGPinPropertiesBlueprintHelpers"></a>