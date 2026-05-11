# 01. Two-body Problem / 2체문제

## 핵심식
a = -mu r / r^3
h = r × v
epsilon = v^2/2 - mu/r

## 손유도 PDF
See: derivations/two_body_derivation.pdf

## 코드 연결
two_body_acceleration() → a = -mu r / r^3
specific_angular_momentum() → h = r × v
specific_energy() → epsilon = v^2/2 - mu/r

## 검증 결과
r = [7000, 0, 0] km일 때 acceleration은 -x 방향으로 나왔다.
energy는 음수이므로 bound elliptical orbit 상태다.

## 헷갈린 점
- 왜 r^3인지 처음에 헷갈렸다.
- h가 왜 궤도면 normal인지 추가 확인 필요.

## Eccentricity Vector / 이심률 벡터

손유도 PDF:
derivations/02_eccentricity_vector_derivation.pdf

핵심식:
e_vec = cross(v, h) / mu - r / |r|

여기서:
- h = cross(r, v)
- |r| = 위치벡터 r의 크기
- e = |e_vec|

의미:
- e_vec의 방향은 근점 방향이다.
- e_vec의 크기는 이심률이다.
- e_vec는 단위가 없다. 왜냐하면 cross(v, h) / mu도 무차원이고, r / |r|도 무차원이기 때문이다.

이번 예제:
- r = [7000, 0, 0] km
- v = [0, 7.5, 1.0] km/s
- e_vec = [0.00539276, 0, 0]
- e = 0.00539276
- a = 7037.954 km

해석:
- e가 0에 매우 가까우므로 거의 원궤도에 가까운 타원궤도이다.
- e_vec가 +x 방향이므로 근점 방향은 +x 방향이다.
- 현재 r도 +x 방향이므로 현재 위치는 근점 근처이다.

## Orbit Geometry Parameters / 궤도 기하 파라미터

손유도 PDF:
derivations/03_orbit_geometry_parameters.pdf

이번 단계의 목적:
상태벡터 r, v에서 궤도의 크기, 근점, 원점, 주기, 속도 기준을 읽어내는 것.

---

### 1. Semi-latus rectum / 반통경 p

핵심식:
p = |h|^2 / mu

여기서:
- h = cross(r, v)
- |h| = 비각운동량 벡터의 크기
- mu = 중심천체의 중력계수
- p = semi-latus rectum / 반통경

의미:
p는 궤도의 크기와 관련된 길이 파라미터이다.
특히 p는 각운동량 h와 중력계수 mu를 통해 결정된다.

직관:
- h가 크면 옆으로 도는 운동이 강하므로 궤도가 더 넓어진다.
- mu가 크면 중심천체가 더 강하게 잡아당기므로 궤도가 더 조여진다.
- 따라서 p = |h|^2 / mu 는 동역학 정보 h를 궤도 형상 정보로 연결하는 값이다.

이번 예제:
p = 7037.749350 km

해석:
이번 예제에서는 e가 매우 작기 때문에 p와 a가 거의 비슷하다.
a = 7037.954027 km
p = 7037.749350 km

---

### 2. Orbit equation / 궤도방정식

핵심식:
r = p / (1 + e*cos(nu))

여기서:
- r = 중심천체에서 위성까지의 현재 거리
- p = semi-latus rectum / 반통경
- e = eccentricity / 이심률
- nu = true anomaly / 진근점이각

의미:
이 식은 2체문제에서 나오는 표준 궤도방정식이다.
위성이 궤도 위에서 어느 각도 nu에 있느냐에 따라 중심천체로부터의 거리 r이 결정된다.

현재 이해 수준:
이번 단계에서는 이 식을 완전 유도하지 않고 2체문제의 표준 결과로 사용한다.
완전 유도에는 극좌표 가속도, 중심력 운동, Binet equation 등이 필요하므로 나중에 별도 보스로 다시 정리한다.

TODO:
Orbit equation r = p / (1 + e*cos(nu))의 완전 유도는 추후 별도 정리.

---

### 3. Periapsis radius / 근점반경 rp

근점은 궤도에서 중심천체에 가장 가까운 지점이다.

궤도방정식에서:
nu = 0 deg
cos(nu) = 1

따라서:
rp = p / (1 + e)

타원궤도에서는 다음 식도 사용한다:
rp = a * (1 - e)

여기서:
- a = semi-major axis / 장반경
- e = eccentricity / 이심률

이번 예제:
rp = 7000.000000 km

해석:
현재 |r| = 7000.000000 km 이고, rp도 7000.000000 km 이다.
따라서 현재 위성은 근점에 있다.

---

### 4. Apoapsis radius / 원점반경 ra

원점은 궤도에서 중심천체로부터 가장 먼 지점이다.

궤도방정식에서:
nu = 180 deg
cos(nu) = -1

따라서:
ra = p / (1 - e)

타원궤도에서는 다음 식도 사용한다:
ra = a * (1 + e)

이번 예제:
ra = 7075.908053 km

해석:
rp = 7000.000000 km
ra = 7075.908053 km

근점과 원점 차이가 약 75.9 km 정도로 작다.
따라서 이번 궤도는 거의 원에 가까운 타원궤도이다.

---

### 5. Orbital period / 궤도주기 T

핵심식:
T = 2*pi*sqrt(a^3 / mu)

여기서:
- T = orbital period / 궤도주기
- a = semi-major axis / 장반경
- mu = gravitational parameter / 중력계수

의미:
타원궤도에서 r은 순간순간 변하는 현재 거리이다.
반면 a는 궤도 전체의 크기를 나타내는 일정한 값이다.
따라서 타원궤도의 주기는 순간 거리 r이 아니라 장반경 a로 결정된다.

이번 예제:
T = 5875.984194 s
T = 97.933070 min

해석:
이 위성은 약 98분에 한 바퀴 도는 궤도에 있다.

---

### 6. Circular speed / 원궤도 속도

핵심식:
v_circ = sqrt(mu / |r|)

의미:
현재 거리 |r|에서 원궤도를 유지하기 위해 필요한 속도이다.

이번 예제:
v_circ = 7.546053 km/s

현재 속도:
|v| = 7.566373 km/s

해석:
현재 속도는 원궤도 속도보다 약간 크다.
따라서 완전 원궤도는 아니고, 약간 타원궤도이다.

---

### 7. Escape speed / 탈출속도

핵심식:
v_esc = sqrt(2*mu / |r|)

의미:
현재 거리 |r|에서 중심천체의 중력을 벗어나기 위해 필요한 최소 속도이다.
이 속도는 specific mechanical energy가 0이 되는 경계이다.

이번 예제:
v_esc = 10.671731 km/s

현재 속도:
|v| = 7.566373 km/s

해석:
현재 속도는 탈출속도보다 작다.
따라서 위성은 지구 중력에 묶여 있다.
즉, bound orbit이다.

---

### 8. 이번 예제 전체 해석

입력:
r = [7000, 0, 0] km
v = [0, 7.5, 1.0] km/s
mu = 398600.4418 km^3/s^2

계산 결과:
|r| = 7000.000000 km
|v| = 7.566373 km/s
epsilon = -28.317920 km^2/s^2
orbit type = elliptic / 타원궤도

e = 0.005392764
a = 7037.954027 km
p = 7037.749350 km
rp = 7000.000000 km
ra = 7075.908053 km
T = 5875.984194 s = 97.933070 min

v_circ = 7.546053 km/s
v_esc = 10.671731 km/s

최종 해석:
- epsilon이 음수이므로 타원궤도이다.
- e가 0.00539로 매우 작으므로 거의 원에 가까운 타원궤도이다.
- rp = 7000 km이고 현재 |r| = 7000 km이므로 현재 위치는 근점이다.
- 현재 속도는 원궤도 속도보다 약간 크지만, 탈출속도보다는 작다.
- 따라서 현재 상태는 near-circular bound elliptical orbit / 거의 원에 가까운 묶인 타원궤도이다.

---

### 9. 아직 완전히 유도하지 않은 것

이번 단계에서 완전 유도하지 않은 식:
- r = p / (1 + e*cos(nu))
- p = a*(1 - e^2)
- T = 2*pi*sqrt(a^3 / mu)의 엄밀한 타원궤도 유도

현재 처리:
이 식들은 2체문제의 표준 결과로 사용한다.
나중에 궤도방정식 보스에서 극좌표 운동방정식과 Binet equation을 이용해 따로 유도한다.

중요:
지금 Level 1의 목표는 모든 식을 처음부터 완전 유도하는 것이 아니라,
상태벡터 r, v에서 궤도의 성질을 읽고 코드로 검증하는 것이다.