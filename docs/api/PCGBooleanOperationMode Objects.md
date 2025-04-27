## PCGBooleanOperationMode Objects

```python
class PCGBooleanOperationMode(EnumBase)
```

EPCGBoolean Operation Mode

**C++ Source:**

- **Plugin**: PCGGeometryScriptInterop
- **Module**: PCGGeometryScriptInterop
- **File**: PCGBooleanOperation.h

<a id="unreal.PCGBooleanOperationMode.EACH_A_WITH_EACH_B"></a>

#### EACH_A_WITH_EACH_B

0: Each input in A is boolean'd with its associated input in B (A1 with B1, A2 with B2, etc...). Produces N outputs.

<a id="unreal.PCGBooleanOperationMode.EACH_A_WITH_EACH_B_SEQUENTIALLY"></a>

#### EACH_A_WITH_EACH_B_SEQUENTIALLY

1: Each input in A is boolean'd with every input in B sequentially. (A1 with B1 then with B2, A2 with B1 then B2, etc...). Produces N outputs.

<a id="unreal.PCGBooleanOperationMode.EACH_A_WITH_EVERY_B"></a>

#### EACH_A_WITH_EVERY_B

2: Each input in A is boolean'd with input in B individually (Cartesian product: A1 with B1, A1 with B2, A2 with B1, A2 with B2, etc...). Produces N * M outputs.

<a id="unreal.PCGMeshSamplingMethod"></a>