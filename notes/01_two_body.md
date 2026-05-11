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