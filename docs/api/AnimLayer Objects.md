## AnimLayer Objects

```python
class AnimLayer(Object)
```

Anim Layer

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRigEditor
- **File**: AnimLayers.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``anim_layer_items`` (Map[Object, AnimLayerItem]):  [Read-Only]
- ``state`` (AnimLayerState):  [Read-Only]

<a id="unreal.AnimLayer.set_weight"></a>

#### set\_weight

```python
def set_weight(weight: float) -> None
```

x.set_weight(weight) -> None
Set Weight

Args:
    weight (double):

<a id="unreal.AnimLayer.set_type"></a>

#### set\_type

```python
def set_type(layer_type: AnimLayerType) -> None
```

x.set_type(layer_type) -> None
Set Type

Args:
    layer_type (AnimLayerType):

<a id="unreal.AnimLayer.set_selected"></a>

#### set\_selected

```python
def set_selected(selected: bool, clear_selection: bool) -> None
```

x.set_selected(selected, clear_selection) -> None
Set Selected

Args:
    selected (bool): 
    clear_selection (bool):

<a id="unreal.AnimLayer.set_name"></a>

#### set\_name

```python
def set_name(name: Text) -> None
```

x.set_name(name) -> None
Set Name

Args:
    name (Text):

<a id="unreal.AnimLayer.set_lock"></a>

#### set\_lock

```python
def set_lock(lock: bool) -> None
```

x.set_lock(lock) -> None
Set Lock

Args:
    lock (bool):

<a id="unreal.AnimLayer.set_keyed"></a>

#### set\_keyed

```python
def set_keyed() -> None
```

x.set_keyed() -> None
Set Keyed

<a id="unreal.AnimLayer.set_active"></a>

#### set\_active

```python
def set_active(active: bool) -> None
```

x.set_active(active) -> None
Set Active

Args:
    active (bool):

<a id="unreal.AnimLayer.remove_selected_in_sequencer"></a>

#### remove\_selected\_in\_sequencer

```python
def remove_selected_in_sequencer() -> bool
```

x.remove_selected_in_sequencer() -> bool
Remove Selected in Sequencer

Returns:
    bool:

<a id="unreal.AnimLayer.get_weight"></a>

#### get\_weight

```python
def get_weight() -> float
```

x.get_weight() -> double
Get Weight

Returns:
    double:

<a id="unreal.AnimLayer.get_type"></a>

#### get\_type

```python
def get_type() -> AnimLayerType
```

x.get_type() -> AnimLayerType
Get Type

Returns:
    AnimLayerType:

<a id="unreal.AnimLayer.get_selected"></a>

#### get\_selected

```python
def get_selected() -> CheckBoxState
```

x.get_selected() -> CheckBoxState
Get Selected

Returns:
    CheckBoxState:

<a id="unreal.AnimLayer.get_name"></a>

#### get\_name

```python
def get_name() -> Text
```

x.get_name() -> Text
Get Name

Returns:
    Text:

<a id="unreal.AnimLayer.get_lock"></a>

#### get\_lock

```python
def get_lock() -> bool
```

x.get_lock() -> bool
Get Lock

Returns:
    bool:

<a id="unreal.AnimLayer.get_keyed"></a>

#### get\_keyed

```python
def get_keyed() -> CheckBoxState
```

x.get_keyed() -> CheckBoxState
Get Keyed

Returns:
    CheckBoxState:

<a id="unreal.AnimLayer.get_active"></a>

#### get\_active

```python
def get_active() -> bool
```

x.get_active() -> bool
Get Active

Returns:
    bool:

<a id="unreal.AnimLayer.add_selected_in_sequencer"></a>

#### add\_selected\_in\_sequencer

```python
def add_selected_in_sequencer() -> bool
```

x.add_selected_in_sequencer() -> bool
Add Selected in Sequencer

Returns:
    bool:

<a id="unreal.AnimLayers"></a>