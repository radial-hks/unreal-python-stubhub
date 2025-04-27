## MVVMSlateBrushConversionLibrary Objects

```python
class MVVMSlateBrushConversionLibrary(BlueprintFunctionLibrary)
```

Conversion library that contains methods for FSlateBrush

Primarily consists of methods to set material params on an existing FSlateBrush

**C++ Source:**

- **Plugin**: ModelViewViewModel
- **Module**: ModelViewViewModel
- **File**: MVVMSlateBrushConversionLibrary.h

<a id="unreal.MVVMSlateBrushConversionLibrary.conv_set_vector_parameter_mid"></a>

#### conv_set_vector_parameter_mid

```python
@classmethod
def conv_set_vector_parameter_mid(cls, brush: SlateBrush,
                                  material: MaterialInterface,
                                  parameter_name: Name,
                                  value: LinearColor) -> SlateBrush
```

X.conv_set_vector_parameter_mid(brush, material, parameter_name, value) -> SlateBrush
Sets a vector value on a brush material assuming it exists, handles MID existance appropriately

Args:
    brush (SlateBrush): Brush with a material we want to set a parameter on
    material (MaterialInterface): Material to set on the brush
    parameter_name (Name): Name of material parameter to set
    value (LinearColor): Value to set material parameter to

Returns:
    SlateBrush:

<a id="unreal.MVVMSlateBrushConversionLibrary.conv_set_vector_parameter"></a>

#### conv_set_vector_parameter

```python
@classmethod
def conv_set_vector_parameter(cls, brush: SlateBrush, parameter_name: Name,
                              value: LinearColor) -> SlateBrush
```

X.conv_set_vector_parameter(brush, parameter_name, value) -> SlateBrush
Sets a vector value on a brush material assuming it exists, handles MID existance appropriately

Args:
    brush (SlateBrush): Brush with a material we want to set a parameter on
    parameter_name (Name): Name of material parameter to set
    value (LinearColor): Value to set material parameter to

Returns:
    SlateBrush:

<a id="unreal.MVVMSlateBrushConversionLibrary.conv_set_texture_parameter_mid"></a>

#### conv_set_texture_parameter_mid

```python
@classmethod
def conv_set_texture_parameter_mid(cls, brush: SlateBrush,
                                   material: MaterialInterface,
                                   parameter_name: Name,
                                   value: Texture) -> SlateBrush
```

X.conv_set_texture_parameter_mid(brush, material, parameter_name, value) -> SlateBrush
Sets a texture value on a brush material assuming it exists, handles MID existance appropriately

Args:
    brush (SlateBrush): Brush with a material we want to set a parameter on
    material (MaterialInterface): Material to set on the brush
    parameter_name (Name): Name of material parameter to set
    value (Texture): Value to set material parameter to

Returns:
    SlateBrush:

<a id="unreal.MVVMSlateBrushConversionLibrary.conv_set_texture_parameter"></a>

#### conv_set_texture_parameter

```python
@classmethod
def conv_set_texture_parameter(cls, brush: SlateBrush, parameter_name: Name,
                               value: Texture) -> SlateBrush
```

X.conv_set_texture_parameter(brush, parameter_name, value) -> SlateBrush
Sets a texture value on a brush material assuming it exists, handles MID existance appropriately

Args:
    brush (SlateBrush): Brush with a material we want to set a parameter on
    parameter_name (Name): Name of material parameter to set
    value (Texture): Value to set material parameter to

Returns:
    SlateBrush:

<a id="unreal.MVVMSlateBrushConversionLibrary.conv_set_scalar_parameter_mid"></a>

#### conv_set_scalar_parameter_mid

```python
@classmethod
def conv_set_scalar_parameter_mid(cls, brush: SlateBrush,
                                  material: MaterialInterface,
                                  parameter_name: Name,
                                  value: float) -> SlateBrush
```

X.conv_set_scalar_parameter_mid(brush, material, parameter_name, value) -> SlateBrush
Sets a scalar value on a brush material assuming it exists, handles MID existance appropriately

Args:
    brush (SlateBrush): Brush with a material we want to set a parameter on
    material (MaterialInterface): Material to set on the brush
    parameter_name (Name): Name of material parameter to set
    value (float): Value to set material parameter to

Returns:
    SlateBrush:

<a id="unreal.MVVMSlateBrushConversionLibrary.conv_set_scalar_parameter"></a>

#### conv_set_scalar_parameter

```python
@classmethod
def conv_set_scalar_parameter(cls, brush: SlateBrush, parameter_name: Name,
                              value: float) -> SlateBrush
```

X.conv_set_scalar_parameter(brush, parameter_name, value) -> SlateBrush
Sets a scalar value on a brush material assuming it exists, handles MID existance appropriately

Args:
    brush (SlateBrush): Brush with a material we want to set a parameter on
    parameter_name (Name): Name of material parameter to set
    value (float): Value to set material parameter to

Returns:
    SlateBrush:

<a id="unreal.UserWidgetExtension"></a>