## PCGSubdivisionModuleAttributeNames Objects

```python
class PCGSubdivisionModuleAttributeNames(StructBase)
```

PCGSubdivision Module Attribute Names

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSubdivisionBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``debug_color_attribute_name`` (Name):  [Read-Write] Optional. Expected type: Vector4. If disabled, default value will be (1.0, 1.0, 1.0, 1.0).
- ``provide_debug_color`` (bool):  [Read-Write]
- ``provide_scalable`` (bool):  [Read-Write]
- ``scalable_attribute_name`` (Name):  [Read-Write] Optional. Expected type: bool. If disabled, default value will be false.
- ``size_attribute_name`` (Name):  [Read-Write] Mandatory. Expected type: double.
- ``symbol_attribute_name`` (Name):  [Read-Write] Mandatory. Expected type: FName.

<a id="unreal.PCGSubdivisionModuleAttributeNames.__init__"></a>

#### __init__

```python
def __init__(symbol_attribute_name: Name = "None",
             size_attribute_name: Name = "None",
             provide_scalable: bool = False,
             scalable_attribute_name: Name = "None",
             provide_debug_color: bool = False,
             debug_color_attribute_name: Name = "None") -> None
```

<a id="unreal.PCGSubdivisionModuleAttributeNames.symbol_attribute_name"></a>

#### symbol_attribute_name

```python
@property
def symbol_attribute_name() -> Name
```

(Name):  [Read-Write] Mandatory. Expected type: FName.

<a id="unreal.PCGSubdivisionModuleAttributeNames.symbol_attribute_name"></a>

#### symbol_attribute_name

```python
@symbol_attribute_name.setter
def symbol_attribute_name(value: Name) -> None
```

<a id="unreal.PCGSubdivisionModuleAttributeNames.size_attribute_name"></a>

#### size_attribute_name

```python
@property
def size_attribute_name() -> Name
```

(Name):  [Read-Write] Mandatory. Expected type: double.

<a id="unreal.PCGSubdivisionModuleAttributeNames.size_attribute_name"></a>

#### size_attribute_name

```python
@size_attribute_name.setter
def size_attribute_name(value: Name) -> None
```

<a id="unreal.PCGSubdivisionModuleAttributeNames.provide_scalable"></a>

#### provide_scalable

```python
@property
def provide_scalable() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGSubdivisionModuleAttributeNames.provide_scalable"></a>

#### provide_scalable

```python
@provide_scalable.setter
def provide_scalable(value: bool) -> None
```

<a id="unreal.PCGSubdivisionModuleAttributeNames.scalable_attribute_name"></a>

#### scalable_attribute_name

```python
@property
def scalable_attribute_name() -> Name
```

(Name):  [Read-Write] Optional. Expected type: bool. If disabled, default value will be false.

<a id="unreal.PCGSubdivisionModuleAttributeNames.scalable_attribute_name"></a>

#### scalable_attribute_name

```python
@scalable_attribute_name.setter
def scalable_attribute_name(value: Name) -> None
```

<a id="unreal.PCGSubdivisionModuleAttributeNames.provide_debug_color"></a>

#### provide_debug_color

```python
@property
def provide_debug_color() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGSubdivisionModuleAttributeNames.provide_debug_color"></a>

#### provide_debug_color

```python
@provide_debug_color.setter
def provide_debug_color(value: bool) -> None
```

<a id="unreal.PCGSubdivisionModuleAttributeNames.debug_color_attribute_name"></a>

#### debug_color_attribute_name

```python
@property
def debug_color_attribute_name() -> Name
```

(Name):  [Read-Write] Optional. Expected type: Vector4. If disabled, default value will be (1.0, 1.0, 1.0, 1.0).

<a id="unreal.PCGSubdivisionModuleAttributeNames.debug_color_attribute_name"></a>

#### debug_color_attribute_name

```python
@debug_color_attribute_name.setter
def debug_color_attribute_name(value: Name) -> None
```

<a id="unreal.PCGPinPropertiesGPUStruct"></a>