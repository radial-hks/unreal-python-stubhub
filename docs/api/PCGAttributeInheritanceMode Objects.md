## PCGAttributeInheritanceMode Objects

```python
class PCGAttributeInheritanceMode(EnumBase)
```

Method for inheriting attribute data from input pins.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGPinPropertiesGPU.h

<a id="unreal.PCGAttributeInheritanceMode.NONE"></a>

#### NONE

0: No attributes inherited from initialization pins.

<a id="unreal.PCGAttributeInheritanceMode.COPY_ATTRIBUTE_SETUP"></a>

#### COPY_ATTRIBUTE_SETUP

1: Take attribute names and types from initialization pins. Pins declared first will take priority during conflicts. Does not copy values.

<a id="unreal.PCGWorldQueryFilterByTag"></a>