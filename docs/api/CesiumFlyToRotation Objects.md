## CesiumFlyToRotation Objects

```python
class CesiumFlyToRotation(EnumBase)
```

Indicates which rotation to use for orienting the object during flights.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumFlyToComponent.h

<a id="unreal.CesiumFlyToRotation.ACTOR"></a>

#### ACTOR

0: Uses the relative rotation of the root component of the Actor to which the
CesiumFlyToComponent is attached.

<a id="unreal.CesiumFlyToRotation.CONTROL_ROTATION_IN_UNREAL"></a>

#### CONTROL\_ROTATION\_IN\_UNREAL

1: Uses the ControlRotation of the Controller of the Pawn to which the
CesiumFlyToComponent is attached. The ControlRotation is interpreted as
being relative to the Unreal coordinate system.

If the component is attached to an Actor that is not a Pawn, or if the Pawn
does not have a Controller, this option is equivalent to the "Actor"
option.

<a id="unreal.CesiumFlyToRotation.CONTROL_ROTATION_IN_EAST_SOUTH_UP"></a>

#### CONTROL\_ROTATION\_IN\_EAST\_SOUTH\_UP

2: Uses the ControlRotation of the Controller of the Pawn to which the
CesiumFlyToComponent is attached. The ControlRotation is interpreted as
being relative to the Pawn's local East-South-Up coordinate system.

This is the option to use with a GlobeAwareDefaultPawn or a DynamicPawn,
because those classes interpret the ControlRotation as being relative to
East-South-Up.

If the component is attached to an Actor that is not a Pawn, or if the Pawn
does not have a Controller, this option is equivalent to the "Actor"
option.

<a id="unreal.CesiumMetadataBlueprintType"></a>