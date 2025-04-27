## MovieSceneNumericVariant Objects

```python
class MovieSceneNumericVariant(StructBase)
```

A variant type that masquerades as a numeric (double) value.

This type is 8 bytes (sizeof(double)) and uses a technique called NaN-boxing to encode variants into those 8-bytes,
while a literal double value maintains the exact same bits in-memory as a double. By default this variant can only
represent a double, or a UMovieSceneNumericVariantGetter*, but additional variant types can be encoded by deriving
from this type and associating type 'IDs' to typed-data (upto 48 bit in size), where the type bits are encoded into
the nan bits of the double.

Extensive reading around NaN-boxing techniques can be found elsewhere.

UMovieSceneNumericVariantGetter may be used to assign an external, dynamic value to this variant.

The benefit of using this technique is that this type can be used as a drop-in replacement for any double member
variable to provide it with dynamic getter functionality without inflating the size of the class, and with barely any
runtime overhead whatsoever. Automatic UPROPERTY upgrade exists for all numeric property types that make sense:
int64 and uint64 are not supported in this variant due to loss of precision (doubles only have 52 bits of mantissa)

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneNumericVariant.h

<a id="unreal.MovieSceneNumericVariant.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.ComponentMaterialInfo"></a>