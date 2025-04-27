## AttenuationSettings Objects

```python
class AttenuationSettings(SoundAttenuationSettings)
```

deprecated: 'AttenuationSettings' was renamed to 'SoundAttenuationSettings'.

<a id="unreal.AttenuationSettings.__init__"></a>

#### __init__

```python
def __init__(
    distance_algorithm: AttenuationDistanceModel = AttenuationDistanceModel.
    LINEAR,
    attenuation_shape: AttenuationShape = AttenuationShape.SPHERE,
    falloff_mode: NaturalSoundFalloffMode = NaturalSoundFalloffMode.CONTINUES,
    d_b_attenuation_at_max: float = 0.000000,
    attenuation_shape_extents: Vector = [0.000000, 0.000000, 0.000000],
    cone_offset: float = 0.000000,
    falloff_distance: float = 0.000000,
    cone_sphere_radius: float = 0.000000,
    cone_sphere_falloff_distance: float = 0.000000,
    custom_attenuation_curve: RuntimeFloatCurve = [],
    attenuate: bool = False,
    spatialize: bool = False,
    attenuate_with_lpf: bool = False,
    enable_listener_focus: bool = False,
    enable_focus_interpolation: bool = False,
    enable_occlusion: bool = False,
    use_complex_collision_for_occlusion: bool = False,
    enable_reverb_send: bool = False,
    enable_priority_attenuation: bool = False,
    apply_normalization_to_stereo_sounds: bool = False,
    enable_log_frequency_scaling: bool = False,
    enable_submix_sends: bool = False,
    enable_source_data_override: bool = False,
    enable_send_to_audio_link: bool = False,
    spatialization_algorithm:
    SoundSpatializationAlgorithm = SoundSpatializationAlgorithm.
    SPATIALIZATION_DEFAULT,
    audio_link_settings_override: AudioLinkSettingsAbstract = None,
    binaural_radius: float = 0.000000,
    custom_lowpass_air_absorption_curve: RuntimeFloatCurve = [],
    custom_highpass_air_absorption_curve: RuntimeFloatCurve = [],
    absorption_method: AirAbsorptionMethod = AirAbsorptionMethod.LINEAR,
    occlusion_trace_channel: CollisionChannel = CollisionChannel.
    ECC_WORLD_STATIC,
    reverb_send_method: ReverbSendMethod = ReverbSendMethod.LINEAR,
    priority_attenuation_method:
    PriorityAttenuationMethod = PriorityAttenuationMethod.LINEAR,
    non_spatialized_radius_start: float = 0.000000,
    non_spatialized_radius_end: float = 0.000000,
    non_spatialized_radius_mode:
    NonSpatializedRadiusSpeakerMapMode = NonSpatializedRadiusSpeakerMapMode.
    OMNI_DIRECTIONAL,
    stereo_spread: float = 0.000000,
    lpf_radius_min: float = 0.000000,
    lpf_radius_max: float = 0.000000,
    lpf_frequency_at_min: float = 0.000000,
    lpf_frequency_at_max: float = 0.000000,
    hpf_frequency_at_min: float = 0.000000,
    hpf_frequency_at_max: float = 0.000000,
    focus_azimuth: float = 0.000000,
    non_focus_azimuth: float = 0.000000,
    focus_distance_scale: float = 0.000000,
    non_focus_distance_scale: float = 0.000000,
    focus_priority_scale: float = 0.000000,
    non_focus_priority_scale: float = 0.000000,
    focus_volume_attenuation: float = 0.000000,
    non_focus_volume_attenuation: float = 0.000000,
    focus_attack_interp_speed: float = 0.000000,
    focus_release_interp_speed: float = 0.000000,
    occlusion_low_pass_filter_frequency: float = 0.000000,
    occlusion_volume_attenuation: float = 0.000000,
    occlusion_interpolation_time: float = 0.000000,
    reverb_wet_level_min: float = 0.000000,
    reverb_wet_level_max: float = 0.000000,
    reverb_distance_min: float = 0.000000,
    reverb_distance_max: float = 0.000000,
    manual_reverb_send_level: float = 0.000000,
    priority_attenuation_min: float = 0.000000,
    priority_attenuation_max: float = 0.000000,
    priority_attenuation_distance_min: float = 0.000000,
    priority_attenuation_distance_max: float = 0.000000,
    manual_priority_attenuation: float = 0.000000,
    custom_reverb_send_curve: RuntimeFloatCurve = [],
    submix_send_settings: Array[AttenuationSubmixSendSettings] = [],
    custom_priority_attenuation_curve: RuntimeFloatCurve = [],
    plugin_settings: SoundAttenuationPluginSettings = [[], [], [],
                                                       []]) -> None
```

<a id="unreal.SourceEffectChainEntry"></a>