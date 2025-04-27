## NiagaraCullProxyMode Objects

```python
class NiagaraCullProxyMode(EnumBase)
```

Controls how cull proxies should be handled for a system.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraEffectType.h

<a id="unreal.NiagaraCullProxyMode.NONE"></a>

#### NONE

0: No cull proxy replaces culled systems.

<a id="unreal.NiagaraCullProxyMode.INSTANCED_RENDERED"></a>

#### INSTANCED_RENDERED

1: A single simulation is used but rendered in place of all culled systems. This saves on simulation cost but can still incur significant render thread cost.

<a id="unreal.GroomCacheAttributes"></a>