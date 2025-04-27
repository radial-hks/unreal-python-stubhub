## InterchangeMaterialXEDF Objects

```python
class InterchangeMaterialXEDF(EnumBase)
```

Data type representing an Emission Distribution Function.

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeCommon
- **File**: InterchangeMaterialXDefinitions.h

<a id="unreal.InterchangeMaterialXEDF.UNIFORM"></a>

#### UNIFORM

0: An EDF node for uniform emission.

<a id="unreal.InterchangeMaterialXEDF.CONICAL"></a>

#### CONICAL

1: Constructs an EDF emitting light inside a cone around the normal direction.

<a id="unreal.InterchangeMaterialXEDF.MEASURED"></a>

#### MEASURED

2: Constructs an EDF emitting light according to a measured IES light profile.

<a id="unreal.InterchangeMaterialXVDF"></a>