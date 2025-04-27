## AutomaticRadius Objects

```python
class AutomaticRadius(EnumBase)
```

UENUM(BlueprintType)
enum class ERBFSolverType : uint8
{
       Additive,
       Interpolative
};

UENUM(BlueprintType)
enum class ERBFFunctionType : uint8
{
       Gaussian,
       Exponential,
       Linear,
       Cubic,
       Quintic,
};

UENUM(BlueprintType)
enum class ERBFDistanceMethod : uint8
{
       Euclidean,
       Quaternion,
       SwingAngle,
       TwistAngle,
};

UENUM(BlueprintType)
enum class ERBFNormalizeMethod : uint8
{
       OnlyNormalizeAboveOne,
       AlwaysNormalize
};

**C++ Source:**

- **Plugin**: RigLogic
- **Module**: RigLogicModule
- **File**: DNACommon.h

<a id="unreal.AutomaticRadius.ON"></a>

#### ON

0

<a id="unreal.AutomaticRadius.OFF"></a>

#### OFF

1

<a id="unreal.TwistAxis"></a>