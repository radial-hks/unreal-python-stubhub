## InterchangeLightNode Objects

```python
class InterchangeLightNode(InterchangeBaseLightNode)
```

Interchange Light Node

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeNodes
- **File**: InterchangeLightNode.h

<a id="unreal.InterchangeLightNode.set_custom_use_ies_brightness"></a>

#### set\_custom\_use\_ies\_brightness

```python
def set_custom_use_ies_brightness(attribute_value: bool,
                                  add_apply_delegate: bool = True) -> bool
```

x.set_custom_use_ies_brightness(attribute_value, add_apply_delegate=True) -> bool
Set Custom Use IESBrightness

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeLightNode.set_custom_rotation"></a>

#### set\_custom\_rotation

```python
def set_custom_rotation(attribute_value: Rotator,
                        add_apply_delegate: bool = True) -> bool
```

x.set_custom_rotation(attribute_value, add_apply_delegate=True) -> bool
Set Custom Rotation

Args:
    attribute_value (Rotator): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeLightNode.set_custom_intensity_units"></a>

#### set\_custom\_intensity\_units

```python
def set_custom_intensity_units(attribute_value: InterchangeLightUnits) -> bool
```

x.set_custom_intensity_units(attribute_value) -> bool
Set Custom Intensity Units

Args:
    attribute_value (InterchangeLightUnits): 

Returns:
    bool:

<a id="unreal.InterchangeLightNode.set_custom_ies_texture"></a>

#### set\_custom\_ies\_texture

```python
def set_custom_ies_texture(attribute_value: str) -> bool
```

x.set_custom_ies_texture(attribute_value) -> bool
Set Custom IESTexture

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeLightNode.set_custom_ies_brightness_scale"></a>

#### set\_custom\_ies\_brightness\_scale

```python
def set_custom_ies_brightness_scale(attribute_value: float,
                                    add_apply_delegate: bool = True) -> bool
```

x.set_custom_ies_brightness_scale(attribute_value, add_apply_delegate=True) -> bool
Set Custom IESBrightness Scale

Args:
    attribute_value (float): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeLightNode.set_custom_attenuation_radius"></a>

#### set\_custom\_attenuation\_radius

```python
def set_custom_attenuation_radius(attribute_value: float) -> bool
```

x.set_custom_attenuation_radius(attribute_value) -> bool
Set Custom Attenuation Radius

Args:
    attribute_value (float): 

Returns:
    bool:

<a id="unreal.InterchangeLightNode.get_custom_use_ies_brightness"></a>

#### get\_custom\_use\_ies\_brightness

```python
def get_custom_use_ies_brightness() -> Optional[bool]
```

x.get_custom_use_ies_brightness() -> bool or None
Get Custom Use IESBrightness

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeLightNode.get_custom_rotation"></a>

#### get\_custom\_rotation

```python
def get_custom_rotation() -> Optional[Rotator]
```

x.get_custom_rotation() -> Rotator or None
Get Custom Rotation

Returns:
    Rotator or None: 

    attribute_value (Rotator):

<a id="unreal.InterchangeLightNode.get_custom_intensity_units"></a>

#### get\_custom\_intensity\_units

```python
def get_custom_intensity_units() -> Optional[InterchangeLightUnits]
```

x.get_custom_intensity_units() -> InterchangeLightUnits or None
Get Custom Intensity Units

Returns:
    InterchangeLightUnits or None: 

    attribute_value (InterchangeLightUnits):

<a id="unreal.InterchangeLightNode.get_custom_ies_texture"></a>

#### get\_custom\_ies\_texture

```python
def get_custom_ies_texture() -> Optional[str]
```

x.get_custom_ies_texture() -> str or None
Get Custom IESTexture

Returns:
    str or None: 

    attribute_value (str):

<a id="unreal.InterchangeLightNode.get_custom_ies_brightness_scale"></a>

#### get\_custom\_ies\_brightness\_scale

```python
def get_custom_ies_brightness_scale() -> Optional[float]
```

x.get_custom_ies_brightness_scale() -> float or None
Get Custom IESBrightness Scale

Returns:
    float or None: 

    attribute_value (float):

<a id="unreal.InterchangeLightNode.get_custom_attenuation_radius"></a>

#### get\_custom\_attenuation\_radius

```python
def get_custom_attenuation_radius() -> Optional[float]
```

x.get_custom_attenuation_radius() -> float or None
Get Custom Attenuation Radius

Returns:
    float or None: 

    attribute_value (float):

<a id="unreal.InterchangePointLightNode"></a>