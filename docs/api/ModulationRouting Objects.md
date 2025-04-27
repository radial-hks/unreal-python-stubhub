## ModulationRouting Objects

```python
class ModulationRouting(EnumBase)
```

EModulation Routing

**C++ Source:**

- **Module**: Engine
- **File**: SoundModulationDestination.h

<a id="unreal.ModulationRouting.DISABLE"></a>

#### DISABLE

0: Disables modulation routing

<a id="unreal.ModulationRouting.INHERIT"></a>

#### INHERIT

1: Inherits modulation routing (AudioComponent inherits from Sound, Sound inherits from SoundClass)

<a id="unreal.ModulationRouting.OVERRIDE"></a>

#### OVERRIDE

2: Ignores inherited settings and uses modulation settings on this object

<a id="unreal.ModulationRouting.UNION"></a>

#### UNION

3: Performs set union on local modulation sources with those inherited (AudioComponent inherits from Sound, Sound inherits from SoundClass)

<a id="unreal.ModulationDestination"></a>