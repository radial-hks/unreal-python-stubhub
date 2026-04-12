## WdpMath Objects

```python
class WdpMath(BlueprintFunctionLibrary)
```

WDP数学库

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpMath.h

<a id="unreal.WdpMath.zero_roll"></a>

#### zero\_roll

```python
@classmethod
def zero_roll(cls, rotator_in: Rotator) -> Rotator
```

X.zero_roll(rotator_in) -> Rotator
将角度的roll归零

Args:
    rotator_in (Rotator): 

Returns:
    Rotator:

<a id="unreal.WdpMath.slerp_skip_normalization"></a>

#### slerp\_skip\_normalization

```python
@classmethod
def slerp_skip_normalization(cls, from_: Vector, to: Vector,
                             alpha: float) -> Vector
```

X.slerp_skip_normalization(from_, to, alpha) -> Vector
Slerp Skip Normalization

Args:
    from_ (Vector): 
    to (Vector): 
    alpha (float): 

Returns:
    Vector:

<a id="unreal.WdpMath.s_lerp_not_normalized"></a>

#### s\_lerp\_not\_normalized

```python
@classmethod
def s_lerp_not_normalized(cls, a: Vector, b: Vector, alpha: float) -> Vector
```

X.s_lerp_not_normalized(a, b, alpha) -> Vector
Slerp Vector Direction and Lerp Vector Length

Args:
    a (Vector): 
    b (Vector): 
    alpha (double): 

Returns:
    Vector:

<a id="unreal.WdpMath.s_lerp_normalized"></a>

#### s\_lerp\_normalized

```python
@classmethod
def s_lerp_normalized(cls, normal_a: Vector, normal_b: Vector,
                      alpha: float) -> Vector
```

X.s_lerp_normalized(normal_a, normal_b, alpha) -> Vector
Slerp Direction Normalized

Args:
    normal_a (Vector): 
    normal_b (Vector): 
    alpha (double): 

Returns:
    Vector:

<a id="unreal.WdpMath.r_interp_to_linear"></a>

#### r\_interp\_to\_linear

```python
@classmethod
def r_interp_to_linear(cls, current: Rotator, target: Rotator,
                       delta_time: float, interp_speed: float) -> Rotator
```

X.r_interp_to_linear(current, target, delta_time, interp_speed) -> Rotator
RInterp线性插值，不归一

Args:
    current (Rotator): 
    target (Rotator): 
    delta_time (float): 
    interp_speed (float): 

Returns:
    Rotator:

<a id="unreal.WdpMath.radian_to_direction_xy"></a>

#### radian\_to\_direction\_xy

```python
@classmethod
def radian_to_direction_xy(cls, radian: float) -> Vector
```

X.radian_to_direction_xy(radian) -> Vector
Radian to Direction XY

Args:
    radian (float): 

Returns:
    Vector:

<a id="unreal.WdpMath.radian_to_direction"></a>

#### radian\_to\_direction

```python
@classmethod
def radian_to_direction(cls, radian: float) -> Vector2D
```

X.radian_to_direction(radian) -> Vector2D
Radian to Direction

Args:
    radian (float): 

Returns:
    Vector2D:

<a id="unreal.WdpMath.q_interp_to_rotator"></a>

#### q\_interp\_to\_rotator

```python
@classmethod
def q_interp_to_rotator(cls, current: Rotator, target: Rotator,
                        delta_time: float,
                        rotation_lag_speed: float) -> Rotator
```

X.q_interp_to_rotator(current, target, delta_time, rotation_lag_speed) -> Rotator
QInterp插值，四元数旋转

Args:
    current (Rotator): 
    target (Rotator): 
    delta_time (float): 
    rotation_lag_speed (float): 

Returns:
    Rotator:

<a id="unreal.WdpMath.perpendicular_counter_clockwise_xy"></a>

#### perpendicular\_counter\_clockwise\_xy

```python
@classmethod
def perpendicular_counter_clockwise_xy(cls, vector: Vector) -> Vector
```

X.perpendicular_counter_clockwise_xy(vector) -> Vector
Perpendicular Counter Clockwise XY

Args:
    vector (Vector): 

Returns:
    Vector:

<a id="unreal.WdpMath.perpendicular_clockwise_xy"></a>

#### perpendicular\_clockwise\_xy

```python
@classmethod
def perpendicular_clockwise_xy(cls, vector: Vector) -> Vector
```

X.perpendicular_clockwise_xy(vector) -> Vector
Perpendicular Clockwise XY

Args:
    vector (Vector): 

Returns:
    Vector:

<a id="unreal.WdpMath.override_roll"></a>

#### override\_roll

```python
@classmethod
def override_roll(cls, rotator_in: Rotator, new_roll: float) -> Rotator
```

X.override_roll(rotator_in, new_roll) -> Rotator
替换roll的角度

Args:
    rotator_in (Rotator): 
    new_roll (double): 

Returns:
    Rotator:

<a id="unreal.WdpMath.move_point_along_sphere"></a>

#### move\_point\_along\_sphere

```python
@classmethod
def move_point_along_sphere(cls, origin: Vector, location: Vector,
                            direction: Vector, distance: float) -> Vector
```

X.move_point_along_sphere(origin, location, direction, distance) -> Vector
计算在球面上 向一个方向运动一段距离后的新位置

Args:
    origin (Vector): 
    location (Vector): 
    direction (Vector): 
    distance (double): 

Returns:
    Vector:

<a id="unreal.WdpMath.minus_delta_rotator"></a>

#### minus\_delta\_rotator

```python
@classmethod
def minus_delta_rotator(cls, a: Rotator, b: Rotator) -> Rotator
```

X.minus_delta_rotator(a, b) -> Rotator
两个角度相减，但是不做Normalize处理

Args:
    a (Rotator): 
    b (Rotator): 

Returns:
    Rotator:

<a id="unreal.WdpMath.lerp_rotator"></a>

#### lerp\_rotator

```python
@classmethod
def lerp_rotator(cls, from_: Rotator, to: Rotator, alpha: float) -> Rotator
```

X.lerp_rotator(from_, to, alpha) -> Rotator
Lerp Rotator

Args:
    from_ (Rotator): 
    to (Rotator): 
    alpha (float): 

Returns:
    Rotator:

<a id="unreal.WdpMath.lerp_clamped"></a>

#### lerp\_clamped

```python
@classmethod
def lerp_clamped(cls, from_: float, to: float, alpha: float) -> float
```

X.lerp_clamped(from_, to, alpha) -> float
Lerp Clamped

Args:
    from_ (float): 
    to (float): 
    alpha (float): 

Returns:
    float:

<a id="unreal.WdpMath.lerp_angle"></a>

#### lerp\_angle

```python
@classmethod
def lerp_angle(cls, from_: float, to: float, alpha: float) -> float
```

X.lerp_angle(from_, to, alpha) -> float
Lerp Angle

Args:
    from_ (float): 
    to (float): 
    alpha (float): 

Returns:
    float:

<a id="unreal.WdpMath.is_zero_rotator"></a>

#### is\_zero\_rotator

```python
@classmethod
def is_zero_rotator(cls, rotator_in: Rotator) -> bool
```

X.is_zero_rotator(rotator_in) -> bool
判断角度是否为零

Args:
    rotator_in (Rotator): 

Returns:
    bool:

<a id="unreal.WdpMath.is_point_in_polygon"></a>

#### is\_point\_in\_polygon

```python
@classmethod
def is_point_in_polygon(cls, point: Vector2D,
                        polygon_points: Array[Vector2D]) -> bool
```

X.is_point_in_polygon(point, polygon_points) -> bool
计算一个点是否在Polygon内

Args:
    point (Vector2D): 
    polygon_points (Array[Vector2D]): 

Returns:
    bool:

<a id="unreal.WdpMath.is_point_in_box2d"></a>

#### is\_point\_in\_box2d

```python
@classmethod
def is_point_in_box2d(cls, point: Vector, point_a: Vector2D,
                      point_b: Vector2D) -> bool
```

X.is_point_in_box2d(point, point_a, point_b) -> bool
判断一个点是否在2D空间内，Z会被忽略，2个点是矩形对角

Args:
    point (Vector): 
    point_a (Vector2D): 
    point_b (Vector2D): 

Returns:
    bool:

<a id="unreal.WdpMath.interpolate_angle_constant"></a>

#### interpolate\_angle\_constant

```python
@classmethod
def interpolate_angle_constant(cls, current: float, target: float,
                               delta_time: float,
                               interpolation_speed: float) -> float
```

X.interpolate_angle_constant(current, target, delta_time, interpolation_speed) -> float
Interpolate Angle Constant

Args:
    current (float): 
    target (float): 
    delta_time (float): 
    interpolation_speed (float): 

Returns:
    float:

<a id="unreal.WdpMath.helix_arc_length"></a>

#### helix\_arc\_length

```python
@classmethod
def helix_arc_length(cls,
                     radius_a: float,
                     radius_b: float,
                     angle_degree: float,
                     height: float,
                     num_steps: int = 100) -> float
```

X.helix_arc_length(radius_a, radius_b, angle_degree, height, num_steps=100) -> double
积分计算Helix弧线的弧长

Args:
    radius_a (double): 
    radius_b (double): 
    angle_degree (double): 
    height (double): 
    num_steps (int32): 

Returns:
    double:

<a id="unreal.WdpMath.get_sphere_haversine_distance"></a>

#### get\_sphere\_haversine\_distance

```python
@classmethod
def get_sphere_haversine_distance(cls,
                                  long_a: float,
                                  lat_a: float,
                                  long_b: float,
                                  lat_b: float,
                                  radius: float = 6371010.000000) -> float
```

X.get_sphere_haversine_distance(long_a, lat_a, long_b, lat_b, radius=6371010.000000) -> double
计算正圆球面上经纬度的两个点在球面上的大圆路径长度 输出单位 米

Args:
    long_a (double): 
    lat_a (double): 
    long_b (double): 
    lat_b (double): 
    radius (double): 

Returns:
    double:

<a id="unreal.WdpMath.get_rotator_between_normals"></a>

#### get\_rotator\_between\_normals

```python
@classmethod
def get_rotator_between_normals(cls, normal_a: Vector,
                                normal_b: Vector) -> Rotator
```

X.get_rotator_between_normals(normal_a, normal_b) -> Rotator
计算两个向量的角度，将向量A旋转到向量B需要变化的rotator

Args:
    normal_a (Vector): 
    normal_b (Vector): 

Returns:
    Rotator:

<a id="unreal.WdpMath.get_point_in_direction"></a>

#### get\_point\_in\_direction

```python
@classmethod
def get_point_in_direction(cls, target: Vector, direction: Vector,
                           distance: float) -> Vector
```

X.get_point_in_direction(target, direction, distance) -> Vector
根据距离获取一个方向上的点

Args:
    target (Vector): 
    direction (Vector): 
    distance (double): 

Returns:
    Vector:

<a id="unreal.WdpMath.get_point_distance_to_plane"></a>

#### get\_point\_distance\_to\_plane

```python
@classmethod
def get_point_distance_to_plane(cls, point: Vector, point_on_plane: Vector,
                                plane_normal: Vector) -> float
```

X.get_point_distance_to_plane(point, point_on_plane, plane_normal) -> double
获取点到Plane距离

Args:
    point (Vector): 
    point_on_plane (Vector): 
    plane_normal (Vector): 

Returns:
    double:

<a id="unreal.WdpMath.get_line_plane_intersection"></a>

#### get\_line\_plane\_intersection

```python
@classmethod
def get_line_plane_intersection(cls, direction: Vector, origin: Vector,
                                plane_normal: Vector,
                                plane_coord: Vector) -> Tuple[Vector, bool]
```

X.get_line_plane_intersection(direction, origin, plane_normal, plane_coord) -> (Vector, intersect=bool)
获取Line和Plane的焦点

Args:
    direction (Vector): 
    origin (Vector): 
    plane_normal (Vector): 
    plane_coord (Vector): 

Returns:
    bool: 

    intersect (bool):

<a id="unreal.WdpMath.get_height_to_sphere_center"></a>

#### get\_height\_to\_sphere\_center

```python
@classmethod
def get_height_to_sphere_center(cls, location: Vector,
                                origin: Vector) -> float
```

X.get_height_to_sphere_center(location, origin) -> double
计算坐标距离球心的半径

Args:
    location (Vector): 
    origin (Vector): 

Returns:
    double:

<a id="unreal.WdpMath.get_gravity_world_rotation"></a>

#### get\_gravity\_world\_rotation

```python
@classmethod
def get_gravity_world_rotation(cls, rotation: Rotator,
                               gravity_direction: Vector) -> Rotator
```

X.get_gravity_world_rotation(rotation, gravity_direction) -> Rotator
将旋转从重力相对空间转换为世界空间（注意旋转并不在东南天坐标系下）

Args:
    rotation (Rotator): 
    gravity_direction (Vector): 

Returns:
    Rotator:

<a id="unreal.WdpMath.get_gravity_relative_rotation"></a>

#### get\_gravity\_relative\_rotation

```python
@classmethod
def get_gravity_relative_rotation(cls, rotation: Rotator,
                                  gravity_direction: Vector) -> Rotator
```

X.get_gravity_relative_rotation(rotation, gravity_direction) -> Rotator
将旋转从世界空间转换为重力相对空间（注意旋转并不在东南天坐标系下）

Args:
    rotation (Rotator): 
    gravity_direction (Vector): 

Returns:
    Rotator:

<a id="unreal.WdpMath.get_gravity_control_right_vector"></a>

#### get\_gravity\_control\_right\_vector

```python
@classmethod
def get_gravity_control_right_vector(cls, control_rotation: Rotator,
                                     gravity_direction: Vector) -> Vector
```

X.get_gravity_control_right_vector(control_rotation, gravity_direction) -> Vector
通过Control Rotation 和重力方向获取Right Vector

Args:
    control_rotation (Rotator): 
    gravity_direction (Vector): 

Returns:
    Vector:

<a id="unreal.WdpMath.get_gravity_control_forward_vector"></a>

#### get\_gravity\_control\_forward\_vector

```python
@classmethod
def get_gravity_control_forward_vector(cls, control_rotation: Rotator,
                                       gravity_direction: Vector) -> Vector
```

X.get_gravity_control_forward_vector(control_rotation, gravity_direction) -> Vector
通过Control Rotation 和重力方向获取Forward Vector

Args:
    control_rotation (Rotator): 
    gravity_direction (Vector): 

Returns:
    Vector:

<a id="unreal.WdpMath.get_corrected_point_from_dots_shape_with_segment"></a>

#### get\_corrected\_point\_from\_dots\_shape\_with\_segment

```python
@classmethod
def get_corrected_point_from_dots_shape_with_segment(
        cls, start: Vector, target: Vector,
        polygon_points: Array[Vector2D]) -> Optional[Vector]
```

X.get_corrected_point_from_dots_shape_with_segment(start, target, polygon_points) -> Vector or None
根据Dots形状获取线段到几何Box的交点（只支持凸多边形）bool 是否有交点

Args:
    start (Vector): 
    target (Vector): 
    polygon_points (Array[Vector2D]): 

Returns:
    Vector or None: 

    intersection (Vector):

<a id="unreal.WdpMath.get_corrected_destination_from_dots_shape"></a>

#### get\_corrected\_destination\_from\_dots\_shape

```python
@classmethod
def get_corrected_destination_from_dots_shape(
        cls, destination: Vector, polygon_points: Array[Vector2D]) -> Vector
```

X.get_corrected_destination_from_dots_shape(destination, polygon_points) -> Vector
获取根据Dots形状的正确目标点

Args:
    destination (Vector): 
    polygon_points (Array[Vector2D]): 

Returns:
    Vector:

<a id="unreal.WdpMath.get_closest_point_on_polygon"></a>

#### get\_closest\_point\_on\_polygon

```python
@classmethod
def get_closest_point_on_polygon(cls, point: Vector2D,
                                 polygon_points: Array[Vector2D]) -> Vector2D
```

X.get_closest_point_on_polygon(point, polygon_points) -> Vector2D
获取距离Polygon上最近的点

Args:
    point (Vector2D): 
    polygon_points (Array[Vector2D]): 

Returns:
    Vector2D:

<a id="unreal.WdpMath.get_attitude_to_sphere_surface"></a>

#### get\_attitude\_to\_sphere\_surface

```python
@classmethod
def get_attitude_to_sphere_surface(cls, location: Vector, origin: Vector,
                                   radius: float) -> float
```

X.get_attitude_to_sphere_surface(location, origin, radius) -> double
计算坐标距离球面的距离

Args:
    location (Vector): 
    origin (Vector): 
    radius (double): 

Returns:
    double:

<a id="unreal.WdpMath.get_actor_focus_distance"></a>

#### get\_actor\_focus\_distance

```python
@classmethod
def get_actor_focus_distance(cls,
                             actor: Actor) -> Optional[Tuple[Vector, float]]
```

X.get_actor_focus_distance(actor) -> (location=Vector, ideal_zoom=float) or None
根据Actor的Bounds自动计算合适的距离和中心点

Args:
    actor (Actor): 

Returns:
    tuple or None: 

    location (Vector): 

    ideal_zoom (float):

<a id="unreal.WdpMath.generate_helix_spline_points"></a>

#### generate\_helix\_spline\_points

```python
@classmethod
def generate_helix_spline_points(cls,
                                 origin: Vector,
                                 axis: Vector,
                                 start_radius: float,
                                 end_radius: float,
                                 start_angle_d: float,
                                 end_angle_d: float,
                                 height: float,
                                 num_points: int = 100) -> Array[Vector]
```

X.generate_helix_spline_points(origin, axis, start_radius, end_radius, start_angle_d, end_angle_d, height, num_points=100) -> Array[Vector]
构建Helix弧线

Args:
    origin (Vector): 
    axis (Vector): 
    start_radius (double): 
    end_radius (double): 
    start_angle_d (double): 
    end_angle_d (double): 
    height (double): 
    num_points (int32): 

Returns:
    Array[Vector]:

<a id="unreal.WdpMath.generate_greate_circle_spline_points"></a>

#### generate\_greate\_circle\_spline\_points

```python
@classmethod
def generate_greate_circle_spline_points(
        cls,
        origin: Vector,
        point_a: Vector,
        point_b: Vector,
        num_points: int = 20) -> Array[Vector]
```

X.generate_greate_circle_spline_points(origin, point_a, point_b, num_points=20) -> Array[Vector]
构建球面大圆路径的弧线

Args:
    origin (Vector): 
    point_a (Vector): 
    point_b (Vector): 
    num_points (int32): 

Returns:
    Array[Vector]:

<a id="unreal.WdpMath.fix_fov_by_aspect_ratio"></a>

#### fix\_fov\_by\_aspect\_ratio

```python
@classmethod
def fix_fov_by_aspect_ratio(cls, original_fov: float,
                            viewport_size: Vector2D) -> float
```

X.fix_fov_by_aspect_ratio(original_fov, viewport_size) -> float
返回修正后的FOV长宽比

Args:
    original_fov (float): 
    viewport_size (Vector2D): 

Returns:
    float:

<a id="unreal.WdpMath.find_vector_at_z"></a>

#### find\_vector\_at\_z

```python
@classmethod
def find_vector_at_z(cls, direction: Vector, z: float) -> Tuple[Vector, bool]
```

X.find_vector_at_z(direction, z) -> (Vector, intersect=bool)
查找方向与Z高度平面的焦点

Args:
    direction (Vector): 
    z (double): 

Returns:
    bool: 

    intersect (bool):

<a id="unreal.WdpMath.find_ray_sphere_intersection"></a>

#### find\_ray\_sphere\_intersection

```python
@classmethod
def find_ray_sphere_intersection(cls, start: Vector, direction: Vector,
                                 sphere_origin: Vector,
                                 sphere_radius: float) -> Optional[Vector]
```

X.find_ray_sphere_intersection(start, direction, sphere_origin, sphere_radius) -> Vector or None
计算射线和球面的焦点

Args:
    start (Vector): 
    direction (Vector): 
    sphere_origin (Vector): 
    sphere_radius (double): 

Returns:
    Vector or None: 

    point (Vector):

<a id="unreal.WdpMath.find_ray_plane_intersect_point"></a>

#### find\_ray\_plane\_intersect\_point

```python
@classmethod
def find_ray_plane_intersect_point(cls, origin: Vector, direction: Vector,
                                   plane_normal: Vector,
                                   point_on_plane: Vector) -> Optional[Vector]
```

X.find_ray_plane_intersect_point(origin, direction, plane_normal, point_on_plane) -> Vector or None
计算射线与任意平面的交点，PlaneNormal为平面Z轴的方向，PointOnPlane是平面上任意的一点

Args:
    origin (Vector): 
    direction (Vector): 
    plane_normal (Vector): 
    point_on_plane (Vector): 

Returns:
    Vector or None: 

    intersect_point (Vector):

<a id="unreal.WdpMath.find_closest_intersection2d"></a>

#### find\_closest\_intersection2d

```python
@classmethod
def find_closest_intersection2d(
        cls, start: Vector2D, target: Vector2D,
        polygon_points: Array[Vector2D]) -> Optional[Vector2D]
```

X.find_closest_intersection2d(start, target, polygon_points) -> Vector2D or None
判断2D线段和Polygon的交点

Args:
    start (Vector2D): 
    target (Vector2D): 
    polygon_points (Array[Vector2D]): 

Returns:
    Vector2D or None: 

    intersection_point (Vector2D):

<a id="unreal.WdpMath.exponential_decay_rotator"></a>

#### exponential\_decay\_rotator

```python
@classmethod
def exponential_decay_rotator(cls, current: Rotator, target: Rotator,
                              delta_time: float, lambda_: float) -> Rotator
```

X.exponential_decay_rotator(current, target, delta_time, lambda_) -> Rotator
Exponential Decay Rotator

Args:
    current (Rotator): 
    target (Rotator): 
    delta_time (float): 
    lambda_ (float): 

Returns:
    Rotator:

<a id="unreal.WdpMath.exponential_decay_angle"></a>

#### exponential\_decay\_angle

```python
@classmethod
def exponential_decay_angle(cls, current: float, target: float,
                            delta_time: float, lambda_: float) -> float
```

X.exponential_decay_angle(current, target, delta_time, lambda_) -> float
Exponential Decay Angle

Args:
    current (float): 
    target (float): 
    delta_time (float): 
    lambda_ (float): 

Returns:
    float:

<a id="unreal.WdpMath.exponential_decay"></a>

#### exponential\_decay

```python
@classmethod
def exponential_decay(cls, delta_time: float, lambda_: float) -> float
```

X.exponential_decay(delta_time, lambda_) -> float
Exponential Decay

Args:
    delta_time (float): 
    lambda_ (float): 

Returns:
    float:

<a id="unreal.WdpMath.direction_to_angle_xy"></a>

#### direction\_to\_angle\_xy

```python
@classmethod
def direction_to_angle_xy(cls, direction: Vector) -> float
```

X.direction_to_angle_xy(direction) -> double
Direction to Angle XY

Args:
    direction (Vector): 

Returns:
    double:

<a id="unreal.WdpMath.direction_to_angle"></a>

#### direction\_to\_angle

```python
@classmethod
def direction_to_angle(cls, direction: Vector2D) -> float
```

X.direction_to_angle(direction) -> double
Direction to Angle

Args:
    direction (Vector2D): 

Returns:
    double:

<a id="unreal.WdpMath.damp_rotator"></a>

#### damp\_rotator

```python
@classmethod
def damp_rotator(cls, current: Rotator, target: Rotator, delta_time: float,
                 smoothing: float) -> Rotator
```

X.damp_rotator(current, target, delta_time, smoothing) -> Rotator
Damp Rotator

Args:
    current (Rotator): 
    target (Rotator): 
    delta_time (float): 
    smoothing (float): 

Returns:
    Rotator:

<a id="unreal.WdpMath.damp_angle"></a>

#### damp\_angle

```python
@classmethod
def damp_angle(cls, current: float, target: float, delta_time: float,
               smoothing: float) -> float
```

X.damp_angle(current, target, delta_time, smoothing) -> float
Damp Angle

Args:
    current (float): 
    target (float): 
    delta_time (float): 
    smoothing (float): 

Returns:
    float:

<a id="unreal.WdpMath.damp"></a>

#### damp

```python
@classmethod
def damp(cls, delta_time: float, smoothing: float) -> float
```

X.damp(delta_time, smoothing) -> float
Damp

Args:
    delta_time (float): 
    smoothing (float): 

Returns:
    float:

<a id="unreal.WdpMath.convert_screen_position_dpi"></a>

#### convert\_screen\_position\_dpi

```python
@classmethod
def convert_screen_position_dpi(cls, screen_position: Vector2D,
                                viewport_scale: float) -> Vector2D
```

X.convert_screen_position_dpi(screen_position, viewport_scale) -> Vector2D
将无DPI修正的屏幕坐标转换为DPI的屏幕坐标

Args:
    screen_position (Vector2D): 
    viewport_scale (float): 

Returns:
    Vector2D:

<a id="unreal.WdpMath.clamp_target_point_in_distance_range"></a>

#### clamp\_target\_point\_in\_distance\_range

```python
@classmethod
def clamp_target_point_in_distance_range(
        cls,
        start_point: Vector,
        target_point: Vector,
        min_distance: float = 0.000000,
        max_distance: float = 1000000.000000) -> Vector
```

X.clamp_target_point_in_distance_range(start_point, target_point, min_distance=0.000000, max_distance=1000000.000000) -> Vector
限制目标碰撞点到距离限制的范围内，并保持目标点的方向

Args:
    start_point (Vector): 
    target_point (Vector): 
    min_distance (double): 
    max_distance (double): 

Returns:
    Vector:

<a id="unreal.WdpMath.clamp_segment_in_box2d"></a>

#### clamp\_segment\_in\_box2d

```python
@classmethod
def clamp_segment_in_box2d(cls, start: Vector, target: Vector,
                           point_a: Vector2D,
                           point_b: Vector2D) -> Optional[Vector]
```

X.clamp_segment_in_box2d(start, target, point_a, point_b) -> Vector or None
Clamp并计算射线和Box2D在空间中的交点 bool 为是否存在交点

Args:
    start (Vector): 
    target (Vector): 
    point_a (Vector2D): 
    point_b (Vector2D): 

Returns:
    Vector or None: 

    intersection (Vector):

<a id="unreal.WdpMath.clamp_point_in_box2d"></a>

#### clamp\_point\_in\_box2d

```python
@classmethod
def clamp_point_in_box2d(cls, point_in: Vector, point_a: Vector2D,
                         point_b: Vector2D) -> Vector
```

X.clamp_point_in_box2d(point_in, point_a, point_b) -> Vector
将一个点Clamp到一个2D空间的Box内，不对Z做修正，A和B两个点是Box的两个对角

Args:
    point_in (Vector): 
    point_a (Vector2D): 
    point_b (Vector2D): 

Returns:
    Vector:

<a id="unreal.WdpMath.clamp_magnitude012d"></a>

#### clamp\_magnitude012d

```python
@classmethod
def clamp_magnitude012d(cls, vector: Vector2D) -> Vector2D
```

X.clamp_magnitude012d(vector) -> Vector2D
Clamp Magnitude 012D

Args:
    vector (Vector2D): 

Returns:
    Vector2D:

<a id="unreal.WdpMath.clamp_magnitude01"></a>

#### clamp\_magnitude01

```python
@classmethod
def clamp_magnitude01(cls, vector: Vector) -> Vector
```

X.clamp_magnitude01(vector) -> Vector
Clamp Magnitude 01

Args:
    vector (Vector): 

Returns:
    Vector:

<a id="unreal.WdpMath.clamp_float_in_range_flexible"></a>

#### clamp\_float\_in\_range\_flexible

```python
@classmethod
def clamp_float_in_range_flexible(cls,
                                  current: float,
                                  delta: float,
                                  min: float = 0.000000,
                                  max: float = 1.000000) -> float
```

X.clamp_float_in_range_flexible(current, delta, min=0.000000, max=1.000000) -> double
Clamp 一个数值，修正Delta的数值，确保数值尽量在Range范围内，如果Current不在范围内也会尽力向Range内靠近

Args:
    current (double): 
    delta (double): 
    min (double): 
    max (double): 

Returns:
    double:

<a id="unreal.WdpMath.clamp_direction_pitch_surface"></a>

#### clamp\_direction\_pitch\_surface

```python
@classmethod
def clamp_direction_pitch_surface(
        cls,
        direction_in: Vector,
        plane_normal: Vector,
        up_range: Vector2D = [5.000000, 89.000000],
        down_range: Vector2D = [-89.000000, -5.000000]) -> Vector
```

X.clamp_direction_pitch_surface(direction_in, plane_normal, up_range=[5.000000, 89.000000], down_range=[-89.000000, -5.000000]) -> Vector
Clamp 一个方向，给定上下的范围限制，对方向的Pitch角度进行限制

Args:
    direction_in (Vector): 
    plane_normal (Vector): 
    up_range (Vector2D): 
    down_range (Vector2D): 

Returns:
    Vector:

<a id="unreal.WdpMath.clamp_direction_pitch"></a>

#### clamp\_direction\_pitch

```python
@classmethod
def clamp_direction_pitch(cls, direction_in: Vector, plane_normal: Vector,
                          min_pitch: float, max_pitch: float) -> Vector
```

X.clamp_direction_pitch(direction_in, plane_normal, min_pitch, max_pitch) -> Vector
Clamp一个方向的Pitch角度，避免方向水平时点击距离几乎是无限远的问题//注意Min一定比Max小

Args:
    direction_in (Vector): 
    plane_normal (Vector): 
    min_pitch (double): 
    max_pitch (double): 

Returns:
    Vector:

<a id="unreal.WdpMath.clamp01"></a>

#### clamp01

```python
@classmethod
def clamp01(cls, value: float) -> float
```

X.clamp01(value) -> float
其他常用插值算法

Args:
    value (float): 

Returns:
    float:

<a id="unreal.WdpMath.calc_scaled_zoom_location_to_target"></a>

#### calc\_scaled\_zoom\_location\_to\_target

```python
@classmethod
def calc_scaled_zoom_location_to_target(
        cls,
        target: Vector,
        current: Vector,
        scale: float = 0.500000,
        min_distance: float = 0.000000) -> Vector
```

X.calc_scaled_zoom_location_to_target(target, current, scale=0.500000, min_distance=0.000000) -> Vector
计算向一个方向缩放目标点距离的位置，并限制最小距离，Scale：前进的距离倍数，如果当前和目标距离为100米，0.8表示前进80米，也就是距离目标20米

Args:
    target (Vector): 
    current (Vector): 
    scale (float): 
    min_distance (double): 

Returns:
    Vector:

<a id="unreal.WdpMath.calc_min_bounding_sphere_welzl"></a>

#### calc\_min\_bounding\_sphere\_welzl

```python
@classmethod
def calc_min_bounding_sphere_welzl(
        cls, locations: Array[Vector]) -> Tuple[Vector, float]
```

X.calc_min_bounding_sphere_welzl(locations) -> (center=Vector, radius=double)
Calc Min Bounding Sphere Welzl

Args:
    locations (Array[Vector]): 

Returns:
    tuple: 

    center (Vector): 

    radius (double):

<a id="unreal.WdpMath.calc_min_bounding_sphere_simple"></a>

#### calc\_min\_bounding\_sphere\_simple

```python
@classmethod
def calc_min_bounding_sphere_simple(
        cls, locations: Array[Vector]) -> Tuple[Vector, float]
```

X.calc_min_bounding_sphere_simple(locations) -> (center=Vector, radius=double)
计算一堆点的最小外接球 简易版

Args:
    locations (Array[Vector]): 

Returns:
    tuple: 

    center (Vector): 

    radius (double):

<a id="unreal.WdpMath.calc_camera_distance_to_sphere_bounds"></a>

#### calc\_camera\_distance\_to\_sphere\_bounds

```python
@classmethod
def calc_camera_distance_to_sphere_bounds(cls,
                                          radius: float,
                                          view_port_size: Vector2D = [
                                              1920.000000, 1080.000000
                                          ],
                                          fov: float = 90.000000,
                                          scale: float = 1.000000) -> float
```

X.calc_camera_distance_to_sphere_bounds(radius, view_port_size=[1920.000000, 1080.000000], fov=90.000000, scale=1.000000) -> double
计算能装下一个Sphere尺寸的相机距离

Args:
    radius (double): 
    view_port_size (Vector2D): 
    fov (float): 
    scale (float): 

Returns:
    double:

<a id="unreal.WdpMath.calc_auto_rotation_speed_and_direction"></a>

#### calc\_auto\_rotation\_speed\_and\_direction

```python
@classmethod
def calc_auto_rotation_speed_and_direction(
        cls, current_rotation: Rotator, target_rotation: Rotator,
        duration: float) -> Tuple[int, float]
```

X.calc_auto_rotation_speed_and_direction(current_rotation, target_rotation, duration) -> (direction=int32, speed=float)
计算自动旋转的方向，并得到速度（单位 度/秒）

Args:
    current_rotation (Rotator): 
    target_rotation (Rotator): 
    duration (float): 

Returns:
    tuple: 

    direction (int32): 

    speed (float):

<a id="unreal.WdpMath.arc_length_to_angle"></a>

#### arc\_length\_to\_angle

```python
@classmethod
def arc_length_to_angle(cls, radius: float, arc_length: float) -> float
```

X.arc_length_to_angle(radius, arc_length) -> double
计算球面弧长对应的角度

Args:
    radius (double): 
    arc_length (double): 

Returns:
    double:

<a id="unreal.WdpMath.angle_to_direction_xy"></a>

#### angle\_to\_direction\_xy

```python
@classmethod
def angle_to_direction_xy(cls, angle: float) -> Vector
```

X.angle_to_direction_xy(angle) -> Vector
Angle to Direction XY

Args:
    angle (float): 

Returns:
    Vector:

<a id="unreal.WdpMath.angle_to_direction"></a>

#### angle\_to\_direction

```python
@classmethod
def angle_to_direction(cls, angle: float) -> Vector2D
```

X.angle_to_direction(angle) -> Vector2D
Angle to Direction

Args:
    angle (float): 

Returns:
    Vector2D:

<a id="unreal.WdpMath.angle_to_arc_length"></a>

#### angle\_to\_arc\_length

```python
@classmethod
def angle_to_arc_length(cls, radius: float, angle: float) -> float
```

X.angle_to_arc_length(radius, angle) -> double
计算角度对应的球面弧长

Args:
    radius (double): 
    angle (double): 

Returns:
    double:

<a id="unreal.WdpMath.angle_between_skip_normalization"></a>

#### angle\_between\_skip\_normalization

```python
@classmethod
def angle_between_skip_normalization(cls, from_: Vector, to: Vector) -> float
```

X.angle_between_skip_normalization(from_, to) -> double
Angle Between Skip Normalization

Args:
    from_ (Vector): 
    to (Vector): 

Returns:
    double:

<a id="unreal.WdpMath.add_delta_rotator"></a>

#### add\_delta\_rotator

```python
@classmethod
def add_delta_rotator(cls, a: Rotator, b: Rotator) -> Rotator
```

X.add_delta_rotator(a, b) -> Rotator
两个角度相加，但是不做Normalize处理

Args:
    a (Rotator): 
    b (Rotator): 

Returns:
    Rotator:

<a id="unreal.WdpPlayerController"></a>