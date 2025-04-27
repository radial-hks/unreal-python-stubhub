## PhysicalMaterialStrength Objects

```python
class PhysicalMaterialStrength(StructBase)
```

Defines the directional strengths of a physical material in term of force per surface area

**C++ Source:**

- **Module**: PhysicsCore
- **File**: PhysicalMaterial.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``compression_strength`` (float):  [Read-Write] Compression strength of the material in MegaPascal ( 10^6 N/m2 )
  This amount of compression force per area the material can withstand before it fractures, crumbles or buckles
- ``shear_strength`` (float):  [Read-Write] Shear strength of the material in MegaPascal ( 10^6 N/m2 )
  This amount of shear force per area the material can withstand before it fractures
- ``tensile_strength`` (float):  [Read-Write] Tensile strength of the material in MegaPascal ( 10^6 N/m2 )
  This amount of tension force per area the material can withstand before it fractures

<a id="unreal.PhysicalMaterialStrength.__init__"></a>

#### __init__

```python
def __init__(tensile_strength: float = 0.000000,
             compression_strength: float = 0.000000,
             shear_strength: float = 0.000000) -> None
```

<a id="unreal.PhysicalMaterialStrength.tensile_strength"></a>

#### tensile_strength

```python
@property
def tensile_strength() -> float
```

(float):  [Read-Only] Tensile strength of the material in MegaPascal ( 10^6 N/m2 )
This amount of tension force per area the material can withstand before it fractures

<a id="unreal.PhysicalMaterialStrength.compression_strength"></a>

#### compression_strength

```python
@property
def compression_strength() -> float
```

(float):  [Read-Only] Compression strength of the material in MegaPascal ( 10^6 N/m2 )
This amount of compression force per area the material can withstand before it fractures, crumbles or buckles

<a id="unreal.PhysicalMaterialStrength.shear_strength"></a>

#### shear_strength

```python
@property
def shear_strength() -> float
```

(float):  [Read-Only] Shear strength of the material in MegaPascal ( 10^6 N/m2 )
This amount of shear force per area the material can withstand before it fractures

<a id="unreal.PhysicalMaterialDamageModifier"></a>