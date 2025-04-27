## DMMaterialEffectStackPresetSubsystem Objects

```python
class DMMaterialEffectStackPresetSubsystem(EditorSubsystem)
```

DMMaterial Effect Stack Preset Subsystem

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMaterialEffectStackPresetSubsystem.h

<a id="unreal.DMMaterialEffectStackPresetSubsystem.save_preset"></a>

#### save_preset

```python
def save_preset(preset_name: str, preset: DMMaterialEffectStackJson) -> bool
```

x.save_preset(preset_name, preset) -> bool
Save Preset

Args:
    preset_name (str): 
    preset (DMMaterialEffectStackJson): 

Returns:
    bool:

<a id="unreal.DMMaterialEffectStackPresetSubsystem.remove_preset"></a>

#### remove_preset

```python
def remove_preset(preset_name: str) -> bool
```

x.remove_preset(preset_name) -> bool
Remove Preset

Args:
    preset_name (str): 

Returns:
    bool:

<a id="unreal.DMMaterialEffectStackPresetSubsystem.load_preset"></a>

#### load_preset

```python
def load_preset(preset_name: str) -> Optional[DMMaterialEffectStackJson]
```

x.load_preset(preset_name) -> DMMaterialEffectStackJson or None
Load Preset

Args:
    preset_name (str): 

Returns:
    DMMaterialEffectStackJson or None: 

    out_preset (DMMaterialEffectStackJson):

<a id="unreal.DMMaterialEffectStackPresetSubsystem.get_preset_names"></a>

#### get_preset_names

```python
def get_preset_names() -> Array[str]
```

x.get_preset_names() -> Array[str]
Get Preset Names

Returns:
    Array[str]:

<a id="unreal.DMMaterialLayerObject"></a>