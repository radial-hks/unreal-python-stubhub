## NiagaraRendererProperties Objects

```python
class NiagaraRendererProperties(NiagaraMergeable)
```

Emitter properties base class
Each EmitterRenderer derives from this with its own class, and returns it in GetProperties; a copy
of those specific properties is stored on UNiagaraEmitter (on the System) for serialization
and handed back to the System renderer on load.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraRendererProperties.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_in_cull_proxies`` (bool):  [Read-Write]
- ``motion_vector_setting`` (NiagaraRendererMotionVectorSetting):  [Read-Write] Hint about how to generate motion (velocity) vectors for this renderer.
- ``platforms`` (NiagaraPlatformSet):  [Read-Write] Platforms on which this renderer is enabled.
- ``renderer_enabled_binding`` (NiagaraVariableAttributeBinding):  [Read-Write] Binding to control if the renderer is enabled or disabled.
  When disabled the renderer does not generate or render any particle data.
  When disabled via a static bool the renderer will be removed in cooked content.
- ``sort_order_hint`` (int32):  [Read-Write] By default, emitters are drawn in the order that they are added to the system. This value will allow you to control the order in a more fine-grained manner.
        Materials of the same type (i.e. Transparent) will draw in order from lowest to highest within the system. The default value is 0.

<a id="unreal.NiagaraEffectRendererProperties"></a>