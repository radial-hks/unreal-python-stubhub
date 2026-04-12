## WdpVisualSubsystem Objects

```python
class WdpVisualSubsystem(TickableWorldSubsystem)
```

Wdp Visual Subsystem

**C++ Source:**

- **Plugin**: WdpApplication
- **Module**: WdpVisual
- **File**: WdpVisualSubsystem.h

<a id="unreal.WdpVisualSubsystem.set_visual_style"></a>

#### set\_visual\_style

```python
def set_visual_style(custom_style_index: int, color: str) -> bool
```

x.set_visual_style(custom_style_index, color) -> bool
Set Visual Style

Args:
    custom_style_index (int32): 
    color (str): 

Returns:
    bool:

<a id="unreal.WdpVisualSubsystem.set_outline_thickness"></a>

#### set\_outline\_thickness

```python
def set_outline_thickness(thickness: float) -> bool
```

x.set_outline_thickness(thickness) -> bool
Set Outline Thickness

Args:
    thickness (float): 

Returns:
    bool:

<a id="unreal.WdpVisualSubsystem.outline_component"></a>

#### outline\_component

```python
def outline_component(pc: PrimitiveComponent,
                      enabled: bool = True,
                      custom_style_index: int = 0) -> bool
```

x.outline_component(pc, enabled=True, custom_style_index=0) -> bool
Outline Component

Args:
    pc (PrimitiveComponent): 
    enabled (bool): 
    custom_style_index (int32): 

Returns:
    bool:

<a id="unreal.WdpVisualSubsystem.outline_by_layer"></a>

#### outline\_by\_layer

```python
def outline_by_layer(outline_params: Array[VisualParam]) -> bool
```

x.outline_by_layer(outline_params) -> bool
Outline by Layer

Args:
    outline_params (Array[VisualParam]): 

Returns:
    bool:

<a id="unreal.WdpVisualSubsystem.outline_by_f_id"></a>

#### outline\_by\_f\_id

```python
def outline_by_f_id(outline_params: Array[VisualParam]) -> bool
```

x.outline_by_f_id(outline_params) -> bool
for baseplate

Args:
    outline_params (Array[VisualParam]): 

Returns:
    bool:

<a id="unreal.WdpVisualSubsystem.outline_actor"></a>

#### outline\_actor

```python
def outline_actor(actor: Actor,
                  enabled: bool = True,
                  custom_style_index: int = 0) -> bool
```

x.outline_actor(actor, enabled=True, custom_style_index=0) -> bool
for model

Args:
    actor (Actor): 
    enabled (bool): 
    custom_style_index (int32): 

Returns:
    bool:

<a id="unreal.WdpVisualSubsystem.highlight_component"></a>

#### highlight\_component

```python
def highlight_component(pc: PrimitiveComponent,
                        enabled: bool = True,
                        custom_style_index: int = 0) -> bool
```

x.highlight_component(pc, enabled=True, custom_style_index=0) -> bool
Highlight Component

Args:
    pc (PrimitiveComponent): 
    enabled (bool): 
    custom_style_index (int32): 

Returns:
    bool:

<a id="unreal.WdpVisualSubsystem.highlight_by_layer"></a>

#### highlight\_by\_layer

```python
def highlight_by_layer(outline_params: Array[VisualParam]) -> bool
```

x.highlight_by_layer(outline_params) -> bool
Highlight by Layer

Args:
    outline_params (Array[VisualParam]): 

Returns:
    bool:

<a id="unreal.WdpVisualSubsystem.highlight_by_f_id"></a>

#### highlight\_by\_f\_id

```python
def highlight_by_f_id(outline_params: Array[VisualParam]) -> bool
```

x.highlight_by_f_id(outline_params) -> bool
Highlight by FId

Args:
    outline_params (Array[VisualParam]): 

Returns:
    bool:

<a id="unreal.WdpVisualSubsystem.highlight_actor"></a>

#### highlight\_actor

```python
def highlight_actor(actor: Actor,
                    enabled: bool = True,
                    custom_style_index: int = 0) -> bool
```

x.highlight_actor(actor, enabled=True, custom_style_index=0) -> bool
Highlight Actor

Args:
    actor (Actor): 
    enabled (bool): 
    custom_style_index (int32): 

Returns:
    bool:

<a id="unreal.WdpVisualSubsystem.hidden_by_f_id"></a>

#### hidden\_by\_f\_id

```python
def hidden_by_f_id(hidden_f_ids: Set[int]) -> bool
```

x.hidden_by_f_id(hidden_f_ids) -> bool
Hidden by FId

Args:
    hidden_f_ids (Set[int32]): 

Returns:
    bool:

<a id="unreal.WdpVisualSubsystem.get_visual_style"></a>

#### get\_visual\_style

```python
def get_visual_style() -> Array[VisualStyleValue]
```

x.get_visual_style() -> Array[VisualStyleValue]
Get Visual Style

Returns:
    Array[VisualStyleValue]:

<a id="unreal.WdpVisualSubsystem.get_outline_thickness"></a>

#### get\_outline\_thickness

```python
def get_outline_thickness() -> float
```

x.get_outline_thickness() -> float
Get Outline Thickness

Returns:
    float:

<a id="unreal.WdpNodeSelection"></a>