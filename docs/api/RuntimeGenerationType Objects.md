## RuntimeGenerationType Objects

```python
class RuntimeGenerationType(EnumBase)
```

Supported options for runtime navigation data generation

**C++ Source:**

- **Module**: NavigationSystem
- **File**: NavigationData.h

<a id="unreal.RuntimeGenerationType.STATIC"></a>

#### STATIC

0: No runtime generation, fully static navigation data

<a id="unreal.RuntimeGenerationType.DYNAMIC_MODIFIERS_ONLY"></a>

#### DYNAMIC_MODIFIERS_ONLY

1: Supports only navigation modifiers updates

<a id="unreal.RuntimeGenerationType.DYNAMIC"></a>

#### DYNAMIC

2: Fully dynamic, supports geometry changes along with navigation modifiers

<a id="unreal.NavigationInvokerPriority"></a>